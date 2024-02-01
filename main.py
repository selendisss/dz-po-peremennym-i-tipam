#экспериментирую с переводом данных в различные типы данных
x = 5.65
print(int(x))
x = 5
print(float(x))
x = 5
print("x=" + str(x))
#ввожу своё имя и фамилию
NameSurname = input("Введите ваше имя и фамилию: ")
print("Ваше имя и фамилия — " + NameSurname)
#считаю сумму трёх целых чисел
IntegerOne = int(input("Введите x — "))
IntegerTwo = int(input("Введите y — "))
IntegerThree = int(input("Введите z — "))
print("Сумма чисел x, y, z равна " + str(IntegerOne+IntegerTwo+IntegerThree))
#считаю сумму трёх дробных чисел
FloatOne = float(input("Введите x — "))
FloatTwo = float(input("Введите y — "))
FloatThree = float(input("Введите z — "))
print("Сумма чисел x, y, z равна " + str(FloatOne+FloatTwo+FloatThree))
#вывожу предыдущее и следуещее какому-либо числу
x = int(input("Введите x — "))
y = x - 1
z = x + 1
print("Число, предшествующее числу " + str(x) + ", равно " + str(y))
print("Число, следующее за числом " + str(x) + ", равно " + str(z))
#вывожу имя и возраст человека
Name = input("Введите ваше имя — ")
Age = input("Введите ваш возраст — ")
print("Привет, " + Name + "! Ваш возраст — " + Age)
#использую метод replace() для замены всех вхождений в строке
StringOne = input("Введите фразу «Меня зовут Андрей и мне нравится имя Андрей» — ")
StringTwo = StringOne.replace("Андрей", "Валентин")
print("А вот если бы вас звали Валентин, фраза была бы такой: " + StringTwo)
#привожу строку к верхнему и нижнему регистру соответственно
string = input("Введите фразу «Hello World!» — ")
StringUpper = string.upper()
StringLower = string.lower()
print("Ваша фраза в верхнем регистре выглядит так: " + StringUpper + ", а в нижнем регистре — так: " + StringLower)






