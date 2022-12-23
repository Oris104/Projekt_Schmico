# Projekt Schmico

from serial.tools import list_ports
import guizero as gz
import CustomButton as CB
import serial
import pickle
import time
# variabeln
mode = "Single Player Mode"  # or "Multi Player mode"
color_standart = "blue"  # standart farbe für spielsteine des spielfelds
color_player1 = "green"  # standart farbe für spielsteine des spielers 1
color_player2 = "red"  # standart farbe für spielsteine des spielers 2
turn = 1  # varable die deklariert, wer am zug ist (spieler 1 oder spieler 2)
error_msg = ""  # falls eine fehlermeldung eingeblendet werden soll > hier einfügen
flg = 1  # Wird auf True gesetzt beim ersten durchlauf
muehle_stage = "setzen"  # steine setzen, fortgeschritten steinen fahren
snake = 0  # zähler wie viele steine die spieler noch übrig haben
frosch = 0  # zähler wie viele steine die spieler noch übrig haben
sxy = []
p1mov = 1
p2mov = 1
selectedButton = False
JumpToken = False
removestonep1 = False
removestonep2 = False
jsSelec = False
maxtkk=5
p1name="lmao"
p2name="LamO"
hasconfirmed=False

isP1=True
MUltipl = False
mpnAme =""



Dict = {  # Dict welche felder buttons werden
    0: [0, 6, 12],
    2: [2, 6, 10],
    4: [4, 6, 8],
    6: [0, 2, 4, 8, 10, 12],
    8: [4, 6, 8],
    10: [2, 6, 10],
    12: [0, 6, 12],
    1: [-1],
    3: [-1],
    5: [-1],
    7: [-1],
    9: [-1],
    11: [-1]
}
Line = {  # Dict welche Felder eine linie benötigen
    0: [-1],
    1: [0, 6, 12],
    2: [0, 12],
    3: [0, 2, 6, 10, 12],
    4: [0, 2, 10, 12],
    5: [0, 2, 4, 8, 10, 12],
    6: [-1],
    7: [0, 2, 4, 8, 10, 12],
    8: [0, 2, 10, 12],
    9: [0, 2, 6, 10, 12],
    10: [0, 12],
    11: [0, 6, 12],
    12: [-1]
}


class Player():
    def __init__(self, name,maxtk):
        self.name = name
        self.tokens = maxtk
        self.tokensbord = 0

    def looseToken(self):
        self.tokens += -1
        self.tokensbord += -1

    def placeToken(self):
        self.tokensbord += 1

    def movecor(self):
        self.tokensbord -= 1


def canSLide(t1, t2):
    global BList
    global MList
    for item in MList:
        if t1 in item and t2 in item and abs(item.index(t1) - item.index(t2)) <= 1:
            return True

    return False


