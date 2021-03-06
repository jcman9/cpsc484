from visual import *
import time

print("""
Use "W,S,A,D" for moving forwards, backwards, strafe left and strafe right respectively. Use spacebar
to jump over gaps and jump onto platforms. If you fall, the game resets.  Reach the final platform to win.

Created by Richard Erdtsieck and Josh Manulat
""")


# A surreal scene that illustrates many of the features of VPython

scene.title = "3D Platformer"
##scene.stereo = 'redcyan'````
scene.height = 1000
scene.width = 1000
scene.range = (1,1,1)
#scene.center = (0,2,20)
scene.center = (0,2.2,0)
scene.background = (0, 0.5, 1)
scene.userspin = False
scene.userzoom = False
scene.autozoom = False
scene.autospin = False
grey = (0.8, 0.8, 0.8)
Nslabs = 8
R = 10
w = 5
d = 0.5
h = 5
photocenter = 0.15*w
# -Z coord is forward, pos for box() is center of the box
# The floor, central post, and ball atop the
#floor = box(pos=(0,-0.1,0),size=(0.2,15,15), axis=(0,1,0), color=color.orange, material=materials.wood)
#floor = box(pos=(0,0.1,20),size=(0.2,10,10), axis=(0,1,0), color=color.orange, material=materials.wood)
#floor = box(pos=(0,0.1,-20),size=(0.2,10,10), axis=(0,1,0), color=color.orange, material=materials.wood)

#with axis (0,1,0), size refers to (ylength, xlength, zlength)
#floor1 z values go from (0,0,0) to (0,0,-50)
floor1 = box(pos = (0,0,-25), size = (.2,2,50), axis=(0,1,0), color = color.orange, material = materials.wood)

#floor 2 z values go from (0,0,-55) to (0,0,-105)
floor2 = box(pos = (0,0,-80), size = (.2,2,50), axis = (0,1,0), color = color.orange, material = materials.wood)

#movingPlatform z values go from (0,0,-107.5) to (0,0,-112.5)
movingPlatform = box(pos = (0,0, -110), size = (.2,10,5), axis = (0,1,0), color = color.orange, material = materials.wood)

#movingPlatform2 z values go from (0,0,-115) to (0,0,-120)
movingPlatform2 = box(pos = (0,0, -117.5), size = (.2,10,5), axis = (0,1,0), color = color.orange, material = materials.wood)

#movingPlatform3 z values go from (0,0,-122.5) to (0,0,-127.5)
movingPlatform3 = box(pos = (0,0,-125), size = (.2,10,5), axis = (0,1,0), color = color.orange, material = materials.wood)

#floor3 z values go from (0,0,-130) to (0,0,-135)
floor3 = box(pos =(0,5, -132.5), size = (.2,10,5), axis = (0,1,0), color = color.orange, material = materials.wood)

player = box (pos = (0,1.1,-2), size = (2,2,2), axis = (0,1,0), color = color.blue, opacity = 0.3)

#first box z values go from (0,0,-18) to (0,0,-22)
firstBox = box(pos = (0,1,-20), size = (2,2,2), axis = (0,1,0), color = color.orange, material = materials.wood)

### Here is the code used to create the cactus flower display
##import Image # Must install PIL, the Python Imaging Library
##name = "flower"
##width = 128 # must be power of 2
##height = 128 # must be power of 2
##im = Image.open(name+".jpg")
###print im.size # optionally see size of image
### Optional cropping:
###im = im.crop((x1,y1,x2,y2)) # (0,0) is upper left
##im = im.resize((width,height), Image.ANTIALIAS)
##materials.saveTGA(name,im)



# Display smoke rings rising out of a black tube
##smoke = []
##Nrings = 20
##x0, y0, z0 = -5, 1.5, -2
##r0 = 0.1
##spacing = .5
##thick = r0/4
##dr = 0.015
##dthick = thick/Nrings
##gray = 1
##cylinder(pos=(x0,0,z0), axis=(0,y0+r0,0), radius=1.5*r0, color=color.green)
##
### Create the smoke rings
##for i in range(Nrings):
##  smoke.append(ring(pos=(x0,y0+spacing*i,z0), axis=(0,1,0),
##                  radius=r0+dr*i, thickness=thick-dthick*i, color=(gray,gray,gray)))
##y = 0
##dy = spacing/20
##top = Nrings-1
##

