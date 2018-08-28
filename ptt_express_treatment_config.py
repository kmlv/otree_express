############################################
#  accumulate experiments used down below.
#  make sure they are commented
############################################


############################################
# Date: April 13 2017
# Location: LEEPS
# Notes: TEST

real_world_currency_per_point = 1
participation_fee = 4.00,
num_demo_participants = 6
targetIncome = [10]
screenTime = 20
maxScreens = 20
pointDistMax = 120
pointDistMin = 20
num_readers = 0
reader_endowment = [3]
params = [ #direct, free, no message 
    {'treat': 'DM', 'val_typ': 'WTP', 'elic_met': 'BDM', 'BDM_typ': 'CONT', 'Met_par': [0, 'end'],  'end': [3, 3]},
    {'treat': 'FM', 'val_typ':  None, 'elic_met':  None, 'BDM_typ':   None, 'Met_par':        None, 'end': [3, 3]},
    {'treat': 'NM', 'val_typ':  None, 'elic_met':  None, 'BDM_typ':   None, 'Met_par':           None, 'end': [3, 3]}
]


    # {'treat': 'DM', 'val_typ': 'WTP', 'elic_met': 'BDM', 'BDM_typ': 'CONT', 'Met_par': [0, 'end'],  'end': [3, 3]},
    # {'treat': 'DM', 'val_typ': 'WTP', 'elic_met': 'BDM', 'BDM_typ': 'CONT', 'Met_par': [0, 'end'],  'end': [3, 3]},
    # {'treat': 'FM', 'val_typ':  None, 'elic_met':  None, 'BDM_typ':   None, 'Met_par':        None, 'end': [3, 3]},
    # {'treat': 'FM', 'val_typ':  None, 'elic_met':  None, 'BDM_typ':   None, 'Met_par':        None, 'end': [3, 3]},
    # {'treat': 'NM', 'val_typ':  None, 'elic_met':  None, 'BDM_typ':   None, 'Met_par':           None, 'end': [3, 3]},

# {'treat': 'TP', 'val_typ': 'WTP','elic_met': 'BDM', 'BDM_typ': 'CONT', 'Met_par': [0, 'end'], 'end': [3, 3]},
    # {'treat': 'DM', 'val_typ': 'WTA', 'elic_met': 'BDM', 'BDM_typ': 'CONT', 'Met_par': [0, 'end'],  'end': [3, 3]},
    # {'treat': 'FM', 'val_typ':  None, 'elic_met':  None, 'BDM_typ':   None, 'Met_par':        None, 'end': [3, 3]},
    # {'treat': 'NM', 'val_typ':  None, 'elic_met':  None, 'BDM_typ':   None, 'Met_par':           None, 'end': [3, 3]},
    # {'treat': 'FM', 'val_typ':  None, 'elic_met':  None, 'BDM_typ':   None, 'Met_par':           None, 'end': [3, 3]},
    # {'treat': 'NM', 'val_typ':  None, 'elic_met':  None, 'BDM_typ':   None, 'Met_par':           None, 'end': [3, 3]}    

    # {'treat': 'DM', 'val_typ': 'WTP', 'elic_met': 'BDM', 'BDM_typ': 'CONT', 'Met_par': [0, 'end'],  'end': [3, 3]},
	# {'treat': 'TP', 'val_typ': 'WTP','elic_met': 'BDM', 'BDM_typ': 'CONT', 'Met_par': [0, 'end'], 'end': [3, 3]},
	# {'treat': 'TP', 'val_typ': 'WTP','elic_met': 'BDM', 'BDM_typ': 'CONT', 'Met_par': [0, 'end'], 'end': [3, 3]},
	# {'treat': 'TP', 'val_typ': 'WTP','elic_met': 'BDM', 'BDM_typ': 'CONT', 'Met_par': [0, 'end'], 'end': [3, 3]}

   # {'treat': 'FM', 'val_typ':  None, 'elic_met':  None, 'BDM_typ':   None, 'Met_par':           None, 'end': [3, 3]},
   #  {'treat': 'NM', 'val_typ':  None, 'elic_met':  None, 'BDM_typ':   None, 'Met_par':           None, 'end': [3, 3]},
 
# ############################################
# # Date: April 6 2017
# # Location: LEEPS
# # Notes: DM 

# real_world_currency_per_point = 1
# participation_fee = 4.00
# num_demo_participants = 10
# targetIncome = [10]
# screenTime = 25
# maxScreens = 25
# pointDistMax = 100
# pointDistMin = 20
# num_readers = 0
# reader_endowment = [3]
# params = [
#     {'treat': 'DM', 'val_typ': 'WTA', 'elic_met': 'BDM', 'BDM_typ': 'LIST', 'Met_par': [0, 'end', 0.25],  'end': [3, 3]},
#     {'treat': 'DM', 'val_typ': 'WTA', 'elic_met': 'BDM', 'BDM_typ': 'LIST', 'Met_par': [0, 'end', 0.25],  'end': [3, 3]},
#     {'treat': 'DM', 'val_typ': 'WTA', 'elic_met': 'BDM', 'BDM_typ': 'LIST', 'Met_par': [0, 'end', 0.25],  'end': [3, 3]},
#     {'treat': 'DM', 'val_typ': 'WTA', 'elic_met': 'BDM', 'BDM_typ': 'LIST', 'Met_par': [0, 'end', 0.25],  'end': [3, 3]},
#     {'treat': 'DM', 'val_typ': 'WTA', 'elic_met': 'BDM', 'BDM_typ': 'LIST', 'Met_par': [0, 'end', 0.25],  'end': [3, 3]},
# ]

