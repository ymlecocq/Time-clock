# Time & clock v1

import time

# epoch = début du temps, soit le 1er janvier 1970
# seconds = nombre de secondes depuis epcoch

mois = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Décembre"]
old_seconde = 0



# ---------------------------------------------------------------
running = True
while running :
    seconds = time.time()
    local_time = time.ctime(seconds)

    result = time.localtime(seconds)


    # print("Heure locale : ",local_time)
    # print(result)
    if old_seconde != result.tm_sec:
        print("Nous sommes le ", result.tm_mday," ",mois[result.tm_mon-1],result.tm_year,".")
        print("Il est ",result.tm_hour," heure",result.tm_min,"et ",result.tm_sec," secondes.")
        old_seconde = result.tm_sec