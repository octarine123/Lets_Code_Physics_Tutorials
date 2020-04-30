#!/usr/bin/env python3
#Projectile_motion_1.py
# Author: octarine123

from vpython import *
import math

projectile = sphere(pos = vector(-5,0,0), radius = 0.1, color = color.red, make_trail = True)

projectile.speed = 10 # Initial speed.
projectile.angle = 45*(math.pi/180) # Initial angle, from the +x-axis.

projectile.velocity = vector(projectile.speed*cos(projectile.angle),
                             projectile.speed*sin(projectile.angle),
                             0)

projectile.mass = 1.0
grav_field = 9.81       #m/s2

dt = 0.01
time = 0

while (projectile.pos.y >=0):
    rate(100)

    # Calculate the force.
    grav_force = vector(0,-projectile.mass*grav_field,0)

    force = grav_force
    
    # Update velocity.
    projectile.velocity = projectile.velocity + force/projectile.mass * dt

    # Update position.
    projectile.pos = projectile.pos + projectile.velocity * dt

    # Update time.
    time = time + dt
    print(time,' - ', projectile.pos)

