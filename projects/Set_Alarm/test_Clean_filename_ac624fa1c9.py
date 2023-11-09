# Importing necessary Libraries 
import pytest
import os.path

# Function to clean filename
def clean_filename(filename):
    if filename == "":
        return ""
    name, ext = os.path.splitext(filename)
    name_words = name.split('_')
    capitalized_words = [word.capitalize() for word in name_words]
    return ' '.join(capitalized_words)

class TestCaseCleanFilename:

    def test_Clean_filename_ac624fa1c9(self):
        # testcase 1
        assert clean_filename("my_photo.jpg") == "My Photo", "Test case 1 failed"

        # testcase 2
        assert clean_filename("my_first_photo.jpg") == "My First Photo", "Test case 2 failed"

        # testcase 3
        assert clean_filename("myphoto.jpg") == "Myphoto", "Test case 3 failed"

        # testcase 4
        assert clean_filename("My_First_photo.jpg") == "My First Photo", "Test case 4 failed"
        
        # scenario 5
        assert clean_filename("my_photo.JPG") == "My Photo", "Test case 5 failed"

        # scenario 6
        assert clean_filename("myphoto") == "Myphoto", "Test case 6 failed"

        # scenario 7
        assert clean_filename("MYPHOTO") == "MYPHOTO", "Test case 7 failed"

        # scenario 8
        assert clean_filename("") == "", "Test case 8 failed"
