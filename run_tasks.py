import os
import sys

def run_task1():
    print("\nRunning Task 1: File Sorter")
    source = input("Enter source directory (default: task1_file_sorter/source): ").strip() or "task1_file_sorter/source"
    destination = input("Enter destination directory (default: task1_file_sorter/destination): ").strip() or "task1_file_sorter/destination"
    os.system(f"python task1_file_sorter/file_sorter.py {source} {destination}")

def run_task2():
    print("\nRunning Task 2: Koch Snowflake")
    try:
        os.system("python task2_koch_snowflake/koch_snowflake.py")
    except Exception as e:
        print(f"An error occurred while running Task 2: {e}")

def run_task3():
    print("\nRunning Task 3: Hanoi Towers")
    try:
        os.system("python task3_hanoi_towers/hanoi_towers.py")
    except Exception as e:
        print(f"An error occurred while running Task 3: {e}")

def main():
    while True:
        print("\nSelect a task to run:")
        print("1. Task 1: File Sorter")
        print("2. Task 2: Koch Snowflake")
        print("3. Task 3: Hanoi Towers")
        print("0. Exit")

        try:
            choice = int(input("Enter the task number (0-3): "))
            if choice == 1:
                run_task1()
            elif choice == 2:
                run_task2()
            elif choice == 3:
                run_task3()
            elif choice == 0:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number between 0 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Exiting gracefully.")
            break

if __name__ == "__main__":
    main()
