import numpy as np
import math
import yaml
from icp import icp

def read_lidar_data(filepath):
    """ Reads LiDAR data from a text file. """
    with open(filepath, 'r') as file:
        data=yaml.safe_load(file)

    return data

def convert_to_cartesian(angle_min, angle_increment, ranges):
    """ Converts polar coordinates to Cartesian (x, y, z) coordinates. """
    angles = angle_min + np.arange(len(ranges)) * angle_increment
    xs = ranges * np.cos(angles)
    ys = ranges * np.sin(angles)

    return np.column_stack((xs, ys))

def process_lidar_file(filepath):
    data = read_lidar_data(filepath)
    angle_min = data['angle_min']
    angle_max = data['angle_max']
    ranges = data['ranges']
    angle_increment = data['angle_increment']
    coordinates = convert_to_cartesian(angle_min, angle_increment, ranges)
    return coordinates


file_1 = './scan1.yaml'
file_2 = './scan2.yaml'
lidar_data_1 = process_lidar_file(file_1)
lidar_data_2 = process_lidar_file(file_2)

transformation, aligned_points = icp(lidar_data_1,lidar_data_2)

print("T: ",transformation)
print("Align: ",aligned_points)
