from tkinter import *


canvas_height = 400
canvas_width =  600
canvas_color = "black"
p1_y = canvas_height
p1_x = canvas_width/2

p1_colour = "green"
line_width = 5
line_height = 5
#
#
def p1_mode_N(event):
    global p1_y  # 해당 변수를 전역변수에 적용한다.
    # 선을 연결한다.
    canvas.create_line(p1_x, p1_y, p1_x,(p1_y-line_height),
                       width = line_width, fill=p1_colour)
    p1_y = p1_y - line_width # 현재y를 바뀐 값으로 변경

def p1_mode_S(event):
    global p1_y  # 해당 변수를 전역변수에 적용한다.
    # 선을 연결한다.
    canvas.create_line(p1_x, p1_y, p1_x,(p1_y-line_height),
                       width = line_width, fill=p1_colour)
    p1_y = p1_y + line_width # 현재y를 바뀐 값으로 변경

def p1_mode_W(event):
    global p1_x  # 해당 변수를 전역변수에 적용한다.
    # 선을 연결한다.
    canvas.create_line(p1_x, p1_y, p1_x,(p1_y-line_height),
                       width = line_width, fill=p1_colour)
    p1_x = p1_x - line_width # 현재y를 바뀐 값으로 변경

def p1_mode_E(event):
    global p1_x  # 해당 변수를 전역변수에 적용한다.
    # 선을 연결한다.
    canvas.create_line(p1_x, p1_y, p1_x,(p1_y-line_height),
                       width = line_width, fill=p1_colour)
    p1_x = p1_x + line_width # 현재y를 바뀐 값으로 변경


def erase_all(event):
    canvas.delete(ALL)


window = Tk()

window.title("내 스케치")
canvas = Canvas(bg=canvas_color, height = canvas_height,
                width =canvas_width, highlightthickness = 0)
canvas.pack()

window.bind("<Up>", p1_mode_N) # UP키를 누르면 p1_move_N매소드 실행
window.bind("<Down>", p1_mode_S)
window.bind("<Left>", p1_mode_W)
window.bind("<Right>", p1_mode_E)
window.bind("u", erase_all)

window.mainloop()