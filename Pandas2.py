# Pandas 불러오기 및 pd로 설정
import numpy as np
import pandas as pd

# Pandas의 연산과 함수

# 데이터 프레임의 Null 여부 확인
word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근',
    'Durian': '두리안'
}

frequency_dict = {
    'Apple': 3,
    'Banana': 5,
    'Carrot': np.nan,
    'Durian': 2
}

importance_dict = {
    'Apple': 3,
    'Banana': 2,
    'Carrot': 1,
    'Durian': 1
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
print(summary.notnull())
print(summary.isnull())
summary['frequency'] = summary['frequency'].fillna('데이터 없음')
print(summary)

# 시리즈 자료형의 연산
array1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
array2 = pd.Series([4, 5, 6], index=['B', 'C', 'D'])

array3 = array1.add(array2)
print(array1)
print(array2)
print(array3)

array3 = array1.add(array2, fill_value=0)
print(array3)
print(array3.sum())

# 데이터 프레임 자료형의 연산
array1 = pd.DataFrame([[1, 2], [3, 4]], index=['A', 'B'])
array2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['B', 'C', 'D'])

print(array1)
print(array2)

array3 = array1.add(array2)
print(array3)

array3 = array1.add(array2, fill_value=0)
print(array3)

# 데이터 프레임 집계함수
# 기본 적으로 NaN은 0으로 계산 : 집계함수 특성
print("컬럼 1의 합 :", array3[1].sum())
print(array3.sum())

# 데이터 프레임 정렬 함수
print(array3)
array3 = array3.sort_values(1, ascending=True)
print(array3)