import time

# Move: Belly Flop

#move('Shrivel')
#time.sleep(.2)

hexy.RF.hip(0)
hexy.RF.knee(-85)
hexy.RF.ankle(-85)

hexy.RM.hip(0)
hexy.RM.knee(-85)
hexy.RM.ankle(-85)

hexy.RB.hip(0)
hexy.RB.knee(-85)
hexy.RB.ankle(-85)

hexy.LF.hip(0)
hexy.LF.knee(-85)
hexy.LF.ankle(-85)

hexy.LM.hip(0)
hexy.LM.knee(-85)
hexy.LM.ankle(-85)

hexy.LB.hip(0)
hexy.LB.knee(-85)
hexy.LB.ankle(-85)

hexy.neck.set(0)

for i in range(4):
    #Too
    hexy.RF.hip(25)
    hexy.RF.knee(-70)
    hexy.RF.ankle(-70)
    
    hexy.RM.hip(-25)
    hexy.RM.knee(-85)
    hexy.RM.ankle(-40)
    
    hexy.RB.hip(25)
    hexy.RB.knee(-70)
    hexy.RB.ankle(-70)
    
    hexy.LF.hip(-25)
    hexy.LF.knee(-85)
    hexy.LF.ankle(-40)
    
    hexy.LM.hip(25)
    hexy.LM.knee(-70)
    hexy.LM.ankle(-70)
    
    hexy.LB.hip(-25)
    hexy.LB.knee(-85)
    hexy.LB.ankle(-40)
    
    hexy.neck.set(45)
    
    time.sleep(.3)
    
    
    #Fro
    hexy.RF.hip(-25)
    hexy.RF.knee(-85)
    hexy.RF.ankle(-40)
    
    hexy.RM.hip(25)
    hexy.RM.knee(-70)
    hexy.RM.ankle(-70)
    
    hexy.RB.hip(-25)
    hexy.RB.knee(-85)
    hexy.RB.ankle(-40)
    
    hexy.LF.hip(25)
    hexy.LF.knee(-70)
    hexy.LF.ankle(-70)
    
    hexy.LM.hip(-25)
    hexy.LM.knee(-85)
    hexy.LM.ankle(-40)
    
    hexy.LB.hip(25)
    hexy.LB.knee(-70)
    hexy.LB.ankle(-70)
    
    hexy.neck.set(-45)
    
    time.sleep(.3)



time.sleep(2)
#move('Shrivel')
