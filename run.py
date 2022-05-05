import os

if __name__ == '__main__':

    os.system('python3.8 -m torch.distributed.launch --master_port=9900 --nproc_per_node=1 train.py --work_dir results')
    
