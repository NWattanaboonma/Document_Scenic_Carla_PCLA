# # # scenic testing_car.scenic --2d --model scenic.simulators.carla.model --simulate

# import random
# param map = localPath('Scenic/assets/maps/CARLA/Town05.xodr')  # or other CARLA map that definitely works
# param carla_map = 'Town05'
# model scenic.simulators.carla.model

# # EGO_MODEL = "vehicle.lincoln.mkz_2017"
# # num = random.uniform(5, 15)
# # print("EGO_SPEED = %f" % num)  # Print the random speed for debugging purposes
# # EGO_SPEED = num  # Random speed for the ego vehicle


# # behavior EgoBehavior(speed):
# #     try:
# #         do FollowLaneBehavior(speed)
# #     interrupt when withinDistanceToObjsInLane(self, 15):
# #         take SetBrakeAction(1.0)
# #     interrupt when withinDistanceToRedYellowTrafficLight(self, 15):
# #         take SetBrakeAction(1.0)
        

# # # PEDESTRIAN BEHAVIOR: cross the street
# # behavior PedestrianBehavior(min_speed=1, threshold=10):
# #     do CrossingBehavior(ego, min_speed, threshold)


# # # Background activity
# # background_vehicles = []
# # for _ in range(25):
# #     lane = Uniform(*network.lanes)
# #     spot = new OrientedPoint on lane.centerline

# #     background_car = new Car at spot,
# #         with behavior AutopilotBehavior()
# #     background_vehicles.append(background_car)

# # background_walkers = []
# # for _ in range(10):
# #     sideWalk = Uniform(*network.sidewalks)
# #     background_walker = new Pedestrian in sideWalk,
# #         with behavior PedestrianBehavior()
# #     background_walkers.append(background_walker)


# # ego = new Car following roadDirection from spot for Range(-30, -20),
# #     with blueprint EGO_MODEL,
# #     with behavior EgoBehavior(EGO_SPEED)

# # import random

# # param map = localPath('Scenic/assets/maps/CARLA/Town01.xodr')
# # param carla_map = 'Town01'

# # model scenic.simulators.carla.model

# # EGO_MODEL = "vehicle.lincoln.mkz_2017"
# # EGO_SPEED = random.uniform(5, 15)  # Random speed for ego vehicle

# # # This parameter decides if the ego will 'break the rules' this simulation:
# # ego_break_rules = random.choice([True, False])  # 50% chance

# # behavior EgoBehavior(speed, break_rules):
# #     try:
# #         do FollowLaneBehavior(speed)
# #     interrupt when withinDistanceToObjsInLane(self, 40):
# #         if break_rules:
# #             # Do NOT brake; keep going (increase chance of collision)
# #             pass
# #         else:
# #             take SetBrakeAction(1.0)
# #     interrupt when withinDistanceToRedYellowTrafficLight(self, 15):
# #         if break_rules:
# #             # Ignore red/yellow light; keep going (run red light possibility)
# #             pass
# #         else:
# #             take SetBrakeAction(1.0)

# # behavior PedestrianBehavior(min_speed=1, threshold=10):
# #     do CrossingBehavior(ego, min_speed, threshold)

# # # Spawn 25 autopilot background vehicles
# # background_vehicles = []
# # for _ in range(25):
# #     lane = Uniform(*network.lanes)
# #     spot = new OrientedPoint on lane.centerline
# #     background_car = new Car at spot, with behavior AutopilotBehavior()
# #     background_vehicles.append(background_car)

# # # Spawn 10 background walkers crossing
# # background_walkers = []
# # for _ in range(10):
# #     sideWalk = Uniform(*network.sidewalks)
# #     background_walker = new Pedestrian in sideWalk, with behavior PedestrianBehavior()
# #     background_walkers.append(background_walker)

# # # Ego vehicle placed randomly, may break rules in this simulation
# # ego = new Car following roadDirection from spot for Range(-30, -20),
# #     with blueprint EGO_MODEL,
# #     with behavior EgoBehavior(EGO_SPEED, ego_break_rules)

# import random

