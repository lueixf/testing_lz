from testing import func
import unittest



result =func(1,"",3,2,4)
   

"""
1. 2 положительных одинаковых числа в знаменателе +
2. все нули +
3. 2 отрицательных одинаковых числа в знаменателе +
4. разные числа в знаменателе +
5. отрицательное число под корнем +
6. текст +
7. пустой ввод +

"""


class Test_func(unittest.TestCase):

    def test_division_by_zerors(self):
        self.assertEqual(func(1,2,2),'Деление на ноль')
        self.assertEqual(func(1,-2,-2),'Деление на ноль')
    
    def test_all_zero(self):
        self.assertEqual(func(0,0,0),'Деление на ноль')

    def test_dif_num(self):
        self.assertEqual(func(1,2,-2),0.4431471805599453) 

    def test_neg_Cb_under_the_root(self):
        self.assertEqual(func(1,-3,-1), 'Извлечение корня из отрицательного числа')
    
    def test_pos_Cb_under_the_root(self):
        self.assertEqual(func(1,2,8), 'Извлечение корня из отрицательного числа')

    def test_neg_pos__under_the_root(self):
        self.assertEqual(func(1,), 'Извлечение корня из отрицательного числа')
    
    def test_str(self):
        self.assertEqual(func("a",0,1),'Ошибка типов данных')

    def test_zero_input(self):
        self.assertEqual(func("",0,3),'Ошибка типов данных')

if __name__ == "__main__":
    unittest.main() 