# -*- coding: utf-8 -*-
from __future__ import print_function

import numpy as np
import numpy
import pcl
import time
import pcl.pcl_visualization
# from pcl.pcl_registration import icp, gicp, icp_nl


def main():
    # cloud = pcl.load_XYZRGB(
    #     './examples/pcldata/tutorials/table_scene_mug_stereo_textured.pcd')
    cloud = pcl.load("/home/student/Documents/cartographer/test/turtlebot3_imuodompt2_3/mapdata_37.pcd")
    # Centred the data
    # print(centred)
    ptcloud_centred = pcl.PointCloud()

    cloud_np = np.array(cloud)
    cloud_np_valid = cloud_np[~np.isnan(cloud_np).any(axis=1), :]
    cloud_np_valid_cen = cloud_np_valid-np.mean(cloud_np_valid, 0)
    cloud_xyzrgb_np1 = numpy.pad(cloud_np_valid, ((0,0),(0,1)), mode='constant', constant_values=1)
    cloud_xyzrgb_np2 = numpy.pad(cloud_np_valid_cen, ((0,0),(0,1)), mode='constant', constant_values=26600)

    #expand column to make point xyzrgb
    #cloud_xyzrgb_np = numpy.pad(cloud_np_valid, ((0,0),(0,1)), mode='constant', constant_values=1)
    pc2 = pcl._pcl.PointCloud_PointXYZRGB()
    visual = pcl.pcl_visualization.CloudViewing()
    twocloud_np = np.concatenate((cloud_xyzrgb_np1, cloud_xyzrgb_np2), axis=0)

    #pc2.from_array(cloud_xyzrgb_np1)
    #pc2.from_array(cloud_xyzrgb_np2)
    pc2.from_array(twocloud_np)
    visual.ShowColorCloud(pc2, b'cloud')
    time.sleep(0.1)

    # PointXYZ
#    visual.ShowMonochromeCloud(ptcloud_centred, b'cloud')
#    visual.ShowMonochromeCloud(cloud, b'cloud2')
#    visual.ShowColorCloud(pc2, b'cloud')

    v = True
    while v:
        v = not(visual.WasStopped())


if __name__ == "__main__":
    # import cProfile
    # cProfile.run('main()', sort='time')
    main()