## Roll a log back and forth
rlog = 1
wide = 4
zpos = 2
zface = 4
#tlogend = 0.2
v0 = 1
v = v0
omega = -v0/rlog
theta = 0
dt = 0.1
tstop = 0.3
#log = frame(pos=(-wide,rlog,zpos), axis=(1,0,0))
#cylinder(frame=log,
#         pos=(3,-.5,-105), axis=(zface-zpos,0,0),radius= .5,
#         color=(0.8,0.5,0))

log = cylinder(pos = (-1,.6,-105), axis = (1,0,0), length = 2, radius = .5, material = materials.wood)

##box(frame=log,
##    pos=(zface-zpos+tlogend/2.+.01,0,0), axis=(0,0,1),
##    length=rlog, height=rlog, width=tlogend,
##    color=color.yellow, opacity=0.5)

##leftstop = box(pos=(-wide-rlog-tstop/2,0.6*rlog,(zpos+zface)/2),
##    length=tstop, height=1.2*rlog, width=(zface-zpos), color=color.red)
##rightstop = box(pos=(wide+rlog+tstop/2,0.6*rlog,(zpos+zface)/2),
##    length=tstop, height=1.2*rlog, width=(zface-zpos), color=color.red)
##
##
### Display an ellipsoid
##Rcloud = 0.8*R
##omegacloud = v0/Rcloud
##cloud = ellipsoid(pos=(0,0.7*h,-Rcloud), size=(5,2,2),
##                  color=(1,1,1), opacity=1)
##
##rhairs = 0.025 # half-length of crosshairs
##dhairs = 2 # how far away the crosshairs are
##maxcosine = dhairs/sqrt(rhairs**2+dhairs**2) # if ray inside crosshairs, don't move
##haircolor = color.black
##roam = 0

def keyInput(evt):
    global roam
    global forward, backwards, left, right, jump
    s = evt.key
    if len(s) == 1:
        if (s == 'w'):
            forward = True
        elif (s == 's'):
            backwards = True
        elif (s == 'a'):
            left = True
        elif (s == 'd'):
            right = True
        elif (s == ' '):
            jump = True

def keyRelease(evt):
    #global roam
    global forward, backwards, left, right, jump
    s = evt.key
    if len(s) == 1:
        if (s == 'w'):
            forward = False
        elif (s == 's'):
            backwards = False
        elif (s == 'a'):
            left = False
        elif (s == 'd'):
            right = False
        elif (s == ' '):
            jump = False



scene.bind('keydown', keyInput)
scene.bind('keyup', keyRelease)

global forward, backwards, left, right, jump, ray, falling, v_Platform, v0_Platform, dtPlatform
global dtPlatform2, v_Platform2, v0_Platform2
global dtPlatform3, v_Platform3, v0_Platform3
global peakHeight
global gameover
forward = False
backwards = False
left = False
right = False
jump = False
falling = False
peakHeight = False
ray = (0,0,0)

gameover = False

v_Platform = 1
v0_Platform = 1
dtPlatform = .1

v_Platform2 = -1
v0_Platform2 = -1
dtPlatform2 = .125

v_Platform3 = 1
v0_Platform3 = 1
dtPlatform3 = .1
         
