import time

# Move: Lean Back

# Pick up back feet
move('Stand')

hexy.RM.hip(60)
hexy.LM.hip(-60)

hexy.RF.knee(-60)
hexy.RF.ankle(0)

hexy.LF.knee(-60)
hexy.LF.ankle(0)

for i in range(4):
    hexy.RF.hip(-45)
    hexy.RF.ankle(-45)
    hexy.LF.hip(-45)
    hexy.LF.ankle(45)
    hexy.neck.set(45)
    time.sleep(.3)
    
    hexy.RF.hip(45)
    hexy.RF.ankle(45)
    hexy.LF.hip(45)
    hexy.LF.ankle(-45)
    hexy.neck.set(-45)
    time.sleep(.3)
    
hexy.RF.hip(0)
hexy.RF.ankle(0)
hexy.LF.hip(0)
hexy.LF.ankle(0)
hexy.neck.set(0)

time.sleep(1)
move('Stand')