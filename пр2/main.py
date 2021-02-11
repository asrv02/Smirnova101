# Задание 3
a = "Путешествия"
print(a[2])
print(a[-2])
print(a[0:5])
print(a[0:9])
print(a[::2])
print(a[1::2])
print(a[::-1])
print(a[-1::-2])
print(len(a))

# Задание 2
d = int(input("День"))
m = int(input("Месяц"))
year = int(input("Год"))
c = year//100 #Количество столетий
y = (year - c)%100 #Номер года в столетии
p = (d+((13*m-1)//5)+y+(y//4+c//4-2*c+777))%7
print(p)

