"""
# 함수 (Function)

## 📌 개념
- 특정 작업을 수행하는 코드 묶음
- 필요할 때 호출해서 재사용 가능

## 📌 장점
- 코드 재사용
- 가독성 향상
- 유지보수 쉬움
"""

# =========================
# 1️⃣ 함수 기본
# =========================
def hello():
    print("Hello, Python!")

hello()  # 함수 호출


# =========================
# 2️⃣ 매개변수 (Parameter)
# =========================
def greet(name):
    print(f"안녕하세요, {name}님!")

greet("뽀삐")


# =========================
# 3️⃣ 반환값 (Return)
# =========================
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8


# =========================
# 4️⃣ 기본값 (Default Parameter)
# =========================
def greet2(name="선생"):
    print(f"안녕하세요, {name}님!")

greet2()
greet2("철수")


# =========================
# 5️⃣ 여러 값 반환
# =========================
def calc(a, b):
    return a + b, a * b

sum_value, mul_value = calc(3, 4)
print(sum_value, mul_value)


# =========================
# 6️⃣ 주의할 점
# =========================

# 함수 정의 전에 호출하면 에러 발생
# hello2()  # ❌

def hello2():
    print("Hi")

# return 이후 코드는 실행되지 않음
def test():
    return 1
    print("실행 안됨")  # ❌

# 함수 이름을 변수로 쓰면 에러 발생
