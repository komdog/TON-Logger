
import modules.terrorManager as database
from print_color import print

round_colors = {
    'Classic': 'white',
    'Fog': 'gray',
    'Punished': 'yellow',
    'Sabotage': 'green',
    'Cracked': 'putple',
    'Alternate': 'blue',
    'Bloodbath': 'red',
    'Midnight': 'red',
    'Mystic Moon': 'blue',
    'Twilight': 'yellow',
    'Solstice': 'green',
    '8 Pages': 'gray',
    'Blood Moon': 'red',
    'Unbound': 'orange',
    'Ghost': 'blue'
}

def is_standard_log_entry(log_entry):
    # if "Killers have been revealed - " in log_entry: return True
    if not "Round type is" in log_entry: return False
    if not "Killers have been set - " in log_entry: return False
    return True

def get_map_name(log_entry):
    round_data = log_entry.split("This round is taking place at ")[1].split(" and the round type is ")
    return round_data[0]

def get_round_type(log_entry):
    round_data = log_entry.split("This round is taking place at ")[1].split(" and the round type is ")
    return round_data[1].rstrip('\n')

# Get killer names
def get_killers(log_entry):
    killers_indexes = log_entry.split("Killers have been set - ")[1].split("//")[0].rstrip(' ').split(" ")
    return map(lambda k: database.get_terror_name(round, k), killers_indexes)


def get_round_info(log_entry):
    # Get Map Name and Round Type Name

    global map_name
    global round_type

    if 'This round is taking place at' in log_entry: 
        map_name = get_map_name(log_entry)
        round_type = get_round_type(log_entry)
        # print(f"{map_name} | {round_type}")

    # Get Killer names
    if "Killers have been set - " in log_entry:
        killers = get_killers(log_entry)
        log_print(map_name, killers, round_type)
        
    # Fog Round
    if "Killers is unknown" in log_entry:
        # round = log_entry.split("Round type is ")[1].rstrip('\n') # Round type is fog
        # print(f"Killer Will Be Revealed Soon...")
        pass

    # Get for round killers
    if "Killers have been revealed - " in log_entry:
        killers_indexes = log_entry.split("Killers have been revealed - ")[1].split("//")[0].rstrip(' ').split(" ")
        killers = map(lambda k: database.get_terror_name(round, k), killers_indexes)
        log_print(map_name, killers, round_type)


def log_print(map_name, killers, round_type):
    print(f"{map_name} {list(killers)}", tag=f'{round_type}', tag_color=f'{round_colors[round_type]}', color=f'{round_colors[round_type]}', background='grey')
