

from tkinter import *


def click(key):
    #버튼 이밴트 처리
    if key == '=':
        try:
            # eval : 문자열로 된 수식을 받아서 계산을 해서 결과를 리턴한다. .
            result = str(eval(display.get()))
            # 파이썬은 숫자와 문자의 + 연산을 못한다.
            display.insert(END, '='+ result)
        except:
            display.insert(END, "--> Error")
    elif key == 'C':
        display.delete(0,END) # 화면 클리어
    else:
        display.insert(END, key)


window = Tk()
window.title("계산기")
# Frame 컨테이너
# 컴포넌트들을 담는다. ?
top_row = Frame(window)

#sticky = N 북쪽에 
#columnspan=2 열2칸 사용

# 0,0 위치에 col두칸을 사용하여 북쪽에 위치
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

#입력가능한 45픽셀 배경 light green 입력창
display = Entry(top_row, width=45, bg="light green")

#그리드에 붙여서 보여준다.
display.grid()
#숫자버튼을 여러개 담아서 window에 붙일것
num_pad = Frame(window)
# 1행0열에 서쪽에 위치
num_pad.grid(row=1, column=0, sticky=W)
num_pad_list = ['7','8','9',
                '4','5','6',
                '1','2','3',
                '0','.','=']
r = 0
c = 0
for btn_text in num_pad_list:
    def cmd(x=btn_text):
        click(x)
    Button(num_pad, text = btn_text, width=5,
           command=cmd).grid(row=r, column=c)
    c += 1
    if c > 2:
        c = 0
        r+=1
#연산자
operator = Frame(window)
operator.grid(row=1, column=1, sticky=E)
operator_list = ['*','/',
                 '+','-',
                 '(',')',
                 'C']
r = 0
c = 0
for btn_text in operator_list:
    def cmd(x=btn_text):
        click(x)
    Button(operator, text = btn_text, width=5,
           command=cmd).grid(row=r, column=c)
    c += 1
    if c > 1:
        c = 0
        r+=1

window.mainloop()






