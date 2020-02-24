import os
from CRABClient.UserUtilities import config

import optparse
from optparse import OptionParser

usage = 'usage: %prog [options]'
parser = optparse.OptionParser(usage)
parser.add_option('--mp', dest='mass_point', help='mass point', type='string')
parser.add_option('--sng', dest='sng', help='sign string (pos or neg)', type='string')
(options, args) = parser.parse_args()

mp = options.mass_point
sgn = options.sng

w_dir = 'step0_big'
rq_name = 'darkHiggs_'+mp+'_step0_'+sgn
if os.path.isdir(w_dir+'/crab_'+rq_name):
    print(w_dir+'/crab_'+rq_name+' already exists')
    exit()

config = config()

from CRABAPI.RawCommand import crabCommand

config.section_("General")
config.General.transferLogs = True
config.General.workArea = w_dir
#config.General.requestName  = 'EXO-RunIIFall17wmLHEGS-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_'+mp+'_step0_'+sgn
config.General.requestName  = rq_name

config.section_("JobType")
config.JobType.pluginName  = 'PrivateMC'
config.JobType.psetName    = 'step0_'+sgn+'.py'
config.JobType.pyCfgParams = [mp]
config.JobType.inputFiles = ['/afs/cern.ch/user/s/svanputt/work/monoHiggs/MCprod/CMSSW_9_4_9/src/monoH_MC_production_2017/darkHiggs/2017/LHE/darkHiggs_theta_0p01_gq_0p25_gx_1p0_'+mp+'_WW.lhe']
config.JobType.disableAutomaticOutputCollection = False

config.section_("Data")
config.Data.splitting       = 'EventBased'
config.Data.unitsPerJob     = 10000
config.Data.totalUnits 	    = 10000
config.Data.outputDatasetTag = 'EXO-RunIIFall17wmLHEGS-darkHiggs_theta_0p01_gq_0p25_gx_1p0_'+mp+'_step0_big_'+sgn
config.Data.publication     = True
config.Data.outLFNDirBase = '/store/user/svanputt/monoHiggs/'
config.Data.outputPrimaryDataset = 'monoHiggsMC_darkHiggs_semiLep'

config.section_("Site")
config.Site.storageSite = 'T2_BE_IIHE'

#crabCommand('submit', config=config, dryrun=True)
crabCommand('submit', config=config)


