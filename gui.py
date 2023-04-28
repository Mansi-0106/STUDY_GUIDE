import tkinter as tk
from PIL import ImageTk, Image
import os
import winsound
def program1():
    os.system(r'python "C:\Users\mansi\OneDrive\Desktop\DROWSINESS DETECTION\main.py"')

def program2():
    os.system(r'python "C:\Users\mansi\OneDrive\Desktop\DROWSINESS DETECTION\focus.py"')

def program3():
    os.system(r'python "C:\Users\mansi\OneDrive\Desktop\DROWSINESS DETECTION\Doubts.py"')
    
def program4():
    os.system(r'python "C:\Users\mansi\OneDrive\Desktop\DROWSINESS DETECTION\exercise.py"')

class MainWindow:

    def __init__(self, master):
        self.master = master
        master.title("Ai-LARM Drowsiness And Posture Detection System")
        master.geometry("600x500")

        winsound.PlaySound(r"C:\Users\mansi\OneDrive\Desktop\DROWSINESS DETECTION\gepanel.wav", winsound.SND_ASYNC)

        image_path = r"C:\Users\mansi\OneDrive\Desktop\DROWSINESS DETECTION\My project-1(1).jpg"
        bg_image = Image.open(image_path)
        bg_image = bg_image.resize((600, 570), Image.ANTIALIAS)
        self.bg_image = ImageTk.PhotoImage(bg_image)


        bg_label = tk.Label(master, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)

        button = tk.Button(master, text="Let's Start", command=self.second_window, width=15, height=2, bg="purple", fg="white",font=("Arial black", 12))
        button.place(relx=0.5, rely=0.8, anchor="center")
    

    def second_window(self):
        second_window = tk.Toplevel(self.master)
        second_window.title("Ai-LARM Drowsiness And Posture Detection Syste")
        second_window.geometry("600x500")

        bg_label = tk.Label(second_window, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)

        button1 = tk.Button(second_window, text="Ai-LARM Alert", padx=20, pady=10, bg="purple", fg="white", font=("Arial black", 10),command=program1)
        button1.place(relx=0.2, rely=0.88, anchor="s")

        button2 = tk.Button(second_window, text="Check Focus", padx=20, pady=10, bg="purple", fg="white", font=("Arial black", 10),command=program2)
        button2.place(relx=0.492, rely=0.88, anchor="s")

        button3 = tk.Button(second_window, text="Doubts Session", padx=20, pady=10, bg="purple", fg="white", font=("Arial black", 10),command=program3)
        button3.place(relx=0.8, rely=0.88, anchor="s")

        button4 = tk.Button(second_window, text="Read with Focus", padx=20, pady=10, bg="purple", fg="white", font=("Arial black", 10),command=program4)
        button4.place(relx=0.492, rely=0.9888, anchor="s")



root = tk.Tk()
app = MainWindow(root)

root.mainloop()
