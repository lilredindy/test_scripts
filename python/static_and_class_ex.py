
####
#No, cls and MyClass aren't interchangeable unless you are positive that MyClass doesn't have any subclasses.
#The point of a @classmethod is to get the right class type if you call it through a subclass. 
#If you don't need the actual class type, then you can use @staticmethod instead.
#####


class Base:
    @classmethod
    def f(cls):
        print(f'class is {cls}')

class Sub(Base):
    pass

Sub.f()  # calls Base.f with cls=Sub


#############
#Though classmethod and staticmethod are quite similar, 
#there's a slight difference in usage for both entities: classmethod must have a reference 
#to a class object as the first parameter, whereas staticmethod can have no parameters at all.
#############

class Date(object):
    
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

date2 = Date.from_string('11-09-2012')
is_date = Date.is_date_valid('11-09-2012')