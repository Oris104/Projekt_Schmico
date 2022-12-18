# Projekt Schmico
import guizero as gz
import CustomButton as CB

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
p1rem=9
p2rem=9


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
    def __init__(self, name):
        self.name = name
        self.tokens = 9
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
            JumpToken = but
            p1mov = 1
        elif turn == 2 and but.state == 2 and not removestonep2:
            jsSelec = True
            but.state = 6
            if JumpToken:
                JumpToken.state = 2
                JumpToken.uPdate_color()
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
            JumpToken = but
            p1mov = 1
        elif turn == 2 and but.state == 2 and not removestonep2:
            jsSelec = True
            but.state = 6
            if JumpToken:
                JumpToken.state = 2
                JumpToken.uPdate_color()
            JumpToken = but
            p2mov = 1
        if turn == 1 and but.state == 0 and jsSelec and not removestonep1:
            but.state = 3
            selectedButton = but
            p1mov = 0
        elif turn == 2 and but.state == 0 and jsSelec and not removestonep1:
            but.state = 4
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
        elif p1mov == 0 or p2mov == 0:

            if turn == 1:
                turnindiChanger(p1, p2)
                p1mov = 1
                turn = 2
            else:
                turnindiChanger(p1, p2)
                p2mov = 1
                turn = 1
            selectedButton = False
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
    if turn == 1:

        text_player1.value = text_player1.value[1:]
        text_player2.value = ">" + text_player2.value
        player1.border = False
        player2.border = 2
        if selectedButton:
            if snake.tokensbord <= 9:
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
            if frosch.tokensbord < 10:
                player_anzeige2[frosch.tokensbord - 1].bg = "purple"
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

text_player1 = gz.Text(player1, text="Player 1: ", align="top")
text_player2 = gz.Text(player2, text="Player 2: ", align="top")
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

p1 = Player("n1")
p2 = Player("n2")

app.display()
