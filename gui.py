from game import LudoGame
from tkinter import *
import random


root = Tk()

root.title("Ludo")
root.geometry("680x680")

game = LudoGame()

# Top row (1 - 15)
for i in range(0, 15):
    if i == 0:
        sqr1 = Canvas(root, width=40, height=40, bg="#FFD580", highlightthickness=1, highlightbackground="black")
        sqr1.grid(row=0, column=i)
        sqr1.create_text(20, 20, text=i+1, font=('Helvetica 15'))
    elif i == 7 or i == 14:
        sqr8_15 = Canvas(root, width=40, height=40, bg="#ADD8E6", highlightthickness=1, highlightbackground="black")
        sqr8_15.grid(row=0, column=i)
        sqr8_15.create_text(20, 20, text=i+1, font=('Helvetica 15'))
    else:
        sqr = Canvas(root, width=40, height=40, bg="white", highlightthickness=1, highlightbackground="black")
        sqr.grid(row=0, column=i)
        sqr.create_text(20, 20, font=('Helvetica 15'))

# Right side (15 - 29)
for i in range(1, 15):
    if i == 7:
        sqr22 = Canvas(root, width=40, height=40, bg="#FFC0CB", highlightthickness=1, highlightbackground="black")
        sqr22.grid(row=i, column=14)
        sqr22.create_text(20, 20, text="22", font=('Helvetica 15'))
    elif i == 14:
        sqr29 = Canvas(root, width=40, height=40, bg="#FFC0CB", highlightthickness=1, highlightbackground="black")
        sqr29.grid(row=i, column=14)
        sqr29.create_text(20, 20, text="29", font=('Helvetica 15'))
    else:
        sqr = Canvas(root, width=40, height=40, bg="white", highlightthickness=1, highlightbackground="black")
        sqr.grid(row=i, column=14)
        sqr.create_text(20, 20, font=('Helvetica 15'))

# Bottom row (29 - 43)
for i in range(0, 14):
    if i == 0:
        sqr43 = Canvas(root, width=40, height=40, bg="#90ee90", highlightthickness=1, highlightbackground="black")
        sqr43.grid(row=14, column=i)
        sqr43.create_text(20, 20, text="43", font=('Helvetica 15'))
    elif i == 7:
        sqr36 = Canvas(root, width=40, height=40, bg="#90ee90", highlightthickness=1, highlightbackground="black")
        sqr36.grid(row=14, column=i)
        sqr36.create_text(20, 20, text="36", font=('Helvetica 15'))
    else:
        sqr = Canvas(root, width=40, height=40, bg="white", highlightthickness=1, highlightbackground="black")
        sqr.grid(row=14, column=i)
        sqr.create_text(20, 20, font=('Helvetica 15'))

# Left side (43 - 56)
for i in range(1, 14):
    if i == 7:
        sqr50 = Canvas(root, width=40, height=40, bg="#FFD580", highlightthickness=1, highlightbackground="black")
        sqr50.grid(row=i, column=0)
        sqr50.create_text(20, 20, text="50", font=('Helvetica 15'))
    else:
        sqr = Canvas(root, width=40, height=40, bg="white", highlightthickness=1, highlightbackground="black")
        sqr.grid(row=i, column=0)
        sqr.create_text(20, 20, font=('Helvetica 15'))

# Final squares
for i in range(7, 51, 14):
    x = 7
    if i == 7:
        for j in range(1, 7):
            blue_sqr = Canvas(root, width=40, height=40, bg="#ADD8E6", highlightthickness=1, highlightbackground="black")
            blue_sqr.grid(row=j, column=7)
            blue_sqr.create_text(20, 20, text="B" + str(j), font=('Helvetica 15'))
    if i == 21:
        for j in range(8, 14):
            x -= 1
            pink_sqr = Canvas(root, width=40, height=40, bg="#FFC0CB", highlightthickness=1, highlightbackground="black")
            pink_sqr.grid(row=7, column=j)
            pink_sqr.create_text(20, 20, text="C" + str(x), font=('Helvetica 15'))
    if i == 35:
        for j in range(8, 14):
            x -= 1
            green_sqr = Canvas(root, width=40, height=40, bg="#90ee90", highlightthickness=1, highlightbackground="black")
            green_sqr.grid(row=j, column=7)
            green_sqr.create_text(20, 20, text="D" + str(x), font=('Helvetica 15'))
    if i == 49:
        for j in range(1, 7):
            pink_sqr = Canvas(root, width=40, height=40, bg="#FFD580", highlightthickness=1, highlightbackground="black")
            pink_sqr.grid(row=7, column=j)
            pink_sqr.create_text(20, 20, text="A" + str(j), font=('Helvetica 15'))

