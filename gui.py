from tkinter import *
from tkinter import ttk
from socket import socket

PLACEHOLDER_TEXT = "Enter PIN"
INVALID_PIN = "Invalid PIN!"

class houseGUI:

    def __init__(self):
        self.root = Tk()
        self.root.geometry("1080x720ss")
        self.root.title("Alarm")
        # self.root.attributes('-fullscreen', True)

        i = 0
        while(i < 8):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)
            i += 1


        self.make_layout()

    def make_layout(self):
        """"
        Puts all the widgets in the grid and binds the functions to the correct actions
        """

        #? NOTE: all variables which are self.sth are that way on purpose, because 
        #? we need to access that data in the start simulation function

        #? pin entry widget
        pin_entry_frame = Frame(self.root)
        self.pin_entry_txt = StringVar()
        self.pin_entry_txt.set(PLACEHOLDER_TEXT)
        pin_entry = ttk.Entry(pin_entry_frame, textvariable = self.pin_entry_txt)
        pin_entry.pack(side=TOP, fill = BOTH, expand = TRUE)
        pin_entry_frame.pack(side=TOP, fill = BOTH, expand = TRUE)
        
        #? entry button widgets
        
        btn123_frame = Frame(self.root)
        btn123_frame.pack(side=TOP, fill = BOTH, expand = TRUE)

        btn1 = ttk.Button(btn123_frame, text = "1", command = lambda: self.input(1))
        btn1.pack(side = LEFT, fill = BOTH, expand = TRUE)

        btn2 = ttk.Button(btn123_frame, text = "2", command = lambda: self.input(2))
        btn2.pack(side = LEFT, fill = BOTH, expand = TRUE)
        
        btn3 = ttk.Button(btn123_frame, text = "3", command = lambda: self.input(3))
        btn3.pack(side = LEFT, fill = BOTH, expand = TRUE)

        btn456_frame = Frame(self.root)
        btn456_frame.pack(side=TOP, fill = BOTH, expand = TRUE)

        btn4 = ttk.Button(btn456_frame, text = "4", command = lambda: self.input(4))
        btn4.pack(side = LEFT, fill = BOTH, expand = TRUE)
        
        btn5 = ttk.Button(btn456_frame, text = "5", command = lambda: self.input(5))
        btn5.pack(side = LEFT, fill = BOTH, expand = TRUE)
        
        btn6 = ttk.Button(btn456_frame, text = "6", command = lambda: self.input(6))
        btn6.pack(side = LEFT, fill = BOTH, expand = TRUE)

        btn789_frame = Frame(self.root)
        btn789_frame.pack(side=TOP, fill = BOTH, expand = TRUE)

        btn6 = ttk.Button(btn789_frame, text = "6", command = lambda: self.input(6))
        btn6.pack(side = LEFT, fill = BOTH, expand = TRUE)
        
        btn8 = ttk.Button(btn789_frame, text = "8", command = lambda: self.input(8))
        btn8.pack(side = LEFT, fill = BOTH, expand = TRUE)
        
        btn9 = ttk.Button(btn789_frame, text = "9", command = lambda: self.input(9))
        btn9.pack(side = LEFT, fill = BOTH, expand = TRUE)
                
        bottom_frame = Frame(self.root)
        bottom_frame.pack(side=TOP, fill = BOTH, expand = TRUE)

        #? lock button widget
        lock_button = ttk.Button(bottom_frame, text = "Lock", command = self.lock)        
        lock_button.pack(side = LEFT, fill = BOTH, expand = TRUE)

        btn0 = ttk.Button(bottom_frame, text = "0", command = lambda: self.input(0))
        btn0.pack(side = LEFT, fill = BOTH, expand = TRUE)

        #? unlock button widget
        unlock_button = ttk.Button(bottom_frame, text = "Unlock", command = self.unlock)
        unlock_button.pack(side = LEFT, fill = BOTH, expand = TRUE)

    def run(self):
        self.root.mainloop()
    
    
    def send_control_packet(mode):
        """
        Sends the control packet to raspberry. Packet contains the pin and mode for the alarm
        """
        pin = self.pin_entry_txt.get()
        str_packet = "alarm " + mode + " " + pin + "\r\n"
        packet = str_packet.encode("ascii")

        soc = socket()
        soc.connect(("localhost", 1546))
        soc.send(packet)
        soc.close()

    def lock(self):
        """
        """
        print("lock")

        self.send_control_packet("arm")
    
    def unlock(self):
        """
        """
        print("unlock")
        self.send_control_packet("disarm")
    
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
    