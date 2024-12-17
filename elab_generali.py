
import geopandas as gpd

dataf = gpd.read_file ("C:\\Users\\fraru\\OneDrive\\Desktop\\UNIVERSITA'\\magistrale\\ICAR_Qgis\\Materiali\\Prodotto_da_me\\Carta_Uso_del_suolo_Taranto\\CDS_Taranto_2006\\CDS_Taranto_2006_ritagliato.shp")

corrisp_dict = {
    1: "superfici artificiali",
    2: "superfici agricole utilizzate",
    3: "superfici boscate ed altri ambienti naturali",
    4: "ambiente umido",
    5: "ambiente delle acque",
    9: "superfici non classificate"
}

dataf ["desc_L1"] = dataf ["L1_2006"].map (corrisp_dict)
print (dataf [["L1_2006" , "desc_L1"]])

