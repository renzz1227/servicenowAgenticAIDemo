from datadog import initialize, api
import pandas as pd
import time

# Replace with your real API and APP keys
options = {
    'api_key': 'your_api_key_here',
    'app_key': 'your_app_key_here'
}

initialize(**options)

# Time range: last 30 minutes
end_time = int(time.time())
start_time = end_time - 1800  # 30 minutes ago

# Query: CPU Idle metric (change as needed)
query = 'avg:system.cpu.idle{*}by{host}'

# Call Datadog API
res = api.Metric.query(start=start_time, end=end_time, query=query)

# Process data
series = res.get('series', [])
data = []

for s in series:
    host = s.get('scope', 'unknown')
    for point in s['pointlist']:
        timestamp, value = point
        data.append({
            'host': host,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp / 1000)),
            'value': value
        })

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("datadog_cpu_report.csv", index=False)
print("✅ Report saved as datadog_cpu_report.csv")
