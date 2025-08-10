import carla
import random

# Connect to the CARLA simulator
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)
# client.load_world("Town02")
# Get world object
world = client.get_world()


# Access the blueprint library (contains all vehicles)
blueprint_library = world.get_blueprint_library()
# Filter for vehicle blueprints
car_blueprint = random.choice(blueprint_library.filter('vehicle.*'))
print(car_blueprint)
# Choose a random spawn point from world map
print(world)
spawn_points = world.get_map().get_spawn_points()
spawn_point = random.choice(spawn_points)

# Spawn the car
vehicle = world.spawn_actor(car_blueprint, spawn_point)
print('Vehicle spawned:', vehicle)

# vehicle.destroy()