# Funktionen
def change_colors(but):
    global sxy
    global p1mov
    global p2mov
    global selectedButton
    global JumpToken
    global removestonep1
    global removestonep2
    global jsSelec
    if (p1.tokens > p1.tokensbord and turn == 1) or (p2.tokens > p2.tokensbord and turn == 2):
        if turn == 1 and but.state == 0 and not removestonep1:
            if selectedButton and not p1mov:
                selectedButton.state = 0
                selectedButton.uPdate_color()
            but.state = 3
            p1mov = 0
            selectedButton = but
        elif turn == 2 and but.state == 0 and not removestonep2:
            if selectedButton and not p2mov:
                selectedButton.state = 0
                selectedButton.uPdate_color()
            but.state = 4
            p2mov = 0
            selectedButton = but
    elif (p1.tokensbord == p1.tokens and turn == 1 and p1.tokens > 3) or (
            p2.tokens == p2.tokensbord and turn == 2 and p2.tokens > 3):
        if turn == 1 and but.state == 1 and not removestonep1:
            jsSelec = True
            but.state = 5
            if JumpToken:
                JumpToken.state = 1
                JumpToken.uPdate_color()
                selectedButton.state = 0
                selectedButton.uPdate_color()
            JumpToken = but
            p1mov = 1
        elif turn == 2 and but.state == 2 and not removestonep2:
            jsSelec = True
            but.state = 6
            if JumpToken:
                JumpToken.state = 2
                JumpToken.uPdate_color()
                selectedButton.state = 0
                selectedButton.uPdate_color()
            JumpToken = but
            p2mov = 1
        if turn == 1 and but.state == 0 and jsSelec and canSLide(but, JumpToken) and not removestonep1:
            but.state = 3
            selectedButton = but
            p1mov = 0
        elif turn == 2 and but.state == 0 and jsSelec and canSLide(but, JumpToken) and not removestonep1:
            but.state = 4
            p2mov = 0
            selectedButton = but
    elif (p1.tokensbord == p1.tokens and turn == 1) or (p2.tokens == p2.tokensbord and turn == 2):
        if turn == 1 and but.state == 1 and not removestonep1:
            jsSelec = True
            but.state = 5
            if JumpToken:
                JumpToken.state = 1
                JumpToken.uPdate_color()
                selectedButton.state = 0
                selectedButton.uPdate_color()
            JumpToken = but
            p1mov = 1
        elif turn == 2 and but.state == 2 and not removestonep2:
            jsSelec = True
            but.state = 6
            if JumpToken:
                JumpToken.state = 2
                JumpToken.uPdate_color()
                selectedButton.state=0
                selectedButton.uPdate_color()
            JumpToken = but
            p2mov = 1
        if turn == 1 and but.state == 0 and jsSelec and not removestonep1:
            but.state = 3
            if selectedButton:
                selectedButton.state=0
                selectedButton.uPdate_color()
            selectedButton = but
            p1mov = 0
        elif turn == 2 and but.state == 0 and jsSelec and not removestonep1:
            but.state = 4
            if selectedButton:
                selectedButton.state = 0
                selectedButton.uPdate_color()
            p2mov = 0
            selectedButton = but

    if turn == 1 and but.state == 2 and removestonep1 and canRemove(but):
        if selectedButton:
            selectedButton.state = 2
            selectedButton.uPdate_color()
        selectedButton = but
        but.state = 4
        p1mov = 0
    elif turn == 2 and but.state == 1 and removestonep2 and canRemove(but):
        if selectedButton:
            selectedButton.state = 1
            selectedButton.uPdate_color()
        selectedButton = but
        but.state = 3
        p2mov = 0

    but.uPdate_color()


def confirm():
    global turn
    global flg
    global selectedButton
    global p1mov
    global p2mov
    global MList
    global BList
    global removestonep1
    global removestonep2
    global JumpToken
    global MUltipl
    scoreCHeck = False
    if selectedButton:
        for item in BList:
            if item.state == 3 and not removestonep2:
                item.state = 1
                p1.placeToken()
            elif removestonep2 and item.state == 3:
                item.state = 0
                p1.looseToken()
                removestonep2 = False
            if item.state == 4 and not removestonep1:
                item.state = 2
                p2.placeToken()
            elif removestonep1 and item.state == 4:
                item.state = 0
                removestonep1 = False
                p2.looseToken()
            if item.state == 5:
                item.state = 0
                p1.movecor()
            elif item.state == 6:
                item.state = 0
                p2.movecor()
            item.uPdate_color()
        for itemm in MList:
            if itemm.CheckiScore():
                scoreCHeck = True
        if scoreCHeck:
            selectedButton = False
            if turn == 1:
                p1mov = 1
                removestonep1 = True
            elif turn == 2:
                p2mov = 1
                removestonep2 = True
        elif (p1mov == 0 or p2mov == 0 )and not MUltipl:

            if turn == 1:
                turnindiChanger(p1, p2)
                p1mov = 1
                turn = 2
            else:
                turnindiChanger(p1, p2)
                p2mov = 1
                turn = 1
            selectedButton = False
        elif p1mov == 0 or p2mov == 0:
            if turn == 1:
                turnindiChanger(p1, p2)
                writes("P2T".encode())
                time.sleep(0.5)
                writes(pIckler(BList))
                while not reads(False).decode()=="P1T":
                    pass
                while reads(False).decode()=="P1T":
                    time.sleep(0.5)
                unpickler(reads(False),BList)
                p1mov=1
            else:
                turnindiChanger(p1, p2)
                turn=1
                writes("P1T".encode())
                time.sleep(0.5)
                writes(pIckler(BList))
                while not reads(False).decode()=="P2T":
                    pass
                while reads(False).decode() =="P2T":
                    time.sleep(0.5)
                unpickler(reads(False), BList)
                turn = 2
                p2mov=1
        flg = 0

    JumpToken = False
    if p1.tokens<=2:
        print("p2 wins")
        app.destroy()
    if p2.tokens<=2:
        print("p1 wins")
        app.destroy()


