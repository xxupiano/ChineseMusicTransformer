# Chinese Music Transformer
A REMI-based Transformer-XL for Chinese Piano Generation

## Install Dependencies

- python 3.6
- `conda install --yes --file requirements.txt`

## Download the Pre-trained Checkpoint

- [Chinese-piano-checkpoint (474 MB)](https://drive.google.com/drive/folders/1rVdFPlisPKwNDkIjVJIyQ7i0i-LyKz7U)


## Download the dataset *Red Melody*

- training set: 193 pieces

- development set: 10 pieces

- test set: 10 pieces

- The file, Red_Melody.csv, contains all information of the dataset.

- link: https://drive.google.com/file/d/1gAmQD_vrJJFQzfWMPTu0ZwMiThV7ERxW/view?usp=sharing

## Finetune
`python finetune.py`

## Predict
`python main.py`
