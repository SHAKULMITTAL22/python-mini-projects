import os
import pytest


def rename_files_with_whitespaces(dir_path, files):
    for file in files:
        # Check if file exists
        if os.path.isfile(os.path.join(dir_path, file)):
            # Check if file name contains whitespaces
            if any(c.isspace() for c in file):
                new_file_name = file.replace(' ', '_')
                os.rename(os.path.join(dir_path, file), os.path.join(dir_path, new_file_name))


def test_Rename_files_with_whitespaces_413bb6262b():
    # Create a test directory with diverse types of filenames
    os.mkdir('testdir')
    open(os.path.join('testdir', 'file 1.txt'), 'a').close()
    open(os.path.join('testdir', 'file2.txt'), 'a').close()
    open(os.path.join('testdir', ' file3.txt'), 'a').close()
    open(os.path.join('testdir', 'file 4 .txt'), 'a').close()
    open(os.path.join('testdir', 'FILE 5.TXT'), 'a').close()
    open(os.path.join('testdir', 'fi$le 6.txt'), 'a').close()
    files = os.listdir('testdir')

    # Scenario 1 
    rename_files_with_whitespaces('testdir', ['file2.txt'])
    assert 'file2.txt' in os.listdir('testdir'), "file2.txt should not be renamed."
  
    # Scenario 2
    with pytest.raises(FileNotFoundError):
        rename_files_with_whitespaces('not_a_real_dir', ['not_a_real_file.txt'])

    # Scenario 3, 4, 5, 7, 8, 12, 13, 14, 15
    rename_files_with_whitespaces('testdir', files)
    renamed_files = os.listdir('testdir')
    assert all(' ' not in filename for filename in renamed_files), "No files should have white spaces in their names." 

    # Scenario 6
    open(os.path.join('testdir', '.txt'), 'a').close()
    rename_files_with_whitespaces('testdir', ['.txt'])
    assert '.txt' in os.listdir('testdir'), "Zero-length filename file should not be renamed." 

    # Scenario 10
    open(os.path.join('testdir', 'file_1.txt'), 'a').close()
    with pytest.raises(FileExistsError):
        rename_files_with_whitespaces('testdir', ['file 1.txt'])

    # Clean up the test directory
    for file in os.listdir('testdir'):
        os.remove(os.path.join('testdir', file))
    os.rmdir('testdir')
