import tkinter as Tk
import customtkinter as Ctk
import Motor

class App(Ctk.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Tea chooser")
        self._set_appearance_mode("dark")
        self.grid_rowconfigure(5,weight=1)
        self.grid_columnconfigure(5,weight=1)

        
        self.Black_tea = Ctk.CTkSegmentedButton(self, values=["Earl Grey","Darjeeling","Assam"],dynamic_resizing=True,command=self.button_click)
        self.Black_tea.place(x=250,y=10)

        self.Green_tea = Ctk.CTkSegmentedButton(self,values=["Geen tea"],dynamic_resizing=True,command=self.button_click)
        self.Green_tea.place(x=250,y=40)

    
    def button_click(self,name):
        info = Motor.database(name)
        self.text = Ctk.CTkTextbox(master=self,width=150,height=150,corner_radius=0)
        self.text.place(x=150,y=150)
        self.text.insert("0.0",info[2])

app = App()
app.mainloop()