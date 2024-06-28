import random
print('максимальная грузоподъемность лодки (кг):')
m = random.randint(1,100) # получения случайного числа максимальной грузоподъемности 10е6(10 000 000)
n = random.randint(1,10) # создаем число рыбаков случайное в диапазоне
massa1n = [random.randint(1, m) for i in range(n)] # масса каждого рыбака
massa1n.sort() # сортировка значений массива по возростанию
count = 0 # колличество лодок

x = 0

while len(massa1n) > 1:
        x = 0
        summ = []
        summ.append(massa1n[0])
        summ.append(massa1n[-1])
        x = sum(summ)
        if x > m:
            massa1n.pop()
            print('один рыбак', massa1n)
            count += 1
        else:
            massa1n.pop(0)
            massa1n.pop()
            print('два рыбака', massa1n)
            count += 1
            
count += 1
print(massa1n)




print('Минимальное число лодок необходимое для переправы всех рыбаков: ', count)