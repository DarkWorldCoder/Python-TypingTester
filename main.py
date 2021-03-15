from tkinter import *
from time import gmtime,strftime
tk = Tk()
from words import query
import random
import wikipedia


tk.geometry(("800x600"))

tk.title("Typing Tester")

difficultList = ['EASY','MEDIUM','HARD']

class Draw:

    def __init__(self):
        self.time = 0
        self.level = 1
        self.cancel = None
        self.count = 0
        self.end = False
       
        # self.textLen = 0
        self.widgets()
       

    def start(self):
            b =self.inputArea.get("1.0",'end-1c')
           
            if len(b) == 0:
                self.cancel = tk.after(100,self.start)

            if len(b) != 0:
                self.timeStart()
                
                # print(self.textLen)
                tk.after_cancel(self.cancel)
            


    

    def lenFIle(self):
        self.inputTextLen = len(self.inputArea.get("1.0","end-1c"))
        self.inputArea.after(10,self.lenFIle)
    def timeStart(self):
        if not self.end:
            self.lenFIle()
            self.end = True
        
        self.time = self.time +1
        allTime = strftime("%M:%S",gmtime(self.time))
        self.timeLabel.config(text=f"Time: {allTime}")
        # self.textLen = len(self.text)
        if (self.inputTextLen) >= (self.textLen):
            self.textArea.after_cancel(self.cancelTime)   
            self.showResults()
            print(self.count)
        self.cancelTime = self.textArea.after(1000,self.timeStart)
        
        print(self.inputTextLen,self.textLen)
       
            
            
    def callback(self,*args):
        a = self.difficultSet.get()
        if a == "EASY":
            self.level = 1
        elif a == "MEDIUM":
            self.level = 2
        else:
            self.level = 3
        
        self.text = wikipedia.summary(query[random.randint(0,len(query)-1)],sentences=self.level)
        print(len(self.text))
        self.textLen  = len(self.text)
        self.textArea.delete('1.0','end-1c')
        self.inputArea.delete("1.0","end-1c")
        self.textArea.insert(INSERT,self.text)
        
    def reset(self):
        try: 
            self.time=0
            self.count = 0
            tk.after_cancel(self.cancelTime)
            self.timeLabel.config(text="Time: 0")
            self.callback()
            self.start()
        except Exception:
            self.count = 0
            self.callback()
            self.start()

    def showResults(self):
        
            for i,c in enumerate(self.text):
                try:
                    if self.inputArea.get("1.0","end-1c")[i] == c:
                        self.count += 1 
                except Exception:
                    pass
    def widgets(self):
        self.textArea = Text(tk,font=("Courier",20),height=10,width=50)
        self.textArea.pack()
        self.text = wikipedia.summary(query[random.randint(0,len(query)-1)],sentences=self.level)
        self.textArea.insert(INSERT,self.text)
        self.inputArea = Text(tk,font=("Courier",20),height=5,width=50)
        self.inputArea.pack(pady=10)
        buttonFrame = Frame(tk)
        buttonFrame.pack_propagate(False)
        buttonFrame.pack(pady=20)
        self.difficultSet = StringVar(buttonFrame)
        self.difficultSet.set("EASY")
        self.textLen = len(self.text)
        difficultMenu = OptionMenu(buttonFrame,self.difficultSet,*difficultList,command = self.callback)
        difficultMenu.grid(row=0,column=0,padx=5)
        resetBtn = Button(buttonFrame,text="RESET",command=self.reset,bg="red",font=("Courier",10))
        resetBtn.grid(row=0,column=2,padx=5)
        startBtn = Button(buttonFrame,text="START",font=("Courier",10),bg="#87ceeb",command=self.start)
        startBtn.grid(row=0,column=1)
        self.timeLabel = Label(buttonFrame,font=('Courier',10),text=f"Time: {self.time}")
        self.timeLabel.grid(row=0,column=3)
        tk.after(100,self.start)
        tk.mainloop()


if __name__ =="__main__":
    Draw() 


