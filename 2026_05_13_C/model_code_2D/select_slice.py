import xarray as xr

def unpack_bathy(var_dict):

    ## UNPACK
    bathy_path   = var_dict['bathy_path']
    slice_y_ind  = var_dict['slice_y_ind']
    mult_factor  = var_dict['mult_factor']
    # Open the dataset
    ds = xr.open_dataset(bathy_path)
    #ds = ds.isel(y_sd=[slice_y_ind])
    # Force dimension order
    Z_da = ds['Z_detrend'].transpose('y_sd', 'x_sd')
    
    # Unpack
    x = ds.x_sd.values
    y = ds.y_sd.values
    Z = mult_factor*Z_da.values
    print('3D')
    
    return {'x': x,'y': y,'Z': Z}