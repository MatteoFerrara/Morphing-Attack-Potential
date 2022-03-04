# Morph Attack Potential
This repository contains the Python source code to compute the Morph Attack Potential (MAP) metric.

# Overview
`MAP.py` provides the core functionalities to calculate the MAP metric.

`ComputeMAP.py` contains a script to compute the MAP metric given the following input parameters:
- *input_folder_path* - the folder containing a text file for each Face Recognition Systems (FRSs) involved containing the corresponding comparison scores;
- *output_folder_path* - the folder path where the MAP metric values will be saved as text files;
- *frs_info_file_path* - the path of a JSON file containing information about the involved FRSs.

`PaperScores` is a folder containing the scores used to generate the results reported in the MAP paper useful to test the Python scripts.

# FRS score file text format

A text file can be loaded by `ComputeMAP.py` as a FRS score file, if it contains for each morphed image as many lines as the number of subjects involved in its generation process (usually two). Given a morphed image and one of the involved subject, the corresponding score line must fulfill the following format:

*morphID* *subjectID* *score1* *score2* ... *scoreN*

where:
 - *morphID* is the unique identifier of the given morphed image (e.g., M001, M002, etc.);
 - *subjectID* is the unique identifier of the given subject;
 - *score1* *score2* ... *scoreN* are the scores obtained by comparing the morphed image against all probe images of the given subject.

Note that, to compute the MAP metric on multiple FRSs, the *morphID* and *subjectID* identifiers must be the same in the different score files.

If something is not clear, we suggest to take a look to example files store into `PaperScores` folder.


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

