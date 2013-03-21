import time

move("Stand")

hexy.RM.hip(60)
hexy.LM.hip(-60)

hexy.RF.hip(-50)
hexy.LF.hip(50)

#y
hexy.RF.knee(-50)
hexy.LF.knee(-50)

hexy.RF.ankle(0)
hexy.LF.ankle(0)

time.sleep(1)
#m
hexy.RF.ankle(-85)
hexy.LF.ankle(-85)

hexy.RF.knee(-25)
hexy.LF.knee(-25)

time.sleep(1)
#c
move('TiltLeft')
hexy.LB.knee(20)

hexy.RF.knee(-75)
hexy.RF.ankle(60)

time.sleep(1)

hexy.LF.ankle(65)
hexy.LF.knee(-20)

time.sleep(1)
#stand
hexy.LM.hip(0)

hexy.LF.knee(40)
hexy.LF.ankle(-60)
hexy.LM.knee(20)
hexy.LB.knee(50)
hexy.LB.ankle(-35)

time.sleep(.2)

hexy.LM.ankle(-45)
hexy.LM.knee(30)

time.sleep(.2)

hexy.LM.knee(30)
hexy.LM.ankle(-25)

hexy.LB.hip(0)
hexy.LB.knee(30)
hexy.LB.ankle(-35)

time.sleep(.2)

hexy.LM.hip(0)
hexy.LM.knee(60)
hexy.LM.ankle(-45)

hexy.LB.hip(0)
hexy.LB.knee(60)
hexy.LB.ankle(-45)
time.sleep(.2)

#a
hexy.RF.knee(-85)
hexy.LF.knee(-85)
hexy.RF.ankle(25)
hexy.LF.ankle(25)



time.sleep(2)
move("Stand")

