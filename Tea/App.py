import tkinter as Tk
import customtkinter as Ctk
import Motor

class MyTabView(Ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("Black Tea")
        self.add("Green Tea")

        # add widgets on tabs
        self.label = Ctk.CTkLabel(master=self.tab("Black Tea"),text="Select from black teas")
        self.label.place(x=200, y=0)

        self.Black_tea = Ctk.CTkSegmentedButton(master=self.tab("Black Tea"), values=["Earl Grey","Darjeeling","Assam"],dynamic_resizing=True,command=App.button_click)
        self.Black_tea.place(x=180,y=40)


class App(Ctk.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Tea Selecter")
        self._set_appearance_mode("dark")

        self.tab_view = MyTabView(master=self,width = 550,height = 450)
        self.tab_view.place(x=20,y=20)

    
    def button_click(self,name):
        info = Motor.database(name)
        self.text = Ctk.CTkTextbox(master=self,width=150,height=150,corner_radius=0)
        self.text.place(x=150,y=150)
        self.text.insert("0.0",info[2])

app = App()
app.mainloop()