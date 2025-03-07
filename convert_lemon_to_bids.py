# %%
import argparse
import os
import pathlib
from tkinter import BOTTOM
import urllib.request
import numpy as np
import pandas as pd
from joblib import Parallel, delayed
import mne
# from mne.io.brainvision.brainvision import _aux_vhdr_info

from mne_bids import write_raw_bids, print_dir_tree, make_report, BIDSPath

# %%

lemon_info = pd.read_csv(
    "META_File_IDs_LEMON_new.csv")
    # "./META_File_IDs_Age_Gender_Education_Drug_Smoke_SKID_LEMON.csv")
lemon_info = lemon_info.set_index("ID")
eeg_subjects = pd.read_csv('lemon_eeg_subjects.csv')



# %%

lemon_info = lemon_info.loc[eeg_subjects.subject]
lemon_info['gender'] = lemon_info['Gender_ 1=female_2=male'].map({1: 2, 2: 1})



# %%
lemon_info['age_guess'] = np.array(
  lemon_info['Age'].str.split('-').tolist(), dtype=int).mean(1) #ad: changed np.int to int.
subjects = list(lemon_info.index)

# %% TESTING ADRIAN 

# data_path = "/u/home/dena/Documents/clean_brain_age/brain-age-benchmark/raw_LEMON/data/sub-010002"
# fname = pathlib.Path(data_path) / "RSEEG" / "sub-010002.vhdr"    
# raw = mne.io.read_raw_brainvision(fname)

# raw.set_channel_types({"VEOG": "eog"})
# montage = mne.channels.make_standard_montage('standard_1005')
# raw.set_montage(montage)
# sub_id = "010002"
# subject = "sub-010002"

# raw.info['subject_info'] = {
#     'participant_id': sub_id,
#     'sex': lemon_info.loc["sub-010002", 'gender'],
#     'age': lemon_info.loc["sub-010002", 'age_guess'],
#     # XXX LEMON shares no public age 
#     'hand': lemon_info.loc["sub-010002", 'Handedness']
# }
# events, event_id = mne.events_from_annotations(raw)
# additional_annotations = {"eyes/open": 200, "eyes/closed": 210}

# event_id.update(additional_annotations)

# %%


# %% 

# subjects_ = subjects
# if True:
#     subjects_ = subjects[:1]

# # good_subjects = Parallel(n_jobs=40)(
# #     delayed(_convert_subject)(subject, lemon_data_dir, bids_save_dir)
# #     for subject in subjects_) 
# # subjects_ = [sub for sub in good_subjects if not isinstance(sub, tuple)]
# # _, bad_subjects, errs = zip(*[
# #     sub for sub in good_subjects if isinstance(sub, tuple)])
# # bad_subjects = pd.DataFrame(
# #     dict(subjects= bad_subjects, error=errs))

# good_subjects = Parallel(n_jobs=n_jobs)(
#         delayed(_convert_subject)(subject, lemon_data_dir, bids_save_dir)
#         for subject in subjects_) 
#     # print("Printing good subjects !!!")
#     print(good_subjects)

#%%

def convert_lemon_to_bids(lemon_data_dir, bids_save_dir, n_jobs=1, DEBUG=False):
    """Convert TUAB dataset to BIDS format.

    Parameters
    ----------
    lemon_data_dir : str
        Directory where the original LEMON dataset is saved, e.g.
        `/storage/store3/data/LEMON_RAW`.
    bids_save_dir : str
        Directory where to save the BIDS version of the dataset.
    n_jobs : None | int
        Number of jobs for parallelization.
    """
    subjects_ = subjects

    if DEBUG:
        subjects_ = subjects[:1]

    good_subjects = Parallel(n_jobs=n_jobs)(
        delayed(_convert_subject)(subject, lemon_data_dir, bids_save_dir)
        for subject in subjects_) 
    
    # ad: I don't see how this could be a tuple and not just a string. 
    subjects_ = [sub for sub in good_subjects if not isinstance(sub, tuple)]


    # ad: Exclude data which is not useful for us: Bad subjects only are bad due to following missing data:
    # “Comment/no USB Connection to actiCAP, New Segment/, Stimulus/S 1, Stimulus/S200, Stimulus/S210” 
    # _, bad_subjects, errs = zip(*[
    #     sub for sub in good_subjects if isinstance(sub, tuple)])
    
    # bad_subjects = pd.DataFrame(dict(subjects= bad_subjects, error=errs))
    # bad_subjects.to_csv(
    #     'processed_LEMON/bids_conv_erros.csv')

    # update the participants file as LEMON has no official age data
    participants = pd.read_csv(
        "Participants_LEMON.csv", sep=',')
    participants = participants.set_index("ID")
    participants.loc[subjects_, 'age'] = lemon_info.loc[subjects_, 'age_guess']
    participants.to_csv(
        "processed_LEMON/data/participants.csv", sep='\t')


def _convert_subject(subject, data_path, bids_save_dir):
    """Get the work done for one subject"""
    try:
        fname = pathlib.Path(data_path) / subject / "RSEEG" / f"{subject}.vhdr"    
        raw = mne.io.read_raw_brainvision(fname)

        raw.set_channel_types({"VEOG": "eog"})
        montage = mne.channels.make_standard_montage('standard_1005')
        raw.set_montage(montage)
        sub_id = subject.strip("sub-")
        raw.info['subject_info'] = {
            'participant_id': sub_id,
            'sex': lemon_info.loc[subject, 'gender'],
            'age': lemon_info.loc[subject, 'age_guess'],
            # XXX LEMON shares no public age 
            'hand': lemon_info.loc[subject, 'Handedness']
        }
        events, event_id = mne.events_from_annotations(raw)

        events = events[(events[:, 2] == 200) | (events[:, 2] == 210)]
        # event_id = {"eyes/open": 200, "eyes/closed": 210}
        event_id.update({"eyes/open": 200, "eyes/closed": 210}) # ad: Seems previously like a significant error. 
        bids_path = BIDSPath(
            subject=sub_id, session=None, task='RSEEG',
            run=None,
            root=bids_save_dir, datatype='eeg', check=True)

        write_raw_bids(
            raw,
            bids_path,
            events_data=events,
            event_id=event_id,
            overwrite=True
        )
    except Exception as err:
        print(err)
        return ("BAD", subject, err)
    return subject


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert LEMON to BIDS.')
    parser.add_argument(
        '--lemon_data_dir', type=str,
        default='raw_LEMON/data',
        help='Path to the original data.')
    parser.add_argument(
        '--bids_data_dir', type=str,
        default=pathlib.Path("processed_LEMON/data"),
        help='Path to where the converted data should be saved.')
    parser.add_argument(
        '--n_jobs', type=int, default=1,
        help='number of parallel processes to use (default: 1)')
    parser.add_argument(
        '--DEBUG', type=bool, default=False,
        help='activate debugging mode')
    args = parser.parse_args()

    convert_lemon_to_bids(
        args.lemon_data_dir, args.bids_data_dir, n_jobs=args.n_jobs,
        DEBUG=args.DEBUG)

    print_dir_tree(args.bids_data_dir)
    print(make_report(args.bids_data_dir))

# %%
