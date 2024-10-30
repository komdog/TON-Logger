import os
import glob
import time
import json
from enum import Enum
from pythonosc.udp_client import SimpleUDPClient

with open('data/terrors.json', 'r') as f:
    # Load the JSON data into a Python dictionary
    terrors = json.load(f)

with open('data/alternates.json', 'r') as f:
    # Load the JSON data into a Python dictionary
    alternates = json.load(f)

def find_latest_log(directory):
    log_files = glob.glob(os.path.join(directory, "*.txt"))
    if not log_files:
        print("No log files found.")
        return None
    
    latest_log = max(log_files, key=os.path.getmtime)
    print(f"Pulling From: {latest_log}\n===================")
    return latest_log

def get_round_type_count(rounds):
    for round_type in round_types:
        print(round_type)
        # count = rounds.count(f' {round_type}')
        # print(f"{round_type}: {count}")

def get_terror_name(round, id):
    # No killer
    if int(id) == 0: return "<>"

    match round:
        case "Alternate": return f"{alternates[int(id)]} : {int(id)}"
        case  _: return f"{terrors[int(id)]} : {int(id)}"
    
    

def is_valid_log_entry(log_entry):
    # if "Killers have been revealed - " in log_entry: return True
    if not "Round type is" in log_entry: return False
    if not "Killers have been set - " in log_entry: return False
    return True

def monitor_round_types(log_file, round_types):
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
                    killers = map(lambda k: get_terror_name(round, k), killers_indexes)
                    print(f"{round} : {list(killers)}")


                
                if is_valid_log_entry(log_entry):
                    # Get round name
                    round = log_entry.split("Round type is ")[1].rstrip('\n')

                    # Get Killer names
                    # print(log_entry.split("Killers have been set - "))
                    # continue
                    killers_indexes = log_entry.split("Killers have been set - ")[1].split("//")[0].rstrip(' ').split(" ")
                    killers = map(lambda k: get_terror_name(round, k), killers_indexes)
                    
                    # Append the round type to the list
                    rounds.append(round)
                    print(f"{round} : {list(killers)}")
                
            # Count the number of each round type    
            # get_round_type_count(rounds)

            last_position = new_position
        
        time.sleep(1)
        

# # Current round types in game
round_types = [
    'Classic', 'Fog', 'Punished', 'Sabotage', 'Cracked', 'Alternate',
    'Bloodbath', 'Midnight', 'Mystic Moon', 'Twilight', 'Solstice', 
    '8 Pages', 'Blood Moon', 'Unbound'
]

# # Directory and file search UPDATED becuase some people's getlogin function EXPLODED so we're doing it this way now :3
log_directory = os.path.join(os.path.expanduser("~"), "AppData", "LocalLow", "VRChat", "VRChat")
latest_log_file = find_latest_log(log_directory)

if latest_log_file:
    monitor_round_types(latest_log_file, round_types)

    
