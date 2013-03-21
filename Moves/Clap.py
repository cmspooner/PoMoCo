import time

hexy.RM.hip(60)
hexy.LM.hip(-60)

hexy.RF.knee(0)
hexy.RF.ankle(0)
hexy.LF.knee(0)
hexy.LF.ankle(0)
time.sleep(.2)

hexy.RF.hip(65)
hexy.LF.hip(-65)

time.sleep(.25)
move('Stand')
