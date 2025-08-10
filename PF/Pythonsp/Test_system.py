import carla
import time
import scenic
import sys
import os  # <- สำหรับ set environment variables
from PCLA.PCLA import PCLA

def setup_environment(agent_name: str, route_path: str):
    """Set environment variables according to agent type."""

    # เคลียร์ environment variables เก่า
    os.environ.pop("STOP_CONTROL", None)
    os.environ.pop("DIRECT", None)
    os.environ.pop("UNCERTAINTY_THRESHOLD", None)
    os.environ.pop("ROUTES", None)

    if agent_name.startswith("tfpp_l6_"):
        os.environ["UNCERTAINTY_THRESHOLD"] = "033"

    elif agent_name.startswith("tfpp_lav_"):
        os.environ["STOP_CONTROL"] = "1"

    elif agent_name.startswith("tfpp_aim_") or agent_name.startswith("tfpp_wp_"):
        os.environ["DIRECT"] = "0"

    elif agent_name == "if_if":
        os.environ["ROUTES"] = route_path  # ให้ path ที่ส่งเข้าไปกับ route

    print("--- Environment variables set for agent:", agent_name, "---")

def main():
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)

    print("--- DEBUG: Loading Scenic scenario... ---")
    scenario = scenic.scenarioFromFile('scenic_scenarios/Case1.scenic')
    scene, _ = scenario.generate()

    print(f"--- DEBUG: Loading map '{scene.params['carla_map']}'... ---")
    world = client.load_world(scene.params['carla_map'])
    time.sleep(2.0)

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
            is_ego = (obj is scene.egoObject)
            print(f"  - Blueprint from Scenic: '{obj.blueprint}'")
            print(f"  - Position (x,y,z): {obj.position}")
            print(f"  - Heading: {obj.heading}")
            print(f"  - Is this the designated ego vehicle? {is_ego}")

            blueprint = world.get_blueprint_library().find(obj.blueprint)
            location = carla.Location(x=obj.position.x, y=obj.position.y + 212, z=obj.position.z)
            rotation = carla.Rotation(yaw=obj.heading)
            transform = carla.Transform(location, rotation)

            print(f"  - Attempting to spawn at: {transform.location}")
            actor = world.try_spawn_actor(blueprint, transform)

            if actor:
                print(f"  - >>> SUCCESS: Spawned actor with ID: {actor.id}")
                spawned_actors.append(actor)
                if is_ego:
                    print("  - >>> EGO VEHICLE IDENTIFIED AND ASSIGNED!")
                    ego_vehicle = actor
            else:
                print("  - >>> FAILURE: Could not spawn actor.")

        print("\n--- DEBUG: Exited spawn loop. ---")
        if ego_vehicle is None:
            raise RuntimeError("Ego vehicle not defined or spawned.")

        world.tick()

        print("--- DEBUG: Moving spectator camera to ego vehicle... ---")
        spectator = world.get_spectator()
        transform = ego_vehicle.get_transform()
        spectator.set_transform(carla.Transform(transform.location + carla.Location(z=30), carla.Rotation(pitch=-45)))

        # --- SETUP AGENT ---
        agent = "tfpp_lav_0"  # ← เปลี่ยนได้ตามที่ต้องการ เช่น tfpp_l6_0, if_if, etc.
        route = "C:/Users/bluet/Desktop/Project_Final/Carla_File/Sort_order/waypoints__Game_Carla_Maps_Town02_sorted.xml"
        setup_environment(agent, route)  # ← ตั้งค่าตัวแปร environment ให้ตรงกับ agent

        print("--- DEBUG: Initializing PCLA agent... ---")
        pcla = PCLA(agent, ego_vehicle, route, client)
        print('Spawned vehicle from Scenic with model =', agent, ', press Ctrl+C to exit.\n')

        while True:
            ego_action = pcla.get_action()
            print(f"Applying action: Throttle={ego_action.throttle}, Steer={ego_action.steer}, Brake={ego_action.brake}")
            ego_vehicle.apply_control(ego_action)

            velocity = ego_vehicle.get_velocity()
            speed = (velocity.x ** 2 + velocity.y ** 2 + velocity.z ** 2) ** 0.5
            location = ego_vehicle.get_location()
            print(f"Ego Location: x={location.x:.2f}, y={location.y:.2f}, z={location.z:.2f} | Speed: {speed:.2f} m/s")

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

if __name__ == '__main__':
    print("--- Script starting. Checking CARLA connection... ---")
    try:
        main()
    except KeyboardInterrupt:
        print('Script interrupted by user.')
    except Exception as e:
        print("\n\n--- AN ERROR OCCURRED! ---")
        import traceback
        traceback.print_exc()
        print(f"ERROR DETAILS: {e}")
        print("--------------------------\n")
    finally:
        print('Done.')
