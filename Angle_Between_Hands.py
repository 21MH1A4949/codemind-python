n=input()
h = (ord(n[0])-48)*10 + ord(n[1])-48
m =(ord(n[3])-48)*10  +ord(n[4])-48
angle=(11*m/2)-30*h
if angle<0:
    angle+=360
if angle>180:
    angle=360-angle
print(angle)