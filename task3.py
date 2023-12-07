from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value: str):
        if not isinstance(value, str):
            raise TypeError

        super().__init__(value)

    def __eq__(self, __o):
        if not isinstance(__o, Name):
            return False

        return self.value == __o.value

    def __hash__(self):
        return hash(self.value)


class Phone(Field):
    def __init__(self, value: str):
        if not isinstance(value, str):
            raise TypeError
        if not (len(value) == 10):
            raise ValueError

        super().__init__(value)

    def __eq__(self, __o):
        # print(f"WE ARE IN PHONE({self.value}) and colling __eq__")
        if not isinstance(__o, Phone):
            return False

        return self.value == __o.value


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []

    # реалізація класу
    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        self.phones.remove(Phone(phone))

    def edit_phone(self, old_phone: str, new_phone: str):
        old_phone = Phone(old_phone)
        new_phone = Phone(new_phone)

        index = self.phones.index(old_phone)
        self.phones[index] = new_phone

    def find_phone(self, phone_number: str) -> Phone:
        phone_number = Phone(phone_number)
        index = self.phones.index(phone_number)
        return self.phones[index]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    # def __init__(self):
    #     self.data = {}  # <- from UserDict

    ...

    # реалізація класу
    def add_record(self, record: Record):
        self.data[record.name] = record

    def find(self, name: str) -> Record:
        name = Name(name)
        return self.data[name]

    def delete(self, name: str):
        name = Name(name)
        self.data.pop(name)

    def __str__(self):
        return f"AddressBook: ({') ('.join(str(p) for p in self.data.values())})"


if __name__ == '__main__':
    r = Record("Andrii")
    # Phone("9876543210") == Phone("0123456789")
    r.add_phone("0123456789")
    # r.remove_phone("0123456789")

    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)
    print("book after add John", book)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)
    print("book after add Jane", book)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print("book after John edit phone", book)
    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")

    # found_phone = john.find_phone("+380680000000")
    # found_phone = john.find_phone("+38(068) 0000 000")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
    print("book after delete Jane", book)
