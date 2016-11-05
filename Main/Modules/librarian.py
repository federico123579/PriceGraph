from library import library
from converter import convert
class Videogame:
    def __init__(self, videogame_name, videogame_price, v_url):
        self.name = videogame_name
        self.price = videogame_price
        self.url = v_url
def show_list():
    print library
def search(name_of_it):
    return next((item for item in library if item["name"] == name_of_it), None)
def new_game(its_name, its_price, its_url):
    new_game_object = Videogame(its_name, its_price, its_url)
    library.append(new_game_object.__dict__)
    with open("library.py", "w") as f:
        f.write("library = " + str(library))
    convert()
if __name__ == "__main__":
    new_videogame_option = input("New Videogame?(1/0)")
    if new_videogame_option == 1:
        name = raw_input("What's its name?")
        price = raw_input("What's its price?")
        url = raw_input("What's its url?")
        new_game(name, price, url)
