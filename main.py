import random

secret_number = random.randint(1, 100)
guesses = []

while True:
    guess = input("Угадай число от 1 до 100: ")
    try:
        guess = int(guess)
        guesses.append(guess)
    
        if guess == secret_number:
            print(f"Победа! Ты угадал число {secret_number} за {len(guesses)} попыток.")
            break
        elif guess < secret_number:
            print("Загаданное число больше твоего.")
        else:
            print("Загаданное число меньше твоего.")
    except ValueError:
        print("Ошибка ввода. Нужно ввести число.")
