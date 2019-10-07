import os
import time
from CRABClient.UserUtilities import config

import optparse
from optparse import OptionParser

usage = 'usage: %prog [options]'
parser = optparse.OptionParser(usage)
parser.add_option('--skip', dest='skip', help='Skip these mass points (string that contains mass point and sign, comma seperated, no " " in between)', type='string', default='')
(options, args) = parser.parse_args()

skip_p = options.skip.split(',')

cmd_str = 'dasgoclient -query="dataset=/monoHiggsMC_2HDMa_semiLep*/*step2*/USER instance=prod/phys03"'
out_cmd = os.popen(cmd_str).read()
out_list = out_cmd.split('\n')

#from WMCore.Configuration import Configuration

mc_sets = [
    #'MH3_1200_MH4_150_MH2_1200_MHC_1200', 
    #'MH3_200_MH4_150_MH2_200_MHC_200', 
    #'MH3_300_MH4_150_MH2_300_MHC_300', 
    #'MH3_400_MH4_150_MH2_400_MHC_400', 
    #'MH3_500_MH4_150_MH2_500_MHC_500', 
    #'MH3_700_MH4_150_MH2_700_MHC_700', 
    'MH3_900_MH4_150_MH2_900_MHC_900'
    ]

sign = [
    #'pos', 
    'neg'
    ]

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand

    for sgn in sign:
        print('----- Sarting the ' + sgn + ' config\'s') 
        for mass_point in mc_sets:
            print('--- Mass point: ' + mass_point ) 

            to_skip = False
            for skp in skip_p:
                if mass_point in skp and sgn in skp: to_skip = True 
            if to_skip: 
                print('skipped')
                continue

            in_dtset = []   
            for dataset in out_list:
                if sgn in dataset and mass_point in dataset:
                    in_dtset.append(dataset)

            if len(in_dtset) == 0: raise IOError('Previous step data set on DAS not found')
            if len(in_dtset) > 1: 
                print('WARNING: multiple matches for config.Data.inputDataset:' )
                print(in_dtset)
                raw_input('Proceed with [0]? (press enter if yes ctrl C otherwise)')

            print('Dataset previous step: ' + in_dtset[0])

            sbm_cfg = config()

            sbm_cfg.section_("General")
            sbm_cfg.General.transferLogs = True
            sbm_cfg.General.workArea = 'step3'
            sbm_cfg.General.requestName  = '2HDMa_'+mass_point+'_step3_'+sgn
            
            sbm_cfg.section_("JobType")
            sbm_cfg.JobType.pluginName  = 'Analysis'
            sbm_cfg.JobType.psetName    = 'step3.py'
            sbm_cfg.JobType.pyCfgParams = [mass_point, sgn]
            sbm_cfg.JobType.maxMemoryMB = 10000

            sbm_cfg.section_("Data")
            sbm_cfg.Data.splitting       = 'FileBased'
            sbm_cfg.Data.unitsPerJob = 1
            sbm_cfg.Data.outputDatasetTag = 'EXO-RunIIFall17wmLHEGS-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_'+mass_point+'_step3_'+sgn
            sbm_cfg.Data.inputDBS = 'phys03'
            sbm_cfg.Data.outLFNDirBase = '/store/user/svanputt/monoHiggs/'
            sbm_cfg.Data.publication     = True
            sbm_cfg.Data.inputDataset = in_dtset[0]

            sbm_cfg.section_("Site")
            sbm_cfg.Site.storageSite = 'T2_BE_IIHE'

            #print(sbm_cfg)
            #print(sbm_cfg.JobType.psetName)

            #crabCommand('submit', config=sbm_cfg, dryrun=True)
            crabCommand('submit', config=sbm_cfg)


