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


paths = [["./calvin-network-data/data/sacramento-river/central-basin-east/sr_fol/elevation_area_capacity.csv", "./Folsom_Area_Capacitance.csv"],
         ["./calvin-network-data/data/tulare-lake/uplands/sr_pnf/elevation_area_capacity.csv", "./Pine_Flat_Area_Capacitance.csv"],
         ["./calvin-network-data/data/north-coast/lower-klamath/sr_cle/elevation_area_capacity.csv", "./Clair_Engle_Area_Capacitance.csv"],
         ["./calvin-network-data/data/sacramento-river/northwest-valley/sr_whi/elevation_area_capacity.csv", "./Whiskey_Town_Area_Capacitance.csv"],
         ["./calvin-network-data/data/sacramento-river/northeast-valley/sr_sha/elevation_area_capacity.csv", "./Shasta_Lake_Area_Capacitance.csv"],
         ["./calvin-network-data/data/sacramento-river/northwest-valley/sr_blb/elevation_area_capacity.csv", "./Black_Butte_Area_Capacitance.csv"],
         ["./calvin-network-data/data/sacramento-river/central-basin-west/sr_clk_inv/elevation_area_capacity.csv", "./Clear_Indian_Valley_Area_Capacitance.csv"],
         ["./calvin-network-data/data/sacramento-river/southeast/sr_eng/elevation_area_capacity.csv", "./Englebright_Area_Capacitance.csv"],
         ["./calvin-network-data/data/sacramento-river/southeast/sr_oro/elevation_area_capacity.csv", "./Oroville_Area_Capacitance.csv"],
         ["./calvin-network-data/data/sacramento-river/southwest/sr_ber/elevation_area_capacity.csv", "./Berryessa_Area_Capacitance.csv"],
         ["./calvin-network-data/data/sacramento-river/southeast/sr_bul/elevation_area_capacity.csv", "./Bullards_Area_Capacitance.csv"],
         ["./calvin-network-data/data/san-joaquin-river/sierra-foothills/sr_nhg/elevation_area_capacity.csv", "./New_Hogan_Area_Capacitance.csv"],
         ["./calvin-network-data/data/san-joaquin-river/sierra-foothills/sr_par/elevation_area_capacity.csv", "./Pardee_Area_Capacitance.csv"],
         ["./calvin-network-data/data/sacramento-river/southeast/sr_cfw/elevation_area_capacity.csv", "./Camp_Far_West_Area_Capacitance.csv"],
         ["./calvin-network-data/data/san-joaquin-river/sierra-foothills/sr_nml/elevation_area_capacity.csv", "./New_Melones_Area_Capacitance.csv"],
         ["./calvin-network-data/data/san-joaquin-river/east-side-uplands/sr_mil/elevation_area_capacity.csv", "./Millerton_Area_Capacitance.csv"],
         ["./calvin-network-data/data/san-joaquin-river/east-side-uplands/sr_mcr/elevation_area_capacity.csv", "./McClure_Area_Capacitance.csv"],
         ["./calvin-network-data/data/san-joaquin-river/east-side-uplands/sr_hid/elevation_area_capacity.csv", "./Hensley_Area_Capacitance.csv"],
         ["./calvin-network-data/data/san-joaquin-river/east-side-uplands/sr_buc/elevation_area_capacity.csv", "./Eastman_Area_Capacitance.csv"],
         ["./calvin-network-data/data/san-joaquin-river/sierra-foothills/sr_dnp/elevation_area_capacity.csv", "./New_Don_Pedro_Area_Capacitance.csv"],
         ["./calvin-network-data/data/san-joaquin-river/sierra-foothills/sr_hth/elevation_area_capacity.csv", "./Hetch_Area_Capacitance.csv"],
         ["./calvin-network-data/data/tulare-lake/uplands/sr_isb/elevation_area_capacity.csv", "./Isabella_Area_Capacitance.csv"],
         ["./calvin-network-data/data/tulare-lake/uplands/sr_scc/elevation_area_capacity.csv", "./Success_Area_Capacitance.csv"]

         ]


for path in paths:
    correct_csv(path[0], path[1])

#
# # FOLSOM
# correct_csv("./calvin-network-data/data/sacramento-river/central-basin-east/sr_fol/elevation_area_capacity.csv", "./Folsom_Area_Capacitance.csv")
#
# # PINE FLAT
# correct_csv("./calvin-network-data/data/tulare-lake/uplands/sr_pnf/elevation_area_capacity.csv", "./Pine_Flat_Area_Capacitance.csv")
