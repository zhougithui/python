#! /usr/bin/evn python


class Student(object):
    __slots__ = ('__birth', '__age')

    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, value):
        self.__birth = value

    @property
    def age(self):
        return 2015 - self.__birth


if __name__ == '__main__':
    stu = Student()
    stu.birth = 1991
    print(stu.age)
