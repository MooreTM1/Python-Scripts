"""
This script retrieves a list of all 
installed applications on a computer
and exports them to a CSV file.

- Trevor Moore

"""

import csv
import subprocess

# Use subprocess to execute 'wmic product get name' command and get installed applications
installed_apps = subprocess.check_output(['wmic', 'product', 'get', 'name']).decode('utf-8').split('\n')[1:]

# Open a CSV file named 'istalled_apps.csv' in write mode
with open('installed_apps.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Application Name'])
    
    # Iterate over the installed applications
    for app in installed_apps:
        writer.writerow([app.strip()])

# Print a message indicating the listed of installed apps has been exported to a CSV file
print('List of installed apps exported to installed_apps.csv')