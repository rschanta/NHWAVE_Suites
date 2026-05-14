import os
import nhwave_amp as fds



#%% MAIN
d = fds.setup_key_dirs(name='2026_05_13_B',
                   main_dir = '.', 
                   input_dir = '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_B/inputs', 
                   log_dir='/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_B/logs',
                   bathy_dir = '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_B/bathy',
                   station_dir = '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_B/stations',
                   friction_dir= '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_B/friction',
                   result_folder_dir = '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_B/output_raw',
                   nc_dir = '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_B/nc_files',
                   nc_sta_dir='/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_B/nc_sta_files',
                   NH_ex = "/mmfs1/gscratch/derakhti/users/rschanta/models/NHWAVE/NHWAVE_JIM/src/nhwave",
                   conda = "schpy",
                   input_sum_dir='/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_B/input_summary',
                   dir_add_ons={'figs': '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_B/figures'})
