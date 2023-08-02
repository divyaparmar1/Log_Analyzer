import re

def parse_log_file(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()

    parsed_logs = []
    for log in logs:
        match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(\w+)', log)
        if match:
            timestamp = match.group(1)
            log_level = match.group(2)
            parsed_logs.append({'timestamp': timestamp, 'log_level': log_level})
    return parsed_logs

def display_results(parsed_logs):

    log_count = len(parsed_logs)
    print(f"Total Log Entries: {log_count}")

    log_levels = [log['log_level'] for log in parsed_logs]
    log_level_counts = {level: log_levels.count(level) for level in set(log_levels)}

    print("Log Level Counts:")
    for level, count in log_level_counts.items():
        print(f"{level}: {count}")

def analyze_log_file(file_path):
    parsed_logs = parse_log_file(file_path)
    display_results(parsed_logs)

# Example usage:
log_file_path = "sample.log"  
analyze_log_file(log_file_path)