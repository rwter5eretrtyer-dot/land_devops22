import random


def choose_difficulty():
    print("\nВыбери уровень сложности:")
    print("1. Лёгкий (1-50)")
    print("2. Средний (1-100)")
    print("3. Сложный (1-500)")

    while True:
        try:
            choice = int(input("Твой выбор (1-3): "))
            if choice == 1:
                return 50
            if choice == 2:
                return 100
            if choice == 3:
                return 500
            print("Выбери 1, 2 или 3!")
        except ValueError:
            print("Пожалуйста, введи число от 1 до 3.")


def guess_number():
    max_number = choose_difficulty()
    number = random.randint(1, max_number)
    attempts = 0

    print(
        f"\nЯ загадал число от 1 до {max_number}. "
        "Попробуй угадать!"
    )

    while True:
        try:
            guess = int(input("Твоя догадка: "))
            attempts += 1

            if guess < number:
                print("Слишком мало! Попробуй ещё раз.")
            elif guess > number:
                print("Слишком много! Попробуй ещё раз.")
            else:
                print(
                    f"Поздравляю! Ты угадал число {number} "
                    f"за {attempts} попыток!"
                )
                break
        except ValueError:
            print("Пожалуйста, введи корректное число.")


if __name__ == "__main__":
    print("Игра «Угадай число» запущена.")
    guess_number()
