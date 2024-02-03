import string
import random
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
password_length = int(input("Введите длинну пароля: "))
generated_password = generate_password(password_length)
print("Пароль:", generated_password)