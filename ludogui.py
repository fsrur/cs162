from tkinter import *

root = Tk()

root.title("Ludo")
root.geometry("680x680")

from PIL import Image
queen = Image.open('queen.PNG')

# Top row (1 - 15)
for i in range(0, 15):
    if i == 0:
        sqr1 = Canvas(root, width=40, height=40, bg="#FFD580", highlightthickness=1, highlightbackground="black")
        sqr1.grid(row=0, column=i)
        sqr1.create_text(20, 20, text=i+1, font=('Helvetica 15'))
    elif i == 7 or i==14:
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
            pink_sqr.create_text(20, 20, text="D" + str(j), font=('Helvetica 15'))

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
a_r_sqr.create_text(40, 20, text="A", font=('Helvetica 15 bold'))
a_r_sqr.create_text(40, 40, text="Home", font=('Helvetica 12'))
# Button(root, image = queen).pack(side = TOP)




# def squares():
#     global black_squares
#     global white_squares
#
#     black = []
#     black += range(0, 32)
#
#     white = []
#     white += range(0, 32)
#
#     for var in black:
#         ind = black.index(var)
#         black[ind] = tkinter.Canvas(root, width=110, height=110, border=0, bg="black")
#
#     for var in white:
#         ind = black.index(var)
#         black[ind] = tkinter.Canvas(root, width=110, height=110, border=0, bg="white")
#
#
# def board(black, white):
#     board = []
#     for num in range(0, 4):
#         board.append(white_squares[num])
#         board.append(black_squares[num])


root.mainloop()




