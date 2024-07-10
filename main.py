import tkinter as tk
from PIL import Image, ImageTk
from random import randint
#ramdom number generator
def getting_computer_choice():
    return randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice==computer_choice:
        return "Its a tie"
    elif (user_choice==1 and computer_choice==3)or \
            (user_choice==2 and computer_choice==1)or \
            (user_choice==3 and computer_choice==2):
        return "User Wins!"
    else:
        return "Computer Wins!"

def update_result(user_choice):
    global user_score,comp_score

    computer_choice = getting_computer_choice()
    result=determine_winner(user_choice, computer_choice)

    if result=="User Wins!":
        user_score+=1
    elif result == "Computer Wins!":
        comp_score+=1

    result_label.config(text=result)
    user_score_label.config(text=str(user_score))
    comp_score_label.config(text=str(comp_score))

def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    user_score_label.config(text=str(user_score))
    comp_score_label.config(text=str(comp_score))
    result_label.config(text="")




def on_rock():
    update_result(1)

def on_paper():
    update_result(2)

def on_scissor():
    update_result(3)

#setting up the windows

color_gray = "#343434"
color_blue = "#4584b6"
color_light_gray = "#646464"
color_yellow = "#FFDE57"

window = tk.Tk()
window.title("Rock Paper Scissor")
window.resizable(False,False)

# width=800
# height=600
# window.geometry(f"{width}x{height}")
# window.configure(bg=color_gray)

frame = tk.Frame(window)
frame.pack()

user_label = tk.Label(frame, text="User", font=("consolas", 30, "bold"), foreground=color_gray)
user_label.grid(row=0, column=1)

semi_label = tk.Label(frame, text=":", font=("Consolas", 30, "bold"), foreground=color_gray)
semi_label.grid(row=0, column=2)

comp_label = tk.Label(frame, text="Comp", font=("Consolas", 30, "bold"), foreground=color_gray)
comp_label.grid(row=0, column=3)

user_score_label = tk.Label(frame, text="0", font=("Consolas",20, "bold"), foreground=color_gray)
user_score_label.grid(row=1, column=1)

semi_label = tk.Label(frame, text=":", font=("Consolas", 20, "bold"), foreground=color_gray)
semi_label.grid(row=1, column=2)

comp_score_label = tk.Label(frame, text="0", font=("Consolas",20, "bold"), foreground=color_gray)
comp_score_label.grid(row=1, column=3)

result_label = tk.Label(frame, text="", font=("Consolas", 20, "bold"), foreground=color_gray)
result_label.grid(row=3, column=1, columnspan=3)

rock_image = Image.open("rockpng.png")
rock_photo = ImageTk.PhotoImage(rock_image)
rock_button = tk.Button(frame, image=rock_photo, command=on_rock,width=200, height=200, foreground=color_light_gray,background=color_yellow)
rock_button.grid(row=2, column=1)

paper_image = Image.open("paperpng.png")
paper_photo = ImageTk.PhotoImage(paper_image)
paper_button = tk.Button(frame, image=paper_photo, command=on_paper,width=200, height=200, foreground=color_light_gray, background=color_blue)
paper_button.grid(row=2, column=2)

scissor_image = Image.open("scissorspng.png")
scissor_photo = ImageTk.PhotoImage(scissor_image)
scissor_button = tk.Button(frame, image=scissor_photo, command=on_scissor,width=200, height=200, foreground=color_light_gray,background=color_gray)
scissor_button.grid(row=2, column=3)

reset_button = tk.Button(frame, text="Reset", command=reset_game, font=("Consolas", 20, "bold"), foreground=color_gray, background=color_yellow)
reset_button.grid(row=4, column=1, columnspan=3, pady=20)

user_score = 0
comp_score = 0






if __name__ == "__main__":

    window.mainloop()










