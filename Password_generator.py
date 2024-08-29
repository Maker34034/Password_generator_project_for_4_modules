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

def generate_random_password(length):
    chars = '+-/*!&$#?=@<>[]{}''"":;`~^()abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890' 
    password =''                                
    for i in range(int(length)):                 
        password += random.choice(chars)         
    print('Сгенерированный пароль:', password)  

def generate_password_only_number(length):
    chars = '1234567890'
    password =''    
    for i in range(int(length)):
        password += random.choice(chars)
    print('Сгенерированный пароль:', password)

def generate_password_only_specal_simvols(length):
    chars = '+-/*!&$#?=@<>[]{}''"":;`~^()'
    password =''    
    for i in range(int(length)):
        password += random.choice(chars)
    print('Сгенерированный пароль:', password)

def generate_password_with_letters_only(length):
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    password =''    
    for i in range(int(length)):
        password += random.choice(chars)
    print('Сгенерированный пароль:', password)

def generate_password_with_letters_and_numbers(length):
    chars = '1234567890abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
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
            password = generate_password_with_letters_and_numbers(length)
        
        elif password_type == '2':
            password = generate_password_only_number(length)
        
        elif password_type == '3':
            password = generate_password_only_specal_simvols(length)
        
        elif password_type == '4':
            password = generate_password_with_letters_only(length)
        
        elif password_type == '5':
            password = generate_random_password(length)
        
        else: 
            print("Неверный выбор. Попробуйте снова.") 

main() 