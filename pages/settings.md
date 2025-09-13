# settings.md — ShopQuote v3 (Settings)

<|part|class_name=topbar|
<|navbar|>   Quote #: <|{quote_number}|text|class_name=badge|>
|>

### Rates & Preferences
> Global defaults come from CSV; you can override them here. Choose scope for your overrides (GLOBAL or CYCLE) and optionally recompute after saving.

<|layout|columns=1fr 1fr 1fr 1fr|gap=16px|
<|part|class_name=card|
**Setup Rate ($/min)**  
<|{setup_rate_per_min}|input|type=number|min=0|step=0.01|>
|>
<|part|class_name=card|
**Labor Rate ($/sec)**  
<|{labor_rate_per_sec}|input|type=number|min=0|step=0.0001|>
|>
<|part|class_name=card|
**Machine Rate ($/hr)**  
<|{machine_rate_per_hr}|input|type=number|min=0|step=0.01|>
|>
<|part|class_name=card|
**Markup %**  
<|{markup_pct}|input|type=number|min=0|max=100|step=0.1|>
|>
|>

<|layout|columns=1fr 1fr|gap=16px|
<|part|class_name=card|
**Quote Quantity (applies to totals)**  
<|{qty}|input|type=number|min=1|step=1|>
|>
<|part|class_name=card|
**Override Scope**  
<|{override_scope}|selector|lov=GLOBAL;CYCLE|dropdown|>
<|{recompute_after_save}|toggle|label=Recompute after save|>
|>
|>

### Overlay Management
- **Upload overlay file** (JSON/CSV): applies rate/settings overlays per chosen scope.  
- **Download overlay**: saves current overrides as a local file (no server disk writes).

**Upload Overlay**  
<|{overlay_file}|file_selector|label=Choose overlay file (.json or .csv)|>

<|Download Current Overrides|button|on_action=btn_download_overlay|>
<|Save Settings|button|on_action=btn_save_settings|>

<style>
.topbar { position: sticky; top: 0; z-index: 40; }
.badge { padding: 4px 8px; border-radius: 8px; background: #eef; }
.card { padding: 12px; border: 1px solid #ddd; border-radius: 12px; }
</style>
