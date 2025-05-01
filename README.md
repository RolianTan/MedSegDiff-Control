MedSegDiff-Control Setup

## Requirement

``pip install -r requirement.txt``

## Example Cases
### Melanoma Segmentation from Skin Images
1. Download ISIC dataset from https://challenge.isic-archive.com/data/. Your dataset folder under "data" should be like:

~~~
data
|   ----ISIC
|       ----Test
|       |   |   ISBI2016_ISIC_Part1_Test_GroundTruth.csv
|       |   |   
|       |   ----ISBI2016_ISIC_Part1_Test_Data
|       |   |       ISIC_0000003.jpg
|       |   |       .....
|       |   |
|       |   ----ISBI2016_ISIC_Part1_Test_GroundTruth
|       |           ISIC_0000003_Segmentation.png
|       |   |       .....
|       |           
|       ----Train
|           |   ISBI2016_ISIC_Part1_Training_GroundTruth.csv
|           |   
|           ----ISBI2016_ISIC_Part1_Training_Data
|           |       ISIC_0000000.jpg
|           |       .....
|           |       
|           ----ISBI2016_ISIC_Part1_Training_GroundTruth
|           |       ISIC_0000000_Segmentation.png
|           |       .....
~~~

    
2. For training, run: ``python scripts/segmentation_train.py --data_name ISIC --data_dir *input data direction* --out_dir *output data direction* --image_size 256 --num_channels 128 --class_cond False --num_res_blocks 2 --num_heads 1 --learn_sigma True --use_scale_shift_norm False --attention_resolutions 16 --diffusion_steps 1000 --noise_schedule linear --rescale_learned_sigmas False --rescale_timesteps False --lr 1e-4 --batch_size 8``

3. For sampling, run: ``python scripts/segmentation_sample.py --data_name ISIC --data_dir *input data direction* --out_dir *output data direction* --model_path *saved model* --image_size 256 --num_channels 128 --class_cond False --num_res_blocks 2 --num_heads 1 --learn_sigma True --use_scale_shift_norm False --attention_resolutions 16 --diffusion_steps 1000 --noise_schedule linear --rescale_learned_sigmas False --rescale_timesteps False --num_ensemble 5``

4. For evaluation, run ``python scripts/segmentation_env.py --inp_pth *folder you save prediction images* --out_pth *folder you save ground truth images*``


In default, the samples will be saved at `` ./results/`` 
### Brain Tumor Segmentation from MRI
1. Download BRATS2020 dataset from https://www.med.upenn.edu/cbica/brats2020/data.html. Your dataset folder should be like:
~~~
data
└───training
│   └───slice0001
│       │   brats_train_001_t1_123_w.nii.gz
│       │   brats_train_001_t2_123_w.nii.gz
│       │   brats_train_001_flair_123_w.nii.gz
│       │   brats_train_001_t1ce_123_w.nii.gz
│       │   brats_train_001_seg_123_w.nii.gz
│   └───slice0002
│       │  ...
└───testing
│   └───slice1000
│       │  ...
│   └───slice1001
│       │  ...
~~~
    
2. For training, run: ``python scripts/segmentation_train.py --data_dir (where you put data folder)/data/training --out_dir output data direction --image_size 256 --num_channels 128 --class_cond False --num_res_blocks 2 --num_heads 1 --learn_sigma True --use_scale_shift_norm False --attention_resolutions 16 --diffusion_steps 1000 --noise_schedule linear --rescale_learned_sigmas False --rescale_timesteps False --lr 1e-4 --batch_size 8``

3. For sampling, run: ``python scripts/segmentation_sample.py --data_dir (where you put data folder)/data/testing --out_dir output data direction --model_path saved model --image_size 256 --num_channels 128 --class_cond False --num_res_blocks 2 --num_heads 1 --learn_sigma True --use_scale_shift_norm False --attention_resolutions 16 --diffusion_steps 1000 --noise_schedule linear --rescale_learned_sigmas False --rescale_timesteps False --num_ensemble 5``



