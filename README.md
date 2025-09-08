Drop-DTW: Aligning Common Signal Between Sequences While Dropping Outliers
========

This is the official PyTorch implementation of Drop-DTW [1] (published at NeurIPS'21). The code includes the core Drop-DTW algorithm as well as the step localization experiments on the COIN dataset [2].

## Set up the data
1. (a) Download pre-extracted features for the COIN dataset by running `download_coin_features.sh` in the root folder of the project. The features are extracted using the S3D net pretrained on HowTo100M [3];
OR
(b) If for some reason you do not want to use pre-extracted features but instead you want to extract the features yourself, please follow the instructions in `video_encoding/`. This step is performed *instead* of step 1a.
2. In the terminal where you are going to run training/testing, run the following command first:
    ```
    ulimit -n 5000
    ```
    This sets the number of simultaneously open files to 5000 which is important to make the data loader function properly.

## Train the network
In order to train a feature mapping with Drop-DTW loss (using 0.3 percentile drop-cost) run the following command:
```
python3 train.py --name=my_model --keep_percentile=0.3
```
Inspect `train.py` for possible additional training configurations, such network architecture changes, learnable drop cost and many more.

## Step localization inference
To test your model's ability to do step localization on the CONI dataset, run the following code:
```
python3 evaluate.py --name=my_model
```
You can change the inference method from Drop-DTW to some other algorithms and alter other testing settings using flags. Please, refer to `evaluate.py` for more details.

## References
[1] Dvornik et al. "Drop-DTW: Aligning Common Signal Between Sequences While Dropping Outliers." NeurIPS'21.
[2] Tang et al. "COIN: A Large-scale Dataset for Comprehensive Instructional Video Analysis." CVPR'19
[3] - Miech et al. "End-to-end learning of visual representations from uncurated instructional videos." CVPR'20.
