#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import ConfigParser
from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))






def intents_callback(hermes, intentMessage) : 
    
    if intentMessage.intent.intent_name == 'selectStation' :
        m = 'station'
    if intentMessage.intent.intent_name == 'changeVolume' :
        m = 'volume'
    if intentMessage.intent.intent_name == 'stopRadio'
        m = 'radio'   
      
    
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, m)


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:    
        
        h.subscribe_intents(intents_callback).start()
        
