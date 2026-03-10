from datetime import datetime
from pathlib import Path

vault = Path("vault")

accounting_file = vault / "Accounting" / "Current_Month.md"
briefings_folder = vault / "Briefings"

date = datetime.now().strftime("%Y-%m-%d")

revenue = 0

if accounting_file.exists():
    with open(accounting_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "$" in line:
                try:
                    amount = float(line.split("$")[1])
                    revenue += amount
                except:
                    pass

report = f"""
# CEO Weekly Briefing

Date: {date}

## Revenue This Month
${revenue}

## Notes
AI generated weekly summary.
"""

file_path = briefings_folder / f"CEO_Briefing_{date}.md"

with open(file_path, "w") as f:
    f.write(report)

print("CEO briefing generated!")