# Ending square
end_sqr = Canvas(root, width=40, height=40, bg="white", highlightthickness=1, highlightbackground="black")
end_sqr.grid(row=7, column=7)
end_sqr.create_text(20, 20, text="E", font=('Helvetica 15'))

# "A" Home and Ready squares
a_h_sqr = Canvas(root, width=81, height=81, bg="#FFD580", highlightthickness=1, highlightbackground="black")
a_h_sqr.grid(row=1, column=1, rowspan=2, columnspan=2)
a_h_sqr.create_text(40, 40, text="Ready", font=('Helvetica 12'))

a_r_sqr = Canvas(root, width=81, height=81, highlightthickness=1, highlightbackground="black")
a_r_sqr.grid(row=3, column=3, rowspan=2, columnspan=2)
a_r_sqr.create_text(40, 20, text="A", fill="orange", font=('Helvetica 15 bold'))
a_r_sqr.create_text(40, 40, text="Home", font=('Helvetica 12'))

# "B" Home and Ready squares
a_h_sqr = Canvas(root, width=82, height=82, bg="#ADD8E6", highlightthickness=1, highlightbackground="black")
a_h_sqr.grid(row=1, column=12, rowspan=2, columnspan=2)
a_h_sqr.create_text(40, 40, text="Ready", font=('Helvetica 12'))

a_r_sqr = Canvas(root, width=81, height=81, highlightthickness=1, highlightbackground="black")
a_r_sqr.grid(row=3, column=10, rowspan=2, columnspan=2)
a_r_sqr.create_text(40, 20, text="B", fill="blue", font=('Helvetica 15 bold'))
a_r_sqr.create_text(40, 40, text="Home", font=('Helvetica 12'))

# "C" Home and Ready squares
a_h_sqr = Canvas(root, width=82, height=82, bg="#FFC0CB", highlightthickness=1, highlightbackground="black")
a_h_sqr.grid(row=12, column=12, rowspan=2, columnspan=2)
a_h_sqr.create_text(40, 40, text="Ready", font=('Helvetica 12'))

a_r_sqr = Canvas(root, width=81, height=81, highlightthickness=1, highlightbackground="black")
a_r_sqr.grid(row=10, column=10, rowspan=2, columnspan=2)
a_r_sqr.create_text(40, 20, text="C", fill="pink", font=('Helvetica 15 bold'))
a_r_sqr.create_text(40, 40, text="Home", font=('Helvetica 12'))

# "D" Home and Ready squares
a_h_sqr = Canvas(root, width=82, height=82, bg="#90ee90", highlightthickness=1, highlightbackground="black")
a_h_sqr.grid(row=12, column=1, rowspan=2, columnspan=2)
a_h_sqr.create_text(40, 40, text="Ready", font=('Helvetica 12'))

a_r_sqr = Canvas(root, width=81, height=81, highlightthickness=1, highlightbackground="black")
a_r_sqr.grid(row=10, column=3, rowspan=2, columnspan=2)
a_r_sqr.create_text(40, 20, text="D", fill="green", font=('Helvetica 15 bold'))
a_r_sqr.create_text(40, 40, text="Home", font=('Helvetica 12'))

# Second Window
window2 = Toplevel(root)
window2.wm_transient(root)
window2.title("Who is ready for Ludo!!!")
window2.geometry("300x300")
# User entry field for number of players
e = Entry(window2, width=10)
e.grid(row=0, column=0)
num = None

