import os
from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config, setConsoleLogLevel, getConsoleLogLevel
from CRABClient.ClientUtilities import LOGLEVEL_MUTE

import optparse
from optparse import OptionParser

LOGLEVEL_ON = getConsoleLogLevel()

usage = 'usage: %prog [options]'
parser = optparse.OptionParser(usage)
parser.add_option('--start-dir', dest='start_dir', help='Directory containing crab job dirs', type='string')
parser.add_option('--cmd', dest='cr_cmd', help='Command to submit to all crab dires in start-dir, special commands are: failed_resubmit, resubmit, status_summary', type='string')
(options, args) = parser.parse_args()

#from WMCore.Configuration import Configuration
config = config()

start_dir = options.start_dir

list_dir = os.listdir(start_dir)

def read_status(key='status', check='SUBMITFAILED'):
    check_list = []
    setConsoleLogLevel(LOGLEVEL_MUTE) 
    for diri in list_dir:
        target = start_dir + '/' + diri
        print('--Target: ' + target)
        #status_dir
        resp = crabCommand('status', d=target)
        if check in resp[key]: check_list.append(target)
    setConsoleLogLevel(LOGLEVEL_ON)
    return check_list 


if __name__ == '__main__':
    if options.cr_cmd == 'failed_resubmit':
        print('received command ' + options.cr_cmd)
        print('Fetching statuses')
       
        skip_str = ''
        nonskip_list = read_status(key='status', check='SUBMITFAILED')
        for diri in list_dir:
            target = start_dir + '/' + diri
            if not target in nonskip_list: skip_str = skip_str + target + ',' 
        
        #setConsoleLogLevel(LOGLEVEL_MUTE) 
        #for diri in list_dir:
        #    target = start_dir + '/' + diri
        #    print('--Target: ' + target)
        #    #status_dir
        #    resp = crabCommand('status', d=target)
        #    if 'SUBMITFAILED' not in resp['status']: skip_str = skip_str + target + ','
        #    else: nonskip_list.append(target)
        #setConsoleLogLevel(LOGLEVEL_ON) 
        for noskp in nonskip_list:
            print('Removing crab directory '+noskp)
            os.system('rm -rf '+noskp)
        print('Starting \'re\'submission')
        os.system('python multicrab_cfg_'+start_dir+'.py --skip='+skip_str) 

    elif options.cr_cmd == 'resubmit':        
        print('received command ' + options.cr_cmd)
        print('Fetching statuses')
        
        failed_list = read_status(key='dagStatus', check='FAILED')
        for diri in list_dir:
            target = start_dir + '/' + diri
            if target in failed_list: crabCommand(options.cr_cmd, d=target)
       
    elif options.cr_cmd == 'status_summary':
        print('received command ' + options.cr_cmd)
        setConsoleLogLevel(LOGLEVEL_MUTE)
        for diri in list_dir:
            target = start_dir + '/' + diri
            print('Sending ' + options.cr_cmd + ' to ' + target)
            resp = crabCommand('status', d=target)
            print('    Status: '+resp['status']+',\t\t DagStatus: '+resp['dagStatus'])
        setConsoleLogLevel(LOGLEVEL_ON) 
        
 
    else:
        for diri in list_dir:
            target = start_dir + '/' + diri
            print('Sending ' + options.cr_cmd + ' to ' + target)
            crabCommand(options.cr_cmd, d=target) 

