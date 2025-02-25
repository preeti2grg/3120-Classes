class Animal:
    def __init__(self, name, type, sound, age, play):
        self.__name = name 
        print("hello, I am", self.__name)
        self.__type= type
        self.__sound= sound
        self.__age= age
        self.__play= play

    def talk(self):
        print("hi")

    def play (self):
        print(f"{self.__name} plays {self.__play} for hours!")

    def age (self):
        print(f"{self.__name} is {self.__age} years old!")

    def sound (self):
        print(f"{self.__name} {self.__sound} all night long.")

    def type (self):
        print(f"{self.__name} is a {self.__type}")