import pandas as pd
import numpy as np

def correct_csv(input, output):
    df = pd.read_csv(input)

    Elevation = df["elevation"]        # [ft]
    Area = df["area"]                  # [acres]
    Storage = df["capacity"]           # [thousand acre-feet]

    Elevation = Elevation * 0.3048     # [ft] --> [m]
    Storage = Storage * 1233481.8375   # [thousand acre-feet] --> [m^3]
    Area = Area * 0.4047               # [acres] --> [hectares]

    Output_data = {'Elevation_m': Elevation, 'Storage_m3': Storage, 'Area_ha': Area}
    Output_df = pd.DataFrame(data=Output_data)

    Output_df.to_csv(output, index=False)

# FOLSOM
correct_csv("./calvin-network-data/data/sacramento-river/central-basin-east/sr_fol/elevation_area_capacity.csv", "./Folsom_Area_Capacitance.csv")

# PINE FLAT
correct_csv("./calvin-network-data/data/tulare-lake/uplands/sr_pnf/elevation_area_capacity.csv", "./Pine_Flat_Area_Capacitance.csv")
