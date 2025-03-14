def filter_logs(log_file, severity):
    with open(log_file, "r") as file:
        logs = [line.strip() for line in file if severity in line]
    return logs

# Ask the user for the severity level
severity_level = input("Enter severity level to filter (INFO, WARNING, ERROR): ").strip().upper()

# Read the log file and filter logs
filtered_logs = filter_logs("app.log", severity_level)

# Display filtered logs
print(f"\nLogs with severity '{severity_level}':")
for log in filtered_logs:
    print(log)

print(f"\nTotal {severity_level} occurrences: {len(filtered_logs)}")
