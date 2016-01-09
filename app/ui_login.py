from Tkinter import Tk, Button, Checkbutton, Label, Entry, Frame

class UiLogin:
    def __init__(self, master):
        column0_padx = 24
        row_pady = 36

    def show(self):

        # Initialise the UI layout
        app = AppUi(root)
        root.mainloop()
        logging.debug("UI running ")