# param map = localPath('Scenic/assets/maps/CARLA/Town01.xodr')
# param carla_map = 'Town01'
# model scenic.simulators.carla.model
# # EGO_MODEL = "vehicle.lincoln.mkz_2017"
# EGO_SPEED = 2  # Random speed for ego vehicle


# # ego = new Car on Uniform(*network.lanes).centerline,
# #     with blueprint "vehicle.lincoln.mkz_2017",
# #     with behavior FollowLaneBehavior(EGO_SPEED)


# param map = localPath('Scenic/assets/maps/CARLA/Town01.xodr')
# param carla_map = 'Town01'
# model scenic.simulators.carla.model

# ## CONSTANTS
# EGO_MODEL = "vehicle.lincoln.mkz_2017"
# EGO_SPEED = 1
# EGO_BRAKING_THRESHOLD = 12

# LEAD_CAR_SPEED = 1
# LEADCAR_BRAKING_THRESHOLD = 1

# BRAKE_ACTION = 1.0

# behavior EgoBehavior(speed=1):
#     # try:
#         do FollowLaneBehavior(speed)

#     # interrupt when withinDistanceToAnyCars(self, EGO_BRAKING_THRESHOLD):
#     #     take SetBrakeAction(BRAKE_ACTION)

# behavior LeadingCarBehavior(speed=1):
#     try:  
#         do FollowLaneBehavior(speed)

#     interrupt when withinDistanceToAnyObjs(self, LEADCAR_BRAKING_THRESHOLD):
#         take SetBrakeAction(BRAKE_ACTION)

# lane = Uniform(*network.lanes)

# obstacle = new Trash on lane.centerline

# leadCar = new Car following roadDirection from obstacle for Range(-50, -30),
#         with behavior LeadingCarBehavior(LEAD_CAR_SPEED)

# ego = new Car following roadDirection from leadCar for Range(-15, -1),
#         with blueprint EGO_MODEL,
#         with behavior EgoBehavior(EGO_SPEED)

# require (distance to intersection) > 80
# terminate when ego.speed < 0.1 and (distance to obstacle) < 30

# EGO_SPEED = 10

# # ego = new Car at (-229.40, -28.55, 10.00)

# # ego = new Car with behavior FollowLaneBehavior(EGO_SPEED, laneToFollow=None, is_oppositeTraffic=False) # what is the lane to follow ? it setting defult to None Ans the lane that this vehicle (agent) is currently on in the road network.
# intersec = Uniform(*network.intersections)
# startLane = Uniform(*intersec.incomingLanes)
# maneuver = Uniform(*startLane.maneuvers)
# spot = new OrientedPoint in maneuver.startLane.centerline
# print("Spot: "+str(spot))
# ego = new Car at spot,
#     with blueprint EGO_MODEL,
#     with behavior FollowLaneBehavior(EGO_SPEED, laneToFollow=None, is_oppositeTraffic=False)
# # terminate when ego.speed < 0.1

# to complex : # # # scenic testing.scenic --2d --model scenic.simulators.carla.model --simulate
# # # # scenic testing.scenic --2d --model scenic.simulators.carla.model --simulate --count x

# # Setting carla map and model
# import random

# Town = 'Town01'
# P_Town = 'Scenic/assets/maps/CARLA/'+ Town +'.xodr'
# param map = localPath(P_Town)
# param carla_map = Town
# model scenic.simulators.carla.model

# # Unknow why it have alot of recommendations
# EGO_MODEL = "vehicle.lincoln.mkz_2017"
# EGO_SPEED = 2  # Speed for the ego vehicle
# Function main car EGO_behavior
# behavior EgoBehavior(speed):
    # try:
        # do FollowLaneBehavior(speed,laneToFollow=network.laneAt(self),is_oppositeTraffic=False)
    # interrupt when withinDistanceToObjsInLane(self, 15):
    #     take SetBrakeAction(1.0)
    # interrupt when withinDistanceToRedYellowTrafficLight(self, 15):
    #     take SetBrakeAction(1.0) 

# The side car that in the other line:

# The Infront of the car : 
#Find lanes that have a lane to their left in the opposite direction
# laneSecsWithLeftLane = []
# for lane in network.lanes:
#     for laneSec in lane.sections:
#         if laneSec._laneToLeft is not None:
#             if laneSec._laneToLeft.isForward is not laneSec.isForward:
#                 laneSecsWithLeftLane.append(laneSec)

