MonoDepth_Prediction - *CMU11785 Project*
======


## Previously attempted baselines
* Big to small: [bts](https://github.com/cleinc/bts)
* Towards Good Practice for CNN Based Monocular Depth Estimation: [supervised dispnet](https://github.com/zenithfang/supervised_dispnet)
## Currently attempting baselines
* Main repo: [GCN](https://github.com/ArminMasoumian/GCNDepth)
* Dataset preparation: [monodepth2](https://github.com/nianticlabs/monodepth2)
## Dataset prep & ground truth generation
| :memo:        | The ground truths are generated according to lidar .bin files        |
|---------------|:------------------------|
1. Select a small portion of dataset to download
```bash
python select_dataset.py mono/datasets/splits/kitti_archives_to_download.txt
```
2. Download process for a specific day of dataset ~ 3h
```bash
wget -i splits/kitti_archives_to_download.txt -P kitti_data/
```
3. Backup original files
```bash
cp mono/datasets/splits/eigen_full/train_files.txt mono/datasets/splits/eigen_full/train_files_ori.txt
```
4. Select a small portion of dataset to test the training performance
```bash
python select_dataset.py mono/datasets/splits/eigen_full/train_files.txt
```
```bash
python select_dataset.py mono/datasets/splits/eigen_full/val_files.txt
```
5. Generate ground truth
```bash
 python mono/datasets/export_gt_depth.py --data_path kitti_data --split eigen 
```
6. Download ResNet pretrained models from pytorch [official website](https://pytorch.org/vision/0.8/_modules/torchvision/models/resnet.html) and place it under `Models/`
7. Change directories in `config/cfg_kitti_autoencoder.py`
