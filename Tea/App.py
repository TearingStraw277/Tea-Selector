import tkinter as Tk
import customtkinter as Ctk
import Motor

class MyTabView(Ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        Black_Tea = ["Earl Grey","Assam"]
        Green_Tea = ["Jasmine"]
        # create tabs
        self.add("Black Tea")
        self.add("Green Tea")

        # add widgets on tabs

        #label for black tea
        self.label = Ctk.CTkLabel(master=self.tab("Black Tea"),text="Select from black teas")
        self.label.place(x=200, y=0)

        #button set for black teas
        self.Black_tea = Ctk.CTkSegmentedButton(master=self.tab("Black Tea"), values=Black_Tea,dynamic_resizing=True,command=self.button_click)
        self.Black_tea.place(x=180,y=40)

        self.label = Ctk.CTkLabel(master=self.tab("Green Tea"),text="Select from green teas")
        self.label.place(x=200, y=0)

        #button set for green teas
        self.Green_tea = Ctk.CTkSegmentedButton(master=self.tab("Green Tea"), values=Green_Tea,dynamic_resizing=True,command=self.button_click)
        self.Green_tea.place(x=180,y=40)


    #def Button(self,values):
        #self.button = Ctk.CTkSegmentedButton(master=self.tab("Black Tea"), values=values,dynamic_resizing=True,command=self.button_click)
        #self.button.place(x=180,y=40)


    #passes data to Motor to find data and move motor
    def button_click(self,name):
        info = Motor.database(name)
        self.text = Ctk.CTkTextbox(master=self,width=150,height=150,corner_radius=0)
        self.text.place(x=150,y=150)
        self.text.insert("0.0",info[1])



class App(Ctk.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Tea Selecter")
        self._set_appearance_mode("dark")

        self.tab_view = MyTabView(master=self,width = 550,height = 450)
        self.tab_view.place(x=20,y=20)

app = App()
app.mainloop()