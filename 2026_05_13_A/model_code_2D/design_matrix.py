def get_design_matrix():
    nhwave_params = {
        
        "TITLE": {
            "TITLE": "None",
        },
        
    
        "DOMAIN AND GRID": {
            # Size of (x,y,z) (ie- number of points)
            "Mglob": "DYNAMIC",
            "Nglob": "1",
            "Kglob": "12",
            # Grid spacing in (x,y)
            "DX": "DYNAMIC",
            "DY": "DYNAMIC",
            # Processors for MPI topology
            "PX": "16",
            "PY": "1",
        },
    
    
        "TIME": {
            "TOTAL_TIME": "DYNAMIC",
            "PLOT_INTV": "0.1",
            "SCREEN_INTV": "10.0",
            "HOTSTART": 'F',
        },
        
        
        "BATHYMETRY": {
            "DEPTH_FILE": "DYNAMIC",
        },
        
    
        "BOTTOM ROUGHNESS": {
        },
        
        
        
    
        "NUMERICS": {
            "HIGH_ORDER": "SECOND",
            "TIME_ORDER": "SECOND",
            "CONVECTION": "HLPA",
            "HLLC": "F",
            "CFL": "0.5",
            "FROUDE_CAP": "10.0",
            "MinDep": "0.05"
        },
        
        "VISCOUS_NUMBER": {
            "VISCOUS_FLOW": "T",
            "VISCOUS_NUMBER": "0.166666"   ,
            "IVTURB": ["3", "10", "20"]  ,
            "IHTURB": "30",
            "VISCOSITY": "1.e-6",
            "Schmidt": "1.0",
            "Cvs": "0.001",
            "Chs": "0.001",
            "RNG": "T"
        },
        
        "NONHYDROSTATIC": {
            "NON_HYDRO": "T",
        },
    

    
        "BOUNDARY CONDITIONS": {
            "PERIODIC_X": "F",
            "PERIODIC_Y": "F",
            "BC_X0": "3",           # Left boundary condition
            "BC_Xn": "1",
            "BC_Y0": "1",
            "BC_Yn": "1",
            "BC_Z0": "1",
            "BC_Zn": "1",
        },
        
        
        "WAVEMAKER PARAMETERS": {
            # Type of Wavemaker
            "WAVEMAKER": "LEF_LIN",
                # Wavemaker: LEF/RIG/INT/FLU/WAV
                "AMP": ["1.50"],
                "PER": ["4.0"],
                "DEP": ["5.0"],
                "THETA": "0.0",
                "CUR": "0.0",
                "sd_return": "0.0",
                
                # INT wavemaker sources
                "Xsource_West": "0.0",
                "Xsource_East": "0.0",
                "Ysource_Suth": "0.0",
                "Ysource_Nrth": "0.0",
                
        },
    
    
        "SPONGE_LAYER": {
            "SPONGE_ON": 'T',
            "Sponge_West_Width": "0.0",
            "SEW_TAG": ['T','F'],
            "Sponge_South_Width": "0.0",
            "Sponge_North_Width": "0.0",
        },
    

    
    
        "OUTPUT": {
            "OUT_H": 'T',   # Water depth
            "OUT_E": 'T' ,  # Surface elevation 
            # Velocity
            "OUT_U": 'T',   # x Velocity
            "OUT_V": 'T',   # y Velocity
            "OUT_W": 'T',   # z Velocity
            "OUT_P": 'T',   # Dynamic Pressure
            # Turbulent Quantities
            "OUT_K": 'T',   # Turbulent Kinetic Energy
            "OUT_D": 'T',   # Turbulent Dissipation Rate
            "OUT_S": 'T',   # Shear Production
            "OUT_C": 'T',   # Eddy Viscosity
            "OUT_A": 'T',   # Reynolds Stress
            "OUT_T": 'T',   # Bottom Shear Stress
        },
        
        
        "CUSTOM PARAMETERS":{
             "slice_y_ind": ["460"],
             "freeboard": ["2.0"],
             "PI_1": "1.5",    # Length of L1 flat portion (in wavelengths)
             "PI_2": "1.50",    # Length of L2 flat portion (in wavelengths)
             "BETA_1": ["100","200"],  # DX = wavelength/ BETA_1
             "slope": "0.1",    # Slope of sloping portion
             "TAU_1": "25",    # Simulation time (in periods)
             "bathy_path": "/Users/ryanschanta/Work/Critical_Data/ROXSI/Hopkins Rock/3D_Processed/DEM3D_d6_T4_H0.5_clean.nc"
        }
    }
    
    return nhwave_params