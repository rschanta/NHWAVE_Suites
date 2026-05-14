import os
import nhwave_amp as fds



#%% MAIN
d = fds.setup_key_dirs(name='2026_05_13_A',
                   main_dir = '.', 
                   input_dir = '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_A/inputs', 
                   log_dir='/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_A/logs',
                   bathy_dir = '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_A/bathy',
                   station_dir = '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_A/stations',
                   friction_dir= '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_A/friction',
                   result_folder_dir = '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_A/output_raw',
                   nc_dir = '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_A/nc_files',
                   nc_sta_dir='/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_A/nc_sta_files',
                   NH_ex = "/mmfs1/gscratch/derakhti/users/rschanta/models/NHWAVE/NHWAVE_JIM/src/nhwave",
                   conda = "schpy",
                   input_sum_dir='/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_A/input_summary',
                   dir_add_ons={'figs': '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_A/figures'})
