from model import PopMusicTransformer
from glob import glob
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

def main():
    # declare model
    model = PopMusicTransformer(
        checkpoint='Chinese-piano-checkpoint',
        is_training=True)
    # prepare data
    midi_paths = glob('data/train/*.mid') # you need to revise it
    training_data = model.prepare_data(midi_paths=midi_paths)

    # check output checkpoint folder
    output_checkpoint_folder = 'my-piano' # your decision
    if not os.path.exists(output_checkpoint_folder):
        os.mkdir(output_checkpoint_folder)
    
    # finetune
    model.finetune(
        training_data=training_data,
        output_checkpoint_folder=output_checkpoint_folder)

    ####################################
    # after finetuning, please choose which checkpoint you want to try
    # and change the checkpoint names you choose into "model"
    # and copy the "dictionary.pkl" into the your output_checkpoint_folder
    # ***** the same as the content format in "REMI-tempo-checkpoint" *****
    # and then, you can use "main.py" to generate your own music!
    # (do not forget to revise the checkpoint path to your own in "main.py")
    ####################################

    # close
    model.close()

if __name__ == '__main__':
    main()
