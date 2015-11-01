#!/usr/bin/python
import sys
from analyser.analyser import Analyser
from analyser.redis_classifier import RedisClassifier
from server.tasks.analyser_task import AnalyserTask


execfile( "server/analyser_server.py")
