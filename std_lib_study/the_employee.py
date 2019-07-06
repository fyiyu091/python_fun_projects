class Employee:
    def __init__(self, age, salary):
        self._age = age
        self._salary = salary
    
    @property
    def age(self):
        return self._age
    
    @property
    def salary(self):
        return self._salary
    
    @age.setter
    def age(self, age):
        self._age = age
    
    @salary.setter
    def salary(self, salary):
        self._salary = salary


def main():
    james = Employee(25, 60000)
    kobe = Employee(30, 70000)
    print(james.age)
    print(kobe.salary)
    kobe.salary = 1000000
    print(kobe.salary)

if __name__ == "__main__":
    main()