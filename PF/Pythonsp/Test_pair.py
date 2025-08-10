# --- File: Test_pair.py (Modified for Debugging) ---
import carla
import time
import scenic
import sys # Import sys to get more error info

from PCLA.PCLA import PCLA

# The main function remains the same as the one we built
def main():
    # ... (Your main function code from the previous step goes here)
    # Make sure it's the full function with the Scenic integration.
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)

    print("--- DEBUG: Loading Scenic scenario... ---")
    scenario = scenic.scenarioFromFile('scenic_scenarios/Case1.scenic')
    # ... after the scenario has been generated
    scene, _ = scenario.generate()

    print(f"--- DEBUG: Loading map '{scene.params['carla_map']}'... ---")
    world = client.load_world(scene.params['carla_map'])
    # --- NEW: Give CARLA a moment to load the map fully ---
    print("--- DEBUG: Map loaded. Pausing for 2 seconds to ensure navmesh is ready... ---")
    time.sleep(2.0)
    # --------------------------------------------------------
    
    synchronous_master = False
    try:
        print("--- DEBUG: Setting up synchronous mode... ---")
        traffic_manager = client.get_trafficmanager(8000)
        settings = world.get_settings()
        if not settings.synchronous_mode:
            synchronous_master = True
            settings.synchronous_mode = True
            settings.fixed_delta_seconds = 0.05
        world.apply_settings(settings)

        print("--- DEBUG: Spawning actors from Scenic scene... ---")
        ego_vehicle = None
        spawned_actors = []

        print("--- DEBUG: Entering detailed spawn loop... ---")
        for i, obj in enumerate(scene.objects):
            print(f"\n[Object #{i}]")
            
            # 1. Print details from Scenic
            is_ego = (obj is scene.egoObject)
            print(f"  - Blueprint from Scenic: '{obj.blueprint}'")
            print(f"  - Position (x,y,z): {obj.position}")
            print(f"  - Heading: {obj.heading}")
            print(f"  - Is this the designated ego vehicle? {is_ego}")

            # 2. Create CARLA transform
            blueprint = world.get_blueprint_library().find(obj.blueprint)
            print(obj.position.x, obj.position.y, obj.position.z)
            location = carla.Location(x=obj.position.x  , y=obj.position.y +212, z=obj.position.z )
            rotation = carla.Rotation(yaw=obj.heading)
            transform = carla.Transform(location, rotation)
            
            # 3. Attempt to spawn
            print(f"  - Attempting to spawn at: {transform.location}")
            actor = world.try_spawn_actor(blueprint, transform)

            # 4. Report the result
            if actor:
                print(f"  - >>> SUCCESS: Spawned actor with ID: {actor.id}")
                spawned_actors.append(actor)
                if is_ego:
                    print("  - >>> EGO VEHICLE IDENTIFIED AND ASSIGNED!")
                    ego_vehicle = actor
            else:
                print("  - >>> FAILURE: Could not spawn actor. Check for collisions or invalid spawn points.")
        print("\n--- DEBUG: Exited spawn loop. ---")
        # --- End of Ultimate Debugging Loop ---

        if ego_vehicle is None:
            raise RuntimeError("Ego vehicle not defined or spawned.")
        
        world.tick()

    # --- NEW: Move camera to the car ---
        print("--- DEBUG: Moving spectator camera to ego vehicle... ---")
        spectator = world.get_spectator()
        transform = ego_vehicle.get_transform()
        spectator.set_transform(carla.Transform(transform.location + carla.Location(z=30), carla.Rotation(pitch=-45)))
        # -----------------------------------

        print("--- DEBUG: Initializing PCLA agent... ---")
        agent = "tfpp_l6_0"
        # tfpp_lav
        # tfpp_l6
        route = "C:/Users/bluet/Desktop/Project_Final/PCLA/sampleRoute.xml"
        pcla = PCLA(agent, ego_vehicle, route, client)
        print('Spawned vehicle from Scenic with model =', agent,', press Ctrl+C to exit.\n')
        
        while True:
            ego_action = pcla.get_action()
            print(f"Applying action: Throttle={ego_action.throttle}, Steer={ego_action.steer}, Brake={ego_action.brake}")
            ego_vehicle.apply_control(ego_action)
            
            # --- Print ego vehicle information ---
            velocity = ego_vehicle.get_velocity()
            speed = (velocity.x**2 + velocity.y**2 + velocity.z**2) ** 0.5  # m/s
            location = ego_vehicle.get_location()
            print(f"Ego Location: x={location.x:.2f}, y={location.y:.2f}, z={location.z:.2f} | Speed: {speed:.2f} m/s")
            # -------------------------------------
            
            world.tick()

    finally:
        if 'settings' in locals() and 'world' in locals():
            settings.synchronous_mode = False
            world.apply_settings(settings)
        print('\nCleaning up the actors')
        if 'client' in locals() and 'spawned_actors' in locals():
            client.apply_batch([carla.command.DestroyActor(actor) for actor in spawned_actors])
        if 'pcla' in locals():
            pcla.cleanup()
        time.sleep(0.5)


# --- IMPORTANT MODIFICATION FOR DEBUGGING ---
if __name__ == '__main__':
    # First, make sure the CARLA server is running!
    print("--- Script starting. Checking CARLA connection... ---")
    
    try:
        main()
    except KeyboardInterrupt:
        print('Script interrupted by user.')
    except Exception as e:
        # This is the crucial part: it will catch any error
        # that is not a KeyboardInterrupt and print it.
        print("\n\n--- AN ERROR OCCURRED! ---")
        import traceback
        traceback.print_exc()
        print(f"ERROR DETAILS: {e}")
        print("--------------------------\n")
    finally:
        print('Done.')