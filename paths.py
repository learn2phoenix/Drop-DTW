import sys
import os

# MIL-NCE code
S3D_PATH = "/user/n.dvornik/Git/S3D_HowTo100M/"
# paths to datasets
COIN_PATH = "/user/n.dvornik/Datasets/COIN/"
CT_PATH = None
YC_PATH = "/mnt/DATA/Datasets/YouCook2/"
ARA_PATH = "/mnt/DATA/Datasets/multimodal-aligned-recipe-corpus/ARA_encodings/"
MR_PATH = "/mnt/DATA/Datasets/multimodal-aligned-recipe-corpus/Microsoft_English_encodings/"
# root project and weights folder
# PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = "/mnt/DATA/Datasets/YouCook2/"
WEIGHTS_PATH = os.path.join(PROJECT_PATH, "weights")
