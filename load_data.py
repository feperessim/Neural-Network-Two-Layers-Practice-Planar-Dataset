import numpy as np
import glob
import os.path as path
from scipy import misc

def loadData():
    IMAGE_PATH = 'planesnet/planesnet/'
    file_paths = glob.glob(path.join(IMAGE_PATH, '*.png'))
    images = [misc.imread(path) for path in file_paths]
    images = np.asarray(images)
    n_images = images.shape[0]
    labels = np.zeros((1, n_images))
    for i in range(n_images):
        filename = path.basename(file_paths[i])[0]
        labels[0][i] = int(filename[0])
    return images, labels