import sys
import os
import time
import random
from shutil import copyfile
from datetime import datetime
from glob import glob


FILES_TO_COPY = []

print "Backup Tool v1.0"

if len(sys.argv) < 3:
    print "USAGE: backup.py <PATH> <DATE YYYYMMDD>"
    sys.exit(0)

PATH = sys.argv[1]
DATETIME = sys.argv[2]

before_date = datetime.strptime(DATETIME, "%Y%m%d")

files = glob(PATH + "/*")

# Create backup dictory
new_backup_directory = "backup_" + time.strftime("%Y%m%d_%H%M%S")
if not os.path.exists(new_backup_directory):
    os.mkdir(new_backup_directory)

print "[*] Processing files"

for f in files:
    created_datetime = datetime.fromtimestamp(os.path.getctime(PATH))
    modified_datetime = datetime.fromtimestamp(os.path.getmtime(PATH))

    cdate = created_datetime.strftime("%Y-%m-%d")
    mdate = modified_datetime.strftime("%Y-%m-%d")

    current_file_created_datetime = datetime.strptime(cdate, "%Y-%m-%d")

    if before_date >= current_file_created_datetime:
        year_dir = cdate[0:4]
        if not os.path.exists(new_backup_directory + "/" + year_dir):
            os.mkdir(new_backup_directory + "/" + year_dir)

        file_to_copy = os.path.abspath(f)
        filename_only = os.path.basename(f)
        destination = "./" + new_backup_directory + "/" + year_dir + "/" + filename_only

        print "[+] Copying (%s)..." % file_to_copy

        copyfile(file_to_copy, destination)        


print
print "All files are copied to (%s)" % new_backup_directory
print "[Done!]"
