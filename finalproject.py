from visual import *
import time

print("""
Press to enter roaming mode, release to exit roaming mode.
In roaming mode, with the mouse button down, move the mouse
above or below the center of the scene to move forward or
backward; right or left rotates your direction of motion.
""")


# A surreal scene that illustrates many of the features of VPython

scene.title = "3D Platformer"
##scene.stereo = 'redcyan'
scene.height = 600
scene.width = 600
scene.range = (1,1,1)
scene.center = (0,2,20)
scene.background = (0, 0.5, 1)
scene.userspin = False
scene.userzoom = False
grey = (0.8, 0.8, 0.8)
Nslabs = 8
R = 10
w = 5
d = 0.5
h = 5
photocenter = 0.15*w

# The floor, central post, and ball atop the post
floor = box(pos=(0,-0.1,0),size=(0.2,15,15), axis=(0,1,0), color=color.orange, material=materials.wood)
floor = box(pos=(0,0.1,20),size=(0.2,10,10), axis=(0,1,0), color=color.orange, material=materials.wood)
floor = box(pos=(0,0.1,-20),size=(0.2,10,10), axis=(0,1,0), color=color.orange, material=materials.wood)

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
smoke = []
Nrings = 20
x0, y0, z0 = -5, 1.5, -2
r0 = 0.1
spacing = .5
thick = r0/4
dr = 0.015
dthick = thick/Nrings
gray = 1
cylinder(pos=(x0,0,z0), axis=(0,y0+r0,0), radius=1.5*r0, color=color.green)

# Create the smoke rings
for i in range(Nrings):
  smoke.append(ring(pos=(x0,y0+spacing*i,z0), axis=(0,1,0),
                  radius=r0+dr*i, thickness=thick-dthick*i, color=(gray,gray,gray)))
y = 0
dy = spacing/20
top = Nrings-1

# Roll a log back and forth
rlog = 1
wide = 4
zpos = 2
zface = 5
tlogend = 0.2
v0 = 1
v = v0
omega = -v0/rlog
theta = 0
dt = 0.1
tstop = 0.3
log = frame(pos=(-wide,rlog,zpos), axis=(0,0,1))
cylinder(frame=log,
         pos=(0,0,0), axis=(zface-zpos,0,0),
         color=(0.8,0.5,0), opacity=0.5)
box(frame=log,
    pos=(zface-zpos+tlogend/2.+.01,0,0), axis=(0,0,1),
    length=rlog, height=rlog, width=tlogend,
    color=color.yellow, opacity=0.5)

leftstop = box(pos=(-wide-rlog-tstop/2,0.6*rlog,(zpos+zface)/2),
    length=tstop, height=1.2*rlog, width=(zface-zpos), color=color.red)
rightstop = box(pos=(wide+rlog+tstop/2,0.6*rlog,(zpos+zface)/2),
    length=tstop, height=1.2*rlog, width=(zface-zpos), color=color.red)


# Display an ellipsoid
Rcloud = 0.8*R
omegacloud = v0/Rcloud
cloud = ellipsoid(pos=(0,0.7*h,-Rcloud), size=(5,2,2),
                  color=(1,1,1), opacity=1)

rhairs = 0.025 # half-length of crosshairs
dhairs = 2 # how far away the crosshairs are
maxcosine = dhairs/sqrt(rhairs**2+dhairs**2) # if ray inside crosshairs, don't move
haircolor = color.black
roam = 0

def keyInput(evt):
    s = evt.key
    if len(s) == 1:
        if (s == 'w'):
            print("w is pressed")
        elif (s == 's'):
            print("s is pressed")
        elif (s == 'a'):
            print("a is pressed")
        elif (s == 'd'):
            print("d is pressed")

scene.bind('keydown', keyInput)

while True:
    # Toggle roam option
    if scene.mouse.events:
        m = scene.mouse.getevent()
        if m.press or m.drag:
            roam = True
        elif m.release or m.drop:
            roam = False

    # If in roaming mode, change center and forward according to mouse position
    if roam:
        ray = scene.mouse.ray
        if abs(dot(ray,scene.forward)) < maxcosine: # do something only if outside crosshairs
            newray = norm(vector(ray.x, 0, ray.z))
            angle = arcsin(dot(cross(scene.forward,newray),scene.up))
            newforward = rotate(scene.forward, axis=scene.up, angle=angle/30)
            scene.center = scene.mouse.camera+newforward*mag(scene.center-scene.mouse.camera)
            scene.forward = newforward
            scene.center = scene.center+scene.forward*ray.y/2.

    # Roll the log
    theta = theta + omega*dt
    log.x = log.x+v*dt
    log.rotate(angle=omega*dt)
    if log.x >= wide:
        v = -v0
        omega = -v/rlog
        if rightstop.color == color.red:
            rightstop.color = color.blue
        else:
            rightstop.color = color.red
    if log.x <= -wide:
        v = +v0
        omega = -v/rlog
        if leftstop.color == color.red:
            leftstop.color = color.blue
        else:
            leftstop.color = color.red

    # Move the cloud
    cloud.rotate(angle=omegacloud*dt, origin=(0,0,0), axis=(0,1,0))

    # Move the smoke rings
    for i in range(Nrings):
        # Raise the smoke rings
        smoke[i].pos = smoke[i].pos+vector(0,dy,0)
        smoke[i].radius = smoke[i].radius+(dr/spacing)*dy
        smoke[i].thickness = smoke[i].thickness-(dthick/spacing)*dy
    y = y+dy
    if y >= spacing:
        # Move top ring to the bottom
        y = 0
        smoke[top].pos = (x0, y0, z0)
        smoke[top].radius = r0
        smoke[top].thickness = thick
        top = top-1
    if top < 0:
        top = Nrings-1
    
    rate(30)

