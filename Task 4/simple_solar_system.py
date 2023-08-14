# simple_solar_system.py

from solar_system_3d import SolarSystem, Sun, Planet

solar_system = SolarSystem(400, projection_2d=False)

sun = Sun(solar_system)

# Modify the planets tuple to include actual data for the first four planets
planets = (
    Planet(
        solar_system,
        mass=1.989e30,  # Mass of the Sun
        position=(0, 0, 0),
        velocity=(0, 0, 0),
    ),
    Planet(
        solar_system,
        mass=0.33011e24,  # Mass of Mercury
        position=(57.9e6, 0, 0),  # Distance from the Sun in meters
        velocity=(0, 47.87e3, 0),  # Velocity in m/s
    ),
    Planet(
        solar_system,
        mass=4.8675e24,  # Mass of Venus
        position=(108.2e6, 0, 0),
        velocity=(0, 35.02e3, 0),
    ),
    Planet(
        solar_system,
        mass=5.972e24,  # Mass of Earth
        position=(149.6e6, 0, 0),
        velocity=(0, 29.78e3, 0),
    ),
    Planet(
        solar_system,
        mass=0.64171e24,  # Mass of Mars
        position=(227.9e6, 0, 0),
        velocity=(0, 24.077e3, 0),
    ),
)

while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()
    solar_system.draw_all()
