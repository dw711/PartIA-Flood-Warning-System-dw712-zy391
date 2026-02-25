from datetime import datetime, timedelta

now = datetime.now()
tendaysago = now - timedelta(days=10)

print(now)
print(tendaysago)
print(datetime(2026, 12, 30))