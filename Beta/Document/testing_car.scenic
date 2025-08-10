# # # scenic testing_car.scenic --2d --model scenic.simulators.carla.model --simulate
# # # scenic testing_car.scenic --2d --model scenic.simulators.carla.model --simulate --count x
 
# Setting carla map and model
import random

Town = 'Town05'
P_Town = 'Scenic/assets/maps/CARLA/'+ Town +'.xodr'
param map = localPath(P_Town)
param carla_map = Town
model scenic.simulators.carla.model

# Unknow why it have alot of recommendations
EGO_MODEL = "vehicle.lincoln.mkz_2017"

# Task 1 : 
# ego = new Car
# object_test = new Trash
# object_test2 = new Debris
# Human = new Pedestrian 
# options: 
# sideWalk = Uniform(*network.sidewalks) # neeed more to studies
# Lane = Uniform(*network.lanes) # need more to studies
# below unsure 
# bridge = Uniform(*network.bridges) # need more to studies
# train = Uniform(*network.trains) # need more to studies


# Human = new Pedestrian  on sideWalk
# Car = new Car on Lane.centerline

# Task 2 : adding movement
EGO_SPEED = random.uniform(1,2)
ego = new Car with behavior FollowLaneBehavior(target_speed = 1)


# # try to make the people at the side walk move 🥲 not working
# sideWalk = Uniform(*network.sidewalks) # neeed more to studies
# behavior PedestrianBehavior(min_speed=1, threshold=10):
#  do CrossingBehavior(ego, min_speed, threshold)

# Human = new Pedestrian on sideWalk,
#     with behavior PedestrianBehavior(1, 10)

# Task 3 : adding some rules and requirements'
# EGO_SPEED = random.uniform(1,2)
# BRAKE_ACTION = 1.0
# LEAD_CAR_SPEED =EGO_SPEED
# LEADCAR_BRAKING_THRESHOLD = 1


# leadCar = new Car  on Uniform(*network.lanes).centerline,
#         with behavior FollowLaneBehavior(LEAD_CAR_SPEED)

# ego = new Car  following roadDirection from leadCar for Range(-15, -1),
#     with blueprint EGO_MODEL,
#     with behavior FollowLaneBehavior(EGO_SPEED)

#  more studies on this requirement
# require (distance to leadCar) > 50
# terminate when (distance to leadCar) < 30 

# # Task 4 :
# # Adding and make it a fucntion for easy use and impelementation
# # Car_speed = random.uniform(2, 3) # make it easy to see in simulater
# Car_speed = 2  # Set a constant speed for the main car
# LCar_speed = 2
# behavior mainCar(speed):
#     try:
#         do FollowLaneBehavior(speed)
#     # interrupt when withinDistanceToAnyObjs(self, 12): # number is the distance to the car
#     #     take SetBrakeAction(1.0)
#     interrupt when withinDistanceToRedYellowTrafficLight(self, 15):
#         take SetBrakeAction(1.0)
#     interrupt when withinDistanceToAnyCars(self, 6):
#         take SetBrakeAction(1)

# behavior EgoBehavior(speed):
#     try:
#         do FollowLaneBehavior(speed)

#     interrupt when withinDistanceToRedYellowTrafficLight(self, 15):
#         take SetBrakeAction(1.0)
#     # interrupt when withinstopSigns(self, 1):
#     #     take SetBrakeAction(1.0)

# leadCar = new Car on Uniform(*network.lanes).centerline,
#         with behavior EgoBehavior(LCar_speed)

# ego = new Car following roadDirection from leadCar for Range(-10, 10), # low,high
#     with blueprint EGO_MODEL,
#     with behavior mainCar(Car_speed)

# require (distance to intersection) > 50
# # require (distance to intersection) < 100
# # require (distance to leadCar) < 50
# # require ego.speed > 0.1 and (distance to leadCar) < 10
# # terminate when (distance to leadCar) < 30
terminate when ego.speed < 0








