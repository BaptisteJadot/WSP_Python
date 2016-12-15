import h5py
import numpy as np
import MultiDimExperiment, ExperimentFileManager

XP = MultiDimExperiment.MultiDimExperiment()
FM = ExperimentFileManager.ExperimentFileManager(XP)

FM.Read_Experiment_File(filepath = '/Users/pierre-andremortemousque/Documents/Research/2014-15_Neel/Experimental/Ratatouille/Ratatouille32CD8f2',\
                        filename = "stat8_1418.lvm",\
                        read_multiple_files = False)
FM.Write_Experiment_to_h5(group_name = 'raw_data_10us')
