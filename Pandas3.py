# pandas 불러오기 및 pd로 사용
import numpy as np
import pandas as pd

# pandas의 활용

# 데이터 프레임의 마스킹
df = pd.DataFrame(np.random.randint(1, 10, (2, 2)), index=[0, 1], columns=["A", "B"])

print(df)
# 컬럼 A의 각 원소가 5보다 작거나 같은지 출력
print(df["A"] <= 5)
# 컬럼 A의 원소가 5보다 작고, 컬럼 B의 원소가 8보다 작은 행 추출
print(df.query("A <= 5 and B <= 8"))

# 데이터 프레임의 개별 연산1
df = pd.DataFrame([[1, 2, 3, 4], [1, 2, 3, 4]], index=[0, 1], columns=["A", "B", "C", "D"])
print(df)

df = df.apply(lambda x: x + 1)
print(df)


def add(x):
    return x + 1


df = df.apply(add)
print(df)

# 데이터 프레임의 개별 연산2
df = pd.DataFrame([
    ['Apple', 'Apple', 'Carrot', 'Banana'],
    ['Durian', 'Banana', 'Apple', 'Carrot']],
    index=[0, 1], columns=["A", "B", "C", "D"]
)
print(df)

df = df.replace({"Apple" : "Lemon"})
print(df)

# 데이터 프레임의 그룹화1
df = pd.DataFrame([
    ['Apple', 7, 'Fruit'],
    ['Banana', 3, 'Fruit'],
    ['Beef', 5, 'Meal'],
    ['Kimchi', 4, 'Meal']], columns=["Name", "Frequency", "Type"])

print(df)
print(df.groupby(['Type']).sum())

# 데이터 프레임의 그룹화2
df = pd.DataFrame([
    ['Apple', 7, 5, 'Fruit'],
    ['Banana', 3, 6, 'Fruit'],
    ['Beef', 5, 2, 'Meal'],
    ['Kimchi', 4, 8, 'Meal']], columns=["Name", "Frequency", "Importance", "Type"])

print(df)
print(df.groupby(["Type"]).aggregate([min, max, np.average]))

# 데이터 프레임의 그룹화3
df = pd.DataFrame([
    ['Apple', 7, 5, 'Fruit'],
    ['Banana', 3, 6, 'Fruit'],
    ['Beef', 5, 2, 'Meal'],
    ['Kimchi', 4, 8, 'Meal']], columns=["Name", "Frequency", "Importance", "Type"])


def my_filter(data):
    return data["Frequency"].mean() >= 5


print(df)
df = df.groupby(["Type"]).filter(my_filter)
print(df)

# 데이터 프레임의 그룹화4
df = df.groupby("Type").get_group("Fruit")
print(df)

# 데이터 프레임의 그룸화5
df = pd.DataFrame([
    ['Apple', 7, 5, 'Fruit'],
    ['Banana', 3, 6, 'Fruit'],
    ['Beef', 5, 2, 'Meal'],
    ['Kimchi', 4, 8, 'Meal']], columns=["Name", "Frequency", "Importance", "Type"])

df["Gap"] = df.groupby("Type")["Frequency"].apply(lambda x: x - x.mean())
print(df)