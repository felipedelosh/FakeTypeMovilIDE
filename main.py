"""
FelipedelosH

This is a fake witer to Tik Tok videos (Personal USE)
This is a simulator of type.

Open a fake ide in 16:9 and all code in file: program.txt is type in the velocity
"""
from tkinter import *
from time import sleep

class Software:
    def __init__(self) -> None:
        self.screem = Tk()
        self._max_x = 540 # width
        self._max_y = 700 # Heigth
        self.canvas = Canvas(self.screem, height=self._max_y, width=self._max_x-6, bg="gray14")
        
        
        # Vars
        self.fake_program_title = ""
        self.fake_program_code = ""
        self.openProgram()
        self.velocity_of_type = 100
        self.counter_type_line = 0 # What line the program write currently
        self.counter_letter_type = 0 # What letter need insert in screem
        self.counter_currenty_type_pos_x = 1 # The pos x to insert letter
        self._setConfiguration()

        
        self.viewAndRun()


    def viewAndRun(self):
        self.screem.title("Fake IDE writer bu loko v1.0")
        self.screem.geometry(str(self._max_x)+"x"+str(self._max_y))

        self.canvas.place(x=0, y=0)

        # Main banner
        self.canvas.create_rectangle(0, 0, self._max_x, self._max_y*0.08, fill="gray10")
        # Left line number banner
        self.canvas.create_rectangle(0, self._max_y*0.08, self._max_x*0.06, self._max_y, fill="gray12")
        # Tree lines of menu
        self.canvas.create_line(self._max_x*0.02, self._max_y*0.03,self._max_x*0.06,self._max_y*0.03, fill="white")
        self.canvas.create_line(self._max_x*0.02, self._max_y*0.04,self._max_x*0.06,self._max_y*0.04, fill="white")
        self.canvas.create_line(self._max_x*0.02, self._max_y*0.05,self._max_x*0.06,self._max_y*0.05, fill="white")
        # Title of program
        self.canvas.create_text(self._max_x*0.2, self._max_y*0.04, text=self.fake_program_title, fill="red")
        # Tree poins
        self.canvas.create_line(self._max_x*0.9, self._max_y*0.03,self._max_x*0.905,self._max_y*0.03, fill="white")
        self.canvas.create_line(self._max_x*0.9, self._max_y*0.04,self._max_x*0.905,self._max_y*0.04, fill="white")
        self.canvas.create_line(self._max_x*0.9, self._max_y*0.05,self._max_x*0.905,self._max_y*0.05, fill="white")

        self.paitLineNUmber()

        self.screem.after(90, self.typePrgram)
        self.screem.mainloop()


    def paitLineNUmber(self):
        for i in range(1, 31):
            _yk = (self._max_y * 0.08) + (i*20)
            self.canvas.create_text(self._max_x*0.03, _yk, text=str(i), fill="white")


    def typePrgram(self):
        
        if self.counter_letter_type < len(self.fake_program_code)-1:
            chr_to_type = self.fake_program_code[self.counter_letter_type]
            
            if chr_to_type == "\n":
                self.counter_type_line = self.counter_type_line + 1
                self.counter_currenty_type_pos_x = 0
                
            
            if chr_to_type != "\n":
                _xk = (self._max_x * 0.07) + (self.counter_currenty_type_pos_x*8)
                _yk = (self._max_y * 0.08) + (self.counter_type_line * 20) + 20
                self.canvas.create_text(_xk, _yk, text=chr_to_type, fill="white")

            self.counter_letter_type = self.counter_letter_type + 1
            self.counter_currenty_type_pos_x = self.counter_currenty_type_pos_x + 1
            


        self.screem.after(self.velocity_of_type, self.typePrgram)



    def openProgram(self):
        try:
            f = open('program.txt', 'r', encoding="UTF-8")
            self.fake_program_code = f.read()
            f.close()
        except:
            self.fake_program_code = "Nothing TO DO .l.."

    def _setConfiguration(self):
        try:
            f = open('config.txt', 'r', encoding="UTF-8")
            for i in f.read().split("\n"):
                data = i.split("=")
                if data[0] == "_max_x" :
                    self._max_x = int(data[1])

                if data[0] == "_max_y" :
                    self._max_y = int(data[1])

                if data[0] == "fake_program_title" :
                    self.fake_program_title = data[1]

                if data[0] == "velocity_of_type" :
                    self.velocity_of_type = int(data[1])

            f.close()
        except:
            print("Error load Config")


s = Software()