def number_of_players():
    game.set_players((int(e.get())))
    global apq
    global ap
    global aq
    global bpq
    global bp
    global bq
    if len(game.get_players_obj()) == 2:
        apq = Label(root, text="PQ", bg="orange")
        ap = Label(root, text="P", bg="orange")
        ap.grid(row=4, column=3)
        aq = Label(text="Q", bg="orange")
        aq.grid(row=4, column=4)
        bpq = Label(text="PQ", bg="blue")
        bp = Label(text="P", bg="blue")
        bp.grid(row=4, column=10)
        bq = Label(text="Q", bg="blue")
        bq.grid(row=4, column=11)
    if len(game.get_players_obj()) == 3:
        Label(text="P", bg="orange").grid(row=4, column=3)
        Label(text="Q", bg="orange").grid(row=4, column=4)
        Label(text="P", bg="blue").grid(row=4, column=10)
        Label(text="Q", bg="blue").grid(row=4, column=11)
        Label(text="P", bg="green").grid(row=11, column=3)
        Label(text="Q", bg="green").grid(row=11, column=4)
    window2.destroy()

number_of_players_button = Button(window2, text="Please enter number of players", command=number_of_players)
number_of_players_button.grid(row=1, column=0)

# Dice

dice_button = Button(root, text="Roll")
dice_button.grid(row=8, column=15)

list1 = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]

rolls = []
rounds = []

