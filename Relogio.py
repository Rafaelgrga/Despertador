from tkinter import *
import pygame
import time

class Interface:
    def __init__(self):
        self.menu_inicial = Tk()
        pygame.init()
        self.music = ["BoxCat Games.mp3", "megalovania.mp3", "8bit-jump.mp3"]
        pygame.mixer.music.load(self.music[0])
        self.definir_volum = 0.3
        pygame.mixer.music.set_volume(self.definir_volum)
        self.menu_inicial.title("Relógio")
        self.menu_inicial.geometry("370x220+950+300")
        self.menu_inicial.resizable(False,False)
        self.clicked = BooleanVar()
        self.clicked.set(True)
        
    def start_alarme(self):
        if time.localtime().tm_hour == int(self.hour.get()) and time.localtime().tm_min == int(self.min.get()) and time.localtime().tm_sec == int(self.sec.get()):
            pygame.mixer.music.play()
    
    def stop_alarme(self):
        pygame.mixer.music.stop()
        
    def select_music(self):
        
        if self.clicked.get():
            self.clicked.set(False)
            self.outra_janela = Toplevel(self.menu_inicial)
            self.outra_janela.resizable(False, False)
            self.list_box = Listbox(self.outra_janela)
            self.list_box.pack()
            
            for music in self.music:
                self.list_box.insert(END,music)

            self.list_box.bind('<Double-1>', self.music_selected)
            self.outra_janela.protocol("WM_DELETE_WINDOW", self.close_window_music)

        elif not self.outra_janela.winfo_exists():
            self.clicked.set(True)
            
    def close_window_music(self):
        
        self.outra_janela.destroy()
            
    def music_selected(self, event):
        selected = self.list_box.curselection()
        if selected:
            pygame.mixer.music.load(self.music[selected[0]])
        self.clicked.set(True)
        self.outra_janela.destroy()

    def volume_up(self):
        self.definir_volum += 0.1
        pygame.mixer.music.set_volume(self.definir_volum)
    
    def volume_down(self):
        self.definir_volum -= 0.1
        pygame.mixer.music.set_volume(self.definir_volum)

    def button_text(self):
        self.text_2 = Label(self.menu_inicial, text = f"Despertador",font="Arial 13",height=2)
        self.text = Label(self.menu_inicial, text = f"{time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec}", font="Arial 20",width=7)
        self.date = Label(self.menu_inicial, text = f"{time.localtime().tm_mday} / {time.localtime().tm_mon} / {time.localtime().tm_year}", font = "Arial 15",height=2)
        self.hour_text = Label(self.menu_inicial,text= "Hours:")
        self.min_text = Label(self.menu_inicial,text= "Minutes:")
        self.sec_text = Label(self.menu_inicial,text= "Seconds:")
        self.hour = Entry(self.menu_inicial,width=6)
        self.min = Entry(self.menu_inicial,width=6) 
        self.sec = Entry(self.menu_inicial,width=6)
        self.botao = Button(self.menu_inicial, text = "Parar Alarme", command= self.stop_alarme)
        self.botao_volumeLow = Button(self.menu_inicial,text= "-", command = self.volume_down)
        self.botao_volumeMore = Button(self.menu_inicial,text= "+", command= self.volume_up)
        self.botao_select_music = Button(self.menu_inicial, text="Select Music", command=self.select_music)

    def insert_entry(self):
        self.hour.insert(0, 0)
        self.min.insert(0, 0)
        self.sec.insert(0, 0)
        
    def update(self):
        self.text.config(text = f"{time.localtime().tm_hour}:{time.localtime().tm_min}:{time.localtime().tm_sec}")
        self.date.config(text= f"{time.localtime().tm_mday} / {time.localtime().tm_mon} / {time.localtime().tm_year}")
        self.menu_inicial.after(1000,self.start_alarme)
        self.menu_inicial.after(1, self.update)
    
    def grid(self):
        self.text_2.grid(row=0,column=0, columnspan=6)
        self.text.grid(row=1,column=0, columnspan=6)
        self.date.grid(row=2,column=0, columnspan=6)
        self.hour_text.grid(row=3,column=0)
        self.hour.grid(row=3,column=1)
        self.min_text.grid(row=3,column=2)
        self.min.grid(row=3, column=3)
        self.sec_text.grid(row=3,column=4)
        self.sec.grid(row=3,column=5)
        self.botao.grid(row=4,column=0, columnspan=6,pady=20)
        self.botao_volumeLow.grid(row=4, column=1)
        self.botao_volumeMore.grid(row=4, column=4)
        self.botao_select_music.grid(row=4,column=6)
        
    def loop(self):
        self.button_text()
        self.insert_entry()
        self.grid()
        self.update()
        self.menu_inicial.mainloop()


interface = Interface()
interface.loop()