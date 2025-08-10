# scenic color.scenic --2d --model scenic.simulators.carla.model --simulate
import random

Town = 'Town02'
P_Town = 'C:/Users/bluet/Desktop/Project_Final/Scenic/assets/maps/CARLA/' + Town + '.xodr'
param map = localPath(P_Town)
param carla_map = Town
param use2DMap = True
param weather = 'ClearSunset'  # ClearNoon, WetNoon, SoftRainNoon, HardRainNoon, ClearSunset, SoftRainSunset, HardRainSunset

model scenic.simulators.carla.model

MODEL = "vehicle.lincoln.mkz_2017"



ego = new Car on Uniform(*network.lanes),
    with blueprint MODEL