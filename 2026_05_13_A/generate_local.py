import model_code_2D as mod
import nhwave_amp as nh



#%% Load in environment variable
from dotenv import load_dotenv
load_dotenv('./envs/Hopkins_2D_new.env') 



design_matrix = mod.get_design_matrix()

function_set = [mod.get_hydrodynamics,
                mod.unpack_bathy,
                mod.setup_domain,
                mod.set_time]



# Filter functions
filter_functions = []

# Plot functions
plot_functions = [mod.plot_domain_setup]

# Print functions
print_functions = [nh.print_DEPTH_FILE]

df_pass,df_fail = nh.process_design_matrix(matrix_dict = design_matrix,
                                    function_set = function_set, 
                                    filter_sets = filter_functions,
                                    plot_sets = plot_functions,
                                    print_sets = print_functions,
                                    summary_formats = ['parquet','csv'])