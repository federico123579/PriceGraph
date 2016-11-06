import sys
sys.path.insert(0, 'Modules')
import librarian, dataProcessor, grapher
new_videogame_option = input("New Videogame?(1/0)")
if new_videogame_option == 1:
    name = raw_input("What's its name?")
    price = raw_input("What's its price?")
    url = raw_input("What's its url?")
    librarian.new_game(name, price, url, 'data.txt')
    dataProcessor.collect_data('data.txt')
else:
    pass
dataProcessor.collect_data('data.txt')
grapher.send_to_make_graph()
