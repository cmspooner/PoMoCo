import time

# Move: Belly Flop

move('Set Zero')
time.sleep(1)

for a in range(0, 85, 5):
    print a
    hexy.RF.knee(-a)
    hexy.RF.ankle(-a)

    hexy.RM.knee(-a)
    hexy.RM.ankle(-a)

    hexy.RB.knee(-a)
    hexy.RB.ankle(-a)

    hexy.LF.knee(-a)
    hexy.LF.ankle(-a)

    hexy.LM.knee(-a)
    hexy.LM.ankle(-a)

    hexy.LB.knee(-a)
    hexy.LB.ankle(-a)