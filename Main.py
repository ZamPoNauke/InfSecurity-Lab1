import getpass


def group_check(new_group):
    group_list = ['admin', 'user']
    for i in group_list:
        if i == new_group:
            return 1
    return 0

def username_check(user_list, user):
    for i in user_list:
        if user == i[0]:
            return 1
    return 0

def user_id(user_list, name):
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
    

def cp(user, login_attepts_setting):
    password_status = 0
    login_attepts = 0
    new_password = ''
    while password_status != 1 and login_attepts<login_attepts_setting:
        login_attepts += 1
        password = getpass.getpass('Введи нынешний пароль пользователя: ')
        if password == user[2]:
            if user[4] == 1: new_password = strong_password(getpass.getpass('Создадим сложный пароль: '))
            else: new_password = getpass.getpass('Вводи любой пароль: ')
            print('Password changed!')
            return new_password
        else: print('incorrect password. Try again')
    print('Смена пароля отмененна из-за ввода некорректного актуального пароля')


def vu(user_list):
    answer = input('All - весь список, User_name - информация по конкретному пользователю ')
    if answer == 'All':
        print('Выводим список всех сотрудников')
        for i in user_list:
            print(f"Имя: {i[0]}, группа: {i[1]}, активность: {i[3]}, ограничения пароля: {i[4]},")
    else:
        for i in user_list:
            if i[0] == answer:
                print(f"Имя: {i[0]}, группа: {i[1]}, активность: {i[3]}, ограничения пароля{i[4]},")


def cu(user_list):
    new_user = ['ADMIN', 'new_user', '', 0, 3]
    print('Создадим нового пользователя.')
    
    new_user[0] = input('Имя: ')
    while username_check(user_list, new_user[0]):
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
        new_user[2] = input('Введи сложный пароль: ') # Функция определения сложного пароля. 
    else:
        new_user[2] = input('Введи любой пароль: ')
        
    while new_user[3] > 1:
        new_user[3] = input('Активировать? (0 / 1) ')
    
    print('New user Data')
    print(f"Имя: {new_user[0]}, группа: {new_user[1]}, активность: {new_user[3]}, ограничения пароля{new_user[4]},")


def pp(user_list):
    print('Смена политики пароля.')
    print('Внимание, политика будет активна только при следующей смене пароля!')
    name = input('Введи имя пользоателя, которому меняем пароль: ')
    user_id(user_list, name)[4] = int(input('Активировать (1) или нет (0) политику?: '))
    
    
def bu(user_list):
    print('Блогировка логина пользователя.')
    name = input('Введи имя пользоателя которого хотите заблокировать: ')
    user_id(user_list, name)[3] = int(input('Блокировать вход(0) или разрешить логин (1) ?: '))


def main():
    debug = 0
    login_status = 0 # статус логина
    login_attepts = 0 # счетчик количества попыток ввода пароля
    login_attepts_setting = 3
    user = 'nouser'
    user_status = 'user'
    password = '000'
    
    # Имя пользователя, группа, пароль, статус активности записи, ограничение пароля
    user_list = []
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
                print (i)
                print (user, i[0], i[3])  
                print (password, i[2]) 
            if user == i[0] and i[3] == '1': # проверка пользователя 
                if str(password) == i[2]:
                    print('Credentials right!')
                    login_status = 1
                    user_status = i[1]
                    personal_id = user_id(user_list, user)
        
        if login_status == 0 and login_attepts < (login_attepts_setting):
            print('Incorrect user or password. Try again')

    
    command = 'pass'
    
    if login_status == 1:
        while command != 'q':
            command_status = 0 # для получения статуса выполнения команды
            command = input('Введи команду: ')
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
                personal_id[2] = cp(personal_id, login_attepts_setting) #передаем id пользователя и количество попыток
                command_status = 1
            if user_status=='admin': # Команды только для админа
                if command == 'vu': 
                    vu(user_list)
                    command_status = 1
                if command == 'cu': 
                    cu(user_list)
                    command_status = 1
                if command == 'pp': 
                    pp(user_list)
                    command_status = 1
                if command == 'bu': 
                    bu(user_list)
                    command_status = 1
            
            if command_status == 0 and command != 'q':
                print('Команда не распознана или у вас недостаточно привилегий')
            


if __name__ == '__main__':
    main()