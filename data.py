from __future__ import print_function
import tensorflow 
import keras
# from keras.preprocessing.image import ImageDataGenerator
# import numpy as np

# import os
# import glob
# import skimage.io as io
# import skimage.transform as trans

# Sky = [128,128,128]
# Building = [128,0,0]
# Pole = [192,192,128]
# Road = [128,64,128]
# Pavement = [60,40,222]
# Tree = [128,128,0]
# SignSymbol = [192,128,128]
# Fence = [64,64,128]
# Car = [64,0,128]
# Pedestrian = [64,64,0]
# Bicyclist = [0,128,192]
# Unlabelled = [0,0,0]

# COLOR_DICT = np.array([Sky, Building, Pole, Road, Pavement,
#                           Tree, SignSymbol, Fence, Car, Pedestrian, Bicyclist, Unlabelled])

# def dataAdjust(img, mask, flag_multiclass, num_class):
#   if(flag_multiclass):
#     img = img/255
    # mask = mask[:, :, :, 0] if (len)
