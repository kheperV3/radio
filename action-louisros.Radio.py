#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import ConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io
import os


CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

class SnipsConfigParser(ConfigParser.SafeConfigParser):
    def to_dict(self):
        return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}
 

def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODIN50G_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, ConfigParser.Error) as e:
        return dict()



def selectStation_callback(hermes, intentMessage):   
    conf = read_configuration_file(CONFIG_INI)
    """"sl = {'RFI' : '0','France Culture': '1','FIP':'2', 'RMC':'3','RTL':'4','France Info':'5','Radio Classic':'6','France Musique':'7',\
          'Jazz Radio':'8','Europe1':'9','Sud Radio':'10','France Inter':'11','Frequence Jazz':'12','Latina':'13','Le Mouv':'14',\
          'Euro News':'15','Radio Grenouille':'16'}
    """
    station = intentMessage.slots.radioName.first().value 
    """os.system("echo " + sl[station] + "==" + str(50) + " >/var/lib/snips/skills/RadioCom")
    """
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, "bien cher Maître")
    
def volume_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)   
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, "")
    

def stop_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    os.system("rm /var/lib/snips/skills/RadioCom")
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, "")


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        
        
        h\
        .subscribe_intent("louisros:selectStation", selectStation_callback) \
        .subscribe_intent("louisros:changeVolume", volume_callback) \
        .subscribe_intent("louisros:stopRadio", stop_callback) \
        .start()
        
