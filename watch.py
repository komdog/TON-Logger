import os
import glob
import time

def get_latest_log():
    # Get Paths
    log_directory = os.path.join(os.path.expanduser("~"), "AppData", "LocalLow", "VRChat", "VRChat")
    log_files = glob.glob(os.path.join(log_directory, "*.txt"))

    # No Logs Found?
    if not log_files: print("No log files found."); return None
    return max(log_files, key=os.path.getmtime)

def watch(latest_log):

    file_stream_position = 0

    while True:
        with open(latest_log, 'r', encoding='utf-8') as file:

            # Read each line of the log file
            file.seek(file_stream_position)
            lines = file.readlines()
            eof = file.tell()

            for entry in lines: 
                if "Log" in entry: 
                    print(entry.rstrip('\n'))

            file_stream_position = eof

        time.sleep(1)



latest_log = get_latest_log()
if latest_log: watch(latest_log)
print(latest_log)
