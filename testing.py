import math

def func(a,b,c):
    return a/(c-b) + math.log(a*math.sqrt(b-c))

def heand(a,b,c):
    try:
        result = func(a,b,c)
        print(result)
    except(ZeroDivisionError):
        print('Деление на ноль')
        result = 'Деление на ноль'
    except(TypeError):
        print('Ошибка типов данных')
        result = 'Ошибка типов данных'
    except(ValueError):
        print('Извлечение корня из отрицательного числа')
        result = 'Извлечение корня из отрицательного числа'
    except Exception as e:
        print(f"Тип ошибки: {e}")
        result = f"Тип ошибки: {e}"
    return result

heand(1,2,8)

''' 1- три положительных одинаковых +
    2- три отрицательных одинаковых +
    3- три положительных разных +
    4- три отрицательных разных +
    5- два положительных одно отриц +
    6- два отриц одно положит +
    7- два положит один нуль +
    8- два отриц один нуль +
    9- три нуля +
    10- пустой ввод +
    11- разные типы данных +
    12- дробные и целые +
    13- str +
'''

'''def test_eq_int():
    assert func(1,1,1) == 'Деление на ноль'
    assert func(0,0,0) == 'Деление на ноль'
    assert func(-1,-1,-1) == 'Деление на ноль'

def test_pos_zero():
    assert func(1,2,0) == -0.1534264097200273

def test_neg_zero():
    assert func(-1,-2,0) == 'Извлечение корня из отрицательного числа'


def test_float_int():
    assert func()'''
    
