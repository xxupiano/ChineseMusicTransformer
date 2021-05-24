from model import PopMusicTransformer
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

def main():
    # declare model
    model = PopMusicTransformer(
        checkpoint='my-piano',
        is_training=False)
    
    for i in range(0,10):
        # generate continuation
        model.generate(
            n_target_bar=30,
            temperature=1.2,
            topk=5,
            output_path='./result/continuation'+str(i)+'.midi',
            prompt='./data/evaluation/00'+str(i)+'.mid')

        # generate from scratch
        model.generate(
            n_target_bar=30,
            temperature=1.2,
            topk=5,
            output_path='./result/from_scratch'+str(i)+'.midi',
            prompt=None)
    
    # close model
    model.close()

if __name__ == '__main__':
    main()
