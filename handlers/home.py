# home.py — ShopQuote v3 (Home handlers)

import datetime as _dt
# import taipy.core as tp   # Uncomment and adjust when integrating with Taipy Core

# -------------------------
# REQUIRED STATE (CYCLE)
# -------------------------
# quote_number_input: str | None
# upload_files: list
# files_manifest: list[dict]
# parse_status_mode: str
# parse_status_pdf: str
# parse_status_step: str
# parse_status_dxf: str
# validation_ok: bool
# count_parsed_success: int
# validation_warnings: list[str]
# validation_errors: list[str]
# quote_number: str (set at Start Quote)

def _detect_staged_types(upload_files):
    exts = set()
    for f in (upload_files or []):
        name = getattr(f, "name", "") or str(f)
        lower = name.lower()
        if lower.endswith(".pdf"): exts.add("pdf")
        if lower.endswith(".step") or lower.endswith(".stp") or lower.endswith(".step.gz") or lower.endswith(".stp.gz"):
            exts.add("step")
        if lower.endswith(".dxf"): exts.add("dxf")
    return exts

def _autogen_quote_number_now():
    now = _dt.datetime.now()
    mm = now.strftime("%m")
    ddyyyy = now.strftime("%d%Y")
    hh12 = now.strftime("%I")
    return f"SQ-{mm}-{ddyyyy}-{hh12}"

def btn_process_files(state):
    # TODO: implement parse + normalize tasks with tp.submit(...)
    pass

def btn_restore_quote(state):
    # TODO: implement restore + normalize tasks with tp.submit(...)
    pass

def btn_clear_uploads(state):
    state.upload_files = []
    state.files_manifest = []
    state.parse_status_mode = ""
    state.parse_status_pdf = "-"
    state.parse_status_step = "-"
    state.parse_status_dxf = "-"
    state.validation_ok = False
    state.count_parsed_success = 0
    state.validation_warnings = []
    state.validation_errors = []

def btn_start_quote(state):
    if not state.validation_ok or (state.count_parsed_success or 0) < 1:
        return

    q_in = (state.quote_number_input or "").strip()
    state.quote_number = q_in if q_in else _autogen_quote_number_now()

    # TODO: create/select scenario keyed to state.quote_number and navigate to Part Summary
    pass

def on_page_load(state):
    state.quote_number = getattr(state, "quote_number", "")
    state.upload_files = getattr(state, "upload_files", [])
    state.home_status = getattr(state, "home_status", "Ready.")

def home_process_files(state):
    state.home_status = "Processed (stub)."

def home_restore_quote(state):
    state.home_status = "Restored (stub)."

def home_start_quote(state):
    state.home_status = "Quote started (stub)."

def home_clear_uploads(state):
    state.upload_files = []
    state.home_status = "Cleared."
