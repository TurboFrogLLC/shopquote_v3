# quote_summary.py — ShopQuote v3 (Quote Summary handlers)

# Read state (CYCLE)
# quote_number: str
# totals: total_setup_cost, total_runtime_cost, hardware_total, outside_process_total, subtotal_cost, markup_pct, grand_total
# KPIs: kpi_cost_per_part_runtime, kpi_setup_per_part, kpi_all_in_per_part, kpi_cycle_time_sec
# Render free tier note: no server disk writes; export must stream to client

def btn_export_quote(state, args=None):
    """Stream a TXT or PDF export to the client (no server disk writes).
    args: 'txt' or 'pdf'
    """
    fmt = (args or '').lower()
    if fmt not in ('txt', 'pdf'):
        # default to txt
        fmt = 'txt'
    # TODO: call your export builder to generate bytes in-memory
    # example:
    # data_bytes = build_export_bytes(state, fmt=fmt)
    # state.download(data_bytes, filename=f"{state.quote_number}.{fmt}", mime="text/plain" if fmt=='txt' else "application/pdf")
    pass

def btn_new_quote(state):
    """Clear all CYCLE data and return to Home to start fresh."""
    # Clear common CYCLE nodes (adjust to your config)
    for var in [
        "quote_number", "ops_overlay", "operations_table",
        "hardware_table", "outside_process_table",
        "total_setup_cost", "total_runtime_cost", "hardware_total",
        "outside_process_total", "subtotal_cost", "grand_total",
        "kpi_cost_per_part_runtime", "kpi_setup_per_part",
        "kpi_all_in_per_part", "kpi_cycle_time_sec",
    ]:
        if hasattr(state, var):
            setattr(state, var, None)

    # Also consider clearing uploads and parsed datasets if you want a true reset:
    # for var in ["upload_files", "files_manifest", "parse_status_mode", "cleaned_dataset"]:
    #     if hasattr(state, var): setattr(state, var, None)

    # Navigate to Home
    # state.navigate("Home")
    pass
