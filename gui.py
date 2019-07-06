from tkinter import *
from tkinter import ttk

PLACEHOLDER_TEXT = "Enter PIN"
INVALID_PIN = "Invalid PIN!"

class houseGUI:

    def __init__(self):
        self.root = Tk()
        self.root.title("Alarm")

        self.make_layout()

    def make_layout(self):
        """"
        Puts all the widgets in the grid and binds the functions to the correct actions
        """

        #? NOTE: all variables which are self.sth are that way on purpose, because 
        #? we need to access that data in the start simulation function

        #? time_period widget
        self.pin_entry_txt = StringVar()
        self.pin_entry_txt.set(PLACEHOLDER_TEXT)
        pin_entry = ttk.Entry(self.root, textvariable = self.pin_entry_txt)

        pin_entry.grid(row = 0, column = 0, columnspan = 3,  sticky = "nwse", padx = 5, pady = 5)
        
        #? entry button widgets
        btn1 = ttk.Button(self.root, text = "1", command = lambda: self.input(1))
        btn1.grid(row = 1, column = 0, sticky = "nwse", padx = 5, pady = 5)
        
        btn2 = ttk.Button(self.root, text = "2", command = lambda: self.input(2))
        btn2.grid(row = 1, column = 1, sticky = "nwse", padx = 5, pady = 5)
        
        btn3 = ttk.Button(self.root, text = "3", command = lambda: self.input(3))
        btn3.grid(row = 1, column = 2, sticky = "nwse", padx = 5, pady = 5)
        
        btn4 = ttk.Button(self.root, text = "4", command = lambda: self.input(4))
        btn4.grid(row = 2, column = 0, sticky = "nwse", padx = 5, pady = 5)
        
        btn5 = ttk.Button(self.root, text = "5", command = lambda: self.input(5))
        btn5.grid(row = 2, column = 1, sticky = "nwse", padx = 5, pady = 5)
        
        btn6 = ttk.Button(self.root, text = "6", command = lambda: self.input(6))
        btn6.grid(row = 2, column = 2, sticky = "nwse", padx = 5, pady = 5)

        btn7 = ttk.Button(self.root, text = "7", command = lambda: self.input(7))
        btn7.grid(row = 3, column = 0, sticky = "nwse", padx = 5, pady = 5)
        
        btn8 = ttk.Button(self.root, text = "8", command = lambda: self.input(8))
        btn8.grid(row = 3, column = 1, sticky = "nwse", padx = 5, pady = 5)
        
        btn9 = ttk.Button(self.root, text = "9", command = lambda: self.input(9))
        btn9.grid(row = 3, column = 2, sticky = "nwse", padx = 5, pady = 5)
        
        btn0 = ttk.Button(self.root, text = "0", command = lambda: self.input(0))
        btn0.grid(row = 4, column = 1, sticky = "nwse", padx = 5, pady = 5)
        
        #? lock button widget
        lock_button = ttk.Button(self.root, text = "Lock", command = self.lock)        
        lock_button.grid(row = 4, column = 0, sticky = "nwse", padx = 5, pady = 5)

        #? unlock button widget
        unlock_button = ttk.Button(self.root, text = "Unlock", command = self.unlock)
        unlock_button.grid(row = 4, column = 2, sticky = "nwse", padx = 5, pady = 5)

    def run(self):
        self.root.mainloop()
    
    
    def lock(self):
        """
        """

        print("Current PIN lock: ", self.pin_entry_txt.get())
    
    def unlock(self):
        """
        """
        if(self.pin_entry_txt.get() != "1234"):
            self.pin_entry_txt.set(INVALID_PIN)

        print("Current PIN unlock: ", self.pin_entry_txt.get())
    
    def input(self, num):
        """
        """
        if(self.pin_entry_txt.get() == PLACEHOLDER_TEXT or self.pin_entry_txt.get() == INVALID_PIN):
            self.pin_entry_txt.set("")
        
        entry = self.pin_entry_txt.get() + str(num)
        self.pin_entry_txt.set(entry)
        


if __name__ == "__main__":
    gui = houseGUI()
    gui.run()
    