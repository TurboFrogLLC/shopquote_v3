# part_summary.md — ShopQuote v3 (Part Summary)

<|part|class_name=topbar|
<|navbar|>   Quote #: <|{quote_number}|input|>
|>

### Part Summary
<|if not {ps_edit_mode}|
Customer: {customer}
Part Number: {part_number}
Description: {description}
Material: {material}
Thickness: {thickness_display}
Flat size: {flat_size}
Bends: {bends}

Hardware
{hardware_readonly}

Outside Process
{outside_proc_readonly}

<|Edit|button|on_action=ps_enter_edit|>
<|else|
Customer: <|{customer}|input|>
Part Number: <|{part_number}|input|>
Description: <|{description}|input|>
Material: <|{material}|selector|lov={material_lovs}|>
Thickness: <|{thickness}|selector|lov={thickness_lovs}|>
Flat size: {flat_size}
Bends: <|{bends}|input|type=number|min=0|step=1|>

Hardware
{hardware_readonly}

Outside Process
{outside_proc_readonly}

<|Save & Continue|button|on_action=btn_save_continue|>
<|Cancel|button|on_action=ps_cancel_edit|>
|>
