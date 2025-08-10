import xml.etree.ElementTree as ET

input_file = "c:/Users/bluet/Desktop/Project_Final/Carla_File/waypoint/waypoints__Game_Carla_Maps_Town02.xml"
output_file = "c:/Users/bluet/Desktop/Project_Final/Carla_File/Sort_order/waypoints__Game_Carla_Maps_Town02_sorted.xml"

tree = ET.parse(input_file)
root = tree.getroot()

# Find all waypoint elements
waypoints = root.findall(".//waypoint")

# Sort by pitch (float), then by x (float)
sorted_waypoints = sorted(
    waypoints,
    key=lambda wp: (float(wp.attrib.get("pitch", "0")), float(wp.attrib.get("x", "0")))
)

# Remove all waypoints from root
for wp in waypoints:
    root.remove(wp)

# Add sorted waypoints back
for wp in sorted_waypoints:
    root.append(wp)

# Write XML in the desired format (with indentation and newlines)
with open(output_file, "w", encoding="utf-8") as f:
    f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
    f.write("   <route")
    # Write route attributes
    attribs = " ".join([f'{k}="{v}"' for k, v in root.attrib.items()])
    if attribs:
        f.write(f" {attribs}")
    f.write(">\n")
    for elem in root:
        if elem.tag == "waypoint":
            attribs = " ".join([f'{k}="{v}"' for k, v in elem.attrib.items()])
            f.write(f"\t<waypoint {attribs}/>\n")
    f.write("   </route>\n")

print(f"Sorted waypoints saved to {output_file} in the requested format.")