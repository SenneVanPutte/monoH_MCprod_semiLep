import os
import json
from CRABClient.UserUtilities import config

import optparse
from optparse import OptionParser

usage = 'usage: %prog [options]'
parser = optparse.OptionParser(usage)
#parser.add_option('--skip', dest='skip', help='Skip these mass points (string that contains mass point and sign, comma seperated, no " " in between)', type='string', default='')
parser.add_option('--mp', dest='mass_point', help='mass point', type='string')
parser.add_option('--sng', dest='sng', help='sign string (pos or neg)', type='string')
(options, args) = parser.parse_args()

def get_latest_dbs(cmd_str):
    out_cmd = os.popen(cmd_str).read()
    cmd_dict = json.loads(out_cmd)
    file_dict = {}
    ts_lst = []
    data_lst = cmd_dict[u'data']
    for sety in data_lst:
        for key in sety:
            if 'dataset' in key:
                ts_lst.append(sety[key][0][u'creation_time'])
                file_dict[sety[key][0][u'creation_time']] = str(sety[key][0][u'name'])
    
    return file_dict[max(ts_lst)]

#skip_p = options.skip.split(',')
mp = options.mass_point
sgn = options.sng

w_dir = 'step2'
rq_name = 'darkHiggs_'+mp+'_step2_'+sgn
if os.path.isdir(w_dir+'/crab_'+rq_name):
    print(w_dir+'/crab_'+rq_name+' already exists')
    exit()

#cmd_str = 'dasgoclient -query="dataset=/monoHiggsMC_2HDMa_semiLep*/*step1*/USER instance=prod/phys03"'
#cmd_str = 'dasgoclient -query="dataset=/monoHiggsMC_2HDMa_semiLep*/*'+mp+'*step1*newLHE*'+sgn+'*/USER instance=prod/phys03"'
cmd_str = 'dasgoclient -query="dataset=/monoHiggsMC_darkHiggs_semiLep*/*'+mp+'*step1*'+sgn+'*/USER instance=prod/phys03" --format=json'
file_str = get_latest_dbs(cmd_str)
#out_cmd = os.popen(cmd_str).read()
#out_list = out_cmd.split('\n')

#from WMCore.Configuration import Configuration
config = config()

from CRABAPI.RawCommand import crabCommand


#in_dtset = []   
#for dataset in out_list:
#    if sgn in dataset and mp in dataset:
#        in_dtset.append(dataset)
#
#if len(in_dtset) == 0: raise IOError('Previous step data set on DAS not found')
#if len(in_dtset) > 1: 
#    print('WARNING: multiple matches for config.Data.inputDataset:' )
#    print(in_dtset)
#    raw_input('Proceed with [0]? (press enter if yes ctrl C otherwise)')
#
#print('Dataset previous step: ' + in_dtset[0])
print('Dataset previous step: ' + file_str)

config.section_("General")
config.General.transferLogs = True
config.General.workArea = w_dir
config.General.requestName  = rq_name

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'step2.py'
config.JobType.pyCfgParams = [mp, sgn]
config.JobType.maxMemoryMB = 5000

config.section_("Data")
config.Data.splitting       = 'FileBased'
config.Data.unitsPerJob = 1
#config.Data.outputDatasetTag = 'EXO-RunIIFall17wmLHEGS-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_'+mp+'_step2_'+sgn
#config.Data.outputDatasetTag = 'EXO-RunIIFall17wmLHEGS-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_'+mp+'_step2_newLHE_'+sgn
config.Data.outputDatasetTag = 'EXO-RunIIFall17wmLHEGS-darkHiggs_theta_0p01_gq_0p25_gx_1p0_'+mp+'_step2_'+sgn
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/user/svanputt/monoHiggs/'
config.Data.publication     = True
config.Data.inputDataset = file_str

config.section_("Site")
config.Site.storageSite = 'T2_BE_IIHE'

#crabCommand('submit', config=config, dryrun=True)
crabCommand('submit', config=config)
