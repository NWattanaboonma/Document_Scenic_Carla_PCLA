# # # scenic testing.scenic --2d --model scenic.simulators.carla.model --simulate
# # # scenic testing.scenic --2d --model scenic.simulators.carla.model --simulate --count x

# Setting carla map and model
import random

Town = 'Town02'
P_Town = 'Scenic/assets/maps/CARLA/'+ Town +'.xodr'
param map = localPath(P_Town)
param carla_map = Town
param weather = 'ClearSunset'  # ClearNoon, WetNoon, SoftRainNoon, HardRainNoon, ClearSunset, SoftRainSunset, HardRainSunset
model scenic.simulators.carla.model

# Unknow why it have alot of recommendations
EGO_MODEL = "vehicle.lincoln.mkz_2017"
EGO_SPEED = 1  # Speed for the ego vehicle


# create the ego car and the function main car EGO_behavior
# other car in front of the ego car
behavior EgoBehavior(speed):
    try:
        do FollowLaneBehavior(speed,laneToFollow=network.laneAt(self),is_oppositeTraffic=False)
    interrupt when withinDistanceToAnyCars(self, 12):
        take SetBrakeAction(1.0)
# Other_Car = new Car at (366.35, 1.99, 0.04)
# Other_Car = new Car at (366.35, 1.99, 0.04),
#     with blueprint EGO_MODEL,
#     # with heading 180 deg relative to roadDirection,
#     with  behavior FollowLaneBehavior(0.2, laneToFollow=None, is_oppositeTraffic=False)

ego = new Car on Uniform(*network.lanes),
    with blueprint EGO_MODEL,
    with behavior EgoBehavior(EGO_SPEED)


