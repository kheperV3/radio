#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import ConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io
import os
import vlc

CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

class SnipsConfigParser(ConfigParser.SafeConfigParser):
    def to_dict(self):
        return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}


def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, ConfigParser.Error) as e:
        return dict()

def subscribe_intent_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    action_wrapper(hermes, intentMessage, conf)


def setStation_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    ip = "http://live03.rfi.fr/rfimonde-96k.mp3"
    """m = vlc.libvlc_media_new_location(inst,ip)
    mp = vlc.libvlc_media_player_new_from_media(m)
    vlc.libvlc_media_release(m)
    vlc.libvlc_media_player_play(mp)
    vlc.libvlc_audio_set_volume(mp,100)
    
    p=vlc.MediaPlayer(ip)
    p.play()
    """
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, "c'est fait Monsieur")
    
def volumeUp_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, "c'est fait Monsieur")
    
def volumeDown_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, "c'est fait Monsieur")
    
def play_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, "c'est fait Monsieur")
    
def pause_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, "c'est fait Monsieur")
    
def stop_callback(hermes, intentMessage):
    conf = read_configuration_file(CONFIG_INI)
    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, "c'est fait Monsieur")


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h\
        .subscribe_intent("louisros:setStation", setStation_callback) \
        .subscribe_intent("louisros:volumeUp", volumeUp_callback) \
        .subscribe_intent("louisros:volumeDown", volumeDown_callback) \
        .subscribe_intent("louisros:play", play_callback) \
        .subscribe_intent("louisros:stop", stop_callback) \
        .subscribe_intent("louisros:pause", pause_callback) \
        .start()
