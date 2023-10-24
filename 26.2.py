list1 = [10, 20, 20, 20, 30, 50, 70, 30]
my_dict = {"key_1": 500, "key_2": 400, "key_3": True, 4: 7}
b = 1
e = 12
str1 = 'max min mat second'

def function(a):
    try:
        if isinstance(a, list):
            len_ = len(a)
            s = sum(a)
            v = s / len_
            print("Среднее арифметическое чисел:")
            print(v)
        elif isinstance(a, dict):
            sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
            print(sorted_dict)
        elif isinstance(a, int):
            if a > 1:
                for i in range(2, a):
                    if (a % i) == 0:
                        print("Число не простое")
                        break
                else:
                    print("Число простое")
            else:
                print("Число не простое")
        elif isinstance(a, str):
            w = a.split()
            print(w)
            print(len(w))
            max_word = max(w, key=len)
            print("Наибольшее слово:", max_word)
        else:
            print("Невозможно обработать входные данные")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль")
    except ValueError:
        print("Ошибка: Некорректный ввод")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        print("Блок try завершил выполнение")
    print("Завершение программы")


function(list1)
function(my_dict)
function(e)
function(str1)
