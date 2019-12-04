
import pandas as pd


exams = pd.read_csv('csv_exam.csv',
                    names=['아이디','반','수학','영어','과학'],
                    skiprows=1) # skiprows 행 1개를 스킵 시킨다.

print(exams)