while True:

    # If in roaming mode, change center and forward according to mouse position

    ray = (0,0,0)

    ##Object Movement
    if movingPlatform.pos.x >= 20:
        v_Platform = -v0_Platform
    elif movingPlatform.pos.x <= -20:
        v_Platform = v0_Platform
    movingPlatform.pos.x = movingPlatform.pos.x + v_Platform *dtPlatform

    if movingPlatform2.pos.x >= 20:
        v_Platform2 = v0_Platform2
    elif movingPlatform2.pos.x <= -20:
        v_Platform2 = -v0_Platform2
    movingPlatform2.pos.x = movingPlatform2.pos.x + v_Platform2 * dtPlatform2

    if movingPlatform3.pos.y <= 0:
        v_Platform3 = v0_Platform3
    elif movingPlatform3.pos.y >= 5:
        v_Platform3 = -v0_Platform3
    movingPlatform3.pos.y = movingPlatform3.pos.y + v_Platform3 * dtPlatform3

    # Roll the log
    theta = theta + omega*dt
    #print (theta)
    #print (omega)
    log.z = log.z+v*dt
    log.rotate(angle=omega*dt)
    if log.z >= -55:
       v = -v0
       omega = -v/rlog
    if log.z <= -105:
        v = +v0
        omega = -v/rlog
        
    #Begining of movement code
    if forward:
        if (forward and jump and not(peakHeight)):
            ray = (0,.25, -.25)
        else:
            ray = (0,0,-.25)
    elif backwards:
        if (backwards and jump and not(peakHeight)):
            ray = (0,.25,.25)
        else:
            ray = (0,0,.25)
    elif left:
        if left and jump and not(peakHeight):
            ray = (-.25,.25,0)
        else:
            ray = (-.25,0,0)
    elif right:
        if right and jump and not(peakHeight):
            ray = (.25,.25,0)
        else:
            ray = (.25,0,0)
    elif jump and peakHeight == False:
        ray = (0,.1,0)

    if jump:
        falling = True
    #End of Movement Code

    #set max height of player jump
    if player.pos.y >= 5 and 0 >= player.pos.z >= -120:
        ray = (ray[0], 0, ray[2])
        peakHeight = True
    elif player.pos.y >= 10 and -122.5 >= player.pos.z >= -135:
        ray = (ray[0], 0, ray[2])

    #if player and first box share a position they collided, move back one spot to stop collision
    #if bottom of player cube is lower then top of the firstBox then collide

    ##COLLISION DETECTION GOES HERE

    ##Dont need to do this anymore, keeping her for now till we finish
    ##ADD any gaps between platforms here 
    #if player.pos.z >= floor1.pos.z + player.size.z:
    #    falling = True
