def is_safe(report):
    """Check if a report is safe based on the original rules."""
    diffs = [report[i+1] - report[i] for i in range(len(report) - 1)]
    increasing = all(1 <= d <= 3 for d in diffs)
    decreasing = all(-3 <= d <= -1 for d in diffs)
    return increasing or decreasing

def is_safe_with_dampener(report):
    """Check if a report is safe, allowing one level to be removed."""
    if is_safe(report):
        return True
    # Try removing each level and check if the resulting report is safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

def count_safe_reports(data):
    """Count reports that are safe with or without the Problem Dampener."""
    safe_count = 0
    for line in data:
        report = list(map(int, line.split()))
        if is_safe_with_dampener(report):
            safe_count += 1
    return safe_count

# Read input from a file or directly paste the data
with open('day2_input.txt', 'r') as f:
    data = f.read().strip().split('\n')

# Count the safe reports
safe_reports = count_safe_reports(data)
print(f"Number of safe reports: {safe_reports}")
