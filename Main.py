from data.Config import Config
from data.Load_data import Load_data
import os

class Main():
    #main holds the current running class
    main = None

    #creates all class objects
    config = Config()
    load_data = Load_data()

    #data holds all of data objects
    data = []

    #array for all databases
    databases_names = []

    for database_name in os.listdir('databases'):
        databases_names.append("databases/" + database_name)

    def main(self, main):
        self.main = main
        main.config.config(self.main)
        main.load_data.load_data(self.main, self.config)

def instantiate():
    main = Main()
    main.main(main)

if __name__ == '__main__':
    instantiate()
