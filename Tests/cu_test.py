import getpass

def user_id(user_list, name):
    for i in user_list:
        if i[0] == name:
            return i
    
        
def main():
    login_attepts_setting = 3
    user1 = ['ADMIN', 'admin', '123456', 1, 1]
    user2 = ['USER1', 'user', '123456789', 1, 0]
    user3 = ['USER2', 'user', '123', 1, 0]
    user_list = [user1, user2, user3]  
    name = 'USER1'
    print (user_id(user_list, name))
    
if __name__ == '__main__':
    main()