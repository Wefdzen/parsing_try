class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def see_fullname(self):
         print(f'Your full name is: {self.first_name} {self.last_name}')

    def say_what_you_goodman(self):
        print('You good :3')


man = Person("Dima", "IDk")
man.see_fullname()
man.say_what_you_goodman()