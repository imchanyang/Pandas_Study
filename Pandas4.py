# pandas 불러오기 및 pd로 사용
import numpy as np
import pandas as pd

# 데이터 프레임의 다중화

df = pd.DataFrame(
    np.random.randint(1, 10, (4, 4)),
    index=[['1차', '1차', '2차', '2차'], ['공격', '수비', '공격', '수비']],
    columns=['1회', '2회', '3회', '4회']
)

print(df)
print(df[['1회', '2회']].loc['2차'])

# 피벗 테이블의 기초
df = pd.DataFrame([
    ['Apple', 7, 5, 'Fruit'],
    ['Banana', 3, 6, 'Fruit'],
    ['Coconut', 2, 6, 'Fruit'],
    ['Rice', 8, 2, 'Meal'],
    ['Beef', 5, 2, 'Meal'],
    ['Kimchi', 4, 8, 'Meal']],
    columns=["Name", "Frequency", "Importance", "Type"])

print(df)

df = df.pivot_table(
    index="Importance", columns="Type", values="Frequency", aggfunc=np.max)

print(df)
