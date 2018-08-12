#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
import time
import datetime

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))
"""
================================================================
ATTENTION utilise la carte audio raspiaudioPlus (raspiaudio.com)
led : pin 22, gpio25
bouton poussoir : pin 16, gpio23

=================================================================
La radio est composée :
      - A: d'une tâche de fond wL lancée au démarrage (non modifiable)
      - B: l'interface Snips (modifiable)
      il contient des noms des stations radios accessibles 
               - dans le slot "radioName" de type custom "stations"
               - dans le dictionnaire "links" qui contient aussi les liens vers les stations
               (attention les valeurs de "stations" et les clés de "links" doivent être strictement identiques!)
      A et B se synchronisent par 4 fichiers:
               - volume : le volume (de 0 à 10)
               - link : le lien vers la radio
               - live : l'état du système
                    = 0     arrêt
                    = 1     1ere station demandée
                    = 2     nouvelle station demandée
                    = 3     nouveau volume demandé
                    = 4     station en cours de diffusion
                    = 5     arrêt immédiat demandé
                    = 6     arrêt temporisé demandé
                   
                    
                - delay : valeur du délai avant arrêt (en secondes) 
                
"""                    
def PyString(s) :
      if s[len(s)-1] == '\0' :
            s = s[0:len(s)-1]
      return s
      
def CString(s):
      if s[len(s)-1] != '\0' :
            s = s + '\0'
      return s 

def intents_callback(hermes, intentMessage) : 
    links = {"RFI":"http://live02.rfi.fr/rfimonde-96k.mp3",\
             "France Culture":"http://direct.franceculture.fr/live/franceculture-midfi.mp3",\
             "FIP":"http://direct.fipradio.fr/live/fip-midfi.mp3",\
             "RMC":"http://rmc.bfmtv.com/rmcinfo-mp3",\
             "RTL":"http://streaming.radio.rtl.fr/rtl-1-44-96",\
             "France Info":"http://direct.franceinfo.fr/live/franceinfo-midfi.mp3",\
             "Radio Classic":"http://broadcast.infomaniak.net:80/radioclassique-high.mp3",\
             "France Musique":"http://direct.francemusique.fr/live/francemusique-midfi.mp3",\
             "Jazz Radio":"http://broadcast.infomaniak.net:80/jazzradio-high.mp3",\
             "Europe1":"http://mp3lg3.scdn.arkena.com/10489/europe1.mp3",\
             "Sud Radio":"http://broadcast.infomaniak.ch/start-sud-high.mp3",\
             "France Inter":"http://direct.franceinter.fr/live/franceinter-midfi.mp3",\
             "Frequence Jazz":"http://broadcast.infomaniak.ch/frequencejazz-high.mp3",\
             "Latina":"http://broadcast.infomaniak.net/start-latina-high.mp3",\
             "Le Mouv":"http://direct.mouv.fr/live/mouv-midfi.mp3",\
             "Euro News":"http://euronews-01.ice.infomaniak.ch/euronews-01.aac",\
             "Radio Grenouille":"http://live.radiogrenouille.com/live",\
             "Belgique":"https://radios.rtbf.be/laprem1ere-128.mp3",\
             "Canada":"http://2QMTL0.akacast.akamaistream.net:80/7/953/177387/v1/rc.akacast.akamaistream.net/2QMTL0",\
             "Suisse":"http://stream.srg-ssr.ch/m/la-1ere/mp3_128"}

    if intentMessage.intent.intent_name == 'louisros:selectStation' :

        station = intentMessage.slots.radioName.first().value  
        fv = open("/var/lib/snips/skills/live","r")
        live = int(PyString(fv.read()))
        fv.close()              
        if live == 0 :
            live = 1
        if live == 4 :
            live = 2        
        fv =open("/var/lib/snips/skills/live","w") 
        fv.write(CString(str(live)))
        fv.close()

        fv=open("/var/lib/snips/skills/link","w")
        fv.write(CString(links[station]))
        fv.close()
        resul = ""
      
    elif intentMessage.intent.intent_name == 'louisros:changeVolume' :
        vol = intentMessage.slots.var.first().value 
        fv =open("/var/lib/snips/skills/volume","r")
        volume = PyString(fv.read())
        fv.close()
        if vol == "plus fort":
            v = int(volume)
            v = v + 1
            if v > 10 :
                v = 10
            volume = str(v) 
        elif vol == "moins fort":
            v = int(volume)
            v = v - 1
            if v < 0 :
                v = 0
            volume =str(v)
        else:
            volume = str(int(vol)) 
          
 
        fv =open("/var/lib/snips/skills/volume","w")
        fv.write(CString(volume))
        fv.close()
        live = 3
        fv = open("/var/lib/snips/skills/live","w") 
        fv.write(CString(str(live)))
        fv.close()
        resul = ""
            
            
            
    elif intentMessage.intent.intent_name == 'louisros:stopRadio':
        try: 
            delay = int(intentMessage.slots.delay.first().value)
        except:
            delay = -1
        
        fv = open("/var/lib/snips/skills/live","r")
        live = int(PyString(fv.read()))
        fv.close()              
        if live == 4 : 
            live = 6
            if delay == -1 :
                  live = 5
            fv =open("/var/lib/snips/skills/live","w") 
            fv.write(CString(str(live)))
            fv.close()
        if delay != 0 :   
            fv =open("/var/lib/snips/skills/delay","w") 
            fv.write(CString(str(delay*60)))
            fv.close()
                  
        resul = "arrêt en cours"
   
      
      
    elif intentMessage.intent.intent_name == 'louisros:time':

            date = datetime.datetime.now()
            heure = str(date.hour)
            if date.hour == 1 :
                heure = "une"
            if date.hour == 21 :
                heure = "vingt et une"
            minute = str(date.minute)
            if date.minute == 0 :
                minute = "précises"
            if date.minute == 1 :
                minute = "une"
            if date.minute == 21 :
                minute = "vingt-et-une"
            if date.minute == 31 :
                minute = "trente-et-une"
            if date.minute == 41 :
                minute = "quarante-et-une"
            if date.minute == 51 :
                minute = "cinquante-et-une"
            resul = "il est   " + heure + 'heures    ' + minute
            
    """elif intentMessage.intent.intent_name == 'louisros:wakeUp':        
            hr = int(intentMessage.slots.heure.first().value)
            mr = int(intentMessage.slots.minute.first().value)
            date = datetime.datetime.now()
            t = date.hour * 60 + date.minute
            tr = hr * 60 + mr
            d = tr - t
            if d <=0 :
                  d = d + 1440
            d = d * 60      
            fv =open("/var/lib/snips/skills/delayR","w") 
            fv.write(CString(str(d)))
            fv.close()
            fv =open("/var/lib/snips/skills/live","w") 
            fv.write(CString(str("7")))
            fv.close()
            mmr = str(mr)
            if mr == 0 :
                  mmr = ""
            resul = "C'est entendu, je vous réveille à " + str(hr) + " heures " + mmr + " précises"
         """   
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, resul)


if __name__ == "__main__":
    with Hermes(MQTT_ADDR) as h:           
        h.subscribe_intents(intents_callback).start()
        
