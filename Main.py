def cp():
    print('cp')

def vu(user_list):
    answer = input('All - весь список, User_name - информация по конкретному пользователю ')
    if answer == 'All':
        print('Выводим список всех сотрудников')
        for i in user_list:
            print(f"Имя: {i[0]}, группа: {i[1]}, активность: {i[3]}, ограничения пароля{i[4]},")
    else:
        for i in user_list:
            if i[0] == answer:
                print(f"Имя: {i[0]}, группа: {i[1]}, активность: {i[3]}, ограничения пароля{i[4]},")

def cu():
    print('cu')

def pp():
    print('pp')

def main():
    debug = 0
    
    login_status = 0 # статус логина
    login_attepts = 0 # счетчик количества попыток ввода пароля
    login_attepts_setting = 3
    user = 'nouser'
    user_status = 'user'
    password = '000'
    
    # Имя пользователя, группа, пароль, статус активности записи, ограничение пароля
    user1 = ['ADMIN', 'admin', '123456', 1, 0]
    user2 = ['USER1', 'user', '123456789', 1, 0]
    user3 = ['USER2', 'user', '123', 1, 0]
    user_list = [user1, user2, user3]
    while login_status != 1 and login_attepts<login_attepts_setting:
        user = input('login: ')
        password = input('password: ')
        login_attepts += 1
        for i in user_list:
            if debug >= 2: print (i)    
            if user == i[0] and i[3] == 1: # проверка пользователя
                if debug >= 2: print (i[0], user)  
                if password == i[2]:
                    print('Credentials right!')
                    login_status = 1
                    user_status = i[1]
        
        if login_status == 0 and login_attepts<(login_attepts_setting):
            print('Incorrect user or password. Try again')
        if debug >= 1:
            print (user, user_status, password)    
            print (login_status, login_attepts)
                   
   
    
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
                cp()
                command_status = 1
            if user_status=='admin': # Команды только для админа
                if command == 'vu': 
                    vu(user_list)
                    command_status = 1
                if command == 'cu': 
                    cu()
                    command_status = 1
                if command == 'pp': 
                    pp()
                    command_status = 1
            
            if command_status == 0 and command != 'q':
                print('Команда не распознана или у вас недостаточно привилегий')
            
            
            
            
            
            
            

        


if __name__ == '__main__':
    print()
    main()