import tkinter as tk

def key_pressed(event):

    label.config(text="")

    label.config(text=f"Tecla pressionada: {event.keysym}")

root = tk.Tk()
root.title("Detector de teclas")
root.geometry("300x200")

label = tk.Label(root, text="Pressione uma tecla", font=("Arial",14))
label.pack(pady=50)

root.bind("<KeyPress>",key_pressed)

root.mainloop()