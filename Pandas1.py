# pandas 불러오기 및 pd로 사용하기
import pandas as pd

# 시리즈의 연산
# 시리즈를 서로 연산

word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근'
}

frequency_dict = {
    'Apple': 3,
    'Banana': 5,
    'Carrot': 7
}

importance_dict = {
    'Apple': 3,
    'Banana': 2,
    'Carrot': 1
}

word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)
importance = pd.Series(importance_dict)

summary = pd.DataFrame({
    'word': word,
    'frequency': frequency,
    'importance': importance
})

# 시리즈 곱하기 연산
score = summary['frequency'] * summary['importance']
print(summary)

# 시리즈 추가
summary['score'] = score
print(summary)


# 데이터 프레임의 슬라이싱
word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근'
}

frequency_dict = {
    'Apple': 3,
    'Banana': 5,
    'Carrot': 7
}

importance_dict = {
    'Apple': 3,
    'Banana': 2,
    'Carrot': 1
}

word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)
importance = pd.Series(importance_dict)

summary = pd.DataFrame({
    'word': word,
    'frequency': frequency,
    'importance': importance
})

print(summary)

# 이름을 기준으로 슬라이싱 .loc[행, 열]
print(summary.loc['Banana':'Carrot', 'importance':])
# 인덱스를 기준으로 슬라이싱 .iloc[행, 열]
print(summary.iloc[1:3, 2:])


# 데이터 프레임의 연산
print(summary)

# 데이터의 변경
summary.loc['Apple', 'importance'] = 5
print(summary)

# 새 데이터 추가
summary.loc['Berry'] = ['베리', 5, 3]
print(summary)


# 데이터프레임 엑셀로 내보내기/불러오기
# encoding = "utf-8-sig" : 한글처리
summary.to_csv("summary.csv", encoding = "utf-8-sig")
save = pd.read_csv("summary.csv", index_col=0)
print(summary)
print(save)