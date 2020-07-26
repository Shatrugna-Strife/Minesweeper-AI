import tkinter

class App(object):
    def __init__(self):
        self.tree = None
        self._setup_widgets()

    def _setup_widgets(self):
        butts = tkinter.Button(text = "add line", state="disabled")
        butts.grid()

def main():
    root = tkinter.Tk()
    app = App()
    root.mainloop()

if __name__ == "__main__":
    main()
