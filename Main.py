from data.Config import Config
from data.Load_data import Load_data
from data.Data import Data
from calculations.Under import Under
import os

class Main():
    #main holds the current running class
    main = None

    #creates all class objects
    config = Config()
    load_data = Load_data()
    data = Data()
    under = Under()

    #array for all databases
    databases_names = []
    small_databases_names = []

    for database_name in os.listdir('databases'):
        databases_names.append("databases/" + database_name)

    def main(self, main):
        self.main = main
        self.main.config.config(self.main)
        self.main.data.data(self.config)
        #main.load_data.load_data(self.main, self.config)
        self.main.data.match_by_permno_and_date("permno", "permno", "crsp.wrds", "final.xls")
        #main.under.under(self.config, self.data)

def instantiate():
    main = Main()
    main.main(main)

if __name__ == '__main__':
    instantiate()
