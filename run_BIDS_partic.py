#! /usr/bin/python


# Set a path to top level subject raw data directory:

#   python needs quotes so it knows dir_path is a string, that was noted in the docstring

#   previously sent in case you ever need to know type a variable should be

dir_path='/mnt/Filbey/common/Studies/MJX/0Data_NL/4_MRIdata/sub-1031' 

 

# Set a path to the bids directory to convert raw data to:

bids_path='/mnt/Filbey/common/Studies/MJX/BIDS/NL'



# Run BIDS conversion script

#  This is all python, you were trying to run it as bash, hence the error,

from mjxproc.utils import Subject

some_subject = Subject(dir_path, bids_path)

some_subject.to_bids()
