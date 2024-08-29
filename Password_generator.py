import random 

def description(): 
    print()
    print("Вы попали в «Генератор сложных паролей». В функционал программы включаетсоздание пароля по следующим условиям:")
    print("1. Длина пароля: любая, которую вы укажете.")
    print("2. Пароль может содержать:")
    print("- буквы разного регистра и цифры;")
    print("- только буквы разного регистра;")
    print("- буквы, цифры и спецсимволы.")
    print("3. Программа умеет создавать пять типов паролей по условиям.")
    print('Чтобы выйти из программы, нужно в строке "Введите номер типа пароля:" написать "stop"')

def Types_of_password(): 
    print()
    print('1 - Буквы разного регистра и цифры') 
    print('2 - Только цифры')
    print('3 - Только спецсимволы')
    print('4 - Только буквы разного регистра')
    print('5 - Буквы, цифры и спецсимволы') 

def generate_password(length, chars):
    password =''                                 
    for i in range(int(length)):                   
        password += random.choice(chars)         
    print('Сгенерированный пароль:', password)   

def main():  
    print()           
    description() 

    while True: 
        print()
        length = input('Введите длину пароля: ') 

        if int(length) <= 0: 
            print('Длина пароля должна быть положительным числом. Попробуйте снова.')
            continue

        Types_of_password() 
        print()
        password_type = input("Введите номер типа пароля: ") 
        if password_type == 'stop': 
            break        

        if password_type == '1': 
            chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890' 
            generate_password(length, chars)

        elif password_type == '2':
            chars = '1234567890' 
            generate_password(length, chars)

        elif password_type == '3':
            chars = '+-/*!&$#?=@<>[]{}''"":;`~^()' 
            generate_password(length, chars)

        elif password_type == '4':
            chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890' 
            generate_password(length, chars)

        elif password_type == '5':
            chars = '+-/*!&$#?=@<>[]{}''"":;`~^()abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890' 
            generate_password(length, chars)

        else: 
            print("Неверный выбор. Попробуйте снова.") 
main() 