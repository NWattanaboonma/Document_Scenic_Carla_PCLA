
import glob
import os
import sys
import carla
import random
import time
import math

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

def main():
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)

    try:
        world = client.get_world()
        original_settings = world.get_settings()

        # Set up synchronous mode
        settings = world.get_settings()
        settings.synchronous_mode = True
        settings.fixed_delta_seconds = 0.05
        world.apply_settings(settings)

        blueprint_library = world.get_blueprint_library()

        # Spawn point
        spawn_point = random.choice(world.get_map().get_spawn_points())

        # Choose a vehicle blueprint
        vehicle_bp = random.choice(blueprint_library.filter('vehicle.tesla.model3'))

        # Spawn the vehicle
        vehicle = world.spawn_actor(vehicle_bp, spawn_point)
        vehicle.set_autopilot(True)
        print(f'Spawned vehicle at {spawn_point.location}')

        spectator = world.get_spectator()
        camera_bp = blueprint_library.find('sensor.camera.rgb')
        camera_bp.set_attribute('image_size_x', '1280')
        camera_bp.set_attribute('image_size_y', '720')
        camera_bp.set_attribute('fov', '110')
        camera_transform = carla.Transform(carla.Location(x=-5.5, z=2.8), carla.Rotation(pitch=-15))
        camera = world.spawn_actor(camera_bp, camera_transform, attach_to=vehicle, attachment_type=carla.AttachmentType.SpringArm)

        # Control loop
        start_time = time.time()
        duration = 30  # seconds

        while time.time() - start_time < duration:
            world.tick()

            # Simple steering control (sine wave)
            elapsed_time = time.time() - start_time
            steering_angle = 0.5 * math.sin(elapsed_time * 2)  # Adjust 0.5 for magnitude, 2 for frequency

            # Apply a control command
            control = vehicle.get_control()
            control.steer = steering_angle
            vehicle.apply_control(control)

            # Update spectator view
            vehicle_transform = vehicle.get_transform()
            spectator.set_transform(carla.Transform(
                vehicle_transform.location + carla.Location(x=-10, z=5),
                carla.Rotation(pitch=-20, yaw=vehicle_transform.rotation.yaw)
            ))

            time.sleep(0.01) # Small delay to make sure the spectator updates smoothly

    finally:
        # Restore original settings
        world.apply_settings(original_settings)
        if vehicle is not None:
            vehicle.destroy()
        if camera is not None:
            camera.destroy()
        print('Cleaned up actors and restored settings.')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nExited by user.')

