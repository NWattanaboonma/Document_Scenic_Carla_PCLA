
import carla
import time
import random

def main():
    """
    Connects to the CARLA simulator, spawns a vehicle, and continuously
    prints its coordinates to the console.
    """
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    vehicle = None  # Initialize vehicle to None

    try:
        world = client.get_world()
        blueprint_library = world.get_blueprint_library()

        # 1. Get a vehicle blueprint (e.g., a Ford Mustang)
        vehicle_bp = random.choice(blueprint_library.filter('vehicle.ford.mustang'))

        # 2. Find a safe, random spawn point provided by the map
        transform = random.choice(world.get_map().get_spawn_points())

        # 3. Spawn the vehicle in the simulator
        vehicle = world.spawn_actor(vehicle_bp, transform)
        print(f"Vehicle spawned! You can now drive it in the simulator window.")
        print("Move the car to your desired starting location and note the coordinates from this console.")

        # 4. Move the spectator camera to follow the vehicle from above
        spectator = world.get_spectator()
        
        # Continuously update the spectator and print location
        while True:
            # Get the vehicle's current transform (location and rotation)
            vehicle_transform = vehicle.get_transform()
            location = vehicle_transform.location
            
            # Update spectator to follow the car smoothly
            spectator_transform = carla.Transform(location + carla.Location(z=30),
                                                  carla.Rotation(pitch=-90))
            spectator.set_transform(spectator_transform)

            # 5. Print the coordinates to the console
            # These are the values you will copy into your Scenic file.
            print(f"Current Location -> X: {location.x:.2f}, Y: {location.y:.2f}, Z: {location.z:.2f}")
            
            # Wait for 1 second before printing the next location
            time.sleep(1)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # 6. Clean up: destroy the vehicle actor when the script is stopped (e.g., with Ctrl+C)
        if vehicle is not None and vehicle.is_alive:
            vehicle.destroy()
            print("\nVehicle has been destroyed. Script finished.")

if __name__ == '__main__':
    main()

