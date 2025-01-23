import turtle

running = True  # Глобальний прапорець для відстеження стану програми


def draw_koch_segment(t, length, level):
    """Draws a single segment of the Koch snowflake."""
    global running
    if not running:  # Перевірка, чи програма активна
        return
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_segment(t, length, level - 1)
        t.left(60)
        draw_koch_segment(t, length, level - 1)
        t.right(120)
        draw_koch_segment(t, length, level - 1)
        t.left(60)
        draw_koch_segment(t, length, level - 1)


def draw_koch_snowflake(t, length, level):
    """Draws the entire Koch snowflake."""
    global running
    for _ in range(3):
        if not running:  # Зупинити малювання, якщо програма завершена
            break
        draw_koch_segment(t, length, level)
        t.right(120)


def on_close():
    """Handles the closure of the turtle window."""
    global running
    print("Closing Turtle screen.")
    running = False
    turtle.bye()  # Закрити вікно Turtle


def main():
    global running

    # Запит рівня рекурсії у користувача
    try:
        level = int(input("Enter recursion level for Koch snowflake (default is 3): ") or 3)
    except ValueError:
        print("Invalid input. Using default level 3.")
        level = 3

    # Set up the turtle
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.title("Koch Snowflake")

    # Налаштування вікна для відкриття у розгорнутому стані
    root = screen._root
    root.attributes("-topmost", True)  # Вікно завжди зверху
    root.attributes("-topmost", False)  # Відключити "завжди зверху", після фокусу
    root.state("zoomed")  # Розгорнути вікно

    # Реєстрація функції закриття вікна
    root.protocol("WM_DELETE_WINDOW", on_close)

    t = turtle.Turtle()
    t.speed(0)  # Set the turtle speed to the fastest
    t.hideturtle()  # Hide the turtle for faster drawing

    # Move the turtle to the starting position
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    # Draw the Koch snowflake
    try:
        draw_koch_snowflake(t, 400, level)
        if running:  # Перевірити, чи вікно ще активне
            screen.mainloop()
    except turtle.Terminator:
        print("Turtle screen was closed before drawing finished.")
    finally:
        print("Program has ended.")

if __name__ == "__main__":
    main()
