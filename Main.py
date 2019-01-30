from data.Config import Config
from data.Load_data import Load_data
from data.Data import Data
import os

class Main():
    #main holds the current running class
    main = None

    #creates all class objects
    config = Config()
    load_data = Load_data()
    data = Data()

    #array for all databases
    databases_names = []

    for database_name in os.listdir('databases'):
        databases_names.append("databases/" + database_name)

    def main(self, main):
        self.main = main
        main.config.config(self.main)
        main.data.data(self.config)
        #main.load_data.load_data(self.main, self.config)
        main.data.match("permno", "permno", "CRSP Total0.txt", "final.xls")

def instantiate():
    main = Main()
    main.main(main)

if __name__ == '__main__':
    instantiate()
