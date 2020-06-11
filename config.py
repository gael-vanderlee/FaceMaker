# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
#
# This work is licensed under the Creative Commons Attribution-NonCommercial
# 4.0 International License. To view a copy of this license, visit
# http://creativecommons.org/licenses/by-nc/4.0/ or send a letter to
# Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

from pathlib import Path

"""Global configuration."""

#----------------------------------------------------------------------------
# Paths.

project_dir = Path(__file__).resolve().parent
result_dir = 'results'
data_dir = 'datasets'
cache_dir = 'cache'
raw_dir = project_dir / "input_images/"
aligned_dir = project_dir / "outputs" / "aligned_images/"
gen_images_dir = project_dir / "outputs" / "generated_images/"
latents_dir = project_dir / "outputs" / "latents_images/"
run_dir_ignore = ['results', 'datasets', 'cache']

# experimental - replace Dense layers with TreeConnect
use_treeconnect = False
treeconnect_threshold = 1024

#----------------------------------------------------------------------------
