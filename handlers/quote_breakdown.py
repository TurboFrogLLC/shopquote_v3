# quote_breakdown.py — ShopQuote v3 (Quote Breakdown handlers)

# Read state (CYCLE)
# quote_number: str
# qty: int
# setup_rate_per_min: float
# labor_rate_per_sec: float
# markup_pct: float
# operations_table: list[dict]                  # read-only, precomputed display
# hardware_table: list[dict]                    # for hardware totals (read only here)
# outside_process_table: list[dict]             # for outside process totals (read only)
# quote_breakdown_json: dict                    # optional precomputed totals

def _recompute_breakdown_if_needed(state):
    """Optional: recompute totals from overlays if your app requires freshness here."""
    # Placeholder for your pipeline call (e.g., tp.submit to recompute KPIs)
    pass

def btn_go_summary(state):
    # Ensure we have a quote number
    if not getattr(state, "quote_number", "").strip():
        return
    # Optionally ensure totals are consistent before proceeding
    _recompute_breakdown_if_needed(state)
    # Navigate to Quote Summary (replace with your router)
    # state.navigate("Quote Summary")
    pass
