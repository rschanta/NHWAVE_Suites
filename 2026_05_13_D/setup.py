import os
import nhwave_amp as fds



#%% MAIN
d = fds.setup_key_dirs(name='2026_05_13_D',
                   main_dir = '.', 
                   input_dir = '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_D/inputs', 
                   log_dir='/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_D/logs',
                   bathy_dir = '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_D/bathy',
                   station_dir = '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_D/stations',
                   friction_dir= '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_D/friction',
                   result_folder_dir = '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_D/output_raw',
                   nc_dir = '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_D/nc_files',
                   nc_sta_dir='/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_D/nc_sta_files',
                   NH_ex = "/mmfs1/gscratch/derakhti/users/rschanta/models/NHWAVE/NHWAVE_JIM/src/nhwave",
                   conda = "schpy",
                   input_sum_dir='/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_D/input_summary',
                   dir_add_ons={'figs': '/mmfs1/gscratch/derakhti/users/rschanta/outputs/2026_05_13_D/figures'})
