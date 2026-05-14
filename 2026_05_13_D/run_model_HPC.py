from dotenv import load_dotenv
import nhwave_amp.HPC.UW_slurm as nh



#%% SETUP
# Load in environment variables
env_file = './envs/2026_05_13_D.env'
load_dotenv(env_file)  

# Specify default parameters
params = {
            'account': 'derakhti',
            'partition': 'compute-bigmem',
            'walltime': '1-07:00:00',
            'ntasks_per_node': '40',
            'mem': '50G',
            'env': env_file
            
        }

#%% PIPELINE
# GENERATE FILES

gen_path = '/mmfs1/gscratch/derakhti/users/rschanta/myprojects/NHWAVE_Suites/2026_05_13_D/generate_HPC.py'
params_gen = params.copy()
params_gen['walltime'] = '2:00:00'

batch_name = nh.write_batch(template_name = 'P.j2',
                                params = params_gen, 
                                name = 'generate',
                                other_params = {'python_script': gen_path})
job_id = nh.submit_slurm_job(batch_name)

# RUN NHWAVE

params_run = params.copy()
comp_path = '/mmfs1/gscratch/derakhti/users/rschanta/myprojects/NHWAVE_Suites/2026_05_13_D/comp.py'
params_run['array'] = '1-12'
params_run['dependency'] = job_id
batch_name = nh.write_batch(template_name = 'NH_P_a.j2', 
                                params = params_run, 
                                name = 'run',
                                other_params = {'python_script': comp_path})
job_id = nh.submit_slurm_job(batch_name)

    