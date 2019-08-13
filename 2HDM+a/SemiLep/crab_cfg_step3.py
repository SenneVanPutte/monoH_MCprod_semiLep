from CRABClient.UserUtilities import config
config = config()

config.section_("General")
config.General.transferLogs = True
config.General.requestName = 'EXO-RunIIFall17wmLHEGS-Zprime_A0h_A0chichi_MZp400_MA0300_step3' 
config.General.workArea = 'crab_projects'


config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName = 'step3.py'
config.JobType.maxMemoryMB = 10000


config.section_("Data")
config.Data.splitting       = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outputDatasetTag = 'EXO-RunIIFall17wmLHEGS-Zprime_A0h_A0chichi_MZp400_MA0300_step3'
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/group/phys_muon/fernanpe/MonoH/' 
config.Data.publication = True
config.Data.inputDataset = '/CRAB_PrivateMC/fernanpe-EXO-RunIIFall17wmLHEGS-Zprime_A0h_A0chichi_MZp400_MA0300_step2-c3d6de13a4792afb4dd0c4ab58e49a3d/USER'


config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
