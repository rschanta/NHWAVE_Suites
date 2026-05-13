import os
import nhwave_amp as nh



#%% MAIN
d = nh.setup_key_dirs(name='Hopkins_2D_new',
                   main_dir = '.', 
                   input_dir = './test_out/inputs', 
                   log_dir='./test_out/logs',
                   bathy_dir = './test_out/bathy',
                   station_dir = './test_out/stations',
                   friction_dir= './test_out/friction',
                   result_folder_dir = './test_out/output_raw',
                   nc_dir = './test_out/nc_files',
                   nc_sta_dir='./test_out/nc_sta_files',
                   NH_ex = ".",
                   conda = ".",
                   input_sum_dir='./test_out/input_summary',
                   dir_add_ons={'figs': './test_out/figures'})
