import os
from datetime import datetime

REPORT_DIR = "reports"

def save_report(target, findings):
    """
    Save audit findings to a report file.

    Args:
        target (str): Target domain.
        findings (list): List of findings.
    """

    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{REPORT_DIR}/{target}_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as report:

        report.write("=" * 60 + "\n")
        report.write("WHITEVISION SECURITY AUDIT REPORT\n")
        report.write("=" * 60 + "\n\n")

        report.write(f"Target: {target}\n")
        report.write(f"Generated: {datetime.now()}\n\n")

        report.write("Findings\n")
        report.write("-" * 60 + "\n")

        for item in findings:
            report.write(f"{item}\n")

        report.write("\n")
        report.write("=" * 60 + "\n")
        report.write("End of Report\n")

    print(f"\n[+] Report saved: {filename}")