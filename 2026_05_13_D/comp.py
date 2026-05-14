import nhwave_amp as nh
from dotenv import load_dotenv
print('Started comp.py')

env_file = './envs/2026_05_13_D.env'
load_dotenv(env_file)  
nh.get_into_netcdf(sigma_transform = True)

print('Finished comp.py')