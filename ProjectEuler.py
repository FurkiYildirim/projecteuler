'''Project Euler Soru Cozumu'''

"""
Soru 1:
10'un altında 3 veya 5'in katı olan tüm doğal sayıları listelersek 3, 5, 6 ve 9 elde ederiz. Bu katların toplamı 23'tür.
1000'in altındaki 3 veya 5'in tüm katlarının toplamını bulun.
Cevap:
233168
"""


def soru1(): return sum((i for i in range(1000) if i % 3 == 0 or i % 5 == 0));

# print(soru1)

"""
Soru 2:
Fibonacci dizisindeki her yeni terim, önceki iki terimin eklenmesiyle oluşturulur. 1 ve 2 ile başlayarak, ilk 10 terim şöyle olacaktır:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Fibonacci dizisindeki değerleri dört milyonu geçmeyen terimleri dikkate alarak çift değerli terimlerin toplamını bulunuz.
Cevap:
4613732
"""
answer = []
answerDemo = []
a = 0
b = 1
def soru2(num1, num2):
    global answerDemo
    global a
    global b
    try:
        a = num2
        b = num1 + num2
        answerDemo.append(a)
        answerDemo.append(b)
        for i in range(1):
            soru2(a, b)
    except:
        for i in answerDemo:
            if i not in answer and i % 2 == 0 and i < 4000000:
                answer.append(i)
            else:
                ...

#soru2(a, b)
#print(sum(answer))

"""
Soru 3:
13195'in asal çarpanları 5, 7, 13 ve 29'dur.
600851475143 sayısının en büyük asal çarpanı kaçtır?

Kod çok uzun süre sonra yanıt döndürüyor
Cevap:
6857
"""
num = 600851475143
factors = []
def largestFact(num):
    def isPrime(n):
        for i in range(1, n+1):
            if (i != 1 and i != n) and n % i == 0:
                return False
            else:
                ...
        return True

    for i in range(2, num):
        if isPrime(i):
            if num % i == 0:
                factors.append(i)
                continue
            else:
                continue
        else:
            continue
# largestFact(num)
# print(factors)

"""
Soru 4:

"""