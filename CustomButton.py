import guizero as gz

class cButton(gz.PushButton):
    def __init__(self, master,xy, state=0):
        super().__init__(master,width="fill",height="fill",text="")
        self.state=state
        self.xy = []

        for item in xy:

            self.xy.append(item)
    def uPdate_color(self):
        match self.state:
            case 0:
                self.bg="blue"
            case 1:
                self.bg = "green"
            case 2:
                self.bg = "red"
            case 3:
                self.bg = "light green"
            case 4:
                self.bg = "pink"
            case 5:
                self.bg = "light green"
            case 6:
                self.bg = "pink"

