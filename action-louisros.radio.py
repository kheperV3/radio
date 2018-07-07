#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes


MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


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
        m = "tout va bien"

        fv = open("/var/lib/snips/skills/live","r")
        live = fv.read()
        fv.close()
      
        if live == 0 :
            live = 1
        if live == 4 :
            live = 2

        fv =open("/var/lib/snips/skills/live","w") 
        fv.write("0036")
        fv.close()

        fv=open("/var/lib/snips/skills/link","w")
        fv.write(links[station])
        fv.close()

        
    elif intentMessage.intent.intent_name == 'louisros:changeVolume' :
        m = 'volume'
    elif intentMessage.intent.intent_name == 'louisros:stopRadio':
        m = 'radio'   
  
    

    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, m)


if __name__ == "__main__":
    with Hermes(MQTT_ADDR) as h:           
        h.subscribe_intents(intents_callback).start()
        
