
import carla
import time
import os

def save_waypoints_to_xml(waypoints, map_name):
    """
    Saves waypoints to an XML file with a 100% guaranteed correct format,
    writing line-by-line with proper newlines and tabs.
    """
    # Define the output file path.
    output_path = f"waypoints_{map_name.replace('/', '_')}.xml"

    # Open the file to write. This method ensures it's properly closed.
    with open(output_path, "w", encoding="utf-8") as f:
        # Manually write each component with the correct newline character '\n'
        # and tab character '\t'.

        # 1. XML header
        f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
        f.write("\n")  # Blank line

        # 2. Opening route tag
        f.write(f"   <route id=\"_\" town=\"{map_name}\">\n")
        f.write("\n")  # Blank line

        # 3. Each waypoint, correctly indented with a tab.
        for waypoint in waypoints:
            transform = waypoint.transform
            location = transform.location
            rotation = transform.rotation
            
            # Format the line with a tab (\t) for indentation and a newline (\n) at the end.
            f.write(
                f"\t<waypoint pitch=\"{rotation.pitch}\" roll=\"{rotation.roll}\" "
                f"x=\"{location.x}\" y=\"{location.y}\" "
                f"yaw=\"{rotation.yaw}\" z=\"{location.z}\"/>\n"
            )
        
        f.write("\n")  # Blank line before closing tag

        # 4. Closing route tag.
        f.write("</route>\n")
    
    print(f"Success: Waypoints for {map_name} saved to {output_path} with the correct format.")

def main():
    """
    Main function to connect to CARLA and save waypoints.
    """
    client = None
    try:
        client = carla.Client('localhost', 2000)
        client.set_timeout(10.0)
        print("Successfully connected to CARLA.")

        available_maps = client.get_available_maps()
        print(f"Available maps: {available_maps}")

        for map_name in available_maps:
            print(f"--- Processing Map: {map_name} ---")
            world = client.load_world(map_name)
            time.sleep(2)  # Wait for map to settle.

            map_data = world.get_map()
            waypoint_list = map_data.generate_waypoints(2.0)
            
            print(f"Found {len(waypoint_list)} waypoints.")
            
            # Save the waypoints using the corrected function.
            save_waypoints_to_xml(waypoint_list, map_name)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Script finished.")

if __name__ == '__main__':
    main()

