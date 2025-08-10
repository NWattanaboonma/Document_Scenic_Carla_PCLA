# scenic Case1.scenic --2d --model scenic.simulators.carla.model --simulate
Town = 'Town02'
P_Town = 'Scenic/assets/maps/CARLA/'+ Town +'.xodr'
param map = localPath(P_Town)
param carla_map = Town
# weather = set from Carla doc
param weather = 'ClearSunset'  # ClearNoon, WetNoon, SoftRainNoon, HardRainNoon, ClearSunset, SoftRainSunset, HardRainSunset
model scenic.simulators.carla.model

#All the Distance are in meters
# All speeds are in meters per second (m/s)

MODEL = "vehicle.lincoln.mkz_2017"
EGO_SPEED = 1

ego = new Car  at (11.64,-105.53,0.25),
    with blueprint MODEL,
    with behavior FollowLaneBehavior(EGO_SPEED)