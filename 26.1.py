list1 = set("1234567890")
list2 = set("ABCDEFGHIJKLMNHOPQRSTUVWXYZ")
list3 = set("abcdefghijklmnhopqrstuvwxyz")
new_set = set()
password = str(input("Введите пароль :\n"))
print(list1)
print(list2)
print(list3)


def is_password_good(password):
    try:
        if len(password) < 8:
            raise Exception("Пароль должен содержать не менее 8 символов.")
        if not any(char in list2 for char in password):
            raise Exception("Пароль должен содержать хотя бы одну заглавную букву.")
        if not any(char in list1 for char in password):
            raise Exception("Пароль должен содержать хотя бы одну цифру.")
        return True
    except Exception as e:
        print("Проверка пароля не удалась:", e)
        return False
    finally:
        print("Блок try завершил выполнение")
    print("Завершение программы")


print(is_password_good(password))
