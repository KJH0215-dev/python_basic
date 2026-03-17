"""
a = "Life is too short, You need Python"
print(len(a))

문자 길이 풀이
"""

"""
a = "Life is too short, You need Python"

print(a[3])

파이썬은 0부터 센다. L = 0, i = 1, f = 2, e = 3
"""

"""
a = "Life is too short, you need Python"
print(a[-2])

-2와 같은 숫자를 붙이면 뒤에서 부터 출력한다. 뒤에서 2번째 글자 'o' 출력
"""

"""
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)

단어를 뽑아내서 출력하는 것도 가능
"""

"""
a = "Life is too short, You need Python"
print(a[0:3])

- 이렇게 하면 Lif 출력 / 이유는 이런 슬라이싱은 끝번호를 제외하고 표현하기 때문
0 <= a < 3을 표현하는거라 3은 초과 범위라 안들어감

a = "Life is too short, You need Python"
print(a[0:4])

==> Life 출력

이게 맞는 표현

만약 a[19:]
이렇게 끝 번호를 지정 안하면 자연스럽게 마지막 번호까지 출력

반대로 a[:17]
이렇게 하면 처음부터 지정 숫자까지만 출력

그럼 a[:]?
이건 그냥 다 출력 (그럼 이건 왜 쓰는거지?)

a[19:-7]
여기서도 마찬가지로 -7같은 거 사용가능
"""

"""
a = "20260319sunny"
year = a[0:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)

이런식으로 나눠서 쓰는 것도 가능(이게 되네)
"""

"""
num = 10
print("I eat %d apples" % num)

문자열 포매팅

이건 왠지 C언어 printf랑 비슷하단 느낌을 받음
"""

"""
num = 6
name = "KJH"
print("My favorite number is %d, My name is %s" %(num, name))

이런 형태로 2개의 변수를 넣는 것도 되더라, 근데 문자 넣는게 C는 %c로 하던데 파이썬은 %s로 하네
형태는 비슷해도 다른 부분은 다르긴하다.
"""



