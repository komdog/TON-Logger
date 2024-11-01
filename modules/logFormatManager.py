
import modules.terrorManager as database
from colored import Fore, Back, Style

round_colors = {
    'Classic': f'{Style.BOLD}{Fore.rgb(255,255,255)}',
    'Fog': f'{Style.BOLD}{Fore.rgb(150,150,150)}',
    'Punished': f'{Style.BOLD}{Fore.rgb(255,200,0)}',
    'Sabotage': f'{Style.BOLD}{Fore.rgb(0,255,0)}',
    'Cracked': f'{Style.BOLD}{Fore.rgb(255,10,255)}',
    'Alternate': f'{Style.BOLD}{Fore.rgb(202,235,255)}',
    'Bloodbath': f'{Style.BOLD}{Fore.rgb(220,0,0)}',
    'Midnight': f'{Style.BOLD}{Fore.rgb(255,0,0)}',
    'Mystic Moon': f'{Style.BOLD}{Fore.rgb(100,100,255)}',
    'Twilight': f'{Style.BOLD}{Fore.rgb(255,255,255)}',
    'Solstice': f'{Style.BOLD}{Fore.rgb(255,255,255)}',
    '8 Pages': f'{Style.BOLD}{Fore.rgb(255,255,255)}',
    'Blood Moon': f'{Style.BOLD}{Fore.rgb(255,0,0)}',
    'Unbound': f'{Style.BOLD}{Fore.rgb(255,100,0)}',
    'Run': f'{Style.BOLD}{Fore.rgb(255,180,0)}',
    'Ghost': f'{Style.BOLD}{Fore.rgb(200,200,255)}',
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
def get_killers(round_type, log_entry):
    killers_indexes = log_entry.split("Killers have been set - ")[1].split("//")[0].rstrip(' ').split(" ")
    return database.get_terror_names(round_type, killers_indexes)

def get_killers_fog(round_type, log_entry):
    killers_indexes = log_entry.split("Killers have been revealed - ")[1].split("//")[0].rstrip(' ').split(" ")
    return database.get_terror_names(round_type, killers_indexes)

def get_round_info(log_entry):
    # Get Map Name and Round Type Name

    global map_name
    global round_type

    if 'is Run' in log_entry: 
        map_name = get_map_name(log_entry)
        round_type = get_round_type(log_entry)
        killers = database.get_terror_names(round_type, [267,0,0])
        log_print(map_name, killers, round_type)

    if 'This round is taking place at' in log_entry: 
        map_name = get_map_name(log_entry)
        round_type = get_round_type(log_entry)

    # Get Killer names
    if "Killers have been set - " in log_entry:
        killers = get_killers(round_type, log_entry)
        if round_type == 'Mystic Moon': killers = ['Psychosis']
        log_print(map_name, killers, round_type)
        
    # Fog Round
    if "Killers is unknown" in log_entry:
        round = log_entry.split("Round type is ")[1].rstrip('\n') # Round type is fog

    # Get fog round killers
    if "Killers have been revealed - " in log_entry:
        print('a')
        print(round_type)
        killers = get_killers_fog(round_type, log_entry)
        log_print(map_name, killers, round_type)


def log_print(map_name, killers, round_type):
    color: str = round_colors[round_type]
    print(f"{color} [{round_type}] {map_name} {killers} {Style.reset}")
