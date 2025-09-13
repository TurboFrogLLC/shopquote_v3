# quote_breakdown.md — ShopQuote v3 (Quote Breakdown)

<|part|class_name=topbar|
<|navbar|>   Quote #: <|{quote_number}|text|class_name=badge|>
|>

### Totals
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

### Operations Breakdown (Read-only)
<|{operations_table}|table|columns=Seq,Operation,Setup,Setup Cost,# Ops,Time,$/Part|height=320px|>

<|Go to Quote Summary|button|on_action=btn_go_summary|>

<style>
.topbar { position: sticky; top: 0; z-index: 40; }
.badge { padding: 4px 8px; border-radius: 8px; background: #eef; }
.card { padding: 12px; border: 1px solid #ddd; border-radius: 12px; }
.card.wide { grid-column: 1 / -1; }
</style>
