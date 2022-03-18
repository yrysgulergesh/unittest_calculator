# написать функцию calculator, ко торая принимает на вход строку, содержащую два целых числа и один знак арифметической 
# операции + - / * и возвращает результат выполнения этой операции. Если числа не целые или нет знака операции то бросать # исключение ValueError


def calculator(expression):
    allowed = "+-/*"
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Выражение должно содержать хотя бы один знак ({allowed})')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                return {
                    '+': lambda a,b: a+b,
                    '-': lambda a,b: a-b,
                    '*': lambda a,b: a*b,
                    '/': lambda a,b: a/b,
                }[sign](left, right)
                # if sign=='+':
                #     return left+right
                # elif sign=='-':
                #     return left-right
                # elif sign=='*':
                #     return left*right
                # elif sign=='/':
                #     return left/right
            except (ValueError, TypeError):
                raise ValueError('Выражение должно содержать 2 целых числа и 1 знак')



if __name__ == '__main__':
    print(calculator('10/2'))