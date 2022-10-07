# add some OTHER text to finish exercise
# This program convert text from lowwer case to upper case
# this is simple program. On the next step i wil add more descriptons
import tkinter
from PIL import ImageTk, Image
from tkinter import BOTH, StringVar, END


# Define Window
root = tkinter.Tk()
root.title("Cześć Użytkowniku - Podaj swoje imię")
root.iconbitmap("wave.ico")
root.geometry("400x400")
root.resizable(0,0)

# Define fonts and colors
root_color = "#000000"
input_color = "#14213D"
output_color = "#E5E5E5"
root.config(bg = root_color)

# Define functions
def submit_name():
    # Say hello to your user
    if case_style.get() == "normal":
        name_label = tkinter.Label(output_frame, text = "Cześć " + name.get() + "! Zacznij uczyć się montażu filmów!", bg = output_color)
    elif case_style.get() == "upper":
            name_label = tkinter.Label(output_frame, text = ("Cześć " + name.get() + "! Zacznij uczyć się montażu filmów!").upper(), bg = output_color)
    name_label.pack()    
    name.delete(0,END)


# Define layout

# Define frames
input_frame = tkinter.LabelFrame(root, bg = input_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)
input_frame.pack(padx=10)
output_frame.pack(padx =10,pady=10, fill=BOTH, expand=True)

# Create widgets
name = tkinter.Entry(input_frame, text = "Podaj swoje imię", width=20)
submit_button = tkinter.Button(input_frame, text = "Zatwierdź", command=submit_name)
name.grid(row=0,column=0, padx=10,pady=10)
submit_button.grid(row=0,column=1, padx=10,pady=10, ipadx=20 )

# Create radio buttons for text display
case_style = StringVar()
case_style.set("normal")
normal_button = tkinter.Radiobutton(input_frame, text = "Normalne litery", font = ("Arial", 16 , 'bold'), variable=case_style, value="normal", bg=input_color, activebackground="#FCA311")
upper_button = tkinter.Radiobutton(input_frame, text = "Wielkie litery", font = ("Arial", 16 , 'bold'),  variable=case_style, value="upper", bg=input_color, activebackground="#FCA311")
normal_button.grid(row=1,column=0,padx=2,pady=2)
upper_button.grid(row=1,column=1)


# Add a image
smile_img = ImageTk.PhotoImage(Image.open("smile.png"))
smile_label  = tkinter.Label(output_frame, image= smile_img, bg = output_color)
smile_label.pack()


# Run root window's main loop
root.mainloop()