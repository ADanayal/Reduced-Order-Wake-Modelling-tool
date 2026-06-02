# Importing general python libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr
import math

# Importing specific PyWake classes
from py_wake.site import XRSite
from py_wake.site.shear import PowerShear
from py_wake.site.xrsite import UniformSite
from py_wake.wind_turbines import WindTurbine, WindTurbines
from py_wake.wind_turbines.power_ct_functions import PowerCtTabular                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
from py_wake.literature.noj import Jensen_1983
from py_wake.literature.gaussian_models import Bastankhah_PorteAgel_2014,  Niayifar_PorteAgel_2016, Zong_PorteAgel_2020
from py_wake.literature.gaussian_models import Blondel_Cathelain_2020 
from py_wake.literature.turbopark import Nygaard_2022
from py_wake.deficit_models.noj import TurboNOJDeficit
from py_wake.turbulence_models.crespo import CrespoHernandez
from py_wake.superposition_models import LinearSum
from py_wake.superposition_models import SquaredSum
from py_wake.superposition_models import MaxSum
from py_wake.superposition_models import WeightedSum
from py_wake.superposition_models import SqrMaxSum
from py_wake.wind_farm_models.engineering_models import PropagateDownwind
from py_wake.deficit_models.utils import ct2a_mom1d
from py_wake.deflection_models import JimenezWakeDeflection, fuga_deflection, GCLHillDeflection

from py_wake.deficit_models import TurboGaussianDeficit
from py_wake.superposition_models import SquaredSum
from py_wake.ground_models import Mirror
from py_wake.rotor_avg_models import GaussianOverlapAvgModel
from py_wake.wind_farm_models import PropagateDownwind




def setup_wind_farm_model(site, wind_turbines, model):

    match model:
        case "Jensen1983":
            wind_farm_model = \
                Jensen_1983(
                    site,
                    wind_turbines
                )
            
        case "Jensen1983_LS":
            wind_farm_model = \
                Jensen_1983(
                    site,
                    wind_turbines, 
                    superpositionModel = LinearSum()
                    
                 )
            
        case "BPA2014":
            wind_farm_model = \
                Bastankhah_PorteAgel_2014(
                    site,
                    wind_turbines,
                    k=0.0324555,
                    turbulenceModel=CrespoHernandez(),
                    
                )

        case "NPA2016":
            wind_farm_model = \
                Niayifar_PorteAgel_2016(
                    site,
                    wind_turbines,
                    a=[0.3837, 0.003678],
                    ceps=.2,
                    superpositionModel=LinearSum(),
                    turbulenceModel=CrespoHernandez(ct2a=ct2a_mom1d, c=[0.73, 0.8325, 0.0325, -0.32], addedTurbulenceSuperpositionModel=SqrMaxSum())   
                )
        case "Nygaard2022":
            wind_farm_model = \
                Nygaard_2022(
                    site,
                    wind_turbines,
                )
            
        case "Nygaard2022_A0.06":

            wake_deficitModel = TurboGaussianDeficit(
                ct2a=ct2a_mom1d,
                A=0.06,   
                groundModel=Mirror(superpositionModel=SquaredSum()),
                rotorAvgModel=GaussianOverlapAvgModel(),
                ctlim=0.96
            )

            wake_deficitModel.WS_key = "WS_jlk"

            wind_farm_model = PropagateDownwind(
                site,
                wind_turbines,
                wake_deficitModel=wake_deficitModel,
                superpositionModel=SquaredSum()
            
            )

        case "ZPA2020":
            wind_farm_model = \
                Zong_PorteAgel_2020(
                    site,
                    wind_turbines,
                    a=[0.38, 4e-3],
                    deltawD=1./np.sqrt(2),
                    lam=7.5,
                    B=3,
                    rotorAvgModel=None,
                    superpositionModel=WeightedSum(),
                    deflectionModel=None,
                    turbulenceModel=CrespoHernandez(),
                    groundModel=None,
                    use_effective_ws=True,
                    use_effective_ti=True
                )





        case "CustomPropagateDownwind":
            wind_farm_model = \
                PropagateDownwind(
                    site,
                    wind_turbines,
                    wake_deficitModel = TurboNOJDeficit(),
                    superpositionModel = SquaredSum(),
                    turbulenceModel = CrespoHernandez()
                )
        case _:
            raise TypeError(f"Farm model type {model} not implemented")
        
    # return the wind farm model object
    return wind_farm_model







