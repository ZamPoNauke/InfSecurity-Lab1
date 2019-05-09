import getpass
from cryptography.fernet import Fernet


def group_check(new_group):
    group_list = ['admin', 'user']
    for i in group_list:
        if i == new_group:
            return 1
    return 0

def username_check(user):
    for i in user_list:
        if user == i[0]:
            return 1
    return 0

def user_id(name):
    for i in user_list:
        if i[0] == name:
            return i

def strong_password(password): # если 8 символов, >3 букв и >3 цифр
    numbers = 0
    letters = 0   
    password_status = 0
    while password_status == 0:
        if len(password)>=8:
            for i in password:
                if i.isdigit(): numbers += 1
                else: letters += 1
            if numbers>2 and letters>2:
                return password
            else:
                print ('Пароль не подходит по символам. Попробуй еще раз')
                password = getpass.getpass('Password: ')
        else: password = getpass.getpass('Увеличь длину пароля: ')
    

def cp(user):
    password_status = 0
    login_attepts = 0
    new_password1 = str('')
    new_password2 = str('')
    password_conformity = 0
    while password_status != 1 and login_attepts<login_attepts_setting:
        login_attepts += 1
        password = getpass.getpass('Введи нынешний пароль пользователя: ')
        if password == cipher.decrypt(bytes(user[2], 'utf-8')).decode('utf-8'): # сравниваем введенный и хранимый пароли
            while password_conformity != 1:
                if debug >= 1: print(user)
                if user[4] == '1': 
                    new_password1 = strong_password(getpass.getpass('Создадим сложный пароль: '))
                    new_password2 = strong_password(getpass.getpass('Введи второй раз для проверки: '))
                else: 
                    new_password1 = getpass.getpass('Вводи любой пароль: ')
                    new_password2 = getpass.getpass('Введи второй раз для проверки: ')
                if new_password1 == new_password2:
                    print('Password changed!')
                    return cipher.encrypt((new_password1).encode('utf-8')).decode("utf-8")
                else: print('Passwords are different. Try again')
        else: print('Incorrect password. Try again')
    print('Смена пароля отмененна из-за ввода некорректного актуального пароля')


def vu():
    answer = input('All - весь список, User_name - информация по конкретному пользователю ')
    if answer == 'All':
        print('Выводим список всех сотрудников')
        for i in user_list:
            print(f"Имя: {i[0]}, группа: {i[1]}, активность: {i[3]}, ограничения пароля: {i[4]},")
    else:
        for i in user_list:
            if i[0] == answer:
                print(f"Имя: {i[0]}, группа: {i[1]}, активность: {i[3]}, ограничения пароля{i[4]},")


def cu():
    new_user = ['ADMIN', 'new_user', '', 0, 3]
    print('Создадим нового пользователя.')
    
    new_user[0] = input('Имя: ')
    while username_check(new_user[0]):
        print('Имя пользователя уже зарезервировано') 
        new_user[0] = input('Имя: ')
    
    new_user[1] = input('Группа (admin / user): ')
    while group_check(new_user[1]) != 1:
        print('Недопустимая группа')
        new_user[1] = input('Группа (admin / user): ')
        
    new_user[4] = int(input('Задать ограничения пароля? (0 / 1) '))
    while new_user[4] > 1:
        print('Недопустимые значения')
        new_user[4] = int(input('Задать ограничения пароля? (0 / 1) '))
    
    if new_user[4] == 1:
        new_user[2] = cipher.encrypt(strong_password(getpass.getpass('Создадим сложный пароль: ')).encode('utf-8')).decode("utf-8") # Функция определения сложного пароля. 
    else:
        new_user[2] = cipher.encrypt(getpass.getpass('Вводи любой пароль: ').encode('utf-8')).decode("utf-8")
        
    new_user[3] = input('Активировать? (0 / 1) ')
    
    print('New user Data')
    print(f"Имя: {new_user[0]}, группа: {new_user[1]}, активность: {new_user[3]}, сложный пароль: {new_user[4]} ")
    final = input('ok? (y/n)')
    if final == 'y':
        user_list.append(new_user)     
    


def pp():
    print('Смена политики пароля.')
    print('Внимание, политика будет активна только при следующей смене пароля!')
    name = input('Введи имя пользоателя, которому меняем пароль: ')
    user_id(name)[4] = int(input('Активировать (1) или нет (0) политику?: '))
    print('Done')
    
    
def bu():
    print('Блогировка логина пользователя.')
    name = input('Введи имя пользоателя которого хотите заблокировать: ')
    user_id(name)[3] = int(input('Блокировать вход(0) или разрешить логин (1) ?: '))
    print('Done')


def main():
    global debug
    debug = 0
    global cipher 
    cipher = Fernet("APM1JDVgT8WDGOWBgQv6EIhvxl4vDYvUnVdg-Vjdt0o=") #CryptoKey
    global login_attepts_setting
    login_attepts_setting = 3
     
    login_status = 0 # статус логина
    login_attepts = 0 # счетчик количества попыток ввода пароля
    
    global user_list 
    user_list = []
    user = 'nouser'
    user_status = 'user'
    password = ''
    
    # Имя пользователя, группа, пароль, статус активности записи, ограничение пароля
    # 123456, 123456789, 123
    
    with open("User_Info.txt") as f:
        for line in f:
            user_list.append([str(x) for x in line.split()])
    f.close()
    
    while login_status != 1 and login_attepts < login_attepts_setting:
        user = input('login: ')
        password = getpass.getpass('Password: ')
        login_attepts += 1
          
        for i in user_list:
            if debug >= 2:
                print ('----> Дебаг логина пользователя <----')
                print (i)
                print (user, i[0], i[3])  
                print (password, i[2]) 
            if user == i[0] and i[3] == '1': # проверка пользователя 
                if password == cipher.decrypt(bytes(i[2], 'utf-8')).decode('utf-8'):
                    print('Credentials right!')
                    login_status = 1
                    user_status = i[1]
                    personal_id = user_id(user)
        
        if login_status == 0 and login_attepts < (login_attepts_setting):
            print('Login Error. Try again')

    
    if login_status == 1:
        command = ''
        while command != 'q':
            command_status = 0 # для получения статуса выполнения команды
            command = input('Введи команду или help: ')
            if command == 'help':  
                print('--> Команды любого пользователя <--')
                print('cp - сменить пароль')
                print('q - выйти')
                print('--> Команды администратора <--')
                print('vu - просмотреть список всех пользователей их атрибуты')
                print('cu - создать нового пользователя')
                print('pp - включени и отключение политик паролей')
                command_status = 1
            if command == 'cp':
                if debug == 1: print(personal_id, personal_id[2])
                personal_id[2] = cp(personal_id) #передаем id пользователя и количество попыток
                command_status = 1
            if command == 'q': 
                with open("User_Info.txt", 'w') as f:
                    for line in user_list:
                        for word in line:
                            f.write(str(word) + ' ')
                        f.write('\n')
                f.close()
            if user_status=='admin': # Команды только для админа
                if command == 'vu': 
                    vu()
                    command_status = 1
                if command == 'cu': 
                    cu()
                    command_status = 1
                if command == 'pp': 
                    pp()
                    command_status = 1
                if command == 'bu': 
                    bu()
                    command_status = 1
                
            
            if command_status == 0 and command != 'q':
                print('Команда не распознана или у вас недостаточно привилегий')
            


if __name__ == '__main__':
    main()