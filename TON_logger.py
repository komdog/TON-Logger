# General Imports
import os
import glob
import time
# from enum import Enum

# TON related imports
import modules.terrorManager as database
import modules.roundTypeManager as roundManager
import modules.logFormatManager as log
import modules.OSCManager as osc


def find_latest_log(directory):
    log_files = glob.glob(os.path.join(directory, "*.txt"))
    if not log_files:
        print("No log files found.")
        return None
    
    latest_log = max(log_files, key=os.path.getmtime)
    print(f"Pulling From: {latest_log}\n===================")
    return latest_log


def display_round_info(log_file):
    file_stream_position = 0
    rounds = []

    while True:
        with open(log_file, 'r', encoding='utf-8') as file:
            
            # Read each line of the log file
            file.seek(file_stream_position)
            lines = file.readlines()
            eof = file.tell()

            # Check each line for the round type
            for log_entry in lines:
                log.get_round_info(log_entry)

            # Add round type to occurance array
            
            if "Round type is " in log_entry:
                round_name = log_entry.split("Round type is ")[1].rstrip('\n')
                print(round_name)
                    
            # Count the number of each round type    
            if "Hud" in lines[0]: continue
            round = roundManager.get_round_type_count(rounds)
            print(round)

            file_stream_position = eof
        
        time.sleep(1)
        

# # Current round types in game


# # Directory and file search UPDATED becuase some people's getlogin function EXPLODED so we're doing it this way now :3
log_directory = os.path.join(os.path.expanduser("~"), "AppData", "LocalLow", "VRChat", "VRChat")
latest_log_file = find_latest_log(log_directory)
if latest_log_file: display_round_info(latest_log_file)

    
