"""

This script retrieves a list of all
processes running on the computer and 
sorts them by memory usages.

- Trevor Moore

"""

import psutil

# Get list of all processes running
processes = []
for proc in psutil.process_iter():
    try:

        # Get process information as named tuple
        process_info = proc.as_dict(attrs=['pid', 'name', 'memory_info'])

        # Add process to list
        processes.append(process_info)

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
# Sort list by memory usage    
processes_sorted = sorted(processes, key=lambda proc: proc['memory_info'].rss, reverse=True)

# Print sorted list
for proc in processes_sorted:
    print(f"PID: {proc['pid']} | Name: {proc['name']} | Memory Usage: {proc['memory_info'].rss / 1024 / 1024:.2f} MB")