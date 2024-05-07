import turtle

def koch_snowflake(order, size):
    if order == 0:  # Базовий випадок: просто рисуємо пряму лінію
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(order-1, size/3)
            turtle.left(angle)

def main():
    # Налаштування вікна
    turtle.setup(800, 600)
    turtle.speed(0)  # Найвища швидкість
    turtle.penup()
    turtle.goto(-200, 100)  # Початкова позиція курсора
    turtle.pendown()

    # Введення рівня рекурсії користувачем
    order = int(input("Введіть рівень рекурсії для сніжинки Коха: "))

    # Створення трьох сторін сніжинки
    for _ in range(3):
        koch_snowflake(order, 300)
        turtle.right(120)

    # Завершення малювання
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
