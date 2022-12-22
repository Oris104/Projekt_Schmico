import serial
import pickle
from guizero import PushButton as PB
from  guizero import App as AP

#app =  AP("test")
#Tlist=[]
#Blist=[]
#for i in range(0,8):
#    Tlist.append(PB(app,"test"))
#for i in range (0,8,1):
#    Blist.append([i])


#test = pickle.dumps(Blist)

#test1 = pickle.loads(test)
#for item in test1:
#    x =test1.index(item)
#    Tlist[x].text=item[0]
#for item in Tlist:
#    print(item.text)
import serial.tools.list_ports
ports = []
for port in serial.tools.list_ports.comports():
    ports.append(port.name)
print(ports)