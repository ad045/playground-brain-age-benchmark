import pathlib

study_name = "age-prediction-benchmark"

# subject name: sub-CC110101


bids_root = pathlib.Path('camcan_one_dataset/raw_2')
# bids_root = pathlib.Path('/vol/aimspace/users/dena/Documents/clean_brain_age/brain-age-benchmark/camcan_one_dataset')
        #/vol/aimspace/users/dena/Documents/clean_brain_age/brain-age-benchmark/camcan_one_dataset')
    # "/vol/aimspace/users/dena/Documents/clean_brain_age/raw_data/CamCAN/storage/raw_data/cc700/meg/pipeline/release005/BIDSsep/rest")

# assumption: deriv_root and subjects_dir are only for outputs, and not for inputs. 
deriv_root = pathlib.Path('camcan_one_dataset/derivatives')
# deriv_root = pathlib.Path('/vol/aimspace/users/dena/Documents/clean_brain_age/brain-age-benchmark/camcan_one_dataset/derivatives')
                        #   '/vol/aimspace/users/dena/Documents/clean_brain_age/brain-age-benchmark/processed_CamCAN/derivatives')

subjects_dir = None #pathlib.Path('/vol/aimspace/users/dena/Documents/clean_brain_age/brain-age-benchmark/camcan_one_dataset/freesurfer')
source_info_path_update = {'processing': 'autoreject',
                           'suffix': 'epo'}

process_empty_room = True #added, just for testing if further steps work. 


interactive = False

inverse_targets = []

noise_cov = 'ad-hoc'

# task = 'rest'
task_is_rest = True
# conditions = ["rest"]
sessions = ['rest']  # keep empty for code flow or: sessions = "all"
data_type = 'meg'
ch_types = ['meg']



analyze_channels = [
    'MEG0111', 'MEG0121', 'MEG0131', 'MEG0141', 'MEG0211',
    'MEG0221', 'MEG0231', 'MEG0241', 'MEG0311', 'MEG0321', 'MEG0331',
    'MEG0341', 'MEG0411', 'MEG0421', 'MEG0431', 'MEG0441', 'MEG0511',
    'MEG0521', 'MEG0531', 'MEG0541', 'MEG0611', 'MEG0621', 'MEG0631',
    'MEG0641', 'MEG0711', 'MEG0721', 'MEG0731', 'MEG0741', 'MEG0811',
    'MEG0821', 'MEG0911', 'MEG0921', 'MEG0931', 'MEG0941', 'MEG1011',
    'MEG1021', 'MEG1031', 'MEG1041', 'MEG1111', 'MEG1121', 'MEG1131',
    'MEG1141', 'MEG1211', 'MEG1221', 'MEG1231', 'MEG1241', 'MEG1311',
    'MEG1321', 'MEG1331', 'MEG1341', 'MEG1411', 'MEG1421', 'MEG1431',
    'MEG1441', 'MEG1511', 'MEG1521', 'MEG1531', 'MEG1541', 'MEG1611',
    'MEG1621', 'MEG1631', 'MEG1641', 'MEG1711', 'MEG1721', 'MEG1731',
    'MEG1741', 'MEG1811', 'MEG1821', 'MEG1831', 'MEG1841', 'MEG1911',
    'MEG1921', 'MEG1931', 'MEG1941', 'MEG2011', 'MEG2021', 'MEG2031',
    'MEG2041', 'MEG2111', 'MEG2121', 'MEG2131', 'MEG2141', 'MEG2211',
    'MEG2221', 'MEG2231', 'MEG2241', 'MEG2311', 'MEG2321', 'MEG2331',
    'MEG2341', 'MEG2411', 'MEG2421', 'MEG2431', 'MEG2441', 'MEG2511',
    'MEG2521', 'MEG2531', 'MEG2541', 'MEG2611', 'MEG2621', 'MEG2631',
    'MEG2641'
]

l_freq = 0.1
h_freq = 49

eeg_reference = []

eog_channels = []

find_breaks = False

# n_proj_eog = 1                    # ad

reject = None

on_rename_missing_events = "warn"

# N_JOBS = 40 # ad: previously 30 
n_jobs = 1 # ad

# decim = 5  # Cam-CAN has 1000 Hz; Cuban Human Brain Project 200Hz
epochs_decim = 5  # decimate by 4, i.e., divide sampling frequency by 4


mf_st_duration = 10.

# XXX the values below differ from our previous papers but would be in line
# with the other EEG data used in this benchmark
epochs_tmin = 0.
epochs_tmax = 10.
rest_epochs_overlap = 0.
rest_epochs_duration = 10.
baseline = None

# Maxfilter.  ad. 
# mf_cal_fname = None #"../raw_data/cc700/meg/pipeline/release005/BIDSsep/rest/sub-CC110101/maxfilterCommandString_basic.txt"

# mf_cal_fname = "/vol/aimspace/users/dena/Documents/clean_brain_age/raw_data/CamCAN/storage/raw_data/cc700/meg/pipeline/release005/BIDSsep/derivatives_rest/aa/AA_movecomp/aamod_meg_maxfilt_00002/sub-CC110101/mf2pt2_sub-CC110101_ses-rest_task-rest_meg.fif"

#prev. Maxfilter
mf_ctc_fname = "/vol/aimspace/users/dena/Documents/clean_brain_age/raw_data/CamCAN/storage/raw_data/cc700/meg/pipeline/release005/BIDSsep/derivatives_rest/aa/AA_movecomp/aamod_meg_maxfilt_00002/sub-CC110101/mf2pt2_sub-CC110101_ses-rest_task-rest_meg.fif"
mf_cal_fname = "/vol/aimspace/users/dena/Documents/clean_brain_age/raw_data/CamCAN/storage/raw_data/cc700/meg/pipeline/release005/BIDSsep/derivatives_rest/aa/AA_movecomp/aamod_meg_maxfilt_00002/sub-CC110101/mf2pt2_sub-CC110101_ses-rest_task-rest_meg.log"
# mf_cal_fname = '/storage/store/data/camcan-mne/Cam-CAN_sss_cal.dat'
# mf_ctc_fname = '/storage/store/data/camcan-mne/Cam-CAN_ct_sparse.fif'

find_flat_channels_meg = True
find_noisy_channels_meg = True
# use_maxwell_filter = False          # trying what happens
run_source_estimation = True
use_template_mri = "fsaverage_small"
adjust_coreg = True

event_repeated = "drop"
l_trans_bandwidth = "auto"

h_trans_bandwidth = "auto"

random_state = 42

shortest_event = 1

log_level = "info"

mne_log_level = "error"

# on_error = 'continue'
on_error = "continue"

N_JOBS = 40
subjects = ['CC110101'] # ad!!


print("done config camcan file")
