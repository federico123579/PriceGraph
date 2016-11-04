from library import library
class Videogame:
    def __init__(self, videogame_name, videogame_price):
        self.name = videogame_name.upper()
        self.price = videogame_price
def show_list():
    print library
def search(name_of_it):
    return next((item for item in library if item["name"] == name_of_it), None)
if __name__ == "__main__":
    new_videogame_option = input("New Videogame?(1/0)")
    if new_videogame_option == 1:
        name = raw_input("What's its name?")
        price = raw_input("What's its price?")
        x = Videogame(name, price)
        print x.__dict__
        library.append(x.__dict__)
        with open("library.py", "w") as f:
            f.write("library = " + str(library))
    show_list()
    print search('BATTLEFIELD 1')
