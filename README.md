# Morph Attack Potential
This repository contains the Python source code to compute the Morph Attack Potential (MAP) metric.

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

