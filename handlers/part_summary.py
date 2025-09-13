# part_summary.py — ShopQuote v3 (Part Summary handlers)

# Required state (CYCLE)
# quote_number: str
# ps_edit_mode: bool
# cleaned_dataset: table-like source of truth
# material_lovs: list[str] (GLOBAL), thickness_lovs: list[str] (GLOBAL)
# Display/read state for current part:
#   customer, part_number, description, material, thickness, thickness_display,
#   flat_size, bends, hardware_readonly, outside_proc_readonly

def ps_enter_edit(state):
    state.ps_edit_mode = True

def ps_cancel_edit(state):
    state.ps_edit_mode = False
    # Optionally re-sync form vars from cleaned_dataset to discard unsaved edits

def _validate_part_summary(state):
    errors = []
    if state.material not in (state.material_lovs or []):
        errors.append("Material must be selected from the list.")
    if state.thickness not in (state.thickness_lovs or []):
        errors.append("Thickness must be selected from the list.")
    try:
        b = int(state.bends)
        if b < 0:
            errors.append("Bends must be 0 or greater.")
    except Exception:
        errors.append("Bends must be an integer.")
    return errors

def btn_save_continue(state):
    # Guard: ensure a quote is active
    if not getattr(state, "quote_number", "").strip():
        # Redirect user back to Home (app-specific nav)
        # state.navigate("Home")
        return

    errors = _validate_part_summary(state)
    if errors:
        # Surface errors to user (toast/message per your app pattern)
        return

    # Apply deltas to cleaned_dataset (and/or a CYCLE overlay then merge)
    # Example (pseudocode): update current part row by some key
    # row = cleaned_dataset.loc[cleaned_dataset.part_id == state.sel_part_id]
    # row.customer = state.customer
    # row.part_number = state.part_number
    # row.description = state.description
    # row.material = state.material
    # row.thickness = state.thickness
    # row.bends = int(state.bends)

    state.ps_edit_mode = False
    # Navigate to Operations
    # state.navigate("Operations")

def on_page_load(state):
    state.customer = getattr(state, "customer", "")
    state.part_number = getattr(state, "part_number", "")
    state.description = getattr(state, "description", "")
    state.material_selected = getattr(state, "material_selected", "")
    state.thickness_choices = getattr(state, "thickness_choices", [])
    state.thickness_selected = getattr(state, "thickness_selected", "")
