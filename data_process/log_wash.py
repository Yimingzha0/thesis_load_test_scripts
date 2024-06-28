# convert log file to csv file, filter out the necessary data
# the csv file contains the following columns: Timestamp, Method, Endpoint, Response Time (ms), Size (bytes)
# Written by: Yiming Zhao
import csv
import re

log_filename = '../train_system/locustfile.log'
csv_filename = '../train_system/results/locust_requests.csv'

log_pattern = re.compile(
    r'\[(?P<timestamp>[\d\-:\s,]+)]\s+[^\]]+/INFO/locust:\s+(?P<status>SUCCESS|FAILURE):\s+(?P<method>\w+)\s+('
    r'?P<endpoint>[\S]+)\s+(?P<response_time>[\d.]+)ms\s+(?P<size>\d+)\s+bytes'
)
with open(log_filename, 'r') as log_file:
    log_lines = log_file.readlines()
with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Timestamp', 'Method', 'Endpoint', 'Response Time (ms)', 'Size (bytes)'])
    for line in log_lines:
        match = log_pattern.search(line)
        if match:
            timestamp = match.group('timestamp').strip()
            method = match.group('method').strip()
            endpoint = match.group('endpoint').strip()
            response_time = match.group('response_time').strip()
            size = match.group('size').strip()
            csv_writer.writerow([timestamp, method, endpoint, response_time, size])

print(f"Log data has been successfully converted to {csv_filename}")
