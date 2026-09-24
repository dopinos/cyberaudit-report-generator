from datetime import datetime
from html import escape


def ask(prompt):
    return input(prompt).strip()


def choose_severity():
    print("\nSeverity:")
    print("1. Critical")
    print("2. High")
    print("3. Medium")
    print("4. Low")
    print("5. Informational")

    choices = {
        "1": "Critical",
        "2": "High",
        "3": "Medium",
        "4": "Low",
        "5": "Informational"
    }

    while True:
        choice = input("Choose: ").strip()
        if choice in choices:
            return choices[choice]
        print("Invalid choice.")


def create_finding():
    print("\n--- New Finding ---")

    title = ask("Finding title: ")
    severity = choose_severity()
    description = ask("Description: ")
    evidence = ask("Evidence: ")
    recommendation = ask("Recommendation: ")

    return {
        "title": title,
        "severity": severity,
        "description": description,
        "evidence": evidence,
        "recommendation": recommendation
    }


def generate_report(project, client, scope, findings):
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Security Audit Report</title>

<style>
body {{
    font-family: Arial, sans-serif;
    max-width: 1000px;
    margin: 40px auto;
    padding: 20px;
    line-height: 1.6;
}}

h1 {{
    border-bottom: 2px solid #222;
    padding-bottom: 10px;
}}

h2 {{
    margin-top: 35px;
}}

.finding {{
    border: 1px solid #ddd;
    padding: 20px;
    margin: 20px 0;
    border-radius: 8px;
}}

.meta {{
    background: #f5f5f5;
    padding: 15px;
    border-radius: 8px;
}}

.label {{
    font-weight: bold;
}}
</style>
</head>

<body>

<h1>Security Audit Report</h1>

<div class="meta">
<p><span class="label">Project:</span> {escape(project)}</p>
<p><span class="label">Client:</span> {escape(client)}</p>
<p><span class="label">Scope:</span> {escape(scope)}</p>
<p><span class="label">Date:</span> {date}</p>
</div>

<h2>Executive Summary</h2>

<p>
This report documents the security findings identified during the
authorized security assessment of the defined scope.
</p>

<h2>Findings</h2>
"""

    if not findings:
        html += "<p>No findings were added.</p>"

    for index, finding in enumerate(findings, start=1):
        html += f"""
<div class="finding">

<h3>{index}. {escape(finding["title"])}</h3>

<p>
<span class="label">Severity:</span>
{escape(finding["severity"])}
</p>

<p>
<span class="label">Description:</span><br>
{escape(finding["description"])}
</p>

<p>
<span class="label">Evidence:</span><br>
{escape(finding["evidence"])}
</p>

<p>
<span class="label">Recommendation:</span><br>
{escape(finding["recommendation"])}
</p>

</div>
"""

    html += """
<h2>Conclusion</h2>

<p>
The findings documented in this report should be reviewed and
addressed according to their severity and the organization's
security priorities.
</p>

</body>
</html>
"""

    filename = "security_audit_report.html"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(html)

    return filename


def main():
    print("=" * 50)
    print("CyberAudit Report Generator")
    print("=" * 50)

    project = ask("\nProject name: ")
    client = ask("Client name: ")
    scope = ask("Audit scope: ")

    findings = []

    while True:
        add = ask("\nAdd a finding? (y/n): ").lower()

        if add == "y":
            findings.append(create_finding())
        elif add == "n":
            break
        else:
            print("Please enter y or n.")

    filename = generate_report(
        project,
        client,
        scope,
        findings
    )

    print("\nReport generated successfully!")
    print(f"File: {filename}")


if __name__ == "__main__":
    main()