def turnindiChanger(snake, frosch):
    global p1rem,p2rem
    global selectedButton
    global turn

    fla = True
    while(fla):
        if len(player_anzeige1)>p1.tokens:
            player_anzeige1[0].destroy()
            player_anzeige1.pop(0)
        if len(player_anzeige2)>p2.tokens:
            player_anzeige2[0].destroy()
            player_anzeige2.pop(0)
        if len(player_anzeige1)==p1.tokens and len(player_anzeige2)==p2.tokens:
            fla=False
    if turn == 1:

        text_player1.value = text_player1.value[1:]
        text_player2.value = ">" + text_player2.value
        player1.border = False
        player2.border = 2
        if selectedButton:
            if snake.tokensbord <= snake.tokens:
                player_anzeige1[snake.tokensbord - 1].bg = "purple"
            selectedButton = False
    else:
        player1.border = False
        player2.border = 2
        player1.border = 2
        player2.border = False
        text_player1.value = ">" + text_player1.value
        text_player2.value = text_player2.value[1:]
        if selectedButton:
            selectedButton = False
            if frosch.tokensbord <= frosch.tokens:
                player_anzeige2[frosch.tokensbord - 1].bg = "purple"
class mueleListe(list):
    def __init__(self, B1, B2, B3):
        super().__init__()
        self.append(B1)
        self.append(B2)
        self.append(B3)
        self.flag = False

    def CheckiScore(self):
        x = 0
        sum = []
        for item in self:
            sum.append(item.state)
        if sum[0] == 1 or sum[0] == 2:
            if all(x == sum[0] for x in sum) and not self.flag:
                self.flag = True
                return True
            elif not all(x == sum[0] for x in sum):
                self.flag = False

        else:
            self.flag = False
        return False

    def viewifinMuele(self):
        sum = []
        for item in self:
            sum.append(item.state)
        if all(x == sum[0] for x in sum):
            return True
        else:
            return False


def canRemove(butoon):
    global MList
    for item in MList:
        if butoon in item and item.viewifinMuele():
            return False
    return True

def pIckler(Blist):
    returner = []
    for item in Blist:
        returner.append(item.state)
    return pickle.dumps(returner)


def unpickler(Plist,Blist):
    for item in Plist:
        x = Plist.index(item)
        Blist[x].state = item
        Blist[x].uPdate_color()


def writes(data):
    ser = serial.Serial(getPort(),baudrate=9600,timeout=1)
    print(ser.write(data))
    ser.close()
def reads(timeo):
    ser = serial.Serial(getPort(),baudrate=9600,timeout=1)
    print(getPort())
    data=ser.readline()
    c=5
    while not data and c >0:
        data=ser.readline()
        print("read")
        if timeo:
            c+=-1
    ser.close()
    if data:
        print(data.decode())

    return  data
def nameexchanger(ownname):
    ser = serial.Serial(getPort(), baudrate=9600, timeout=1)
    noname = True
    while noname:
        ser.write((ownname+"\n").encode())
        det = ser.readline().decode()
        if det:
            noname=False
            time.sleep(2)
            ser.close()
            return det.strip()


def getPort():
    ports=[]
    for port in serial.tools.list_ports.comports():
        ports.append(port.name)
    return ports[0]
def foundPlayer():
    ser = serial.Serial(getPort(), baudrate=9600, timeout=1)
    c=5
    while c>0:
        c-=1
        det =ser.readline().decode()
        if det == "LFG\n":
            ser.write("FOUND\n".encode())
            return True
        else:

            print("no game"+det)
    ser.close()
    return False
def isLonley():
    ser = serial.Serial(getPort(), baudrate=9600, timeout=1)
    ser.write("LFG\n".encode())
    wait = True
    while wait:
        ser.write("LFG\n".encode())
        if ser.readline().decode() =="FOUND\n":
            wait=False
        else:
            print("not found")
    ser.close()


