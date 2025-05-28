import tkinter as tk

class janela:
    def __init__(self):
        self.janela= tk.Tk()
        self.frame= tk.Frame(self.janela, width=210, height=210)
        self.frame.pack()

        self.x,self.y= 0,0
        label_pos= tk.Label(self.frame, text= f"posicao x:{self.x}, y:{self.y}", bg="red")
        label_pos_place(x=self.x, y=self.y)
        
        self.x,self.y = 75,75
        label_pos2= tk.Label(self.frame, text= f"posicao x:{self.x}, y:{self.y}", bg="red")
        label_pos2.place(x=self.x, y=self.y)
        self.janela.mainloop()

        def sobre(self):
            segunda_janela= tk.Toplevel(self.janela)
            segunda_janela.title('Sobre')
            segunda_janela. geometry('200x100')

        def janela_extra(self):
            pass

class Exemplo_grid:
    def __init__(self):
        self.janela= tk.Tk()
        for i in range (3):
            for j in range (3):
                frame = tk.Frame(master= self.janela, relief= tk.RAISED, borderwidth= 1)
                frame.grid (row=i, column=j, padx= 5, pady=5)
                label= tk.Label(master=frame,text=f"linha{i}\ncolunas{j}")
                label.pack()
            self.janela.mainloop()



if __name__ == '__main__':
    Exemplo_grid()