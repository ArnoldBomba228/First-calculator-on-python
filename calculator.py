def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    print('Добро пожаловать в калькулятор!')
    
    
    try:
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число: '))
        operation = input('Выберите операция (+, -): ')
        
        if operation == '+':
            
            result = add(num1, num2)
            
            print(f'Результат: {num1} + {num2} = {result}')
            
        elif operation == '-':
            
            result = subtract(num1, num2)
            
            print(f'Результат: {num1} - {num2} = {result}')
            
        else:
            print('Неизвестная операция!')
            
    except ValueError:
        
        print('Ошибка: введите числа корректно!')

if __name__ == '__main__':
    main()