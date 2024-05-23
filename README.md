# Monocular Object detection & Scene reconstruction

## Table of Contents:
1. [Dataset](#dataset)
2. [Cube R-CNN](#cubercnn)
3. [Metric 3D Inference](#metric3d)
4. [Unprojection](#unprojection)

## Dataset <a name="dataset"> </a>
- We selected 6 images from `Omni3d - ARKitScience dataset`, including our main target objects-indoor furniture. You can download it referencing below.
https://github.com/facebookresearch/omni3d/blob/main/datasets/ARKitScenes/download_arkitscenes_images.sh

## Cube R-CNN Inference <a name="cubercnn"></a>
- Monocular object detection & layout estimation
#### Installation (anaconda, CUDA 11.1) 
###### terminal commands
``` bash
$ conda create -n cubercnn111 -y python=3.8
$ source activate cubercnn111

$ conda install pytorch==1.8.0 torchvision==0.9.0 cudatoolkit=11.1 -c pytorch -c conda-forge -y 
$ conda install -c fvcore fvcore -y
$ conda install -c iopath iopath -y 
$ conda install -c pytorch3d -c conda-forge pytorch3d -y 

$ export PATH=/usr/local/cuda-11.1/bin:$PATH
$ export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/cuda-11.1/lib64
$ export CUDA_PATH=/usr/local/cuda-11.1

$ pip install cython opencv-python
$ pip install 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'
$ python -m pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu111/torch1.8/index.html
$ conda install -c conda-forge scipy seaborn -y

$ pip uninstall pillow -y
$ pip install pillow==9.1.0

$ sh train_bbox.sh 
```


##### train_bbox.sh - extracting 3D bounding box points
*Do not change --congif-file path cubercnn://(...).
- set your own `input-folder` & `OUTPUT_DIR`
- set `threshold` between [0, 1] : the probability of object classification
``` bash
#!/bin/bash
python demo/demo_bbox.py \
--config-file cubercnn://omni3d/cubercnn_DLA34_FPN.yaml \
--input-folder "datasets/custom" \
--threshold 0.8 --display \
MODEL.WEIGHTS cubercnn://omni3d/cubercnn_DLA34_FPN.pth \
OUTPUT_DIR output/custom
```
##### demo_bbox.py 
You can set the focal length in `do_test()` - `focal_length` (default = `1000`)

*Use a focal length same with `Metric3D`.

## Metric3D Inference <a name="metric3d"></a>
- Monocular metric depth estimation
#### Inference via web demo (+ 3D unprojection)
https://huggingface.co/spaces/JUGGHM/Metric3D

You can set the focal length also. (default = `1000`) 

*Use a focal length same with `Cube R-CNN`.

## Unprojection <a name="unprojection"> </a>
- Unproject both scene and bbox points in a point cloud
- set your own file paths in visualize.py
``` bash
#!/bin/bash
python demo/visualize.py
```
