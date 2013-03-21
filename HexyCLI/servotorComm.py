import time
import math
import serial
import serial.tools.list_ports

debug = False
startTime = time.clock()
serialSends = []

BAUD_RATE = 9600

class serHandler():
    def __init__(self):
        self.ser = None

        self.sendQueue=[]

        self.recieveQueue=[]

        self.serOpen = False
        self.serNum = 0
        
        self.connect()
        if not self.ser:
            self.ser = dummySer()
            self.serOpen = True

    def __del__(self):
        if self.ser:
            self.ser.close()
        

    def sendCommand(self):
        # Send waiting messages
        send = False
        if(len(self.sendQueue)>0):
            toSend = self.sendQueue.pop(0)
            send = True
        if send:
            sendTime = time.clock()-startTime
            serialSends.append([float(sendTime),str(toSend)])
            time.sleep(0.003)
            if self.serOpen:
                if self.ser.writable:
                    if self.serOpen:
                        self.ser.write(str(toSend))
                        print "Sent '%s' to COM%d"%(str(toSend).strip('\r'),self.serNum+1)
        if debug:
            print "Sent '%s' to COM%d"%(str(toSend).strip('\r'),self.serNum+1)

    def connect(self):
            comList = []
            comports = serial.tools.list_ports.comports()
            for comport in comports:
                    for thing in comport:
                            #print thing
                            comList.append(thing)
            
            comList = list(set(comList))
            print "Attempting to connect to Servotor"
            for port in comList:
                    try:
                        ser = serial.Serial(port, baudrate= BAUD_RATE, timeout=2)
                        ser.write('V\n')
                        result = ser.readline()
                        if "SERVOTOR" in result:
                            print "Connect Successful! Connected on port:",port
                            self.ser = ser
                            self.ser.flush()
                            self.serOpen = True
                            self.serNum = 1
                            break
                    except:
                        pass
            if self.serOpen == False:
                print "Trying Windows Method"
                for i in range(1,100):
                    try:
                        try:
                            ser = serial.Serial(i, baudrate=BAUD_RATE, timeout=1)
                            #print "ser",i
                        except:
                            #print "ser",i,"failed"
                            raise Exception
                        ser.flush()
                        time.sleep(0.1)
                        ser.write("V\n")
                        time.sleep(1)
                        readReply = ser.readline()
                        #print "read:",readReply
                        if "SERVOTOR" in readReply:
                            print "Connect Successful! Connected on port COM"+str(i+1)
                            ser.flush()
                            self.ser = ser
                            self.serNum = i
                            self.serOpen = True
                            break
                        else:
                            ser.close()
                            pass
                    except:
                        pass
                    
class Servo:
    def __init__(self,servoNum,serHandler,servoPos=1500,offset=0,active=False):
        self.serHandler = serHandler
        self.active = active
        self.servoNum = servoNum

        # Servo position and offset is stored in microseconds (uS)
        self.servoPos = servoPos
        self.offset = offset


    def setPos(self,timing=None,deg=None,move=True):
        if timing != None:
            self.servoPos = timing
        if deg != None:
            self.servoPos = int(1500.0+float(deg)*11.1111111)
        if move:
            self.active = True
            self.move()
            if debug: print "Moved ",self.servoNum
        if debug: print "Servo",self.servoNum,"set to",self.servoPos

    def getPosDeg(self):
        return (self.servoPos-1500)/11.1111111

    def getPosuS(self):
        return self.servoPos

    def getActive(self):
        return self.active

    def getOffsetDeg(self):
        return (self.offset-1500)/11.1111111

    def getOffsetuS(self):
        return self.offset

    def setOffset(self,timing=None,deg=None):
        if timing != None:
            self.offset = timing
        if deg != None:
            self.offset = int(float(deg)*11.1111111)

    def reset(self):
        self.setPos(timing=1500)
        self.move()

    def kill(self):
        self.active = False
        toSend = "#%dL\r"%(self.servoNum)
        self.serHandler.sendQueue.append(toSend)
        if debug: print "Sending command #%dL to queue"%self.servoNum

    def move(self):
        if self.active:
            servoPos = self.servoPos+self.offset
            # Auto-correct the output to bound within 500uS to 2500uS signals, the limits of the servos
            if servoPos < 500:
                servoPos = 500
            if servoPos > 2500:
                servoPos = 2500
                
            # Debug message if needed
            if debug: print "Sending command #%dP%dT0 to queue"%(self.servoNum,int(servoPos))

            # Send the message the serial handler in a thread-safe manner
            toSend = "#%dP%.4dT0\r"%(self.servoNum,int(servoPos))
            self.serHandler.sendQueue.append(toSend)
        else:
            try:
                toSend = "#%.4dL\r"%(self.servoNum,int(servoPos))
                self.serHandler.sendQueue.append(toSend)
                if debug: print "Sending command #%dL to queue"%self.servoNum
            except:
                pass

class dummySer():
    def __init__(self):
        self.writable = True
        print "I'm not really connected...but let's pretend"
    
    def open(self):
        pass
        
    def close(self):
        pass
        
    def write(self, cmd):
        print cmd
        #should make this englis, i.e: FR hip 30 deg
    
    def readline():
        return ""
        
    def flush():
        pass

class Controller:
    def __init__(self,servos=32):
        self.serialHandler = serHandler()
        timeout = time.time()
        while not (self.serialHandler.serOpen or (time.time()-timeout > 10.0)):
            time.sleep(0.01)
        if self.serialHandler.serOpen == False:
            print "Connection to Servotor failed. No robot movement will occur."
        print "Initializing servos."
        self.servos = {}
        for i in range(32):
            self.servos[i]=Servo(i,serHandler=self.serialHandler)
            self.servos[i].kill()

        print "Servos initialized."

    def __del__(self):
        del self.serialHandler

    def killAll(self):
        if self.serialHandler.serOpen:
            for servo in self.servos:
                self.servos[servo].kill()
        print "Killing all servos."

if __name__ == '__main__':
    pass
    conn = Controller()
    conn.servos[1].setPos(deg=30)
    conn.servos[2].setPos(deg=60)
    print conn.serialHandler.sendQueue
    while len(conn.serialHandler.sendQueue) >0:
        conn.serialHandler.sendCommand()
        