##    elif floor1.pos.z - - floor1.size.z > player.pos.z > floor2.pos.z - floor2.size.z:
##        falling = True
##    elif floor2.pos.z - floor2.size.z > player.pos.z > movingPlatform.pos.z - movingPlatform.size.z:
##        falling = True
##    elif player.pos.z < -112.5:
##        falling = True

    falling = True

    ##Beggining of Floor1 Collision

    if not(jump) and -50 <= player.pos.z <= 0:
        if (player.pos.x <= -2 or player.pos.x >= 2):
            falling = True
            peakHeight = True
        elif player.pos.y <= 1.1:
            falling = False
            peakHeight = False
        elif player.pos.y > 1.1:
            falling = True
            peakHeight = True
    
    ##End of Floor1 Collison

    ##Beggining of Floor2 Collision

    if not(jump) and -105 <= player.pos.z <= -55:
        if (player.pos.x <= -2 or player.pos.x >= 2):
            falling = True
            peakHeight = True
        elif player.pos.y <= 1.1:
            falling = False
            peakHeight = False
        elif player.pos.y > 1.1:
            falling = True
            peakHeight = True
            
    ##End of Floor2 Collision

    ##Beggining of firstBox Collision

    #Collision on top of firstBox
    if not(jump) and -22 <= player.pos.z <= -18 and player.pos.y <= firstBox.pos.y + 2:
        falling = False
        peakHeight = False
        #Fall off sides of box
        if (player.pos.x < -2 or player.pos.x > 2):
            falling = True
            peakHeight = True

    if ((player.pos.z - 1) == (firstBox.pos.z + 1)) and (player.pos.y - 1 < firstBox.pos.y + 1):
        #print("Collided with firstBox")
        ray = (ray[0],ray[1],-ray[2] + 1)
    elif ((player.pos.z + 1) == (firstBox.pos.z - 1)) and (player.pos.y - 1 < firstBox.pos.y + 1):
        #print ("Collided with backside of FirstBox")
        ray = (ray[0], ray[1], -ray[2] - 1) 

    ##End of firstBox Collision

    ##Beggining of movingPlatform Collision

    #print(player.pos)
    if not(jump) and -107.5 >= player.pos.z >= -112.5:
        #print("movingPlatform")
        if(player.pos.x < (movingPlatform.pos.x - 5)) or (player.pos.x > (movingPlatform.pos.x + 5)):
            falling = True
            peakHeight = True
        elif player.pos.y <= 1.1:
            falling = False
            peakHeight = False
            player.pos.x = player.pos.x + (v_Platform * dtPlatform)
        elif player.pos.y > 1.1:
            falling = True
            peakHeight = True

    ##End of movingPlatform Collision

    ##Beggining of movingPlatform2 Collision

    if not(jump) and -115 >= player.pos.z >= -120:
        #print("movingPlatform")
        if(player.pos.x < (movingPlatform2.pos.x - 5)) or (player.pos.x > (movingPlatform2.pos.x + 5)):
            falling = True
            peakHeight = True
        elif player.pos.y <= 1.1:
            falling = False
            peakHeight = False
            player.pos.x = player.pos.x + (v_Platform2 * dtPlatform2)
        elif player.pos.y > 1.1:
            falling = True
            peakHeight = True

    ##End of movingPlatform2 Collision

    ##Beggining of movingPlatform3 Collision

    if not(jump) and -122.5 >= player.pos.z >= -127.5:
        #print("movingPlatform")
        if(player.pos.x < (movingPlatform3.pos.x - 5)) or (player.pos.x > (movingPlatform3.pos.x + 5)):
            falling = True
            peakHeight = True
        elif player.pos.y <= movingPlatform3.pos.y + 1:
            falling = False
            peakHeight = False
            player.pos.y = player.pos.y + (v_Platform3 * dtPlatform3)
        elif player.pos.y > movingPlatform3.pos.y + 1:
            falling = True
            peakHeight = True
            
    ##End of movingPlatform3 Collision

    ##Beggining of floor3 Collision
            
    if not(jump) and -130 >= player.pos.z >= -135:
        if (player.pos.x <= floor3.pos.x - 5 or player.pos.x >= floor3.pos.x + 5):
            falling = True
            peakHeight = True
        #elif 5 <= player.pos.y <= 5.2:
        elif not(jump) and player.pos.y - 1 > floor3.pos.y + .1:
            falling = True
            peakHeight = True
        elif not(jump) and player.pos.y - 1 <= floor3.pos.y +.1:
            falling = False
            peakHeight = False
            gameover = True

    ##End of floor3 Collision

    #Beggining Log Collision

    if not(jump) and -55 >= player.pos.z >= -105:
        if not(jump) and log.pos.y - .5 <= player.pos.y - 1 <= log.pos.y + .5 and log.pos.z - .5 <= player.pos.z <= log.pos.z + .5:
            print("top")
            player.pos.z = player.pos.z + 2 * v
        #Checks if Player sides are hitting log
        elif not(jump) and ((log.pos.z + .5 >= player.pos.z - 1 >= log.pos.z - .5) or log.pos.z + .5 >= player.pos.z + 1 >= log.pos.z - .5):
            #print("side")
            player.pos.z = player.pos.z + v * dt

    #End of Log Collision

    if gameover == True:
        print("Congratulations you WIN!")
        break    
    if falling and not(jump):
        ray = (ray[0], -.15, ray[1])

    player.pos = player.pos + ray
    scene.center = player.pos + (0, 0.3, 10)

    if player.pos.y <= -15:
        print("You Lose, Resetting")
        player.pos = (0,1.2,-2)
        scene.center = player.pos + (0,0,10)
        
##    # Move the cloud
##    cloud.rotate(angle=omegacloud*dt, origin=(0,0,0), axis=(0,1,0))
##
##    # Move the smoke rings
##    for i in range(Nrings):
##        # Raise the smoke rings
##        smoke[i].pos = smoke[i].pos+vector(0,dy,0)
##        smoke[i].radius = smoke[i].radius+(dr/spacing)*dy
##        smoke[i].thickness = smoke[i].thickness-(dthick/spacing)*dy
##    y = y+dy
##    if y >= spacing:
##        # Move top ring to the bottom
##        y = 0
##        smoke[top].pos = (x0, y0, z0)
##        smoke[top].radius = r0
##        smoke[top].thickness = thick
##        top = top-1
##    if top < 0:
##        top = Nrings-1
    
    rate(100)

