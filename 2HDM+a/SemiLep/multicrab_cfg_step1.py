
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







from CRABClient.UserUtilities import config
config = config()

config.section_("General")
config.General.transferLogs = True
config.General.requestName = 'EXO-RunIIFall17wmLHEGS-Zprime_A0h_A0chichi_MZp400_MA0300_step1' 
config.General.workArea = 'crab_projects'


config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName = 'step1.py'
config.JobType.maxMemoryMB = 10000


config.section_("Data")
config.Data.splitting       = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outputDatasetTag = 'EXO-RunIIFall17wmLHEGS-Zprime_A0h_A0chichi_MZp400_MA0300_step1'
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/group/phys_muon/fernanpe/MonoH/' 
config.Data.publication = True
config.Data.inputDataset = '/CRAB_PrivateMC/fernanpe-EXO-RunIIFall17wmLHEGS-Zprime_A0h_A0chichi_MZp400_MA0300_step0-794c1c222288ce370cc9331c69902371/USER'


config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
