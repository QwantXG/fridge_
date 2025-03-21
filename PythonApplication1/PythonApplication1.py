class food:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class base:
    def __init__(self):
        self.items = []
    def add_item(self, item: food):
        self.items.append(item)
        print(f"{item.name} �������� � �����������.")

    def remove_item(self, name: str):
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(f"{name} ����� �� ������������.")
                return
        print(f"{name} ������ ���!")

    def show_items(self):
        if not self.items:
            print("����������� ����.")
        else:
            print("������ �����:")
            for item in self.items:
                print(f"- {item}")



if __name__ == "__main__":
    fridge = base()

    while True:
        print("\n�������� ��������:")
        print("1. �������� �������")
        print("2. ������� �������")
        print("3. �������� ��� ������")
        print("4. game over")

        choice = input("������� �����: ")

        if choice == "1":
            name = input("������� �������� ��������: ")
            fridge.add_item(food(name))
        elif choice == "2":
            name = input("������� �������� �������� ��� ��������: ")
            fridge.remove_item(name)
        elif choice == "3":
            fridge.show_items()
        elif choice == "4":
            print("������ ��� ������������.")
            break
        else:
            print("���� �����?)")
            