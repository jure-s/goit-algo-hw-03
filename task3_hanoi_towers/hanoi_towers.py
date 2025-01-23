import turtle

running = True  # Глобальний прапорець для відстеження стану програми


def draw_rod(t, x, label, n_disks):
    """Draw a single rod at position x with a label and optionally show N disks."""
    if not running:
        return
    t.penup()
    t.goto(x, -150)
    t.pendown()
    t.goto(x, 100)
    t.penup()
    t.goto(x, 120)
    t.write(label, align="center", font=("Arial", 12, "bold"))
    if label == 'A':
        t.goto(x, -180)
        t.write(f"{n_disks} дисків", align="center", font=("Arial", 12, "normal"))


def draw_disk(t, disk, x, y):
    """Draw a disk with size proportional to its number (only outline)."""
    if not running:
        return
    width = 30 + disk * 20
    t.penup()
    t.goto(x - width // 2, y)
    t.pendown()
    t.setheading(0)  # Ensure the orientation is reset
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(20)
        t.left(90)
    t.penup()


def setup_visualization(state, n_disks):
    """Set up the Turtle visualization for the Tower of Hanoi."""
    if not running:
        return None, None
    screen = turtle.Screen()
    screen.setup(800, 400)
    screen.title("Tower of Hanoi Visualization")

    # Ensure the window opens in a maximized state
    root = screen._root
    root.attributes("-topmost", True)  # Bring the window to the top
    root.attributes("-topmost", False)  # Allow normal behavior after focusing
    root.state("zoomed")  # Maximize the window

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    # Draw the rods with labels and optional disk count
    rod_positions = {'A': -200, 'B': 0, 'C': 200}
    for rod, x in rod_positions.items():
        draw_rod(t, x, rod, n_disks if rod == 'A' else None)

    return screen, rod_positions


def update_visualization(state, rod_positions):
    """Update the visualization based on the current state."""
    global running
    if not running:
        return

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.clear()  # Clear previous drawings

    for rod, disks in state.items():
        x = rod_positions[rod]
        for i, disk in enumerate(disks):
            y = -150 + i * 20
            draw_disk(t, disk, x, y)


def on_close():
    """Handle the closure of the Turtle window."""
    global running
    print("Closing Turtle screen.")
    running = False
    turtle.bye()


def hanoi_towers(n, source, target, auxiliary, state, rod_positions):
    """Solve the Tower of Hanoi problem with visualization."""
    global running
    if not running:
        return

    if n == 1:
        # Move a single disk from source to target
        disk = state[source].pop()
        state[target].append(disk)
        update_visualization(state, rod_positions)
    else:
        hanoi_towers(n - 1, source, auxiliary, target, state, rod_positions)
        if not running:
            return
        disk = state[source].pop()
        state[target].append(disk)
        update_visualization(state, rod_positions)
        hanoi_towers(n - 1, auxiliary, target, source, state, rod_positions)


def main():
    global running
    try:
        n = int(input("Enter the number of disks: "))
        if n <= 0:
            raise ValueError("The number of disks must be a positive integer.")
    except ValueError as e:
        print(e)
        return

    # Initial state of the rods
    state = {
        'A': list(range(n, 0, -1)),  # All disks start on rod A
        'B': [],  # Rod B is empty initially
        'C': []   # Rod C is empty initially
    }

    print(f"Initial state: {state}")

    # Set up visualization
    screen, rod_positions = setup_visualization(state, n)
    if screen is None:
        return
    screen._root.protocol("WM_DELETE_WINDOW", on_close)  # Handle window close
    update_visualization(state, rod_positions)

    # Solve the problem with visualization
    hanoi_towers(n, 'A', 'C', 'B', state, rod_positions)

    print(f"Final state: {state}")
    if running:
        screen.mainloop()


if __name__ == "__main__":
    main()
