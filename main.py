import random

def play_game():
    number_to_guess = random.randint(1, 100)  # Генерируем случайное число от 1 до 100
    max_attempts = 10  # Ограничиваем количество попыток
    attempt_count = 0

    print("Привет! Я загадал число от 1 до 100. Попробуй его угадать.")

    while attempt_count < max_attempts:
        attempt_count += 1
        try:
            guess = int(input(f"Попытка {attempt_count}: Введите число: "))
        except ValueError:
            print("Неверный ввод. Введите целое число.")
            continue

        if guess < number_to_guess:
            print("Ваше число меньше загаданного.")
        elif guess > number_to_guess:
            print("Ваше число больше загаданного.")
        else:
            print(f"Правильно! Вы угадали число {number_to_guess} за {attempt_count} попыток.")
            return

    print(f"\nК сожалению, вы использовали все {max_attempts} попыток.\nПравильное число было: {number_to_guess}")

if __name__ == "__main__":
    play_game()
