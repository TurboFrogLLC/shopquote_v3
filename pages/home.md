# Home

<|layout|columns=1 1|gap=16px|>
<|part|>
### Quote Inputs
**Quote #**  
<|{quote_number}|input|label=Quote Number|>

**Upload Files** (PDF/STEP/DXF)  
<|{upload_files}|file_selector|extensions=.pdf,.step,.stp,.dxf|multiple|>

<|Process Files|button|on_action=home_process_files|>
<|Restore from Quote PDF|button|on_action=home_restore_quote|>
<|Start Quote|button|on_action=home_start_quote|>
<|Clear Uploads|button|on_action=home_clear_uploads|>
<|endpart|>

<|part|>
### Status
<|{home_status}|text|mode=plain|>
<|endpart|>
<|endlayout|>
