# simple_solar_system.py

from solar_system_3d import SolarSystem, Sun, Planet

solar_system = SolarSystem(400, projection_2d=False)

sun = Sun(solar_system)

planets = (
    Planet(
        solar_system,
        mass=3.3011e23,  # Mass of Mercury in kg
        position=(57.9, 0, 0),  # Semi-major axis of Mercury's orbit in million km
        velocity=(0, 47.87, 0),  # Orbital velocity of Mercury in km/s
    ),
    Planet(
        solar_system,
        mass=4.8675e24,  # Mass of Venus in kg
        position=(108.2, 0, 0),  # Semi-major axis of Venus's orbit in million km
        velocity=(0, 35.02, 0),  # Orbital velocity of Venus in km/s
    ),
    Planet(
        solar_system,
        mass=5.972e24,  # Mass of Earth in kg
        position=(149.6, 0, 0),  # Semi-major axis of Earth's orbit in million km
        velocity=(0, 29.78, 0),  # Orbital velocity of Earth in km/s
    ),
    Planet(
        solar_system,
        mass=6.39e23,  # Mass of Mars in kg
        position=(227.9, 0, 0),  # Semi-major axis of Mars's orbit in million km
        velocity=(0, 24.077, 0),  # Orbital velocity of Mars in km/s
    ),
)

while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()
    solar_system.draw_all()
