from CRABClient.UserUtilities import config
config = config()

config.section_("General")
config.General.transferLogs = True
config.General.requestName = 'EXO-RunIIFall17wmLHEGS-Zprime_A0h_A0chichi_MZp1700_MA0300_step4_nano' 
config.General.workArea = 'crab_projects'


config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName = 'step4.py'
config.JobType.maxMemoryMB = 10000


config.section_("Data")
config.Data.splitting       = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outputDatasetTag = 'EXO-RunIIFall17wmLHEGS-Zprime_A0h_A0chichi_MZp1700_MA0300_step4_nano'
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/group/phys_muon/fernanpe/MonoH/' 
config.Data.publication = True
config.Data.inputDataset = '/CRAB_PrivateMC/calderon-EXO-RunIIFall17wmLHEGS-Zprime_A0h_A0chichi_MZp1700_MA0300_step3-48a7301b3e5f5836da5a727ba66e2752/USER'


config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
