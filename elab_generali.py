
import geopandas as gpd
import pandas as pd

dataf = gpd.read_file ("C:\\Users\\fraru\\OneDrive\\Desktop\\Qgis\\cartine shapefile e QGIS\\cartina dell'Italia x comuni\\Com2011_WGS84\\Com2011_WGS84.shp")

print ("colonne del dataframe")
print (dataf.columns)

dataf_Puglia = dataf [dataf ["COD_REG"] == 16]
print ("comuni della Puglia")
print (dataf_Puglia)

lista_comuni_16 = list (dataf_Puglia ["NOME"])

print ("elenco comuni della Puglia:")
print (lista_comuni_16)

print ("numero comuni della Puglia:")
print (len (lista_comuni_16))

dataf_comuni = pd.read_csv ("C:\\Users\\fraru\\OneDrive\\Desktop\\Qgis\\cartine shapefile e QGIS\\cartina dell'Italia x comuni\\Com2011_WGS84\\Elenco_comuni_Italiani_ISTAT.csv" , sep =";")
print (dataf_comuni)

print (dataf_comuni.columns)



