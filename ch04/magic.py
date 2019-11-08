
import random
# 튜플과 리스트의 차이 수정가능 여부

answers = ( "자! 해보세요!",
 "됐네요, 이 사람아",
 "뭐라고? 다시 생각해보세요.",
 "모르니 두려운 것입니다.",
 "칠푼인가요?? 제 정싞이 아니군요!",
 "당싞이라면 핛 수 있어요!",
 "해도 그맊, 앆 해도 그맊, 아니겠어요?",
 "맞아요, 당싞은 올바른 선택을 했어요."
 )


print("MyMagicBall 에 오신것을 환영합니다. ")
user_name = input("앆녕하세요. 여러분의 이름을 입력하세요.\n")
print("맊나서 반가워요", user_name, ".", sep="")

want_more_advice = "y"
while want_more_advice == "y":
    question = input("조언을 구하고 싶으면 질문을 입력하고 앤터키를 누르세요.\n")
    print("고민중 \n" *2)
    choice = random.randint(0,len(answers))
    print(answers[choice])
    want_more_advice = input("다른 조언이 필요해 y/n")



