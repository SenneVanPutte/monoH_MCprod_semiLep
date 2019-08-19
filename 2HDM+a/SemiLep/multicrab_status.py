import os
from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config

#from WMCore.Configuration import Configuration
config = config()

start_dir = 'step0'

list_dir = os.listdir(start_dir)

if __name__ == '__main__':
    for diri in list_dir:
        target = start_dir + '/' + diri
        print('Status of ' + target)
        crabCommand('status', d=target) 

