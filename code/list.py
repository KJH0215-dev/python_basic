"""a = [1, 2, 3]
print(a[0])

리스트 기본 + 문자역 인덱싱
"""
"""
a = [1,2 ,3 , 4,5]
print(a[2]+a[4])

인덱싱한 값끼리 더하기도 가능
"""

"""
a= [1, 2,3 ,4, 5, 6]
print(a[-3])

-3과 같은 음수 넣었을 때 뒤에서부터 출력되는 것도 같음
"""

"""
a = [1, 2, 3, ['b', 'c', 'd']]
print(a[-1])

리스트 안에 리스트

"""

"""
a = [1, 2, 3,['b', 'c', 'd']]
print (a[-1][2])

리스트 안에서의 안에서도 값을 뽑아낼 수 있다.
"""

"""
a = [1, 2, 3,['b',['life', 'is', 'too', 'short'], 'c']]
print(a[-1][1][3])

고로 이런 3중 리스트도 가능
"""

"""
a = [1, 2, 3, 4, 5]
print(a[0:3])

이런식으로 슬랑이싱 역시 가능

+
a = [1, 2, 3, 4, 5]
b = a[:3]
c = a[2:]

print(b)
print(c)
"""

"""
a = [1, 2, ['b', 'c', 'd', ['Life', 'is', 'short']], 3, 4, 5]
print(a[1:4])
print(a[2][3][0:3])

중첩된 list에 슬라이싱 하기 가능
"""

"""
a = [1, 2, 3, 4]
b = ['c', 'd', 'e'] 
print(a + b)

list끼리 더하기 
"""

"""
address = ['강서구', '강동구', '강남구', '강북구']
pizza_mart =['도미노피자', '피자헛', '59쌀 피자', '알볼로']
num = [1, 2, 3, 4]

print(str(address[0]) + '의' + str(pizza_mart[2]) + "점포 갯수는"+ str(num[2]) +"개 입니다.")

list str을 활용 예제
"""

"""a = [1, 2, 3]
a[2] = '앙'
print(a)

list의 수정과 삭제
"""

"""
a=[1, 2, 3, 4]

while True:

    print("바꾸면 되돌릴 수 없어요.\n")
    choice = input("바꾸시겠습니까? :")

    if choice == "y":
        a[2] = '앙'
        print(a[2])
    elif choice == "0":
        print("이야 이걸 안바꾸네..ㅉ")
        break
    else:
        print("Are you kiddig me?")


이야 이게 되네
"""

""""""
a = [1, 2, '앙', 3, 4]

choice = input("y를 누르면 이상한걸 없앨 수 있어요! :")

if choice == "y":
    del a[2]
    print("와 참 잘하셨어요!")
    print(a)
else:
    print("독하다 독해 이걸 안 없애?!")
    print(a)








