import os
import time
import re
import sys 

# Keep the folders clean for beginners
sys.dont_write_bytecode = True

# Include the moves folder
sys.path.append('Moves')
sys.path.append('HexyCLI')

import servotorComm
from robot import hexapod

if __name__ == '__main__':
    
    # Intialize the servo controller
    controller = servotorComm.Controller()
    
    # Set up the servo controller to run Hexy
    hexy = hexapod(controller)
    __builtins__.hexy = hexy # sets 'hexy' to be a global variable common to all modules
    __builtins__.floor = 60  # this is the minimum level the legs will reach
    
    # Go through the Moves folder to find move files
    moves = []
    for fileName in os.listdir('Moves'):
        if os.path.splitext(fileName)[1] == '.py':
            fileName = os.path.splitext(fileName)[0]
            s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', fileName)
            moves.append(s1)
            __builtins__.moves = moves
    
    # Function for running move files
    def move(moveName):
        print "Performing move:",moveName
        moveName = moveName.replace(' ','')
        if moveName in sys.modules:
            reload(sys.modules[moveName])
        else:
            __import__(moveName)
    
    # Make move global.
    __builtins__.move = move
    
    # Start the GUI. This will handle all further events.
    
    quit = False
    print "Enter a Command"
    while not quit:
        cmd = raw_input("> ")
        if cmd in __builtins__.moves:
            servotorComm.runMovement(move, cmd)
        elif cmd [:4] == "hexy":
            myLeg = cmd.split(".")[1]
            myJoint = cmd.split(".")[2].split("(")[0]
            myAngle = cmd.split(".")[2].split("(")[1].split(")")[0]
            #print myLeg, myJoint, myAngle
            if myLeg == "RF":
                if myJoint == "hip":
                    hexy.RF.hip(int(myAngle))
                elif myJoint == "knee":
                    hexy.RF.knee(int(myAngle))
                elif myJoint == "ankle":
                    hexy.RF.ankle(int(myAngle))
            elif myLeg == "RM":
                if myJoint == "hip":
                    hexy.RM.hip(int(myAngle))
                elif myJoint == "knee":
                    hexy.RM.knee(int(myAngle))
                elif myJoint == "ankle":
                    hexy.RM.ankle(int(myAngle))
            elif myLeg == "RB":
                if myJoint == "hip":
                    hexy.RB.hip(int(myAngle))
                elif myJoint == "knee":
                    hexy.RB.knee(int(myAngle))
                elif myJoint == "ankle":
                    hexy.RB.ankle(int(myAngle))
            elif myLeg == "LF":
                if myJoint == "hip":
                    hexy.LF.hip(int(myAngle))
                elif myJoint == "knee":
                    hexy.LF.knee(int(myAngle))
                elif myJoint == "ankle":
                    hexy.LF.ankle(int(myAngle))
            elif myLeg == "LM":
                if myJoint == "hip":
                    hexy.LM.hip(int(myAngle))
                elif myJoint == "knee":
                    hexy.LM.knee(int(myAngle))
                elif myJoint == "ankle":
                    hexy.LM.ankle(int(myAngle))
            elif myLeg == "LB":
                if myJoint == "hip":
                    hexy.LB.hip(int(myAngle))
                elif myJoint == "knee":
                    hexy.LB.knee(int(myAngle))
                elif myJoint == "ankle":
                    hexy.LB.ankle(int(myAngle))
           
                
        elif cmd in ["quit", "q", "exit"]:
            quit = True
        else:
            print "I don't know how to", cmd
        
        while len(controller.serialHandler.sendQueue) > 0:
            controller.serialHandler.sendCommand()
            time.sleep(.1)
    
    # The program only reaches this point if the GUI has been closed.
    # In this case, we want to clean up and exit.
    del hexy
    del controller
    while len(controller.serialHandler.sendQueue) > 0:
        controller.serialHandler.sendCommand()
        time.sleep(.1)
    print "Quitting!"
    os._exit(0)
