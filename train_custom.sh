#!/bin/bash

CUDA_VISIBLE_DEVICES=7 python demo/demo_bbox.py \
--config-file cubercnn://omni3d/cubercnn_DLA34_FPN.yaml \
--input-folder "datasets/custom" \
--threshold 0.8 --display \
MODEL.WEIGHTS cubercnn://omni3d/cubercnn_DLA34_FPN.pth \
OUTPUT_DIR output/demo/custom_bbox

