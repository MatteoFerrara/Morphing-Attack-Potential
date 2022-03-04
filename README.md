# Morph Attack Potential
This repository contains the Python source code to compute the Morph Attack Potential (MAP) metric.

# Overview
`MAP.py` provides the core functionalities to calculate the MAP metric.

`ComputeMAP.py` contains a script to compute the MAP metric given the following input parameters:
- 'input_folder_path' - a set of text files (stored into the same folder) containing the comparison scores obtained using one or more Face Recognition Systems (FRSs);
- 'output_folder_path' - the folder path where the MAP metric values will be saved as text files;
- 'frs_info_file_path' - the path of a JSON file containing information about the involved FRSs.

`PaperScores` is a folder containing the scores used to generate the results reported in the MAP paper useful to test the Python scripts.

# FRS score file text format

For each FRS evaluated, a text file containing all the corresponding scores must be present in the input_folder_path

# FRS information needed

TODO

# How to run
Clone the repository
```bash
git clone https://github.com/MatteoFerrara/Morph-Attack-Potential.git
 ```   
Execute the `ComputeMAP.py` script
```bash
python3 ComputeMAP <input_folder_path> <output_folder_path> <frs_info_file_path>
 ```
`PaperScores` folder contains the scores used to generate the results reported in the MAP paper. To reproduce the results reported in Tables IV and V execute the following code
```bash
python3 ComputeMAP PaperScores/D/ PaperScores/D/ PaperScores/FRS_Info.json
 ```
 ```bash
python3 ComputeMAP PaperScores/PS/ PaperScores/PS/ PaperScores/FRS_Info.json
 ```

