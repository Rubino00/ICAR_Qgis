import requests as rq
import geopandas as gpd
import os

# Estraiamo i dati relativi ai fogli serie 50.000 presente nella cartella di Qgis sottoforma di shapefile
dataf_base = gpd.read_file ("C:\\Users\\fraru\\OneDrive\\Desktop\\Qgis\\PPTR\\PPTR_sistema_tutele_qgis_20230801\\base\\serie_50_Puglia.shp")

# definiamo una lista cotenente tutti i figli a 50.000 della regione Puglia. Tale lista verrà quindi elaborata per scaricare 
# tutti i fogli della carta di uso del suolo
list_sheet = list (dataf_base ["SHEET"])
len_list = len (list_sheet)
print (list_sheet)

# link generico per scaricare le carte di uso del suolo della regione Puglia dal sito "SIT PUGLIA"
# http://cartografia.sit.puglia.it/download/UDS_2011/493-UDS-2011.zip
# link generico per scaricare l'aggiornamento dell'urbanizzato della Puglia
# http://cartografia.sit.puglia.it/download/URB_2011/493-URB-2011.zip

dir_path = "C:\\Users\\fraru\\OneDrive\\Desktop\\UNIVERSITA'\\magistrale\\ICAR_Qgis\\Materiali\\Prodotto_da_me\\UDS_Puglia_intera"

i = 1
# per ogni foglio vado a scaricare i file relativi
for sheet in list_sheet:
    link = "http://cartografia.sit.puglia.it/download/UDS_2011/" + sheet + "-UDS-2011.zip"
    request = rq.get (link)
    
    if request.status_code == 200:
        file_path = dir_path + "\\" + sheet + ".zip"
        with open (file_path , "wb") as file:
            file.write (request.content)
        print ("ok, " + str (i) + " di " + str (len_list))
    else:
        print ("errore, " + str (i) + " di " + str (len_list))
        
    i = i + 1