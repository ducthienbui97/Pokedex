from PIL import Image
import os
import numpy as np
import copy
np.random.seed(317)
train_data_dir = os.path.join('data','train')
validation_data_dir = os.path.join('data','validate')
def convert(data_dir):
    for root, dirs, filenames in os.walk(data_dir):
        if len(filenames) == 0:
            continue
        oldfiles = copy.copy(filenames)
        print(oldfiles)
        for file in oldfiles:
            old_file = os.path.join(root,file)
            new_file = os.path.join(root,str(np.random.randint(0,1000000000)) + ".jpg")
            Image.open(old_file).convert("RGB").save(new_file,"JPEG")
            os.remove(old_file)
