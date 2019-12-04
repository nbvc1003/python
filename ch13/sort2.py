import pandas as pd

score = {'kor':{1:78,2:88,3:90},
         'eng':{1:88,2:77,3:99},
         'math':{1:67,2:76,3:83}}

fr = pd.DataFrame(score)
print(fr)

print(fr.sort_values(by='eng')) # 영어점수 낮은 값 부터 (오름차순)
print(fr.sort_values(by=['eng','math'])) # 영어 점수가 같으면 수학점수 낮은 값부터

#영어점수 높은 사람부터 같으면 수학 낮은 순으로
print(fr.sort_values(ascending=[False,True],by=['eng','math']))