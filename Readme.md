# Machine Learning in Information Security Final Project

## Setup

### Prerequisites

- Python 3.13
- Pyenv
- Pyenv-virtualenv

### Installation

#### Create a virtual environment and activate it
```bash
pyenv install 3.13.0
pyenv virtualenv 3.13.0 mlis
pyenv activate mlis
```

#### Install dependencies
```bash
pip install -r requirements.txt
```

## Files and folders description

### Data

- `data`: Contains the dataset used in this project.
  - The dataset was obtained from this link and provided by the lecturer of the course. **Dr. Le Kim Hung**
  - `train.csv`: The original training dataset.
  - `test.csv`: The original test dataset.
  - `train_binary.csv`: The original training dataset with binary labels.
  - `train_multiclass.csv`: The original training dataset with multiclass labels.

### Processing files
- `AddBinaryClassColumn.py`: Script to add a binary class column to the dataset.
- `AddMulticlassClassColumn.py`: Script to add a multiclass class column to the dataset.

### Feature Selection Notebooks
- `BinaryFeatureSelection.ipynb`: Notebook to perform feature selection on the binary dataset with Random Forest.
- `MulticlassFeatureSelection.ipynb`: Notebook to perform feature selection on the multiclass dataset with Random Forest.

### Training Notebooks
- `TrainBinaryClassTop25.ipynb`: Notebook to train a binary classifier with the top 25 features.
- `TrainMulticlassClassTop25.ipynb`: Notebook to train a multiclass classifier with the top 25 features.

### Requirements
- The `requirements.txt` file contains the required packages and their versions. 