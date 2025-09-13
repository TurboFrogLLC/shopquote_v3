# quote_summary.md — ShopQuote v3 (Quote Summary)

<|part|class_name=topbar|
<|navbar|>   Quote #: <|{quote_number}|text|class_name=badge|>
|>

### Final Totals
<|layout|columns=1fr 1fr 1fr|gap=16px|
<|part|class_name=card|
**Total Setup**  
<|{total_setup_cost}|text|>
|>
<|part|class_name=card|
**Total Runtime**  
<|{total_runtime_cost}|text|>
|>
<|part|class_name=card|
**Hardware Total**  
<|{hardware_total}|text|>
|>
|>

<|layout|columns=1fr 1fr 1fr|gap=16px|
<|part|class_name=card|
**Outside Process Total**  
<|{outside_process_total}|text|>
|>
<|part|class_name=card|
**Subtotal**  
<|{subtotal_cost}|text|>
|>
<|part|class_name=card|
**Markup %**  
<|{markup_pct}|text|>
|>
|>

<|part|class_name=card wide|
**Grand Total**  
<|{grand_total}|text|>
|>

### KPIs (Read-only)
- Cost / Part (runtime only): <|{kpi_cost_per_part_runtime}|text|>
- Setup amortization / Part: <|{kpi_setup_per_part}|text|>
- All-in Cost / Part: <|{kpi_all_in_per_part}|text|>
- Cycle time / Part (sec): <|{kpi_cycle_time_sec}|text|>

### Export
<|Export TXT|button|on_action=btn_export_quote|args=txt|>
<|Export PDF|button|on_action=btn_export_quote|args=pdf|>

### Finish
<|Start New Quote|button|on_action=btn_new_quote|>

<style>
.topbar { position: sticky; top: 0; z-index: 40; }
.badge { padding: 4px 8px; border-radius: 8px; background: #eef; }
.card { padding: 12px; border: 1px solid #ddd; border-radius: 12px; }
.card.wide { grid-column: 1 / -1; }
</style>
