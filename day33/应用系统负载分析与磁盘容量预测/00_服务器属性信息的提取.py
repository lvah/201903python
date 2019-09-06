import psutil

# cpu信息
print(psutil.cpu_times())
print(psutil.cpu_count())
print(psutil.cpu_percent(interval=3, percpu=True))


# memory
print(psutil.virtual_memory())

# disk
print(psutil.disk_partitions())
print(psutil.disk_usage('/'))

# boot time
timestamp = psutil.boot_time()
from datetime import datetime
print(datetime.fromtimestamp(timestamp))