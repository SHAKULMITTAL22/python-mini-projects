import pytest
import os
import shutil
import pandas as pd
from split_files import Split_Files

class Test_SplitFilesSplitData:

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Setup and teardown for each test."""
        yield
        if os.path.exists("file_split"):
            shutil.rmtree("file_split")

    @pytest.mark.positive
    def test_split_data_creates_correct_number_of_files(self):
        """Ensure that the function correctly splits the input file into multiple smaller files."""
        test_file = "test_data.csv"
        split_size = 20
        total_rows = 100

        # Create test CSV file
        df = pd.DataFrame({"col1": range(total_rows)})
        df.to_csv(test_file, index=False, header=False)

        # Run split_data
        splitter = Split_Files(test_file, split_size)
        splitter.split_data()

        # Assert correct number of files created
        assert len(os.listdir("file_split")) == 5

        os.remove(test_file)

    @pytest.mark.positive
    def test_split_data_handles_remainder_rows_correctly(self):
        """Ensure that remainder rows are handled correctly in the last file."""
        test_file = "test_data.csv"
        split_size = 20
        total_rows = 105

        df = pd.DataFrame({"col1": range(total_rows)})
        df.to_csv(test_file, index=False, header=False)

        splitter = Split_Files(test_file, split_size)
        splitter.split_data()

        assert len(os.listdir("file_split")) == 6

        os.remove(test_file)

    @pytest.mark.positive
    def test_split_data_generates_correct_file_format(self):
        """Ensure that the function correctly determines the output file format."""
        csv_file = "test_data.csv"
        txt_file = "test_data.txt"
        split_size = 10

        df = pd.DataFrame({"col1": range(30)})
        df.to_csv(csv_file, index=False, header=False)
        df.to_csv(txt_file, index=False, header=False, sep=' ')

        csv_splitter = Split_Files(csv_file, split_size)
        csv_splitter.split_data()
        assert all(f.endswith(".csv") for f in os.listdir("file_split"))

        shutil.rmtree("file_split")

        txt_splitter = Split_Files(txt_file, split_size)
        txt_splitter.split_data()
        assert all(f.endswith(".txt") for f in os.listdir("file_split"))

        os.remove(csv_file)
        os.remove(txt_file)

    @pytest.mark.negative
    def test_split_data_handles_empty_file(self):
        """Ensure that no files are created when the input file is empty."""
        test_file = "empty.csv"
        open(test_file, 'w').close()

        splitter = Split_Files(test_file, 10)
        splitter.split_data()

        assert len(os.listdir("file_split")) == 0

        os.remove(test_file)

    @pytest.mark.positive
    def test_split_data_handles_single_row_file(self):
        """Ensure that a single-row file is correctly processed."""
        test_file = "single_row.csv"
        df = pd.DataFrame({"col1": [1]})
        df.to_csv(test_file, index=False, header=False)

        splitter = Split_Files(test_file, 10)
        splitter.split_data()

        assert len(os.listdir("file_split")) == 1
        output_file = os.path.join("file_split", os.listdir("file_split")[0])
        output_df = pd.read_csv(output_file, header=None)
        assert len(output_df) == 1

        os.remove(test_file)

    @pytest.mark.positive
    def test_split_data_handles_large_split_size(self):
        """Ensure that when the split size is larger than the file size, all data is in one file."""
        test_file = "small_data.csv"
        df = pd.DataFrame({"col1": range(15)})
        df.to_csv(test_file, index=False, header=False)

        splitter = Split_Files(test_file, 50)
        splitter.split_data()

        assert len(os.listdir("file_split")) == 1
        output_file = os.path.join("file_split", os.listdir("file_split")[0])
        output_df = pd.read_csv(output_file, header=None)
        assert len(output_df) == 15

        os.remove(test_file)

    @pytest.mark.regression
    def test_split_data_cleans_output_directory(self):
        """Ensure that the function removes existing files before creating new ones."""
        os.mkdir("file_split")
        with open("file_split/dummy.txt", "w") as f:
            f.write("dummy data")

        test_file = "test_data.csv"
        df = pd.DataFrame({"col1": range(30)})
        df.to_csv(test_file, index=False, header=False)

        splitter = Split_Files(test_file, 10)
        splitter.split_data()

        assert "dummy.txt" not in os.listdir("file_split")

        os.remove(test_file)

    @pytest.mark.performance
    def test_split_data_handles_large_files(self):
        """Ensure that the function can handle large input files efficiently."""
        test_file = "large_data.csv"
        split_size = 100000
        total_rows = 1000000

        df = pd.DataFrame({"col1": range(total_rows)})
        df.to_csv(test_file, index=False, header=False)

        splitter = Split_Files(test_file, split_size)
        splitter.split_data()

        assert len(os.listdir("file_split")) == 10

        os.remove(test_file)

    @pytest.mark.valid
    def test_split_data_preserves_data_integrity(self):
        """Ensure that the data in the output files matches the original input data."""
        test_file = "test_data.csv"
        split_size = 10
        df = pd.DataFrame({"col1": range(30)})
        df.to_csv(test_file, index=False, header=False)

        splitter = Split_Files(test_file, split_size)
        splitter.split_data()

        reconstructed_data = []
        for file in sorted(os.listdir("file_split")):
            output_df = pd.read_csv(os.path.join("file_split", file), header=None)
            reconstructed_data.extend(output_df[0].tolist())

        assert reconstructed_data == list(range(30))

        os.remove(test_file)

    @pytest.mark.negative
    def test_split_data_handles_missing_file(self):
        """Ensure that the function raises an error when the input file does not exist."""
        with pytest.raises(FileNotFoundError):
            splitter = Split_Files("nonexistent.csv", 10)
            splitter.split_data()
