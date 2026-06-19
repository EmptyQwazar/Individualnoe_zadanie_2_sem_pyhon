from stack import evaluate
from tree import Tree


def task1():
    print("-" * 40)
    print("Задача 1: Вычисление выражения")
    print("  m(a,b) — минимум, M(a,b) — максимум")
    print("  Пример: M(15,m(16,8))")
    print("  Пустая строка — возврат в меню")
    print("-" * 40)

    while True:
        expr = input("Введите выражение: ").strip()
        if not expr:
            break
        allowed = set('mM(),0123456789')
        bad = [c for c in expr if c not in allowed]
        if bad:
            print(f"Ошибка: недопустимые символы {bad}")
            continue
        if expr.count('(') != expr.count(')'):
            print("Ошибка: скобки не сбалансированы")
            continue
        try:
            print("Результат:", evaluate(expr))
        except Exception as e:
            print(f"Ошибка: {e}")


def task2():
    while True:
        print("-" * 40)
        print("Задача 2: Почтальон Тритон")
        print("-" * 40)
        print("1. Загрузить файл и посчитать")
        print("2. Показать пример файла")
        print("3. В главное меню")
        choice = input("> ").strip()

        if choice == '1':
            filename = input("Имя файла: ").strip() or 'input.txt'
            try:
                with open(filename, encoding='utf-8') as f:
                    lines = f.readlines()
                if not lines:
                    print("Ошибка: файл пуст")
                    continue
                M = int(lines[0].strip())
                if M <= 0 or M >= 1000:
                    print("Ошибка: M должно быть от 1 до 999")
                    continue
                if len(lines) < M + 1:
                    print(f"Ошибка: строк {len(lines)}, нужно {M + 1}")
                    continue
                tree = Tree()
                for i in range(1, M + 1):
                    data = list(map(int, lines[i].split()))
                    tree.add_node(i, data[1], data[2:])
                print("Минимум извинений:", tree.min_apologies())
            except FileNotFoundError:
                print(f"Ошибка: файл '{filename}' не найден")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == '2':
            print("Пример input.txt:")
            print("5")
            print("3 2 2 5 4")
            print("1 1 1")
            print("1 1 4")
            print("2 2 3 1")
            print("1 3 1")

        elif choice == '3':
            break
        else:
            print("Ошибка: неверный пункт")


def main():
    while True:
        print("=" * 40)
        print("ГЛАВНОЕ МЕНЮ")
        print("=" * 40)
        print("1. Задача 1 — вычисление выражения")
        print("2. Задача 2 — почтальон Тритон")
        print("3. Выход")
        choice = input("> ").strip()
        if choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '3':
            print("Выход")
            break
        else:
            print("Ошибка: неверный пункт")


if __name__ == "__main__":
    main()