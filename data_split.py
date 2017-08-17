# -*- coding: utf-8 -*-

import os
import numpy as np
from sklearn.model_selection import train_test_split

np.random.seed(317)
for root, dirs, filenames in os.walk(os.path.join('data','train')):
    if len(filenames) == 0:
        continue
    validate_path = os.path.join('data','validate',os.path.split(root)[1])
    if not os.path.exists(validate_path):
        os.makedirs(validate_path)
    validate_names = train_test_split(np.asarray(filenames))[1]
    for name in validate_names:
        os.rename(os.path.join(root,name),os.path.join(validate_path,name))