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

    for database_name in os.listdir('databases'):
        databases_names.append("databases/" + database_name)

    def main(self, main):
        self.main = main
        self.main.config.config(self.main)
        self.main.data.data(self.config)
        #main.load_data.load_data(self.main, self.config)
        self.main.check_load_files()
        #main.under.under(self.config, self.data)

    def new_matchesbypermno(self):
        if(input("Would you like to collect data by permno and date again: ").lower() == "yes"):
            return True
        else:
            return False

    def check_load_files(self):
        matchesbypermno = False
        for file in os.listdir("."):
            print(file)
            if(file == ".matchesbypermno"):
                matchesbypermno = True
        if(not matchesbypermno):
            self.main.data.match_by_permno_and_date_wrds_and_xls_or_txt("permno", "permno", "crsp.wrds", "final.xls")
        elif(self.new_matchesbypermno()):
            self.main.data.match_by_permno_and_date_wrds_and_xls_or_txt("permno", "permno", "crsp.wrds", "final.xls")


def instantiate():
    main = Main()
    main.main(main)

if __name__ == '__main__':
    instantiate()
