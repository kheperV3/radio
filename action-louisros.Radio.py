#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import ConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
#import io



CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

class SnipsConfigParser(ConfigParser.SafeConfigParser):
    def to_dict(self):
        return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}
 

def read_configuration_file(configuration_file):
    """try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODIN50G_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, ConfigParser.Error) as e:
        return dict()
"""


def selectStation_callback(hermes, intentMessage):   
#    conf = read_configuration_file(CONFIG_INI)   
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, "station cher Maître")
    
def volume_callback(hermes, intentMessage):
   # conf = read_configuration_file(CONFIG_INI)   
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, "volume cher Maître")
    

def stop_callback(hermes, intentMessage):
   # conf = read_configuration_file(CONFIG_INI)
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, "stop cher Maître")


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        
        
        h\
        .subscribe_intent("louisros:selectStation", selectStation_callback) \
        .subscribe_intent("louisros:changeVolume", volume_callback) \
        .subscribe_intent("louisros:stopRadio", stop_callback) \
        .start()
        
