import shutil
import os
import sys
import ConfigParser

def cleanup():

	config = ConfigParser.RawConfigParser()
	config.read('skeletonsuite.cfg')  
	shutil.rmtree(config.get('locations', 'output'), True)