# operations.md — ShopQuote v3 (Operations)

<|part|class_name=topbar|
<|navbar|>   Quote #: <|{quote_number}|input|>
|>

### Operations
<|if not {edit_mode}|
**Read-only view** (per-part runtime costs; setup costs separate).
<|{operations_table}|table|columns=Seq,Operation,Setup,Setup Cost,# Ops,Time,$/Part|height=360px|>

<|Generate Quote|button|on_action=btn_generate_quote|>
<|Edit Operations|button|on_action=btn_edit_operations|>

<|else|
**Edit Mode** (editable fields vary by operation type).

#### Editor Grid (Standard Ops)
- Editable: Seq, Operation, Setup (min), # Ops, Time (sec)
- Computed (read-only): Setup Cost, $/Part

<|{ops_overlay}|table|editable|columns=Seq,Operation,Setup,# Ops,Time,Setup Cost,$/Part|height=360px|>

#### Selected Row Helper Editors (optional)
- If Operation == "Install": show hardware-aware fields (qty from hardware table is read-only):
  - Setup (min), Time (sec) editable
- If Operation is an outside process: vendor & unit cost editor;
  - Setup = [0m], Time = [0s], # Ops = 1, $/Part = vendor unit cost

<|Update Operations|button|on_action=btn_update_operations|>
<|Exit (Save)|button|on_action=btn_exit_edit|>
<|Cancel (No Save)|button|on_action=btn_cancel_edit|>
|>

> **Formatting rules**
> - Column order fixed: Seq | Operation | Setup | Setup Cost | # Ops | Time | $/Part
> - **Setup** shown as `[Xm]` (minutes); **Time** as `[Xs]` (seconds)
> - **$ / Part = Runtime (sec/op) × Labor Rate ($/sec) × # Ops** (runtime only)
> - **Setup Cost = Setup (min) × Setup Rate ($/min)`** (separate column, not included in $/Part)
> - Mandatory operations enforcement happens on **Home → Start Quote**, not here.

<style>
.topbar { position: sticky; top: 0; z-index: 40; }
</style>
