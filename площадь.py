import math as m;

a = str(input("""Здравствуйте. Я помогу Вам вычислить площадь
Введите:
1, если квадрат
2, если прямоугольник
3, если круг"""));
if a := 1:
    sq = int(input("Введите длину стороны квадрата: "));
    print(sq*sq);
elif a := 2:
    pu1 = int(input("Введите одну сторону прямоугольника: "));
    pu2 = int(input("И другую, пожалуйста: "));
    print(pu1*pu2);
elif a := 3:
    d = int(input("Введите диаметр: "));
    print(m.pi*2*d);
else:
    print("Упс... Неверный ввод. Перезапустите программу");
