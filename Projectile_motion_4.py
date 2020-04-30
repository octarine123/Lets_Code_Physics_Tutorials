#!/usr/bin/env python3
#Projectile_motion_3.py
# Author: octarine123


from vpython import *
import math
## display(width = 1300, height = 1000)

scene.width = 1300
scene.height = 1000
scene.autoscale = False

## Projectile info here

## Loop over initial angle (in deg)
angle = 5
delta_angle = 5
max_angle = 90

while angle <= max_angle:
    
    projectile = sphere(pos = vector(-5,0,0),
                        radius = 0.1,
                        color = color.red,
                        make_trail = True)


    ## Dray display
    global drag, lastpos
    drag = False
    def down():
        global drag, lastpos
        scene.center = scene.mouse.pos
        drag = True
        lastpos = vector(scene.mouse.pos.x, scene.mouse.pos.y, 0)

    def up():
        global drag
        drag = False

    scene.bind('mousedown', down)

    scene.bind('mouseup', up)

    projectile.speed = 10.0 # Initial speed.
    theta = 60 
    projectile.angle = angle*(math.pi/180) # Initial angle, from the +x-axis. Radians

    projectile.velocity = vector(projectile.speed*cos(projectile.angle),
                                 projectile.speed*sin(projectile.angle),
                                 0)

    use_ruler = True
    ## Start rulers at projectile initial position.
    if (use_ruler):
        # Make x-axis.
        dx = 1.0 # Box center-to-center separation (AKA ruler marking).
        box_x = projectile.pos.x + 0.5*dx # Box's x-coordinate.
        box_x_max = -box_x ## Will likely need to change.
        while box_x <= box_x_max:
            box(pos=vector(box_x,-0.05,0),
                size=vector(0.95*dx,0.05,0.05),
                color=color.green,
                opacity=0.5)
            box_x += dx

        # Make y-axis.
        dy = dx # Box center-to-center separation (AKA ruler marking).
        box_y = projectile.pos.y + 0.5*dy # Box's y-coordinate.
        box_y_max = max(-box_y,box_x_max) ## Will likely need to change.
        ### May need to generate more ruler boxes within the motion loop.
        while box_y <= box_y_max:
            box(pos=vector(-0.05,box_y,0),
                size=vector(0.05,0.95*dy,0.05),
                color=color.green,
                opacity=0.5)
            box_y += dy

    projectile.mass = 1.0   #kg
    grav_field = 9.81   #m/s2

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

        # Extend Ruler automatically
        if (projectile.pos.x > box_x_max):
            # Add Box x-axis
            box_x_max += dx
            box(pos=vector(box_x_max,-0.05,0),
                size=vector(0.95*dx,0.05,0.05),
                color=color.green,
                opacity=0.5)
            
        if (projectile.pos.y > box_y_max):
            # Add Box y-axis
            box_y_max += dy
            box(pos=vector(-0.05,box_y_max,0),
                size=vector(0.05,0.95*dy,0.05),
                color=color.green,
                opacity=0.5)

    angle += delta_angle
print=('Finished')
            
        
