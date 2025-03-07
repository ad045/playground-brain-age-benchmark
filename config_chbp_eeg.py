import pathlib
import mne

study_name = "age-prediction-benchmark"

# bids_root = pathlib.Path(
#     "/storage/store3/data/CHBMP_EEG_and_MRI/ds_bids_chbmp")
bids_root = pathlib.Path("/u/home/dena/Documents/clean_brain_age/raw_data/CHBP") #processed_CHBM")
# /u/home/dena/Documents/clean_brain_age/brain-age-benchmark/processed_CHBM/participants.csv

deriv_root = pathlib.Path("/u/home/dena/Documents/clean_brain_age/brain-age-benchmark/processed_CHBP") 
                          #storage/store3/derivatives/CHBMP_EEG_and_MRI/")
# "/storage/store2/derivatives/eeg-pred-modeling-summer-school/")

subjects_dir = pathlib.Path("/u/home/dena/Documents/clean_brain_age/brain-age-benchmark/processed_CHBP") 
                    # '/storage/store/data/camcan-mne/freesurfer')

source_info_path_update = {'processing': 'autoreject',
                           'suffix': 'epo'}

inverse_targets = []

noise_cov = 'ad-hoc'

task = "protmap"

sessions = []  # keep empty for code flow
data_type = "eeg"
ch_types = ["eeg"]

analyze_channels = [
    "AF3", "AF4", "C1", "C2", "C3", "C4", "C5", "C6", "CP1", "CP2", "CP3",
    "CP4", "CP5", "CP6", "Cz", "F1", "F2", "F3", "F4", "F5", "F6", "F7",
    "F8", "FC1", "FC2", "FC3", "FC4", "FC5", "FC6", "Fp1", "Fp2", "Fz",
    "O1", "O2", "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "PO3",
    "PO4", "PO5", "PO6", "PO7", "PO8", "Pz", "T7", "T8", "TP7", "TP8",
]

eeg_template_montage = mne.channels.make_standard_montage("standard_1005")
eeg_template_montage.rename_channels({"FFT7h": "FFC7h", "FFT8h": "FFC8h"})

l_freq = 0.1
h_freq = 49

eeg_reference = []

find_breaks = False

# n_proj_eog = 1       # ad
n_proj_eog = dict(n_mag=1, n_grad=1, n_eeg=1) # ad


ssp_reject_eog = "autoreject_global"

reject = None

on_error = "abort"
on_rename_missing_events = "warn"

# N_JOBS = 30               # ad
n_jobs = 30                 # ad

epochs_tmin = 0
epochs_tmax = 10
baseline = None

run_source_estimation = True
# use_template_mri = True           # ad

rename_events = {
    "artefacto": "artefact",
    "discontinuity": "discontinuity",
    "electrodes artifacts": "artefact",
    "eyes closed": "eyes/closed",
    "eyes opened": "eyes/open",
    "fotoestimulacion": "photic_stimulation",
    "hiperventilacion 1": "hyperventilation/1",
    "hiperventilacion 2": "hyperventilation/2",
    "hiperventilacion 3": "hyperventilation/3",
    "hyperventilation 1": "hyperventilation/1",
    "hyperventilation 2": "hyperventilation/2",
    "hyperventilation 3": "hyperventilation/3",
    "ojos abiertos": "eyes/open",
    "ojos cerrados": "eyes/closed",
    "photic stimulation": "photic_stimulation",
    "recuperacion": "recovery",
    "recuperation": "recovery",
}

conditions = ["eyes/open", "eyes/closed"]

event_repeated = "drop"
l_trans_bandwidth = "auto"

h_trans_bandwidth = "auto"


random_state = 42

shortest_event = 1

log_level = "info"

mne_log_level = "error"

# on_error = 'continue'
on_error = "continue"
