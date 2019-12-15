import random 
import string

global users_list
class User:
    '''
    Class to create user accounts and save user information
    '''

    users_list = []
    def __init__(self,realname,password):
        '''
        Constructor defines properties each user object holds
        '''

        self.realname = realname
        self.password = password

    def save_user(self):
        '''
        Method saves newly created user instance
        '''
        User.users_list.append(self)


        

