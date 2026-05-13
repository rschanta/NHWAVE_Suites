import numpy as np
import nhwave_amp as nh

def setup_domain(var_dict):
    ## UNPACK -----------------------------------------------------------------
    # Bathy arrays
    x       = var_dict['x']
    y       = var_dict['y']
    z       = var_dict['Z']
    # Hydrodynamic parameters
    d       = var_dict['DEP']
    L       = var_dict['L']
    # Dimensionless geometric parameters
    m       = var_dict['slope']
    PI_1    = var_dict['PI_1']
    PI_2    = var_dict['PI_2']
    Kglob   = var_dict['Kglob']
    # Dimensional geometric parameters
    fr      = var_dict['freeboard']
    # Grid size parameter
    BETA_1  = var_dict['BETA_1']
    # Sponge east width tag
    SEW_TAG = var_dict['SEW_TAG']
    ## [END] UNPACK -----------------------------------------------------------
    
    
    
    ## ENFORCE ARRAY SHAPES ---------------------------------------------------
    x = np.asarray(x)
    y = np.asarray(y)
    z = np.asarray(z)
    
    if z.ndim != 2:
        raise ValueError('Z must be 2D')
    
    if z.shape != (y.size, x.size):
        raise ValueError('Z must have shape (len(y), len(x))')
    ## [END] ENFORCE ARRAY SHAPES ----------------------------------------------
    
    
    
    ## PLACE ROCK IN FLUME ----------------------------------------------------
    x_rock_begin = x[0]
    x_rock_end   = x[-1]
    length_rock  = x_rock_end - x_rock_begin
    
    # Add distance before the rock
    L1  = PI_1*L
    x   = np.insert(x,0,x[0]-L1)
    z   = np.concatenate([z[:, [0]], z], axis=1)
    
    # Specify the end of the rock (or beginning of second flat portion)
    x_rock_end = x[-1]
    
    # Add distance after the rock
    L2 = PI_2*L
    x = np.append(x,x[-1]+L2)
    z = np.concatenate([z, z[:, [-1]]], axis=1)
    
    
    # Add slopeing portion
    x_slope_begin   = x[-1]
    x_shore         = x_slope_begin+(d)/m
    x_end           = x[-1]+(d+fr)/m
    x               = np.append(x,x_end)
    z_end           = np.full((z.shape[0],1), d+fr)
    z               = np.concatenate([z, z_end], axis=1)
    
    # Adjust so origin is at 0
    minx = np.min(x)
    x = x - minx
    x_rock_begin    = x_rock_begin - minx
    x_rock_end      = x_rock_end - minx
    x_slope_begin   = x_slope_begin - minx
    x_shore         = x_shore - minx
    x_end           = x_end - minx
    
    # Adjust z to be depth
    h = d - z
    ## [END] PLACE ROCK IN FLUME ----------------------------------------------
    
    
    ## INTERPOLATE TO TARGET DX -----------------------------------------------
    # Define resolution from beta_1
    DX = L/BETA_1
    DY = DX
    
    # Create x grid and y grid
    x_coord = DX*np.arange(np.ceil(x[-1]/DX)+1)
    y_coord = DY*np.arange(np.ceil((y[-1]-y[0])/DY)+1) + y[0]
    
    # Interpolate in x first
    h_x = np.empty((h.shape[0], x_coord.size))
    for j in range(h.shape[0]):
        h_x[j, :] = np.interp(x_coord, x, h[j, :])
    
    # Interpolate in y second
    h_coord = np.empty((y_coord.size, x_coord.size))
    for i in range(x_coord.size):
        h_coord[:, i] = np.interp(y_coord, y, h_x[:, i])
    
    # Length of arrays
    Mglob = np.size(x_coord)
    Nglob = np.size(y_coord)
    ## [END] INTERPOLATE TO TARGET DX -----------------------------------------
    
    ## ADD SPONGE LAYER
    if SEW_TAG == 'T':
        Sponge_East_Width = x_end - x_slope_begin
    else:
        Sponge_East_Width = 0
    
    ## CREATE THE DOMAIN OBJECT -----------------------------------------------
    DOM = nh.DomainObject(DX=DX, DY=DY,
                       Mglob=Mglob,
                       Nglob=Nglob,
                       Kglob=Kglob)
    DOM.z_from_2D_array(h_coord.T)
    ## [END] CREATE THE DOMAIN OBJECT -----------------------------------------
    
    
    return {'DOM': DOM, 'Mglob': Mglob, 'Nglob': Nglob, 'DX': DX,'DY': DY,
            'x_rock_begin': x_rock_begin,
            'x_rock_end': x_rock_end,
            'x_slope_begin': x_slope_begin, 
            'x_shore': x_shore,
            'x_end': x_end,
            'length_rock': length_rock,
            'x_coord': x_coord,
            'y_coord': y_coord,
            'h_coord': h_coord,
            'Sponge_East_Width': Sponge_East_Width
            }
