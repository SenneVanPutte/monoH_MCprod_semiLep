from CRABClient.UserUtilities import config

#from WMCore.Configuration import Configuration
config = config()

mc_sets = [
    'MH3_1200_MH4_150_MH2_1200_MHC_1200', 
    'MH3_200_MH4_150_MH2_200_MHC_200', 
    'MH3_300_MH4_150_MH2_300_MHC_300', 
    'MH3_400_MH4_150_MH2_400_MHC_400', 
    'MH3_500_MH4_150_MH2_500_MHC_500', 
    'MH3_700_MH4_150_MH2_700_MHC_700', 
    'MH3_900_MH4_150_MH2_900_MHC_900'
    ]

sign = ['pos', 'neg']

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand

    for sgn in sign:
        print('----- Sarting the ' + sgn + ' config\'s') 
        for mass_point in mc_sets:
            print('--- Mass point: ' + mass_point ) 

            config.section_("General")
            config.General.transferLogs = True
            config.General.workArea = '2HDM+a'
            #config.General.requestName  = 'EXO-RunIIFall17wmLHEGS-Zprime_A0h_A0chichi_MZp800_MA0300_step0'
            #config.General.requestName  = 'EXO-RunIIFall17wmLHEGS-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_'+mass_point+'_step0_'+sgn
            config.General.requestName  = '2HDMa_'+mass_point+'_step0_'+sgn
            config.section_("General")
            config.General.transferLogs = True
            
            config.section_("JobType")
            config.JobType.pluginName  = 'PrivateMC'
            #config.JobType.psetName    = 'step0.py'
            config.JobType.psetName    = 'step0_'+sgn+'.py'
            config.JobType.pyCfgParams = [mass_point]
            #config.JobType.numCores = 1
            #config.JobType.inputFiles = ['Zprime_A0h_A0chichi_MZp800_MA0300_slc6_amd64_gcc481_CMSSW_7_1_30.lhe']
            config.JobType.inputFiles = ['/eos/user/f/fernanpe/Fall2017_nAOD_v1_Full2017v2/2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_'+mass_point+'.lhe']
            config.JobType.disableAutomaticOutputCollection = False
            
            config.section_("Data")
            config.Data.splitting       = 'EventBased'
            config.Data.unitsPerJob     = 200
            config.Data.totalUnits 	    = 5000
            #config.Data.outputDatasetTag = 'EXO-RunIIFall17wmLHEGS-Zprime_A0h_A0chichi_MZp800_MA0300_step0'
            config.Data.outputDatasetTag = 'EXO-RunIIFall17wmLHEGS-2HDMa_gg_sinp_0p35_tanb_1p0_mXd_10_'+mass_point+'_step0_'+sgn
            config.Data.publication     = True
            #config.Data.outLFNDirBase = '/store/group/phys_muon/fernanpe/MonoH'
            config.Data.outLFNDirBase = '/store/user/svanputt/monoHiggs/'
            config.Data.outputPrimaryDataset = 'CRAB_PrivateMC'
            
            config.section_("Site")
            #config.Site.storageSite = 'T2_CH_CERN'
            config.Site.storageSite = 'T2_BE_IIHE'
            #config.Site.storageSite = 'T2_ES_IFCA'
            #config.Site.whitelist = ['T2_ES_IFCA']
            crabCommand('submit', config=config, dryrun=True)

