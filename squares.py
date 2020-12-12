import math

quest1 = str(input(print("Площадь чего Вы желаете вычистить? Варианты: Квадрат, Прямоугольник, Окружность")))

if (quest1 == "Квадрат"):
    a = float(input(print("Введите сторону квадрата в сантиметрах")))
    print(a**2, "см")
elif (quest1 == "Прямоугольник"):
    b = float(input(print("Введите большую сторону прямоугольника в сантиметрах")));
    b1 = float(input(print("И меньшую сторону в сантиметрах")));
    print(b*b1);
elif (quest1 == "Окружность"):
    c = float(input(print("Введите радиус в сантиметрах")));
    print(c*2*math.pi);
