class Room:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.is_clean = False

    def clean(self):
        self.is_clean = True
        return self.size

    #is_clean
    def is_clean(self):
        self.is_clean = True

class Cleaner:
    def __init__(self, name):
        self.name = name
        self.rooms_to_clean = []
        self.cleaned_surface = 0

    def add_room(self, room):
        self.rooms_to_clean.append(room)

    def clean_all(self):
        for room in self.rooms_to_clean:
            self.cleaned_surface += room.clean()
        return self.cleaned_surface



def main():
    h = Room("hálószoba", 16)
    print(h.is_clean)  # False
    h_size = h.clean()
    print(h_size)  # 16
    print(h.is_clean)  # True

    print("<===============SEPARATOR===============>")

    peti = Cleaner("Peti")
    print(peti.cleaned_surface)  # 0
    halo = Room("hálószoba", 16)
    print(halo.is_clean)  # False
    nappali = Room("nappali", 12)
    peti.add_room(halo)
    peti.add_room(nappali)
    peti.clean_all()
    print(halo.is_clean)  # True
    print(peti.cleaned_surface)  # 28


if __name__ == '__main__':
    main()
