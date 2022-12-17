import guizero as gz

class cButton(gz.PushButton):
    def __init__(self, master, state=0):
        super().__init__(master)
        self.state=state
