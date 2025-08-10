# scenic Case1.scenic --2d --model scenic.simulators.carla.model --simulate
Town = 'Town01'
P_Town = 'Scenic/assets/maps/CARLA/'+ Town +'.xodr'
param map = localPath(P_Town)
param carla_map = Town
# weather = set from Carla doc
param weather = 'ClearSunset'  # ClearNoon, WetNoon, SoftRainNoon, HardRainNoon, ClearSunset, SoftRainSunset, HardRainSunset
model scenic.simulators.carla.model

#All the Distance are in meters
# All speeds are in meters per second (m/s)

MODEL = "vehicle.lincoln.mkz_2017"
# EGO_SPEED = Range(2,5)
# NPC_SPEED = 10
EGO_SPEED = 5
NPC_SPEED = Range(1,2)
bre_ak = Range(0.1,1.0)
# bre_ak = 1
start_distance = int(Range(10, 50))
# Function

behavior Main_Car(Speed):
    try:
        # Follow the lane with the given speed
        do FollowLaneBehavior(Speed, laneToFollow=None, is_oppositeTraffic=False)

    interrupt when withinDistanceToAnyCars(self, 10):
        # Stop the car completely when close to NPC
        
        # bre_ak = 0.1
        (print("Break: ", bre_ak))
        take SetBrakeAction(bre_ak)

behavior NPC_Car(Speed):
    try:
        # Follow the lane with the given speed
        do FollowLaneBehavior(Speed)
    interrupt when withinDistanceToRedYellowTrafficLight(self, Range(15, 30)):
        # Stop the car when close to a red or yellow traffic light
        take SetBrakeAction(1.0)

npc_car = new Car at (191.47, 2.04, 0.03),
    with blueprint MODEL,
    with behavior NPC_Car(NPC_SPEED)
    # with blueprint MODEL
    


ego = new Car following roadDirection from npc_car  for -(start_distance),
    with blueprint MODEL,
    with behavior Main_Car(EGO_SPEED)
    # with behavior FollowLaneBehavior(EGO_SPEED)


print(distance to npc_car)
print("Ego car speed: ", EGO_SPEED)
print("NPC car speed: ", NPC_SPEED)

terminate when (distance to npc_car) < 4.9 and ego.speed < 0.1



#Future make all the number more reasonable
#Can Detect the Sign 
#make the car more smart all in the line 
#Find more reserch about the Car the Safe distance
#Report:
 #https://www.mdpi.com/1424-8220/22/18/7051








