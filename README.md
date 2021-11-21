# Chinese Music Transformer
A REMI-based Transformer-XL for Chinese Piano Generation

## Install Dependencies

- python 3.6
- `pip install -r requirements.txt`

## Download the Pre-trained Checkpoint

- `Chinese-piano-checkpoint` (474 MB) 

  link: https://pan.baidu.com/s/1UvjMXkDTXf8dDPR6BClybQ

  key: ci2e

## Download the dataset *Red Melody*

- training set: 193 pieces

- development set: 10 pieces

- test set: 10 pieces

- The file, Red_Melody.csv, contains all information of the dataset.

- link: https://pan.baidu.com/s/16QAMAnGPt-lN70WDkhagtA

  key: d0om

## Finetune
`python finetune.py`

## Predict
`python main.py`
