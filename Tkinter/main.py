from tkinter import * 
import configure
import new


window = Tk()
window.configure(bg = "black")
window.geometry(f'{configure.WIDTH}x{configure.HEIGHT}')
window.title("MinesWeeper")
#window.state('zoomed')
"""
c'est fonction pour pas changer le size juste pour garder contenant des diamètres spécifiés,
on peux pas voir la flèche sur les bords de la fenêtre
"""
window.resizable(False, False) 

top_frame = Frame(window, bg = '#5D6D7E', width = configure.WIDTH, height = new.height_prct(25)) # width on pris dans le fichier configure et le heigh on pris dans le fichier new 
top_frame.place(x=0, y=0)

game_title = Label(top_frame, bg = "#5D6D7E", fg="white", text="Minesweeper", font=('', 48)) # format de title 
game_title.place(x= new.width_prct(25), y=0)

# format de grille (شبكة)
center_frame = Frame(window, bg= "black", width= new.width_prct(75), height= new.height_prct(75)).place(x=new.width_prct(30),y=new.height_prct(30))

# dessign de grille (رسم الشبكه)
 

window.mainloop()





                