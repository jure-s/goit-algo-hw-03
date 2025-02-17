# Проєкт: goit-algo-hw-03

Цей проєкт містить рішення до трьох алгоритмічних завдань:

1. **Сортувальник файлів**
2. **Сніжинка Коха**
3. **Ханойські вежі**

## Як запустити проєкт

Для запуску проєкту виконайте файл `run_tasks.py`, який знаходиться в кореневій директорії:

```bash
python run_tasks.py
```

Вам буде запропоновано меню для вибору завдання:

1. Завдання 1: Сортувальник файлів
2. Завдання 2: Сніжинка Коха
3. Завдання 3: Ханойські вежі
0. Вихід

Введіть номер відповідного завдання для виконання.

---

## Завдання 1: Сортувальник файлів

### Опис
Рекурсивно копіює файли з вихідної директорії до директорії призначення, сортує їх у піддиректорії на основі розширення файлів.

### Використання
1. Оберіть **Завдання 1** з меню.
2. Вкажіть вихідну та директорію призначення, коли вас попросять.
   - Якщо ввід пропущено, за замовчуванням використовуються:
     - Вихідна директорія: `task1_file_sorter/source`
     - Директорія призначення: `task1_file_sorter/destination`

Приклад:
```
Enter source directory (default: task1_file_sorter/source):
Enter destination directory (default: task1_file_sorter/destination):
```

---

## Завдання 2: Сніжинка Коха

### Опис
Генерує фрактал сніжинки Коха за допомогою графіки Turtle.

### Використання
1. Оберіть **Завдання 2** з меню.
2. Вкажіть рівень рекурсії для сніжинки (за замовчуванням: 3).

Приклад:
```
Enter recursion level for Koch snowflake (default is 3): 4
```

Фрактал буде намальований у графічному вікні Turtle. Ви можете закрити вікно в будь-який момент.

---

## Завдання 3: Ханойські вежі

### Опис
Симулює та візуалізує рішення задачі Ханойських веж за допомогою графіки Turtle.

### Використання
1. Оберіть **Завдання 3** з меню.
2. Вкажіть кількість дисків для головоломки, коли вас попросять.

Приклад:
```
Enter the number of disks: 5
```

Кроки для вирішення Ханойських веж будуть візуалізовані у вікні Turtle. Ви можете закрити вікно в будь-який момент, і програма завершиться коректно.

---

## Структура проєкту

```
project/
├── task1_file_sorter/
│   ├── file_sorter.py
│   ├── source/  # Вихідна директорія за замовчуванням
│   ├── destination/  # Директорія призначення за замовчуванням
├── task2_koch_snowflake/
│   ├── koch_snowflake.py
├── task3_hanoi_towers/
│   ├── hanoi_towers.py
├── tests/
│   ├── test_file_sorter.py
│   ├── test_koch_snowflake.py
│   ├── test_hanoi_towers.py
├── run_tasks.py  # Точка входу для запуску завдань
├── README.md
```

---

## Вимоги

- Python 3.10+
- Графіка Turtle (вбудована бібліотека Python)

Для встановлення додаткових залежностей (якщо вони є):

```bash
pip install -r requirements.txt
```

---