from pathlib import Path

from openpyxl import load_workbook
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation


root = Path(__file__).resolve().parent.parent
path = root / "audience-monetization" / "30-day validation tracker.xlsx"
workbook = load_workbook(path)
sheet = workbook["Tasks"]

status_validation = DataValidation(
    type="list",
    formula1='"Not started,In progress,Done"',
    allow_blank=False,
)
status_validation.error = "Choose Not started, In progress, or Done."
status_validation.errorTitle = "Invalid status"
status_validation.prompt = "Select a task status from the dropdown."
status_validation.promptTitle = "Task status"
sheet.add_data_validation(status_validation)
status_validation.add(f"F2:F{sheet.max_row}")

CANONICAL_STATUS = {"not started": "Not started", "in progress": "In progress", "done": "Done", "☑": "Done"}
for row in range(2, sheet.max_row + 1):
    cell = sheet.cell(row, 6)
    raw = (cell.value or "").strip() if isinstance(cell.value, str) else cell.value
    if raw in {"☐", None, ""}:
        cell.value = "Not started"
    else:
        cell.value = CANONICAL_STATUS.get(str(raw).lower(), raw)
    cell.font = Font(color="666666")

sheet.conditional_formatting.add(
    f"F2:F{sheet.max_row}",
    FormulaRule(formula=["F2=\"Done\""], fill=PatternFill("solid", fgColor="C6EFCE"), font=Font(color="006100", bold=True)),
)
sheet.conditional_formatting.add(
    f"F2:F{sheet.max_row}",
    FormulaRule(formula=["F2=\"In progress\""], fill=PatternFill("solid", fgColor="FFEB9C"), font=Font(color="9C6500", bold=True)),
)

# Dashboard formulas still referenced the old "☑" checkbox symbol, so completed
# tasks (marked "Done"/"done") were never counted. Point them at the new status text.
dashboard = workbook["Dashboard"]
fixed = 0
for row in dashboard.iter_rows():
    for cell in row:
        if isinstance(cell.value, str) and "☑" in cell.value:
            cell.value = cell.value.replace('"☑"', '"Done"')
            fixed += 1

instructions = workbook["Instructions"]
for row in instructions.iter_rows():
    if row[1].value == "Choose ☐ for incomplete or ☑ for complete.":
        row[1].value = "Choose Not started, In progress, or Done from the dropdown."

print(f"Repaired {fixed} Dashboard formula(s) referencing the old checkbox symbol.")

workbook.save(path)
print(f"Repaired {path}")

workbook.save(path)
print(f"Repaired {path}")
