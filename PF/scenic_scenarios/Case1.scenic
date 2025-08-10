import random

Town = 'Town02'
P_Town = 'C:/Users/bluet/Desktop/Project_Final/Scenic/assets/maps/CARLA/' + Town + '.xodr'
param map = localPath(P_Town)
param carla_map = Town
param use2DMap = True
param weather = 'ClearSunset'  # ClearNoon, WetNoon, SoftRainNoon, HardRainNoon, ClearSunset, SoftRainSunset, HardRainSunset

from scenic.simulators.carla.behaviors import AIAgentBehavior
model scenic.simulators.carla.model

MODEL = "vehicle.lincoln.mkz_2017"
EGO_SPEED = 10
NPC_SPEED = 0.5
bre_ak = Range(0.1, 1.0)
agents = "tfpp_lav_0"
route = "C:/Users/bluet/Desktop/Project_Final/Carla_File/Sort_order/waypoints__Game_Carla_Maps_Town02_sorted.xml"

ego = new Car at (5.09,-105.50,1),
    with blueprint MODEL,
    with behavior AIAgentBehavior(agents,route)
# switch to the following line if you want to use the FollowLaneBehavior for the ego vehicle
    # with behavior FollowLaneBehavior(EGO_SPEED)
        # with behavior AIAgentBehavior(agents,route)

# leader_Car = new Car following roadDirection from ego for Range(-50, -10),
#     with blueprint MODEL,
#     with targetSpeed NPC_SPEED,
#     with behavior FollowLaneBehavior(NPC_SPEED)




