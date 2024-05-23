import os
import numpy as np
import open3d as o3d

folder = "output/custom"

scene_ext = "_f1000.ply"
bbox_ext = "_bbox.ply"
comb_ext = "_comb.ply"

file_list = []


for file in os.listdir(folder):
    if file.endswith(scene_ext):
        file_name = os.path.basename(file)
        file_name = file_name.replace("_f1000", "")
        file_name = os.path.splitext(file_name)[0]
        file_list.append(file_name)

for file_name in file_list:
    scene_pc = o3d.io.read_point_cloud(os.path.join(folder, file_name + scene_ext))
    bbox_pc = o3d.io.read_point_cloud(os.path.join(folder, file_name + bbox_ext))
    combined_pc = o3d.geometry.PointCloud()
    combined_pc.points = o3d.utility.Vector3dVector(np.vstack([np.asarray(scene_pc.points), np.asarray(bbox_pc.points)]))
    combined_pc.colors = o3d.utility.Vector3dVector(np.vstack([np.asarray(scene_pc.colors), np.asarray(bbox_pc.colors)]))

    o3d.io.write_point_cloud(os.path.join(folder, file_name + comb_ext), scene_pc + bbox_pc)
    print("ply file saved")

