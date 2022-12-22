#It is very important to have a Folder named "Fotos" with the "frog.png" in it!
import guizero as gz

def start_modus():
    if mode.value == "Multi Player Mode":
        if tb11.value != "Please enter a name for your character.":
            name_player = tb11.value
            error_box.visible = False
            box1.visible = False
            box12.visible = False
            picture = gz.Picture(box2, image="Fotos/frog.png") #Change the path if necessary
            box2.bg = "green"
        else:
            error_box.visible = True
            error_msg.value = "Please enter a name!"

    else:
        if tb11.value != "Please enter a name for Player 1.":
            name_player1 = tb11.value
            error_box.visible = False
        else:
            error_box.visible = True
            error_msg.value = "Please enter a name for Player 1!\n"
        if tb12.value != "Please enter a name for Player 2.":
            name_player2 = tb12.value
            error_box.visible = False
        else:
            error_box.visible = True
            error_msg.value += "Please enter a name for Player 2!"

def change_modus():
    if mode.value == "Multi Player Mode":
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

app = gz.App(title="Startbildschirm Schmico")
window = gz.Window(app,"test")

#Boxen erstellen um sichtbar / nicht sichtbar machen
box0 = gz.Box(window,  align= "top", height="fill", width="fill")
box1 = gz.Box(box0,  align= "top", height="fill", width="fill")
box2 = gz.Box(box0,  align= "top", height="fill", width="fill")

tx1 = gz.Text(box1, text="Wilkommen bei Projekt Schmico, dem ein wenig besseren Mühlespiel.")                                           #Starttext
tx2 = gz.Text(box1, text="Bitte wählen Sie ein Modi.")
mode = gz.ButtonGroup(box1,options=["Single Player Mode", "Multi Player Mode"], align= "top", horizontal=True, command=change_modus)    #Modus selektieren
box10 = gz.Box(box1,  align= "top", height=100, width="fill", layout="grid")
box11 = gz.Box(box10,  grid=[0, 0], height=25, width=100, align="top")
box12 = gz.Box(box10,  grid=[0, 1], height=25, width=100)
tb11 = gz.TextBox(box10, text="Please enter a name for Player 1.", grid=[1, 0], height=50, width=300)
tb12 = gz.TextBox(box10, text="Please enter a name for Player 2.", grid=[1, 1], height=50, width=300)
pb1 = gz.PushButton(box1, text="Start", align= "top", command=start_modus)                                                               #Start button
error_box = gz.Box(box1, align= "top", height=50, width="fill")

#Texts
tx11 = gz.Text(box11, text="Player 1:")
tx12 = gz.Text(box12, text="Player 2:")
error_msg = gz.Text(error_box, text="", color= "red")
#Change Colors
box0.bg = "orchid"
tb11.text_color = "medium blue"
tb12.text_color = "medium blue"

app.display()
