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
# Scenic position: Vector(188.87063752752394, -201.67712146057596, 0) -> CARLA position: Location(x=188.870636, y=201.677124, z=0.000000)
spawn_point = carla.Transform(carla.Location(x=5.090000, y=105.500000, z=1.0))

# Spawn the car
vehicle = world.spawn_actor(car_blueprint, spawn_point)
print('Vehicle spawned:', vehicle)

# Print the spawn location
loc = vehicle.get_location()
print(f"Spawned at location: x={loc.x:.2f}, y={loc.y:.2f}, z={loc.z:.2f}")