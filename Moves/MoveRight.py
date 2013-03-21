import time

# Move: Move Forward

move('Stand')
#Tripod 1 up
hexy.LF.knee(15)
hexy.RM.knee(15)
hexy.LB.knee(15)

hexy.LF.ankle(-85)
hexy.RM.ankle(-85)
hexy.LB.ankle(-85)
time.sleep(.2)

#Tripod 2 move
hexy.RF.hip(45)
hexy.LM.knee(45)
hexy.RB.hip(-45)
time.sleep(.2)

#Tripod 1 down
hexy.LF.hip(-45)
hexy.LF.knee(60)
hexy.LF.ankle(-45)
hexy.RM.knee(60)
hexy.RM.ankle(-45)
hexy.LB.hip(45)
hexy.LB.knee(60)
hexy.LB.ankle(-45)
time.sleep(.2)

#Tripod 2 up
hexy.RF.knee(15)
hexy.LM.knee(15)
hexy.RB.knee(15)

hexy.RF.ankle(-85)
hexy.LM.ankle(-85)
hexy.RB.ankle(-85)
time.sleep(.2)

#Tripod 1 move
hexy.LF.hip(45)
hexy.RM.knee(45)
hexy.LB.hip(-45)
time.sleep(.2)

#Tripod 2 down
hexy.RF.hip(-45)
hexy.RF.knee(60)
hexy.RF.ankle(-45)
hexy.LM.knee(60)
hexy.LM.ankle(-45)
hexy.RB.hip(45)
hexy.RB.knee(60)
hexy.RB.ankle(-45)
time.sleep(.2)

move('Stand')

