from sys import path
from pathlib import Path
import mne

study_name = "age-prediction-benchmark"

# On drago
# N_JOBS = 80                   # ad
n_jobs = 1 #40                     # ad

bids_root = Path("../raw_data/TUAB/eval/normal/01_tcp_ar")
#deriv_root = Path("/storage/store3/derivatives/TUAB-healthy-bids2")
deriv_root = Path("processed_TUAB")
subjects_dir = None #Path('/storage/store/data/camcan-mne/freesurfer')

source_info_path_update = {'processing': 'autoreject',
                           'suffix': 'epo'}

eeg_template_montage = mne.channels.make_standard_montage("standard_1005")
eeg_template_montage.rename_channels(
    {ch: ch + '-REF' for ch in eeg_template_montage.ch_names})

inverse_targets = []

noise_cov = 'ad-hoc'
eeg_reference = []  # Tuab has a custom reference

subjects = ['00002355']

task = "rest"
# task = "normal"

analyze_channels = ['Fp1', 'Fp2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1',
                    'O2', 'F7', 'F8', 'T3', 'T4', 'T5', 'T6', 'A1', 'A2',
                    'Fz', 'Cz', 'Pz']

conditions = []

sessions = ["001"]

data_type = "eeg"
ch_types = ["eeg"]

l_freq = 0.1
h_freq = 49
resample_sfreq = 200

find_breaks = False

spatial_filter = None

reject = None

on_error = "abort"
on_rename_missing_events = "warn"


epochs_tmin = 0
epochs_tmax = 10 - 1 / resample_sfreq
rest_epochs_duration = 10. - 1 / resample_sfreq
rest_epochs_overlap = 0.
baseline = None

run_source_estimation = True
use_template_mri = "fsaverage_small" #True    #ad

event_repeated = "drop"
l_trans_bandwidth = "auto"

h_trans_bandwidth = "auto"

random_state = 42

shortest_event = 1

log_level = "info"

mne_log_level = "info"
on_error = 'continue'
# on_error = "continue"

# on_error = 'abort'
# on_error = 'debug'

