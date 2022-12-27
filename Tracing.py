# Ray Tracing Algorthim
import numpy
import random
camera = 0,0,2
maxmiumroomX = 2000
maxmiumroomY = 2000
maxmiumroomZ = 2000
def raytrace(x,y,z,s):
    for i in range(s):
        raysx = x
        raysy = y
        raysz = z
        raysbouncing = random.randint(0,2000)
        seconds = 1
        seconds+=1
        raysx*299792458*seconds
        raysy*299792458*seconds
        raysz*299792458*seconds
        if raysx > 2000:
            raysx*-299792458*seconds
        if raysx < -2000:
            raysx*299792458*seconds
        if raysy < 2000:
            raysy*299792458*seconds
        if raysy < -2000:
            raysy*299792458*seconds
        if raysz < 2000:
            raysz*299792458*seconds
        if raysz < -2000:
            raysz*299792458*seconds
        print("X value for ray is")
        print(raysx)
        print("Y value for ray is")
        print(raysy)
        print("Z value for ray is ")
        print(raysz)
        print("Time value for ray is")
        print(seconds)


print("RX Ray Tracing Algorthim")
lx = input("What is the x coordinate for the camera")
ly = input("What is the y coordinate for the camera")
lz = input("What is the z coordinate for the camera")
sec = input("How long you wanna keep the simulation running for")
lxp = int(lx)
lyp = int(ly)
lzp = int(lz)
secp = int(sec)
raytrace(lxp,lyp,lzp,secp)