app = gz.App(title="Programm Schmico")

titel0 = gz.Box(app, align="top", width="fill")
text_titel = gz.Text(titel0, text=f"Programm Schmico: {mode}", align="top", width=750)

# Spielfeld initialisieren
spielfeld = gz.Box(app, layout="grid", align="top", height="fill", width="fill")
spielfeld.bg = "white"

BoxListB = []
BoxListW = []
BList = []
MList = []
for x in range(0, 13):
    for y in range(0, 13):
        if y in Dict[x]:
            BoxListB.append(gz.Box(spielfeld, grid=[x, y], width=25, height=25))
        else:
            BoxListW.append(gz.Box(spielfeld, grid=[x, y], width=25, height=25))
            if y in Line[x]:
                d = gz.Drawing(BoxListW[-1])
                d.line(0, 12, 25, 12, color="black", width=2)
            else:
                if x in Line[y]:
                    d = gz.Drawing(BoxListW[-1])
                    d.line(12, 0, 12, 25, color="black", width=2)

for item in BoxListB:
    BList.append(CB.cButton(item, item.grid), )
for item in BoxListW:
    item.bg = "white"
for item in BList:
    item.update_command(change_colors, args=[item])
    item.uPdate_color()

dcount = 0
mcounter = 3
b1 = False
b2 = False
b3 = False

for item in BList:
    if mcounter == 3:
        b1 = item
        mcounter -= 1
    elif mcounter == 2:
        b2 = item
        mcounter -= 1
    elif mcounter == 1:
        b3 = item
        mcounter -= 1
        mcounter = 3
        MList.append(mueleListe(b1, b2, b3))
        b1 = False
        b2 = False
        b3 = False

MList.append(mueleListe(BList[0], BList[9], BList[21], ))
MList.append(mueleListe(BList[3], BList[10], BList[18], ))
MList.append(mueleListe(BList[6], BList[11], BList[15], ))
MList.append(mueleListe(BList[1], BList[4], BList[7], ))
MList.append(mueleListe(BList[16], BList[19], BList[22], ))
MList.append(mueleListe(BList[8], BList[12], BList[17], ))
MList.append(mueleListe(BList[5], BList[13], BList[20], ))
MList.append(mueleListe(BList[2], BList[14], BList[23], ))

for item in MList:
    for thing in item:
        thing.text += str(dcount)
    dcount += 1

error_box = gz.Box(app, align="bottom", width="fill", height=27)

player_box2 = gz.Box(app, align="bottom", width="fill", height=27, layout="grid")
player2 = gz.Box(player_box2, grid=[0, 0], width=125, height=25)
anzeige2 = gz.Box(player_box2, grid=[1, 0], width=300, height=25, layout="grid")
player2.bg = color_player2

player_box1 = gz.Box(app, align="bottom", width="fill", height=27, layout="grid")
player1 = gz.Box(player_box1, grid=[0, 0], width=125, height=25)
anzeige1 = gz.Box(player_box1, grid=[1, 0], width=300, height=25, layout="grid")
player1.bg = color_player1

text_player1 = gz.Text(player1, text=p1name+": ", align="top")
text_player2 = gz.Text(player2, text=p2name+": ", align="top")
text_error = gz.Text(error_box, text=f"Error: {error_msg}", align="top")

sbutonBox = gz.Box(app, width=60, height=60, align="right")
ConfirmButton = gz.PushButton(sbutonBox, width="fill", height="fill", command=confirm, text="Confirm")
text_player1.value = ">" + text_player1.value

player1.border = 2
player2.border = False



# Anzeige
player_anzeige1 = []
player_anzeige2 = []
for x in range(0, 9):
    player_anzeige1.append(gz.Box(anzeige1, grid=[x + 1, 0], width=25, height=25))
    player_anzeige2.append(gz.Box(anzeige2, grid=[x + 1, 0], width=25, height=25))
for item in player_anzeige1:
    item.bg = "white"
    item.border = 1
for item in player_anzeige2:
    item.bg = "white"
    item.border = 1




