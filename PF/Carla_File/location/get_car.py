# --- File: find_spawn_points.py ---
import carla
import time

def main():
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    
    try:
        # Change this to the map you want to inspect
        map_name = 'Town01'
        world = client.load_world(map_name)
        print(f"Loaded map: {map_name}")

        spawn_points = world.get_map().get_spawn_points()
        
        if not spawn_points:
            print("This map has no recommended spawn points.")
            return

        print(f"Found {len(spawn_points)} recommended spawn points. Drawing them now.")
        print("----------------------------------------------------")
        
        # Print and draw each spawn point
        for i, spawn_point in enumerate(spawn_points):
            # Print the coordinates to the terminal
            print(f"Point #{i}: Location(x={spawn_point.location.x}, y={spawn_point.location.y}, z={spawn_point.location.z})")
            
            # Draw a green debug box at the location
            world.debug.draw_box(
                carla.BoundingBox(spawn_point.location, carla.Vector3D(0.5, 0.5, 2)),
                spawn_point.rotation,
                0.05,
                carla.Color(0, 255, 0, 0),
                10.0  # Life time in seconds
            )
        
        print("----------------------------------------------------")
        print("Boxes will be visible in the CARLA window for 10 seconds.")
        time.sleep(11) # Keep the script alive so we can see the boxes

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Done.")

if __name__ == '__main__':
    main() 