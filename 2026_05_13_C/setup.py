import os
import nhwave_amp as fds



#%% MAIN
d = fds.setup_key_dirs(name='2026_05_13_C',
                   main_dir = '.', 
                   input_dir = '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_C/inputs', 
                   log_dir='/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_C/logs',
                   bathy_dir = '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_C/bathy',
                   station_dir = '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_C/stations',
                   friction_dir= '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_C/friction',
                   result_folder_dir = '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_C/output_raw',
                   nc_dir = '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_C/nc_files',
                   nc_sta_dir='/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_C/nc_sta_files',
                   NH_ex = "/mmfs1/gscratch/derakhti/users/rschanta/models/NHWAVE/NHWAVE_JIM/src/nhwave",
                   conda = "schpy",
                   input_sum_dir='/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_C/input_summary',
                   dir_add_ons={'figs': '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_C/figures'})
