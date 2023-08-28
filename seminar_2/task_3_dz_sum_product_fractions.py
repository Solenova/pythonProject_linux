# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

a = (input("Введите первую дробь вида m/n: "))
b = (input("Введите вторую дробь вида m/n: "))

numerator1, denominator1 = map(int, a.split('/'))
numerator2, denominator2 = map(int, b.split('/'))


a_f = Fraction(numerator1, denominator1)
b_f = Fraction(numerator2, denominator2)

print(a_f, ' + ', b_f, ' = ', a_f+b_f)
print(a_f,' * ', b_f, ' = ', a_f*b_f)

def NOD(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a
def mult(numerator1, denominator1, numerator2, denominator2 ):
    numerator_res = numerator1 * numerator2
    denominator_res = denominator1 * denominator2
    nod_res = NOD(numerator_res, denominator_res)
    if nod_res != 0:
        numerator_res /= nod_res
        denominator_res /= nod_res
    result = str(int(numerator_res))+'/'+str(int(denominator_res))
    return result

def summa(numerator1, denominator1, numerator2, denominator2) ->str:
    summ_numerator = (numerator1*denominator2+numerator2*denominator1)
    summ_denominator = denominator1*denominator2

    nod_res = NOD(summ_numerator,summ_denominator)
    if nod_res != 1:
4/8
7/2summ_numerator /= nod_res
        summ_denominator /= nod_res
    summ = str(int(summ_numerator)) + '/' + str(int(summ_denominator))
    return summ
print(f'Сумма дробей {summa(numerator1, denominator1, numerator2, denominator2)}')
print(f'Произведение дробей {mult(numerator1, denominator1, numerator2, denominator2)}')



# -------------2 method
# import fractions
#
# a_1 = ""
# a_2 = ""
# b_1 = ""
# b_2 = ""
# fraction_1 = input("Введите первую дробь в виде 'a/b': ")
# fraction_2 = input("Введите вторую дробь в виде 'a/b': ")
# a_1 = int(fraction_1[0])
# a_2 = a_2_2 = int(fraction_1[2])
# b_1 = int(fraction_2[0])
# b_2 = int(fraction_2[2])
# print("Произведение дробей равно: ", a_1 * b_1,"/", a_2 * b_2)
#
# if a_2 != b_2:
#     a_1 *= b_2
#     a_2 *= b_2
#     b_1 *= a_2_2
#     b_2 *= a_2_2
#     print("Сумма дробей равна: ", a_1 + b_1,"/", a_2)
#
# else:
#     print("Cумма дробей равна: ", a_1 + b_1,"/", a_2)
#
# fraction_1 = fractions.Fraction(a_1, a_2)
# fraction_2 = fractions.Fraction(b_1, b_2)
# print("Произведение дробей равно: ", fraction_1 * fraction_2)
# print("Cумма дробей равна: ", fraction_1 + fraction_2)