# Pandas란
# 데이터를 효과적으로 처리하고, 보여줄 수 있도록 도와주는 라이브러리
# 인덱스(Index)에 데이터를 나열
# 시리즈(Series)를 기본적인 자료형으로 사용
# 엑셀(Excel)과 비슷

# Series란
# 인덱스와 값으로 구성

# pandas 불러오기 및 pd로 사용하기
import pandas as pd

array = pd.Series(['사과', '바나나', '당근'], index =['a', 'b', 'c'])

print(array)
print(array['a'])