def get_wind_turbine():

    # Geometric data
    D = 279.9
    HUB_HEIGHT = 169.9

    # Turbine power and thrust coefficient curves.
    # From Frazer-Nash report (Uprated to 20.4 MW and smoothed)
    u_ct_power = np.array([
        [      0,    0.00000,    0.0000 ],
        [      1,    0.00000,    0.0000 ],
        [      2,    0.00000,    0.0000 ],
        [      3,    0.81905,    0.1142 ],
        [      4,    0.80549,    0.8767 ],
        [      5,    0.82208,    2.0242 ],
        [      6,    0.83362,    3.7534 ],
        [      7,    0.80727,    6.1091 ],
        [      8,    0.80322,    9.1795 ],
        [      9,    0.80269,   12.8167 ],
        [     10,    0.74859,   16.7785 ],
        [     11,    0.60935,   19.4770 ],
        [     12,    0.42305,   20.3622 ],
        [     13,    0.32184,   20.4080 ],
        [     14,    0.25107,   20.4080 ],
        [     15,    0.20179,   20.4080 ],
        [     16,    0.16833,   20.4080 ],
        [     17,    0.13916,   20.4080 ],
        [     18,    0.11515,   20.4080 ],
        [     19,    0.09995,   20.4080 ],
        [     20,    0.08495,   20.4080 ],
        [     21,    0.07233,   20.4080 ],
        [     22,    0.06339,   20.4080 ],
        [     23,    0.05605,   20.4080 ],
        [     24,    0.05015,   20.4080 ],
        [     25,    0.04052,   20.4080 ],
        [     26,    0.02867,   20.2810 ],
        [     27,    0.02599,   19.6233 ],
        [     28,    0.02354,   17.8386 ],
        [     29,    0.02106,   14.5123 ],
        [     30,    0.01677,   10.4405 ]
    ])

    # Unpacking to instantiate WindTurbine object
    u       = u_ct_power.T[0]
    ct      = u_ct_power.T[1]
    power   = u_ct_power.T[2]

    wind_turbine = WindTurbine( name = 'IEA15MW_smoothed_uprated',
                                diameter = D,
                                hub_height = HUB_HEIGHT,
                                powerCtFunction = PowerCtTabular(u,power,'MW',ct))
    
    return wind_turbine





def get_wind_turbines():
    # Set the wind turbine objects for each farm
    # wind_turbine_farmA
    # wind_turbine_farmB
    wind_turbine_farmA = get_wind_turbine()
    wind_turbine_farmB = get_wind_turbine()

    # Create a list of wind turbine types from a list
    wind_turbines = WindTurbines.from_WindTurbine_lst(
            [
                wind_turbine_farmA,
                wind_turbine_farmB
            ]
        )
    wind_turbines._names = ["Farm A","Farm B"]

    return wind_turbines





def get_uniform_site(ti):

    # Create the UniformSite object
    my_uniform_site = UniformSite(ti=ti)

    # Return the UniformSite object
    return my_uniform_site







def generate_farm_arrays(farm_distance):
    # Set parameters
    nx = 7
    ny = 7
    Sx = 7.7
    D = 279.9

    # Generate farm A coordinates
    xA, yA = generate_uniform_array(nx, ny, Sx, D)
    
    # Generate farm B coordinates
    y0_offset_farm_B = max(yA) + farm_distance*1000
    xB, yB = generate_uniform_array(nx, ny, Sx, D, y0=y0_offset_farm_B)

    # Return the coordinates of both farms A and B
    return xA, yA, xB, yB






