class Person:
    def __init__(self, name: str, age: int) -> None:

        if not isinstance(name, str):
            raise TypeError(f"Name must be string type")

        if not isinstance(age, int):
            raise TypeError(f"Age must be integer type")

        if age < 0:
            raise ValueError(f"Age must be positive value")

        self.__name = name
        self.__age = age

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        if not isinstance(name, str):
            raise TypeError(f"Name must be string type")
        self.__name = name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age) -> None:
        if not isinstance(age, int):
            raise TypeError(f"Age must be integer type")

        if age < 0:
            raise ValueError(f"Age must be positive value")
        self.__age = age

    def __repr__(self) -> str:
        return f"Person('{self.name}', {self.age})"
