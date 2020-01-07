import os
from CRABClient.UserUtilities import config

import optparse
from optparse import OptionParser

usage = 'usage: %prog [options]'
parser = optparse.OptionParser(usage)
#parser.add_option('--skip', dest='skip', help='Skip these mass points (string that contains mass point and sign, comma seperated, no " " in between)', type='string', default='')
parser.add_option('--mp', dest='mass_point', help='mass point', type='string')
parser.add_option('--sng', dest='sng', help='sign string (pos or neg)', type='string')
(options, args) = parser.parse_args()

#skip_p = options.skip.split(',')
mp = options.mass_point
sgn = options.sng

w_dir = 'step0_new'
rq_name = '2HDMa_'+mp+'_step0_'+sgn
if os.path.isdir(w_dir+'/crab_'+rq_name):
    print(w_dir+'/crab_'+rq_name+' already exists')
    exit()

#from WMCore.Configuration import Configuration
config = config()

#mc_sets = [
#    #'MH3_1200_MH4_150_MH2_1200_MHC_1200', 
#    #'MH3_200_MH4_150_MH2_200_MHC_200', 
#    #'MH3_300_MH4_150_MH2_300_MHC_300', 
#    #'MH3_400_MH4_150_MH2_400_MHC_400', 
#    #'MH3_500_MH4_150_MH2_500_MHC_500', 
#    ##'MH3_700_MH4_150_MH2_700_MHC_700', 
#    ##'MH3_900_MH4_150_MH2_900_MHC_900',
#    'MH3_600_MH4_150_MH2_600_MHC_600'
#    ]
#
#sign = [
#    #'pos', 
#    'neg'
#    ]

#if __name__ == '__main__':
from CRABAPI.RawCommand import crabCommand

 #   for sgn in sign:
  #      print('----- Sarting the ' + sgn + ' config\'s') 
#        config.JobType.psetName    = 'step0_'+sgn+'.py'
#        for mass_point in mc_sets:
 #           print('--- Mass point: ' + mass_point ) 

config.section_("General")
config.General.transferLogs = True
config.General.workArea = w_dir
#config.General.requestName  = 'EXO-RunIIFall17wmLHEGS-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_'+mp+'_step0_'+sgn
config.General.requestName  = rq_name

config.section_("JobType")
config.JobType.pluginName  = 'PrivateMC'
config.JobType.psetName    = 'step0_'+sgn+'.py'
config.JobType.pyCfgParams = [mp]
#config.JobType.numCores = 1
#config.JobType.inputFiles = ['/eos/user/f/fernanpe/Fall2017_nAOD_v1_Full2017v2/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_'+mp+'.lhe']
config.JobType.inputFiles = ['/afs/cern.ch/user/s/svanputt/work/monoHiggs/MCprod/CMSSW_10_2_9/src/monoH_MCprod_semiLep/2HDM+a/SemiLep/LHE/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_'+mp+'.lhe']

config.JobType.disableAutomaticOutputCollection = False

config.section_("Data")
config.Data.splitting       = 'EventBased'
config.Data.unitsPerJob     = 200
config.Data.totalUnits 	    = 10000
config.Data.outputDatasetTag = 'EXO-RunIIFall17wmLHEGS-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_'+mp+'_step0_newLHE_'+sgn
config.Data.publication     = True
config.Data.outLFNDirBase = '/store/user/svanputt/monoHiggs/'
config.Data.outputPrimaryDataset = 'monoHiggsMC_2HDMa_semiLep'

config.section_("Site")
config.Site.storageSite = 'T2_BE_IIHE'

#crabCommand('submit', config=config, dryrun=True)
crabCommand('submit', config=config)


