# operations.py — ShopQuote v3 (Operations handlers)

# CYCLE state (expected)
# edit_mode: bool
# operations_table: list[dict]  # rendered view (read-only when not editing)
# ops_overlay: list[dict]       # editable grid in edit mode
# quote_number: str
# qty: int                      # quote-level quantity (from Home/Settings)
# setup_rate_per_min: float     # from rates (Home/Settings)
# labor_rate_per_sec: float     # from rates (Home/Settings)
# (optional) vendor_lovs, workcenter_lovs, op_lovs, etc.

# ----------------- Utilities -----------------

def _validate_ops_overlay(rows):
    errors = []
    seqs = set()
    for i, r in enumerate(rows or []):
        name = r.get("Operation", "").strip()
        seq = r.get("Seq")
        setup_min = r.get("Setup", 0) or 0
        n_ops = r.get("# Ops", 0) or 0
        runtime_sec = r.get("Time", 0) or 0

        # Basic type/constraint checks
        if not isinstance(seq, int) or seq < 1: errors.append(f"Row {i+1}: Seq must be a positive integer.")
        if seq in seqs: errors.append(f"Row {i+1}: Duplicate Seq {seq}.")
        seqs.add(seq)

        if not name: errors.append(f"Row {i+1}: Operation name is required.")
        if setup_min < 0: errors.append(f"Row {i+1}: Setup (min) cannot be negative.")
        if n_ops < 1: errors.append(f"Row {i+1}: # Ops must be ≥ 1.")
        if runtime_sec < 0: errors.append(f"Row {i+1}: Time (sec) cannot be negative.")
    return errors

def _compute_locked_fields(rows, setup_rate_per_min, labor_rate_per_sec):
    """Return new list with computed 'Setup Cost' and '$/Part' filled (runtime only)."""
    out = []
    for r in rows or []:
        setup_min = float(r.get("Setup", 0) or 0)
        n_ops = int(r.get("# Ops", 0) or 0)
        runtime_sec = float(r.get("Time", 0) or 0)

        setup_cost = setup_min * float(setup_rate_per_min or 0.0)
        run_cost_per_part = runtime_sec * float(labor_rate_per_sec or 0.0) * max(n_ops, 0)

        rr = dict(r)
        rr["Setup Cost"] = round(setup_cost, 2)
        rr["$/Part"] = round(run_cost_per_part, 2)
        out.append(rr)
    return out

def _format_display(rows):
    """Apply bracketed display for Setup and Time and currency for costs."""
    out = []
    for r in rows or []:
        rr = dict(r)
        # Display-only strings (keep raw numeric in overlay; format here for table view)
        try:
            rr["Setup"] = f"[{int(round(float(r.get('Setup', 0))))}m]"
        except Exception:
            rr["Setup"] = "[0m]"
        try:
            rr["Time"] = f"[{int(round(float(r.get('Time', 0))))}s]"
        except Exception:
            rr["Time"] = "[0s]"
        try:
            rr["Setup Cost"] = f"[$ {float(r.get('Setup Cost', 0)):0.2f}]"
        except Exception:
            rr["Setup Cost"] = "[$ 0.00]"
        try:
            rr["$/Part"] = f"[$ {float(r.get('$/Part', 0)):0.2f}]"
        except Exception:
            rr["$/Part"] = "[$ 0.00]"
        out.append(rr)
    return out

def _seed_overlay_from_table(table_rows):
    """Create an editable overlay from the rendered table by stripping display formatting."""
    overlay = []
    for r in table_rows or []:
        row = dict(r)
        # Attempt to parse back numbers if strings present; otherwise keep as-is
        for k in ["Setup", "Time", "Setup Cost", "$/Part"]:
            v = row.get(k)
            if isinstance(v, str):
                import re
                num = re.sub(r"[^0-9.\-]", "", v or "")
                try:
                    row[k] = float(num) if num else 0.0
                except Exception:
                    row[k] = 0.0
        overlay.append(row)
    return overlay

# ----------------- Handlers -----------------

def btn_edit_operations(state):
    if not getattr(state, "quote_number", "").strip():
        # Optional: navigate to Home or show a warning
        return
    state.edit_mode = True
    # Seed overlay from current table
    state.ops_overlay = _seed_overlay_from_table(getattr(state, "operations_table", []))

def btn_update_operations(state):
    rows = list(getattr(state, "ops_overlay", []) or [])
    errors = _validate_ops_overlay(rows)
    if errors:
        # TODO: surface errors in your UI
        return

    # Compute locked fields
    computed = _compute_locked_fields(
        rows,
        getattr(state, "setup_rate_per_min", 0.0),
        getattr(state, "labor_rate_per_sec", 0.0),
    )
    # Update read-only table view with formatted values
    state.operations_table = _format_display(computed)

    # Stay in edit mode
    state.edit_mode = True

def btn_exit_edit(state):
    # Save like Update, then exit edit mode
    btn_update_operations(state)
    state.edit_mode = False

def btn_cancel_edit(state):
    # Discard overlay changes, restore view from last saved table
    state.edit_mode = False
    # Optionally clear overlay
    # state.ops_overlay = _seed_overlay_from_table(state.operations_table)

def btn_generate_quote(state):
    # Only allowed when not editing
    if getattr(state, "edit_mode", False):
        return

    # Here you can submit downstream tasks (e.g., KPIs/breakdown recompute)
    # Example:
    # tp.submit(state.scenario, [task_build_breakdown])
    pass
