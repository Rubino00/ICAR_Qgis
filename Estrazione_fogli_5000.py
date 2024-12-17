
import requests as rq

# interfaccia utente
print ("ESTRAZIONE FOGLI 5.000")
print ("selezionare la carta che vuoi estrarre:")
print ("a. carta di uso del suolo")
print ("b. modello di elevazione digitale del terreno")
print ("c. carta tecnica regionale")

comando = input ("selezionare opzione")

# condizioni che definiscono i parametri di input per l'estrazione della carta
if comando == "a":
    init_link = "http://cartografia.sit.puglia.it/download/UDS/SHP/"
    final_link = "_uds.zip"
    
if comando == "b":
    init_link = "http://cartografia.sit.puglia.it/download/DTM/ASC/"
    final_link = "_asc.zip"
    
if comando == "c":
    init_link = "http://cartografia.sit.puglia.it/download/CTR/SHP/"
    final_link = "_ctr.zip"
    
file_path = input ("inserire il percorso del file .txt che contiene l'elenco dei fogli da estrarre")
dir_output = input ("inserisci il percorso della cartella finale dove vuoi destinare tutti i fogli così scaricati")
file = open (file_path , "r")

text = file.readlines ()[1:]
sheet_list = []

for row in text:
    sheet_list.append (row [0:6])

print ("lista dei fogli:")
print (sheet_list)

# elenco url: 
# CTR regione Puglia: http://cartografia.sit.puglia.it/download/CTR/SHP/493/493013_ctr.zip
# DEM regione Puglia: http://cartografia.sit.puglia.it/download/DTM/ASC/493/493013_asc.zip
# UDS Regione Puglia: http://cartografia.sit.puglia.it/download/UDS/SHP/510/510111_uds.zip

gen_link_name = init_link
link_list = []

for sheet in sheet_list:
    url_path = gen_link_name + sheet [0:3] + "/" + sheet + final_link
    link_list.append (url_path)
    
print ("\nlista dei link agli zip:")
print (link_list)

print ("\n")
i = 0
for link in link_list:
    request = rq.get (link)
    
    if request.status_code == 200:
        path_output_file = dir_output + "\\" + sheet_list [i] + ".zip"
        with open (path_output_file , "wb") as file:
            file.write (request.content)
        i = i + 1
        
        print ("ok")
    else:
        print ("errore")
    