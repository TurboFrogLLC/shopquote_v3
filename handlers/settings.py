# settings.py — ShopQuote v3 (Settings handlers)

# Expected CYCLE state
# quote_number: str
# setup_rate_per_min: float
# labor_rate_per_sec: float
# machine_rate_per_hr: float
# markup_pct: float
# qty: int
# override_scope: str   # 'GLOBAL' or 'CYCLE'
# recompute_after_save: bool
# overlay_file: file-like or bytes (uploaded overlay)

# Optional: global defaults
# default_setup_rate_per_min, default_labor_rate_per_sec, default_machine_rate_per_hr, default_markup_pct

import json

def _apply_overrides(state, overrides: dict, scope: str):
    """Apply overrides to state by scope. For GLOBAL scope you may map to your global store;
    for CYCLE scope we just set CYCLE vars. Adjust mapping to your config."""
    # Map known fields; ignore unknown keys
    if scope == 'GLOBAL':
        # Example mapping (adjust to your app's global mechanism)
        if 'setup_rate_per_min' in overrides: state.setup_rate_per_min = float(overrides['setup_rate_per_min'])
        if 'labor_rate_per_sec' in overrides: state.labor_rate_per_sec = float(overrides['labor_rate_per_sec'])
        if 'machine_rate_per_hr' in overrides: state.machine_rate_per_hr = float(overrides['machine_rate_per_hr'])
        if 'markup_pct' in overrides: state.markup_pct = float(overrides['markup_pct'])
    else:  # CYCLE
        if 'setup_rate_per_min' in overrides: state.setup_rate_per_min = float(overrides['setup_rate_per_min'])
        if 'labor_rate_per_sec' in overrides: state.labor_rate_per_sec = float(overrides['labor_rate_per_sec'])
        if 'machine_rate_per_hr' in overrides: state.machine_rate_per_hr = float(overrides['machine_rate_per_hr'])
        if 'markup_pct' in overrides: state.markup_pct = float(overrides['markup_pct'])
        if 'qty' in overrides: state.qty = int(overrides['qty'])

def _current_overrides_dict(state):
    return {
        "setup_rate_per_min": float(getattr(state, "setup_rate_per_min", 0) or 0),
        "labor_rate_per_sec": float(getattr(state, "labor_rate_per_sec", 0) or 0),
        "machine_rate_per_hr": float(getattr(state, "machine_rate_per_hr", 0) or 0),
        "markup_pct": float(getattr(state, "markup_pct", 0) or 0),
        "qty": int(getattr(state, "qty", 1) or 1),
        "scope": getattr(state, "override_scope", "CYCLE") or "CYCLE",
    }

def btn_save_settings(state):
    """Persist overrides to the chosen scope and optionally recompute downstream tables."""
    scope = (getattr(state, "override_scope", "CYCLE") or "CYCLE").upper()
    overrides = _current_overrides_dict(state)
    _apply_overrides(state, overrides, scope)

    # Optional recompute: update operations table using current overlays
    if getattr(state, "recompute_after_save", False):
        try:
            # Example: recompute locked columns on operations table from overlay
            if hasattr(state, "ops_overlay") and state.ops_overlay:
                # You likely have a shared compute util; leave as a placeholder
                pass
        except Exception:
            # Surface a toast/message in your real app
            pass

def btn_download_overlay(state):
    """Build a minimal JSON overlay of current overrides and trigger a download (no disk writes)."""
    data = _current_overrides_dict(state)
    payload = json.dumps(data, indent=2).encode("utf-8")
    # Example browser stream, replace with your app's download method:
    # state.download(payload, filename=f"{getattr(state,'quote_number','shopquote')}_settings_overlay.json", mime="application/json")
    pass

def on_overlay_file_change(state):
    """Parse uploaded overlay (JSON only in this stub) and apply by chosen scope."""
    file_obj = getattr(state, "overlay_file", None)
    if not file_obj:
        return
    # Expecting .json; adjust if you also support CSV
    try:
        content = getattr(file_obj, "content", None)
        if content and isinstance(content, (bytes, bytearray)):
            text = content.decode("utf-8", errors="ignore")
        else:
            # Some UIs provide .read()
            if hasattr(file_obj, "read"):
                text = file_obj.read().decode("utf-8", errors="ignore")
            else:
                text = str(file_obj)
        overrides = json.loads(text)
    except Exception:
        # Surface parse error in your real app
        return

    scope = (getattr(state, "override_scope", "CYCLE") or "CYCLE").upper()
    _apply_overrides(state, overrides, scope)

    # Optional recompute
    if getattr(state, "recompute_after_save", False):
        try:
            if hasattr(state, "ops_overlay") and state.ops_overlay:
                # Recompute placeholder
                pass
        except Exception:
            pass

def on_page_load(state):
    state.setup_rate_per_min = getattr(state, "setup_rate_per_min", 0.0)
    state.labor_rate_per_sec = getattr(state, "labor_rate_per_sec", 0.0)
    state.markup_pct = getattr(state, "markup_pct", 0.0)
    state.recompute_after_save = getattr(state, "recompute_after_save", False)

def settings_save(state):
    if getattr(state, "recompute_after_save", False):
        state.tp.submit(state.sq_scenario, ["compute_operations", "build_breakdown"])
