"""
a = int(input("숫자를 입력하세요:"))
b = 0
for i in range(1, a+1):
    if a%i ==0:
        b = b+1
print(b)

<약수 만들기 코드> + <카운팅 패턴>
"""

"""
while True:
    a = int(input("숫자를 입력하세요:"))
    b = 0
    for i in range(1, a+1):
        if a%i == 0:
            b = b+1
    if b == 2:
        print("소수입니다.")
    elif b:
        print("소수가 아닙니다.")
    
<소수 판독기>
"""
"""
a = int(input("숫자를 입력하세요:"))
for i in range(1, a+1):
    print("*"*i)
for i in range(a-1, 0,-1):
    print("*"*i)

<중복 나열 방법>
"""

"""
a = int(input("숫자를 입력하세요:"))
b = 1
for i in range(1, a+1):
    b = b*i
    print(b)

    <팩토리얼>
"""

"""
a = int(input("숫자를 입력하세요:"))
if a%2 == 1:
    print("홀수입니다.")
elif():
    print("짝수입니다.")

<짝수 홀수 판독>
"""