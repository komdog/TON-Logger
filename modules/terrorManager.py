terrors = [
    "huggy",  # 0
    "corrupted_toys",  # 1
    "demented_spongebob",  # 2
    "specimen_8",  # 3
    "her",  # 4
    "tails_doll",  # 5
    "black_sun",  # 6
    "aku_ball",  # 7
    "ao_oni",  # 8
    "torens_shadow",  # 9
    "censored",  # 10
    "whitenight",  # 11
    "an_arbiter",  # 12
    "specimen_5",  # 13
    "comedy",  # 14
    "purple_guy",  # 15
    "spongefly_swarm",  # 16
    "hush",  # 17
    "mope_mope",  # 18
    "sawrunner",  # 19
    "imposter",  # 20
    "something",  # 21
    "starved",  # 22
    "the_painter",  # 23
    "the_guidance",  # 24
    "with_many_voices",  # 25
    "nextbots",  # 26
    "harvest",  # 27
    "smileghost",  # 28
    "karol_corpse",  # 29
    "mx",  # 30
    "big_bird",  # 31
    "dev_bytes",  # 32
    "luigi_and_luigi_dolls",  # 33
    "v2",  # 34
    "withered_bonnie",  # 35
    "the_boys",  # 36
    "something_wicked",  # 37
    "seek",  # 38
    "rush",  # 39
    "sonic",  # 40
    "bad_batter",  # 41
    "signus",  # 42
    "mirror",  # 43
    "legs",  # 44
    "mona_and_the_mountain",  # 45
    "judgement_bird",  # 46
    "slender",  # 47
    "maul-a-child",  # 48
    "garten_goers",  # 49
    "dont_touch_me",  # 50
    "specimen_2",  # 51
    "specimen_10",  # 52
    "the_lifebringer",  # 53
    "pale_association",  # 54
    "toy_enforcer",  # 55
    "tbh",  # 56
    "doombox",  # 57
    "christian_brutal_sniper",  # 58
    "nosk",  # 59
    "apocrean_harvester",  # 60
    "arkus",  # 61
    "cartoon_cat",  # 62
    "wario_apparition",  # 63
    "shinto",  # 64
    "hell_bell",  # 65
    "security",  # 66
    "the_swarm",  # 67
    "shiteyanyo",  # 68
    "bacteria",  # 69
    "tiffany",  # 70
    "hoovydundy",  # 71
    "haket",  # 72
    "akumii-kari",  # 73
    "lunatic_cultist",  # 74
    "sturm",  # 75
    "punishing_bird",  # 76
    "prisoner",  # 77
    "red_bus",  # 78
    "waterwraith",  # 79
    "astrum_aureus",  # 80
    "snarbolax",  # 81
    "all-around-helpers",  # 82
    "sakuya_izayoi",  # 83
    "arrival",  # 84
    "miros_birds",  # 85
    "bff",  # 86
    "lain",  # 87
    "scavenger",  # 88
    "tinky_winky",  # 89
    "tricky",  # 90
    "yolm",  # 91
    "red_fanatic",  # 92
    "dr_tox",  # 93
    "ink_demon",  # 94
    "retep",  # 95
    "those_olden_days",  # 96
    "sos",  # 97
    "bigger_boot",  # 98
    "the_pursuer",  # 99
    "spamton",  # 100
    "immortal_snail",  # 101
    "charlotte",  # 102
    "herobrine",  # 103
    "peepy",  # 104
    "the_jester",  # 105
    "wild_yet_curious_creature",  # 106
    "manti",  # 107
    "horseless_headless_horsemann",  # 108
    "ghost_girl",  # 109
    "cubors_revenge",  # 110
    "the_origin",  # 111
    "beyond",  # 112
    "terror_of_nowhere",  # 113
    "fox_squad",
    "express_train_to_hell",  # 117
    "dog_mimic",  # 115
    "warden",  # 116
    "poly",  # 114
    "killer_fish",  # 118
    "deleted",  # 119
    "time_ripper",  # 120
    "malicious_twins",  # 121
    "parhelions_victims",  # 122
    "bed_mecha",  # 123
    "killer_rabbit",  # 124
    "random_flying_knife",  # 125
    "missingno",  # 126
    "living_shadow",  # 127
    "the_plague_doctor",  # 128
    "the_rat",  # 129
    "waldo",  # 130
    "clockey",
]

alternates = [
    "decayed_sponge",
    "whiteface",
    "sanic",
    "",
    "",
    "voidwalker",
    "knight_of_toren",
    "tragedy",
    "apathy",
    "mr_mega",
    "",
    "convict_squad",
    "paradise_bird",
    "angry_munci",
    "",
    "feddys",
    "tbh_spy",
    "",
    "lisa",
    "judas",
    "glaggle_gang",
    "try_not_to_touch_me",
    "ambush",
    "teuthida",
    "eggmans_announcement",
    "stgm",
    "army_in_black",
    "bliss",
    "roblander",
    "fusion_pilot",
    "walpurgisnacht",
    "",
    "sakuya_the_ripper",
    "dev_maulers",
    "the_red_mist",
    "overseer",
]

def get_terror_names(round_type, killers_indexes):
    match round_type:
        case "Alternate": return alternate(killers_indexes)
        case "Midnight": return midnight(killers_indexes)
        case  _: return standard(killers_indexes)

def standard(id):
    slot_0 = terrors[int(id[0])]
    slot_1 = terrors[int(id[1])] if not int(id[1]) == 0 else "<>"
    slot_2 = terrors[int(id[2])] if not int(id[1]) == 0 else "<>"
    return [ slot_0, slot_1, slot_2 ]

def alternate(id):
    slot_0 = alternates[int(id[0])]
    slot_1 = terrors[int(id[1])] if not int(id[1]) == "0" else "<>"
    slot_2 = terrors[int(id[2])] if not int(id[1]) == "0" else "<>"
    return [ slot_0, slot_1, slot_2 ]

def midnight(id):
    slot_0 = terrors[int(id[0])]
    slot_1 = terrors[int(id[1])] if not int(id[1]) == "0" else "<>"
    slot_2 = alternates[int(id[2])] if not int(id[1]) == "0" else "<>"
    return [ slot_0, slot_1, slot_2 ]

