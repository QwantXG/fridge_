class food: #почему не utf8(
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name


class base:
    def __init__(self):
        self.items = []
    def add_item(self, item: food):
        self.items.append(item)
        print(f"{item.name} äîáàâëåí â õîëîäèëüíèê.")

    def remove_item(self, name: str):
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(f"{name} óáðàí èç õîëîäèëüíèêà.")
                return
        print(f"{name} òàêîãî íåò!")

    def show_items(self):
        if not self.items:
            print("õîëîäèëüíèê ïóñò.")
        else:
            print("Âíóòðè ëíæèò:")
            for item in self.items:
                print(f"- {item}")



if __name__ == "__main__":
    fridge = base()

    while True:
        print("\nâûáåðèòå äåéñòâèå:")
        print("1. äîáàâèòü ïðîäóêò")
        print("2. óäàëèòü ïðîäóêò")
        print("3. ïîêàçàòü ÷òî âíóòðè")
        print("4. game over")

        choice = input("ââåäèòå íîìåð: ")

        if choice == "1":
            name = input("ââåäèòå íàçâàíèå ïðîäóêòà: ")
            fridge.add_item(food(name))
        elif choice == "2":
            name = input("ââåäèòå íàçâàíèå ïðîäóêòà äëÿ óäàëåíèÿ: ")
            fridge.remove_item(name)
        elif choice == "3":
            fridge.show_items()
        elif choice == "4":
            print("áîëüøå íåò õîëîäèëüíèêà.")
            break
        else:
            print("êóäà æìåøü?)")
            
