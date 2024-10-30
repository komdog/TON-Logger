# General Imports
import os
import glob
import time
# from enum import Enum

# TON related imports
import modules.terrorManager as database
import modules.roundTypeManager as round
import modules.OSCManager as osc


def find_latest_log(directory):
    log_files = glob.glob(os.path.join(directory, "*.txt"))
    if not log_files:
        print("No log files found.")
        return None
    
    latest_log = max(log_files, key=os.path.getmtime)
    print(f"Pulling From: {latest_log}\n===================")
    return latest_log

def is_valid_log_entry(log_entry):
    # if "Killers have been revealed - " in log_entry: return True
    if not "Round type is" in log_entry: return False
    if not "Killers have been set - " in log_entry: return False
    return True

def display_round_info(log_file):
    last_position = 0
    rounds = []

    while True:
        with open(log_file, 'r', encoding='utf-8') as file:
            
            # Read each line of the log file
            file.seek(last_position)
            lines = file.readlines()
            new_position = file.tell()
            
            # Check each line for the round type
            for log_entry in lines:

                if "Killers is unknown" in log_entry:
                    round = log_entry.split("Round type is ")[1].rstrip('\n')
                    print(f"The Round is {round} // Killer Will Be Revealed Soon")

                if "Killers have been revealed - " in log_entry:
                    round = log_entry.split("Round type is ")[1].rstrip('\n')
                    killers_indexes = log_entry.split("Killers have been revealed - ")[1].split("//")[0].rstrip(' ').split(" ")
                    killers = map(lambda k: database.get_terror_name(round, k), killers_indexes)
                    print(f"{round} : {list(killers)}")


                
                if is_valid_log_entry(log_entry):
                    # Get round name
                    round = log_entry.split("Round type is ")[1].rstrip('\n')

                    # Get Killer names
                    # print(log_entry.split("Killers have been set - "))
                    # continue
                    killers_indexes = log_entry.split("Killers have been set - ")[1].split("//")[0].rstrip(' ').split(" ")
                    killers = map(lambda k: database.get_terror_name(round, k), killers_indexes)
                    
                    # Append the round type to the list
                    rounds.append(round)
                    print(f"{round} : {list(killers)}")
                
            # Count the number of each round type    
            # get_round_type_count(rounds)

            last_position = new_position
        
        time.sleep(1)
        

# # Current round types in game


# # Directory and file search UPDATED becuase some people's getlogin function EXPLODED so we're doing it this way now :3
log_directory = os.path.join(os.path.expanduser("~"), "AppData", "LocalLow", "VRChat", "VRChat")
latest_log_file = find_latest_log(log_directory)
if latest_log_file: display_round_info(latest_log_file)

    
