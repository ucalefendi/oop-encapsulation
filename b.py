####python encapsulation

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.login = name.lower() 
        self.__password = f"{name.lower()}_{age*2}"

    # @property
    def __get_password(self):
        return self.__password    


    def change_password(self,old_pwd,new_pwd):
        if old_pwd == self.__password:
            self.__password = new_pwd
            return self.__get_password()
        else:
            return "Old password is incorrect"



class Person(User):
    ...  # Inherits from User but does not add any new functionality


# person = Person("John", 30)
# print(person.__get_password())    







# user1 = User("Alim",25)
# print(user1.name)
# user1.name = "Ali"
# print(user1.name)
# print(user1.__password)
# print(user1._User__password)  # Accessing private variable using name mangling
# user1._User__password = "new_password"  # Changing the private variable
# print(user1._User__password)  # Accessing the changed private variable
# print(user1.get_password()) # Using the getter method to access the private variable
# user1.get_password = "another_password" #changed
# print(user1.get_password)  
# print(user1.change_password("alim_50", "new_password_123"))




class AdminUser:
    def __init__(self,name,age):
        self.name = name
        self.age = age


admin = AdminUser("Admin", 30)        