def dice_click():
    rand = random.choice(list1)

    dice = Label(root, text=rand, font='Helvetica 50')
    dice.grid(row=6, column=15, rowspan=2, columnspan=2)

    if rand == "\u2680":
        rolls.append(1)
    elif rand == "\u2681":
        rolls.append(2)
    elif rand == "\u2682":
        rolls.append(3)
    elif rand == "\u2683":
        rolls.append(4)
    elif rand == "\u2684":
        rolls.append(5)
    elif rand == "\u2685":
        rolls.append(6)

    if len(game.get_players_obj()) == 2:
        if len(rounds) == 0:
            rounds.append(tuple(['A', rolls[-1]]))
        elif rounds[-1][1] == 6 and rounds[-1][0] == 'A':
            rounds.append(tuple(['A', rolls[-1]]))
        elif rounds[-1][1] == 6 and rounds[-1][0] == 'B':
            rounds.append(tuple(['B', rolls[-1]]))
        elif rounds[-1][0] == 'B':
            rounds.append(tuple(['A', rolls[-1]]))
        elif rounds[-1][0] == 'A':
            rounds.append(tuple(['B', rolls[-1]]))

        game_on = game.play_game(rounds[-1])

        # If AP and AQ tokens are the same
        if game_on[0] == game_on[1] and game_on[0] != "H" and game_on[0] != "R":
            if game_on[0] == "A1" or game_on[0] == "A2" or game_on[0] == "A3" or game_on[0] == "A4" or game_on[0] == "A5" or game_on[0] == "A6":
                apq.grid_forget()
                ap.grid_forget()
                aq.grid_forget()
                apq.grid(row=7, column=int(game_on[0][1]))
            elif game_on[0] == "E":
                apq.grid_forget()
                ap.grid_forget()
                aq.grid_forget()
                dice_button.grid_forget()
                dice.grid_forget()
                apq.grid(row=7, column=7)
                win1 = Label(root, text="Orange Wins!!", font='Helvetica 20', fg="orange")
                win1.grid(row=6, column=1, columnspan=6)
                win2 = Label(root, text="Orange Wins!!", font='Helvetica 20', fg="orange")
                win2.grid(row=6, column=8, columnspan=6)
                win3 = Label(root, text="Orange Wins!!", font='Helvetica 20', fg="orange")
                win3.grid(row=8, column=1, columnspan=6)
                win4 = Label(root, text="Orange Wins!!", font='Helvetica 20', fg="orange")
                win4.grid(row=8, column=8, columnspan=6)
            elif 1 <= int(game_on[0]) <= 15:
                apq.grid_forget()
                ap.grid_forget()
                aq.grid_forget()
                apq.grid(row=0, column=int(game_on[0]) - 1)
            elif 16 <= int(game_on[0]) <= 29:
                apq.grid_forget()
                ap.grid_forget()
                aq.grid_forget()
                apq.grid(row=int(game_on[0]) - 15, column=14)
            elif 30 <= int(game_on[0]) <= 43:
                apq.grid_forget()
                ap.grid_forget()
                aq.grid_forget()
                apq.grid(row=14, column=43 - int(game_on[0]))
            elif 44 <= int(game_on[0]) <= 50:
                ap.place_forget()
                aq.place_forget()
                apq.grid(row=57 - int(game_on[0]), column=0)

        else:
            # If tokens are separate
            # AP
            if game_on[0] == "H":
                ap.grid_forget()
                apq.grid_forget()
                ap.grid(row=4, column=3)
            elif game_on[0] == "R":
                ap.grid_forget()
                apq.grid_forget()
                ap.grid(row=2, column=1)
            elif game_on[0] == "A1" or game_on[0] == "A2" or game_on[0] == "A3" or game_on[0] == "A4" or game_on[0] == "A5" or game_on[0] == "A6":
                ap.grid_forget()
                apq.grid_forget()
                ap .grid(row=7, column=int(game_on[0][1]))
            elif game_on[0] == "E":
                ap.grid_forget()
                apq.grid_forget()
                ap.grid(row=7, column=7)
            elif 1 <= int(game_on[0]) <= 15:
                ap.grid_forget()
                apq.grid_forget()
                ap.grid(row=0, column=int(game_on[0])-1)
            elif 16 <= int(game_on[0]) <= 29:
                ap.grid_forget()
                apq.grid_forget()
                ap.grid(row=int(game_on[0])-15, column=14)
            elif 30 <= int(game_on[0]) <= 43:
                ap.grid_forget()
                apq.grid_forget()
                ap.grid(row=14, column=43-int(game_on[0]))
            elif 44 <= int(game_on[0]) <= 50:
                ap.grid_forget()
                apq.grid_forget()
                ap.grid(row=57-int(game_on[0]), column=0)

            # AQ
            if game_on[1] == "H":
                aq.grid_forget()
                aq.grid(row=4, column=4)
            elif game_on[1] == "R":
                aq.grid_forget()
                aq.grid(row=2, column=2)
            elif game_on[1] == "A1" or game_on[1] == "A2" or game_on[1] == "A3" or game_on[1] == "A4" or game_on[1] == "A5" or game_on[1] == "A6":
                aq.grid_forget()
                aq.grid(row=7, column=int(game_on[1][1]))
            elif game_on[1] == "E":
                aq.grid_forget()
                aq.grid(row=7, column=7)
            elif 1 <= int(game_on[1]) <= 15:
                aq.grid_forget()
                aq.grid(row=0, column=int(game_on[1])-1)
            elif 16 <= int(game_on[1]) <= 29:
                aq.grid_forget()
                aq.grid(row=int(game_on[1])-15, column=14)
            elif 30 <= int(game_on[1]) <= 43:
                aq.grid_forget()
                aq.grid(row=14, column=43-int(game_on[1]))
            elif 44 <= int(game_on[1]) <= 50:
                aq.grid_forget()
                aq.grid(row=57-int(game_on[1]), column=0)

        # If BP and BQ are together
        if game_on[2] == game_on[3] and game_on[2] != "H" and game_on[2] != "R":
            if game_on[2] == "B1" or game_on[2] == "B2" or game_on[2] == "B3" or game_on[2] == "B4" or game_on[2] == "B5" or game_on[2] == "B6":
                bpq.grid_forget()
                bp.grid_forget()
                bq.grid_forget()
                bpq.grid(row=int(game_on[2][1]), column=7)
            elif game_on[2] == "E":
                bpq.grid_forget()
                bp.grid_forget()
                bq.grid_forget()
                dice_button.grid_forget()
                dice.grid_forget()
                bpq.grid(row=7, column=7)
                win1 = Label(root, text="Blue Wins!!", font='Helvetica 20', fg="blue")
                win1.grid(row=6, column=1, columnspan=6)
                win2 = Label(root, text="Blue Wins!!", font='Helvetica 20', fg="blue")
                win2.grid(row=6, column=8, columnspan=6)
                win3 = Label(root, text="Blue Wins!!", font='Helvetica 20', fg="blue")
                win3.grid(row=8, column=1, columnspan=6)
                win4 = Label(root, text="Blue Wins!!", font='Helvetica 20', fg="blue")
                win4.grid(row=8, column=8, columnspan=6)
            elif 1 <= int(game_on[2]) <= 8:
                bpq.grid_forget()
                bp.grid_forget()
                bq.grid_forget()
                bpq.grid(row=0, column=int(game_on[2]) - 1)
            elif 15 <= int(game_on[2]) <= 29:
                bpq.grid_forget()
                bp.grid_forget()
                bq.grid_forget()
                bpq.grid(row=int(game_on[2]) - 15, column=14)
            elif 30 <= int(game_on[2]) <= 43:
                bpq.grid_forget()
                bp.grid_forget()
                bq.grid_forget()
                bpq.grid(row=14, column=43 - int(game_on[2]))
            elif 44 <= int(game_on[2]) <= 57:
                bpq.grid_forget()
                bp.grid_forget()
                bq.grid_forget()
                bpq.grid(row=57 - int(game_on[2]), column=0)

        else:
            # If B tokes are separate
            # BP
            if game_on[2] == "H":
                bp.grid_forget()
                bpq.grid_forget()
                bp.grid(row=4, column=10)
            elif game_on[2] == "R":
                bp.grid_forget()
                bpq.grid_forget()
                bp.grid(row=2, column=12)
            elif game_on[2] == "B1" or game_on[2] == "B2" or game_on[2] == "B3" or game_on[2] == "B4" or game_on[2] == "B5" or game_on[2] == "B6":
                bp.grid_forget()
                bpq.grid_forget()
                bp.grid(row=int(game_on[2][1]), column=7)
            elif game_on[2] == "E":
                bp.grid_forget()
                bpq.grid_forget()
                bp.grid(row=7, column=7)
            elif 1 <= int(game_on[2]) <= 8:
                bp.grid_forget()
                bpq.grid_forget()
                bp.grid(row=0, column=int(game_on[2])-1)
            elif 15 <= int(game_on[2]) <= 29:
                bp.grid_forget()
                bpq.grid_forget()
                bp.grid(row=int(game_on[2])-15, column=14)
            elif 30 <= int(game_on[2]) <= 43:
                bp.grid_forget()
                bpq.grid_forget()
                bp .grid(row=14, column=43-int(game_on[2]))
            elif 44 <= int(game_on[2]) <= 57:
                bp.grid_forget()
                bpq.grid_forget()
                bp.grid(row=57-int(game_on[2]), column=0)

            #BQ
            if game_on[3] == "H":
                bq.grid_forget()
                bq.grid(row=4, column=11)
            elif game_on[3] == "R":
                bq.grid_forget()
                bq.grid(row=2, column=13)
            elif game_on[3] == "B1" or game_on[3] == "B2" or game_on[3] == "B3" or game_on[3] == "B4" or game_on[3] == "B5" or game_on[3] == "B6":
                bq.grid_forget()
                bq.grid(row=int(game_on[3][1]), column=7)
            elif game_on[3] == "E":
                bq.grid_forget()
                bq.grid(row=7, column=7)
            elif 1 <= int(game_on[3]) <= 8:
                bq.grid_forget()
                bq.grid(row=0, column=int(game_on[3])-1)
            elif 15 <= int(game_on[3]) <= 29:
                bq.grid_forget()
                bq.grid(row=int(game_on[3])-15, column=14)
            elif 30 <= int(game_on[3]) <= 43:
                bq.grid_forget()
                bq.grid(row=14, column=43-int(game_on[3]))
            elif 44 <= int(game_on[3]) <= 57:
                bq.grid_forget()
                bq.grid(row=57-int(game_on[3]), column=0)

        print(rounds)
        print(game_on)

    elif len(game.get_players_obj()) == 3:
        if len(rounds) == 0:
            rounds.append(tuple(['A', rolls[-1]]))
        elif rounds[-1][1] == 6 and rounds[-1][0] == 'A':
            rounds.append(tuple(['A', rolls[-1]]))
        elif rounds[-1][1] == 6 and rounds[-1][0] == 'B':
            rounds.append(tuple(['B', rolls[-1]]))
        elif rounds[-1][1] == 6 and rounds[-1][0] == 'C':
            rounds.append(tuple(['C', rolls[-1]]))
        elif rounds[-1][0] == 'A':
            rounds.append(tuple(['B', rolls[-1]]))
        elif rounds[-1][0] == 'B':
            rounds.append(tuple(['C', rolls[-1]]))
        elif rounds[-1][0] == 'C':
            rounds.append(tuple(['A', rolls[-1]]))

        print(rounds)
        print(game.play_game(rounds[-1]))
    else:
        print('Not working')

dice_button.config(command=dice_click)

root.mainloop()
