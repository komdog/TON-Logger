types = [
    'Classic', 
    'Fog', 
    'Punished', 
    'Sabotage', 
    'Cracked', 
    'Alternate',
    'Bloodbath', 
    'Midnight', 
    'Mystic Moon', 
    'Twilight', 
    'Solstice', 
    '8 Pages', 
    'Blood Moon', 
    'Unbound',
    'Ghost',
    'Run'
]

# Get the number of each occouring round type
def get_round_type_count(rounds):
    print('\n=========== TOTAL ROUND TYPES =========== \n')
    for type in types:
        counts = rounds.count(type)
        print(f"{type} : {counts}")