# real_world_currency_per_point = 1
# participation_fee = 4.00,
# num_demo_participants = 14
# targetIncome = [10]
# screenTime = 25
# maxScreens = 20
# pointDistMax = 100
# pointDistMin = 20
# num_readers = 0
# reader_endowment = [3]
# params = [
#     {'treat': 'DM', 'val_typ': 'WTA', 'elic_met': 'BDM', 'BDM_typ': 'LIST', 'Met_par': [0, 'end', 0.25],  'end': [3, 3]},
#     {'treat': 'DM', 'val_typ': 'WTP', 'elic_met': 'BDM', 'BDM_typ': 'LIST', 'Met_par': [0, 'end', 0.25],  'end': [3, 3]},
#     {'treat': 'DM', 'val_typ': 'WTA', 'elic_met': 'BDM', 'BDM_typ': 'CONT', 'Met_par': [0, 'end'], 'end': [3, 3]},
#     {'treat': 'DM', 'val_typ': 'WTP', 'elic_met': 'BDM', 'BDM_typ': 'CONT', 'Met_par': [0, 'end'], 'end': [3, 3]},
#     {'treat': 'FM', 'val_typ':  None, 'elic_met':  None, 'BDM_typ':   None, 'Met_par':           None, 'end': [3, 3]},
#     {'treat': 'NM', 'val_typ':  None, 'elic_met':  None, 'BDM_typ':   None, 'Met_par':           None, 'end': [3, 3]},
#     {'treat': 'FM', 'val_typ':  None, 'elic_met':  None, 'BDM_typ':   None, 'Met_par':           None, 'end': [3, 3]}
# ]


# ############################################
# # Date: Nov 22 2016
# # Location: LEEPS
# # Notes: DM BDM WTA LIST
#
# real_world_currency_per_point = 1
# participation_fee = 4.00,
# num_demo_participants = 10
# targetIncome = [7]
# num_readers = 0
# reader_endowment = [3]
# params = [
#     {'treat': 'DM', 'val_typ': 'WTA', 'elic_met': 'BDM', 'BDM_typ': 'LIST', 'Met_par': [0, 'end', 0.2],  'end': [3, 3]},
#     {'treat': 'DM', 'val_typ': 'WTA', 'elic_met': 'BDM', 'BDM_typ': 'LIST', 'Met_par': [0, 'end', 0.2],  'end': [3, 3]},
#     {'treat': 'DM', 'val_typ': 'WTA', 'elic_met': 'BDM', 'BDM_typ': 'LIST', 'Met_par': [0, 'end', 0.2],  'end': [3, 3]},
#     {'treat': 'DM', 'val_typ': 'WTA', 'elic_met': 'BDM', 'BDM_typ': 'LIST', 'Met_par': [0, 'end', 0.2],  'end': [3, 3]},
#     {'treat': 'DM', 'val_typ': 'WTA', 'elic_met': 'BDM', 'BDM_typ': 'LIST', 'Met_par': [0, 'end', 0.2],  'end': [3, 3]},
# ]

#######################################

# ############################################
# # Date: Oct 28 2016
# # Location: LEEPS
# # Notes: Pilot all DM BDM
#
# real_world_currency_per_point = 1
# participation_fee = 5.00,
# num_demo_participants = 10
# targetIncome = [7]
# num_readers = 0
# reader_endowment  = [3]
# params = [
#     {'treat': 'DM', 'val_typ': 'WTP', 'elic_met': 'BDM', 'BDM_typ': 'CONT', 'Met_par': [0, 'end'],  'end': [3, 3]},
#     {'treat': 'DM', 'val_typ': 'WTP', 'elic_met': 'BDM', 'BDM_typ': 'CONT', 'Met_par': [0, 'end'],  'end': [3, 3]},
#     {'treat': 'DM', 'val_typ': 'WTP', 'elic_met': 'BDM', 'BDM_typ': 'CONT', 'Met_par': [0, 'end'],  'end': [3, 3]},
#     {'treat': 'DM', 'val_typ': 'WTP', 'elic_met': 'BDM', 'BDM_typ': 'CONT', 'Met_par': [0, 'end'],  'end': [3, 3]},
#     {'treat': 'DM', 'val_typ': 'WTP', 'elic_met': 'BDM', 'BDM_typ': 'CONT', 'Met_par': [0, 'end'],  'end': [3, 3]},
# ]
# #######################################