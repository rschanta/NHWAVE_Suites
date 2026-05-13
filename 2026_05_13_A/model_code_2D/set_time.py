def set_time(var_dict):
    ## UNPACK
    T     = var_dict['PER']
    TAU_1 = var_dict['TAU_1'] 
    TOTAL_TIME = TAU_1*T
    
    return {'TOTAL_TIME': TOTAL_TIME}
