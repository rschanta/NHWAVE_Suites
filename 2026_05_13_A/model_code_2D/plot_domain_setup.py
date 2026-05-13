import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import schanta_tools as sch
import textwrap

# TITLE: Add xarray attributes to plot textbox

import textwrap

# TITLE: Compact xarray attribute textbox

import textwrap

# TITLE: Compact textbox with optional red variables

import textwrap

# TITLE: Compact textbox with optional red variable section

def add_attrs_textbox(
    ax,
    var_dict,
    max_chars=80,
    fontsize=8,
    red_vars=None,
):

    if red_vars is None:
        red_vars = []

    red_attrs = []
    black_attrs = []

    # Build attribute strings
    for key, val in var_dict.items():

        if isinstance(val, float):
            val = f"{val:.3f}"

        elif isinstance(val, (str, int)):
            val = f"{val}"

        else:
            continue

        attr = f"{key} = {val}"

        if key in red_vars:
            red_attrs.append(attr)
        else:
            black_attrs.append(attr)

    # Combine and wrap
    red_text = textwrap.fill(" | ".join(red_attrs), width=max_chars)
    black_text = textwrap.fill(" | ".join(black_attrs), width=max_chars)

    # RED TOP BOX
    ax.text(
        0.5,
        0.98,
        red_text,
        transform=ax.transAxes,
        ha="center",
        va="top",
        fontsize=fontsize,
        color="red",
        bbox=dict(facecolor="white", edgecolor="red", alpha=0.8),
    )

    # BLACK BOTTOM BOX
    ax.text(
        0.5,
        0.02,
        black_text,
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=fontsize,
        color="black",
        bbox=dict(facecolor="white", edgecolor="black", alpha=0.8),
    )
def plot_domain_setup(var_dict):
    
    ## UNPACK -----------------------------------------------------------------
    # Important x values
    x_rock_begin    = var_dict['x_rock_begin']
    x_rock_end      = var_dict['x_rock_end']
    x_slope_begin   = var_dict['x_slope_begin']
    # Dimensionless geometry parameters
    PI_1            = var_dict['PI_1']
    PI_2            = var_dict['PI_2']
    # Size of Domain
    Mglob           = var_dict['Mglob']
    Nglob           = var_dict['Nglob']
    Kglob           = var_dict['Kglob']
    # Hydrodynamics
    L               = var_dict['L']
    # Iteration number
    ITER            = var_dict['ITER']
    
    # From the Domain Object
    DOM             = var_dict['DOM']
    x_coord         = DOM.x.values
    y_coord         = DOM.y.values
    h_coord         = DOM.h.values
    # Dimensionless geometry parameters
    PI_1            = var_dict['PI_1']
    PI_2            = var_dict['PI_2']
    BETA_1          = var_dict['BETA_1']
    
    # Hydrodynamics
    d               = var_dict['DEP']
    T               = var_dict['PER']
    a               = var_dict['AMP']
    L               = var_dict['L']
    
    # Dimensional geometry
    fr              = var_dict['freeboard']
    m               = var_dict['slope']
    
    # Spongebob big guy pants okay
    Sponge_East_Width = var_dict['Sponge_East_Width']
    # Path
    fig_path = os.getenv("figs")
    ## [END] UNPACK -----------------------------------------------------------
    
    

    
    ## PREPARE BATHY ----------------------------------------------------------
    X, Y = np.meshgrid(x_coord, y_coord, indexing='xy')
    
    # DOM.h is stored as (X, Y), but plotting wants (Y, X)
    Zplot = -h_coord.T
    ## [END] PREPARE BATHY ----------------------------------------------------
    
    
    ## FIGURE INITIALIZE ------------------------------------------------------
    fig, axes = plt.subplots(2,1,dpi=300, figsize=(8,8), sharex=True)
    
    ax = axes[0]

    
    red_vars=["AMP", "PER","DEP","BETA_1","IVTURB","IHTURB","MinDep",
              "VISCOUS_FLOW","TOTAL_TIME","Mglob","Nglob","Kglob","DX",
              "VISCOSITY","NON_HYDRO","PI_1","PI_2","TAU_1","slice_y_ind","PLOT_INTV"]
    ax.set_title(f'NHWAVE Trial {ITER:05d}\nBathymetry Setup')
    ## [END] TITLE ------------------------------------------------------------
    
    ## TEXTBOX ----------------------------------------------------------
    add_attrs_textbox(ax, var_dict, max_chars=110,red_vars=red_vars)
    #ax.set_xticks([])
    ax.set_yticks([])
    
    for spine in ax.spines.values():
        spine.set_visible(False)
    ## [END] LOWER TEXTBOX ----------------------------------------------------


    ## 2D SLICE ---------------------------------------------------------------
    ax = axes[1]
    hh = -h_coord.ravel()
    ax.plot(x_coord, hh,color='black',zorder=6)
    ax.axhline(0,color='blue',zorder=4)
    ax.fill_between(x_coord,hh,0,color='lightblue',zorder=3,alpha=0.4)
    ax.fill_between(x_coord,hh,1.1*np.min(hh),color='goldenrod',zorder=5)
    ax.set_ylim(1.1*np.min(hh),1.1*np.max(hh))
    ax.set_xlim(min(x_coord),max(x_coord))
    ax.set_xlabel('$x$')
    ax.set_ylabel('$z$')
    ax.axvline(x_coord[-1] - Sponge_East_Width,color='darkgreen')

    ## [END] 2D SLICE ---------------------------------------------------------
    
    
    ## SAVE OUT ---------------------------------------------------------------
    fig_name = f'fig_{ITER:05d}.png'
    fig_path = os.path.join(fig_path, fig_name)
    print(fig_path)
    fig.savefig(fig_path, bbox_inches='tight')
    ## [END] SAVE OUT ---------------------------------------------------------
    
    return