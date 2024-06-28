N = int(input()) # создаем число случайное в диапазоне
print(N, "- Число N")
arr = list(map(int, input().split(None, N) [:N]))

class C:
    def rev(arr): 
        return arr.reverse()

C.rev(arr)
print(arr)


# import random

# N = random.randint(1,100000) # создаем число случайное в диапазоне
# print(N, "- Число N")
# arr = [random.randint(1, 10000000000).split for i in range(N)]
# arr.reverse() # переворачиваем массив
# print(*arr)