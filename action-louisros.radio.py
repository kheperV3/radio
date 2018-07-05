#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intents_callback(hermes, intentMessage) : 
    
    if intentMessage.intent.intent_name == 'selectStation' :
        m = 'station'
    elif intentMessage.intent.intent_name == 'changeVolume' :
        m = 'volume'
    elif intentMessage.intent.intent_name == 'stopRadio':
        m = 'radio'   
    else:
        m = "je n'ai rien compris"
    
    m = "c'est difficile"
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, m)


if __name__ == "__main__":
    with Hermes(MQTT_ADDR) as h:           
        h.subscribe_intents(intents_callback).start()
        
