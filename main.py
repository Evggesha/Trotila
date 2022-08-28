# Задача про треугольники
storona1 = 5
storona2 = 10
storona3 = 15
if storona1 == storona2 == storona3:
    print("Треугольник равносторониий")
elif storona1 < storona2 > storona3:
    print("Треугольник разносторонний")
else:
    print("Такого треугольника не существует")
# Возраст человека
n1 = input("Введите свой возраст:")
if 0==int(n1[:-2:-1])>=5:
    print("Вам " + str(n1)+" лет")
elif 2<=int(n1[:-2:-1])<5:
    print("Вам " + str(n1)+" года")
else:
    print("Вам " + str(n1)+" год")