# assert len(laneSecsWithLeftLane) > 0, \
#     'No lane sections with adjacent left lane with opposing \
#     traffic direction in network.'

# initLaneSec = Uniform(*laneSecsWithLeftLane)
# leftLaneSec = initLaneSec._laneToLeft

# spot = new OrientedPoint on initLaneSec.centerline
# oncomingCar = new Car on leftLaneSec.centerline
# print("oncomingCar: " + str(leftLaneSec.centerline))

# spot = new OrientedPoint in network.lanes[0].centerline
# print("spot: " + str(spot))
# spot1 = new OrientedPoint in network.lanes[1].centerline
# print("spot1: " + str(spot1))
# othercar = new Car following roadDirection from spot for Range(-30, -20)
# ego = new Car following roadDirection from spot for Range(-30, -20),
#     with blueprint EGO_MODEL,
    # with behavior EgoBehavior(EGO_SPEED)

# terminate when ego.speed <0.1


import carla
# import time
# from PCLA import PCLA # Assuming PCLA is in a file named PCLA.py in the same directory

# def main():
#     client = None
#     world = None
#     vehicle = None
#     pcla = None # Initialize pcla to None
#     synchronous_master = False

#     try:
#         client = carla.Client('localhost', 2000)
#         client.set_timeout(10.0)

#         # Load world and set up synchronous mode
#         client.load_world("Town02")
#         world = client.get_world()
#         traffic_manager = client.get_trafficmanager(8000)

#         settings = world.get_settings()
#         asynch = False

#         if not asynch:
#             traffic_manager.set_synchronous_mode(True)
#             if not settings.synchronous_mode:
#                 synchronous_master = True
#                 settings.synchronous_mode = True
#                 settings.fixed_delta_seconds = 0.05
#             # else: # This 'else' block is not strictly necessary but was in your original code
#             #     synchronous_master = False
#         else:
#             print("You are currently in asynchronous mode. If this is a traffic simulation, \
#                     you could experience some issues. If it's not working correctly, switch to \
#                     synchronous mode by using traffic_manager.set_synchronous_mode(True)")
        
#         world.apply_settings(settings)

#         # Finding actors
#         bpLibrary = world.get_blueprint_library()

#         ## Finding vehicle
#         vehicleBP = bpLibrary.filter('model3')[0]
#         vehicle_spawn_points = world.get_map().get_spawn_points()

#         ### Spawn vehicle
#         vehicle = world.spawn_actor(vehicleBP, vehicle_spawn_points[31])

#         # Retrieve the spectator object
#         spectator = world.get_spectator()
#         # Set the spectator with our transform
#         spectator.set_transform(carla.Transform(carla.Location(x=-8, y=108, z=7), carla.Rotation(pitch=-19, yaw=0, roll=0)))

#         world.tick()

#         agent = "neat_neat"
#         route = "./sampleRoute.xml"

#         # This is where the PCLA object is created.
#         # If PCLA fails here, 'pcla' will remain None.
#         pcla = PCLA(agent, vehicle, route, client)

#         print('Spawned the vehicle with model =', agent,', press Ctrl+C to exit.\n')

#         while True:
#             # Check if pcla was successfully initialized before calling its methods
#             if pcla:
#                 ego_action = pcla.get_action()
#                 vehicle.apply_control(ego_action)
#             world.tick()

#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         # Reset to asynchronous mode if it was changed
#         if synchronous_master and world: # Check if world is not None
#             print("Resetting to asynchronous mode.")
#             settings = world.get_settings()
#             settings.synchronous_mode = False
#             world.apply_settings(settings)
        
#         # Clean up the PCLA object and vehicle if they were created
#         if pcla: # Only call cleanup if pcla was successfully instantiated
#             print('\nCleaning up the PCLA object')
#             pcla.cleanup()
        
#         if vehicle: # Only destroy vehicle if it was spawned
#             print('Destroying vehicle')
#             vehicle.destroy()
        
#         time.sleep(0.5) # Give a short delay for cleanup to complete

# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         print("\nSimulation interrupted by user.")
#     finally:
#         print('Done.')