def start_modus():
    global p1name,p2name,mpnAme,MUltipl,isP1,turn
    global p1mov,p2mov,hasconfirmed,selectedButton
    f1=False
    f2=False
    if int(mode.value) ==1:
        if tb11.value != "Please enter a name for your character.":
            mpnAme = str(tb11.value)
            error_box.visible = False
            box1.visible = False
            box12.visible = False
            picture = gz.Picture(box2, image="frog.png") #Change the path if necessary
            box2.bg = "green"

            hasconfirmed=True
        else:
            error_box.visible = True
            error_msg.value = "Please enter a name!"

    else:
        if tb11.value != "Please enter a name for Player 1.":
            p1name = str(tb11.value)
            error_box.visible = False
            f1=True
        else:
            error_box.visible = True
            error_msg.value = "Please enter a name for Player 1!\n"
        if tb12.value != "Please enter a name for Player 2.":
            p2name = str(tb12.value)
            error_box.visible = False
            f2=True
        else:
            error_box.visible = True
            error_msg.value += "Please enter a name for Player 2!"
    if f1 and f2:
        hasconfirmed=True
    MUltipl=int(mode.value)
    if hasconfirmed:

        if MUltipl:


            finded=foundPlayer()
            if finded:

                p1name=nameexchanger(mpnAme)

                p2name = mpnAme
                isP1=False
                turn=2
                p2mov=0
                p1mov=0
                selectedButton=True
                confirm()
            else:
                #app.display()
                isLonley()

                p2name=nameexchanger(mpnAme)
                p1name=mpnAme
        window.destroy()
        text_player1.value = p1name + ": "
        text_player2.value = p2name + ": "


def change_modus():
    if int(mode.value) == 1:
        tx11.value = "Name:"
        tb11.value = "Please enter a name for your character."
        tb12.visible = False
        box12.visible = False
        #colors
        box0.bg = "medium spring green"
        tb11.text_color = "medium violet red"
    else:
        tx11.value = "Player 1:"
        tb11.value = "Please enter a name for Player 1."
        tb12.visible = True
        box12.visible = True
        tb12.value = "Please enter a name for Player 2."
        #colors
        box0.bg = "orchid"
        tb11.text_color = "medium blue"
        tb12.text_color = "medium blue"


window = gz.Window(app,"Menu")

#Boxen erstellen um sichtbar / nicht sichtbar machen
box0 = gz.Box(window,  align= "top", height="fill", width="fill")
box1 = gz.Box(box0,  align= "top", height="fill", width="fill")
box2 = gz.Box(box0,  align= "top", height="fill", width="fill")

tx1 = gz.Text(box1, text="Wilkommen bei Projekt Schmico, dem ein wenig besseren Mühlespiel.")                                           #Starttext
tx2 = gz.Text(box1, text="Bitte wählen Sie ein Modi.")
mode = gz.ButtonGroup(box1,options=[["Single Player Mode",0], ["Multi Player Mode",1]], align= "top", horizontal=True, command=change_modus)    #Modus selektieren
box10 = gz.Box(box1,  align= "top", height=100, width="fill", layout="grid")
box11 = gz.Box(box10,  grid=[0, 0], height=25, width=100, align="top")
box12 = gz.Box(box10,  grid=[0, 1], height=25, width=100)
tb11 = gz.TextBox(box10, text="Please enter a name for Player 1.", grid=[1, 0], height=50, width=300)
tb12 = gz.TextBox(box10, text="Please enter a name for Player 2.", grid=[1, 1], height=50, width=300)
pb1 = gz.PushButton(box1, text="Start", align= "top")                                                               #Start button
error_box = gz.Box(box1, align= "top", height=50, width="fill")
pb1.update_command(start_modus)
#Texts
tx11 = gz.Text(box11, text="P1 Name")
tx12 = gz.Text(box12, text="P2 Name")
error_msg = gz.Text(error_box, text="", color= "red")
#Change Colors
box0.bg = "orchid"
tb11.text_color = "medium blue"
tb12.text_color = "medium blue"
waiting = gz.Text(window, visible=False,text="Waiting for Player")



p1 = Player("n1",   maxtkk)
p2 = Player("n2",maxtkk)






app.display()
while(not hasconfirmed):
    app.disable()
print("done")