# Hospital Readmission Predictor

This project is a fork of 
[keerthikkn's *Hospital Readmission Prediction* process](https://github.com/keerthikkn/Hospital_Readmission_Prediction), 
aimed at enhancing its readability and performance.

## Usage
To get started with this project you can follow these steps:
1. Clone the repository on your local machine and navigate to its directory
2. Create a python virtual environment for the project and activate it
```bash
python -m venv .venv

# Use the appropriate command below based on your operating system and shell:
# source .venv/bin/activate  # On Bash/Zsh shell (Linux/MacOS)
# source .venv/bin/activate.fish  # On Fish shell
# .venv\Scripts\activate  # On Windows
```
3. Install the required dependencies
```bash
pip install -r requirements.txt
```
4. Use [the Jupyter notebook](training.ipynb) to train and evaluate the model, or use the already version to make predictions on new data with
```bash
python run.py --input <input_csv_file> --output <output_csv_file>
```