def plot_wind_data(wind_data_df):

    time = wind_data_df["Time (h)"]
    ws = wind_data_df["Wind Speed (m/s)"]
    wd = wind_data_df["Wind Direction (deg)"]
    ws_mean = wind_data_df["Wind Speed (m/s)"].mean()
    wd_mean = wind_data_df["Wind Direction (deg)"].mean()

    # Plotting time series
    fig, ax1 = plt.subplots(figsize=(5,3))
    ax2 = ax1.twinx()
    ax1.plot(time, ws, '-b')
    ax1.hlines(ws_mean, xmin=time.min(), xmax=time.max(), colors='b', linestyles='dashed')
    ax1.text(time.min(), ws_mean + 0.1 , f"${ws_mean:.2f} m/s$", color='b' )
    ax1.set_ylabel("Wind speed, $m/s$", color='b')
    ax1.set_xlabel("Time, $h$")
    ax1.set_ylim([6,20])
    ax1.set_title("Wind speed and wind direction time series")
    plt.grid()
    ax2.plot(time, wd, '-g')
    ax2.hlines(wd_mean, xmin=time.min(), xmax=time.max(), colors='g', linestyles='dashed')
    ax2.text(time.max(), wd_mean - 2 , f"${wd_mean:.2f}$"+"$^{\circ}$", color='g', va='top', ha='right' )
    ax2.set_ylabel("Wind direction, $^{\circ}$", color='g')
    ax2.set_ylim([160,300])
    plt.tight_layout()
    plt.savefig(f"./wind_time_series.png")






def calc_power_shear(ws_ref_1, ws_ref_2, h_ref_1, h_ref_2):
    alpha = math.log(ws_ref_2/ws_ref_1)/math.log(h_ref_2/h_ref_1)
    return alpha 





def get_power_shear_profile(h, alpha, ws_ref, h_ref):
    ws = ws_ref*(np.array(h)/h_ref)**alpha
    return ws









# Code to generate farms, mainly square arrays
def generate_uniform_array(
    nx,
    ny,
    Sx,
    D,
    x0 = 0,
    y0 = 0,
    Sy = 0
):
    '''
    Function used to generate structured uniform arrays

    Parameters
    ----------
    nx : integer
        Number of turbines in x direction (west to east)
    ny : integer
        Number of turbines in y direction (south to north)
    Sx : float
        Distance between turbines in x direction (in turbine diameters)
    D : float
        Turbine diameter (in meters)
    
    Optional Parameters
    -------------------
    x0 : float
        Offset distance or x-coordinate of the turbine farthest south-west corner
    y0 : float
        Offset distance or y-coordinate of the turbine farthest south-west corner
    Sy : float
        Distance between turbines in y direction (in turbine diameters). By default equal to Sx
    '''

    # If Sy is not provided Sx value is used for uniform array
    if Sy==0:
        Sy = Sx

    # Generate the x and y locations for an square array (starts at 0)
    x_locs = np.linspace(0, Sx*D*(nx-1), nx)
    y_locs = np.linspace(0, Sy*D*(ny-1), ny)
    
    # Create an empty list to store the (x, y) coordinates for each turbine
    x = []
    y = []

    # Generate coordinates with turbine_model and turbine_status
    # Note: currently using the same model for the entire farm
    for yi in y_locs:
        for xi in x_locs:
            x.append(xi)
            y.append(yi)


    # Add offset if first reference turbine
    x = np.array(x) + x0 
    y = np.array(y) + y0 

    # Return x, y values for square array
    return x, y






def get_farm_A_coords():
    # Set parameters
    nx = 7
    ny = 7
    Sx = 7.7
    D = 279.9

    # Generate farm A coordinates
    xA, yA = generate_uniform_array(nx, ny, Sx, D)
    
    # Return the coordinates of both farms A and B
    return xA, yA





def get_configuration_coords(configuration):

    # Construct the file_name for current 'configuration'
    file_name = f"./farm_arrays/array_{configuration}_xy_rotated_translated.csv"

    # Read the file_name using pd.read_csv(file_name)
    array_df = pd.read_csv(file_name)

    # Get the x and y coordinates values into local lists
    x = array_df["x"].values 
    y = array_df["y"].values
    types = array_df["types"].values

    # Return the x and y coordinates
    return x, y, types



