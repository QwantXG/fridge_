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
        print(f"{item.name} добавлен в холодильник.")

    def remove_item(self, name: str):
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(f"{name} убран из холодильника.")
                return
        print(f"{name} такого нет!")

    def show_items(self):
        if not self.items:
            print("холодильник пуст.")
        else:
            print("Внутри лнжит:")
            for item in self.items:
                print(f"- {item}")



if __name__ == "__main__":
    fridge = base()

    while True:
        print("\nвыберите действие:")
        print("1. добавить продукт")
        print("2. удалить продукт")
        print("3. показать что внутри")
        print("4. game over")

        choice = input("введите номер: ")

        if choice == "1":
            name = input("введите название продукта: ")
            fridge.add_item(food(name))
        elif choice == "2":
            name = input("введите название продукта для удаления: ")
            fridge.remove_item(name)
        elif choice == "3":
            fridge.show_items()
        elif choice == "4":
            print("больше нет холодильника.")
            break
        else:
            print("куда жмешь?)")
            
