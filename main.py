import tkinter as tk
#if your using python 2.xx
# import Tkinter as tk
from tkinter import ttk
from comtypes.client import CreateObject
from comtypes.gen import SpeechLib
import logging
from tkinter import messagebox as mbx
"""sets up initial conversion"""


class MainApplication(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        """application configuration"""
        menu = tk.Menu()
        root.grid_rowconfigure(2, weight=2)
        style = ttk.Style()
        style.configure("TLabel", relief="raised", foreground="black", background="lightgreen")
        style.configure("TButton", foreground="grey", background="lightgreen", width=30)
        root.config(menu=menu)
        root.resizable(0, 0)
        root.title("my converter")
        root.geometry("500x200")
        menu.add_command(label="exit", command=root.quit)
        menu.add_command(label="help", command=self.showhelp)
        menu.add_command(label="about", command=self.about)
        root.configure(background="lightgreen")
        menu.configure(background="white")
        self.basic = ttk.Label(text="please click the help menubutton first you use  the application \n" )
        self.basic.pack()
        self.Linput = ttk.Label(root, text="input file", width=30)
        self.Linput.pack()
        self.inputentry = ttk.Entry(root, width=30)
        self.inputentry.pack()
        self.Loutput = ttk.Label(text="output file", width=30)
        self.Loutput.grid_rowconfigure(4, weight=2)
        self.Loutput.pack()
        self.OutputEntry = ttk.Entry(width=30)
        self.OutputEntry.pack()
        self.Lspeed = ttk.Label(text="set voice rate", width=30)
        self.Lspeed.pack() 
        self.Setrate = ttk.Entry(width=30)
        self.Setrate.pack()
        self.Convert = ttk.Button(text="convert", command=self.ConverterToAudio)
        self.Convert.pack(side="top")
        """sets up main function"""
    def ConverterToAudio(self):
        try: 
            self.engine = CreateObject("SAPI.SpVoice")
            self.stream = CreateObject("SAPI.SpFileStream")
            self.infile = self.inputentry.get()
            self.outfile = self.OutputEntry.get()
            self.stream.Open(self.outfile, SpeechLib.SSFMCreateForWrite)
            self.engine.AudioOutputStream = self.stream
            with open(self.infile, "r") as text:
                self.content = text.read()
                self.engine.rate = int(self.Setrate.get())
                self.engine.pitch =int(self.Setrate.get())
                self.engine.GetVoices("microsoft zira")
                self.engine.speak(self.content)
                self.stream.Close()
                #mbx.showinfo("output", f" conversion of {self.infile} {self.outfile}")
                mbx.showinfo("output", "conversion of {} to {}".format(self.infile, self.outfile))
        except Exception as e:
            mbx.showwarning("error", e)
      
    def showhelp(self):
        mbx.showinfo("help", "to use this application make sure you type in the file or directory you need converted in the input and output\n entries for example text.txt and\n then in the output entry do text.mp3 you can also tab to the next entry")
    def about(self):
        mbx.showinfo("about", "\n\n created by austin heisley-cook\ndate 2/1/2018")

root =  tk.Tk()
app = MainApplication()
root.mainloop()
