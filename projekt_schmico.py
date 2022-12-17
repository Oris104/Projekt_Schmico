# Projekt Schmico
import guizero as gz

#variabeln
mode = "Single Player Mode"     #or "Multi Player mode"
color_standart = "blue"         #standart farbe für spielsteine des spielfelds
color_player1 = "green"         #standart farbe für spielsteine des spielers 1
color_player2 = "red"           #standart farbe für spielsteine des spielers 2
turn = 1                        #varable die deklariert wer am zug ist (spieler 1 oder spieler 2)
error_msg = ""                  #falls eine fehlermeldung eingeblendet werden soll -> hier einfügen
flg = True                      #Wird auf True gesetzt beim ersten durchlauf
muehle_stage = "setzen"         #steine setzen, fortgeschritten steinen fahren
snake = 0                       #zähler wie viele steine die spieler noch übrig haben
frosch = 0                      #zähler wie viele steine die spieler noch übrig haben

Dict={                          #Dict welche felder buttons werden
0:[0,6,12],
2:[2,6,10],
4:[4,6,8],
6:[0,2,4,8,10,12],
8:[4,6,8],
10:[2,6,10],
12:[0,6,12],
1:[-1],
3:[-1],
5:[-1],
7:[-1],
9:[-1],
11:[-1]
}
Line={                          #Dict welche Felder eine linie benötigen
0:[-1],
1:[0, 6, 12],
2:[0, 12],
3:[0, 2, 6, 10, 12],
4:[0, 2, 10, 12],
5:[0, 2, 4, 8, 10, 12],
6:[-1],
7:[0, 2, 4, 8, 10, 12],
8:[0, 2, 10, 12],
9:[0, 2, 6, 10, 12],
10:[0, 12],
11:[0, 6, 12],
12:[-1]
}


#Funktionen
def change_colors(but):
    global turn
    global flg
    global error_msg
    global color_standart
    global color_player1
    global color_player2
    global muehle_stage
    global snake
    global frosch


    if turn == 1:
        player1.border = 2
        player2.border = False
        turn = 2

        text_player1.value=">"+text_player1.value
        if flg:
            flg= False
        else:
            text_player2.value=text_player2.value[1:]

        if muehle_stage == "setzen":
            if but.bg==color_standart:
                 but.bg = color_player1
            else:
                 but.bg=color_standart
                 turn = 0
            if snake < 9:
                player_anzeige1[snake].bg = "purple"
                snake = snake + 1
        else:
            if but.bg==color_standart:
                 but.bg = color_player1
            else:
                 but.bg=color_standart
                 turn = 1
            if snake < 0:
                player_anzeige2[snake].bg = "black"
                snake = snake - 1

    else:
        player1.border = False
        player2.border = 2
        turn = 1
        text_player2.value=">"+text_player2.value
        text_player1.value=text_player1.value[1:]

        if muehle_stage == "setzen":
            if but.bg==color_standart:
                 but.bg = color_player2
            else:
                 but.bg=color_standart
                 turn = 1
            if frosch < 9:
                player_anzeige2[frosch].bg = "purple"
                frosch = frosch + 1
        else:
            if but.bg==color_standart:
                 but.bg = color_player2
            else:
                 but.bg=color_standart
                 turn = 2
            if frosch > 0:
                player_anzeige1[frosch].bg = "black"
                frosch = frosch - 1

        if frosch < 9:
            player_anzeige2[frosch].bg = "black"
            frosch = frosch + 1
        else:
            muehle_stage = 1


app = gz.App(title="Programm Schmico")

titel0 = gz.Box(app, align="top", width="fill")
text_titel = gz.Text(titel0, text=f"Programm Schmico: {mode}", align="top", width=750)

#Spielfeld initialisieren
spielfeld = gz.Box(app, layout="grid", align="top", height="fill", width="fill")
spielfeld.bg = "white"

BoxListB = []
BoxListW =[]
BList = []
for x in range (0,13):
      for y in range(0,13):
              if y in Dict[x]:
                     BoxListB.append(gz.Box(spielfeld, grid=[x,y],width =25,height=25))
              else:
                    BoxListW.append(gz.Box(spielfeld, grid=[x,y],width =25,height=25))
                    if y in Line[x]:
                        d = gz.Drawing(BoxListW[-1])
                        d.line(0, 12, 25, 12, color="black", width=2)
                    else:
                        if x in Line[y]:
                            d = gz.Drawing(BoxListW[-1])
                            d.line(12, 0, 12, 25, color="black", width=2)
for item in BoxListB:
      item.bg = color_standart
      BList.append(gz.PushButton(item, text="", width="fill", height="fill"))
for item in BoxListW:
      item.bg = "white"
for item in BList:
    item.update_command(change_colors,args=[item])

error_box = gz.Box(app, align="bottom", width="fill", height=27)

player_box2 = gz.Box(app, align="bottom", width="fill", height=27, layout = "grid")
player2 = gz.Box(player_box2, grid = [0,0], width=125, height=25)
anzeige2 = gz.Box(player_box2, grid = [1,0], width=300, height=25, layout = "grid")
player2.bg = color_player2

player_box1 = gz.Box(app, align="bottom", width="fill", height=27, layout = "grid")
player1 = gz.Box(player_box1, grid = [0,0], width=125, height=25)
anzeige1 = gz.Box(player_box1, grid = [1,0], width=300, height=25, layout = "grid")
player1.bg = color_player1

text_player1 = gz.Text(player1, text="Player 1: ", align="top")
text_player2 = gz.Text(player2, text="Player 2: ", align="top")
text_error = gz.Text(error_box, text=f"Error: {error_msg}", align="top")

#Anzeige
player_anzeige1 = []
player_anzeige2 = []
for x in range (0,9):
    player_anzeige1.append(gz.Box(anzeige1, grid=[x+1, 0], width = 25, height=25))
    player_anzeige2.append(gz.Box(anzeige2, grid=[x+1, 0], width = 25, height=25))
for item in player_anzeige1:
      item.bg = "white"
      item.border = 1
for item in player_anzeige2:
      item.bg = "white"
      item.border = 1





app.display()
