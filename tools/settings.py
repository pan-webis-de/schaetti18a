# -*- coding: utf-8 -*-
#

# Imports
from torchlanguage import transforms as ltransforms
from torchvision import transforms


################
# Settings
################

# Settings
image_size = 223
min_length = 165
voc_sizes = {'c1': {'en': 1628, 'ar': 1839, 'es': 1805}, 'c2': {'en': 21510, 'ar': 31694, 'es': 30025}}
class_to_idx = {'female': 0, 'male': 1}
idx_to_class = {0: 'female', 1: 'male'}
alpha = 0.5
