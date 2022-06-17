from trafficSimulator import *

# Create simulation
sim = Simulation()

# Curve resolution
n = 15

# Add multiple roads
sim.create_roads([
    ((-360, 114), (840, 114)),
    ((-360, 110), (840, 110)),
    ((-360, 106), (840, 106)),
    ((-360, 102), (840, 102)),
    ((840, 98), (-360, 98)),
    ((840, 94), (-360, 94)),
    ((840, 90), (-360, 90)),
    ((840, 86), (-360, 86)),
])

sim.create_gen({
    'vehicle_rate': 17,
    'vehicles': [
        [1, {"path": [0]}]
    ]
})

sim.create_gen({
    'vehicle_rate': 17,
    'vehicles': [
        [1, {"path": [1]}]
    ]
})

sim.create_gen({
    'vehicle_rate': 17,
    'vehicles': [
        [1, {"path": [2]}]
    ]
})

sim.create_gen({
    'vehicle_rate': 17,
    'vehicles': [
        [1, {"path": [3]}]
    ]
})

sim.create_gen({
    'vehicle_rate': 17,
    'vehicles': [
        [1, {"path": [4]}]
    ]
})


sim.create_gen({
    'vehicle_rate': 17,
    'vehicles': [
        [1, {"path": [5]}]
    ]
})

sim.create_gen({
    'vehicle_rate': 18,
    'vehicles': [
        [1, {"path": [6]}]
    ]
})

sim.create_gen({
    'vehicle_rate': 4,
    'vehicles': [
        [1, {"path": [7]}]
    ]
})

# Start simulation
win = Window(sim)
win.offset = (-150, -110)
# win.zoom = 1
win.run(steps_per_update=5)