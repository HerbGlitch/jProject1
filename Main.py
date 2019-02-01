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
        #self.main.load_data.load_data(self.main, self.config)
        self.main.check_load_files()

    def new_matches(self, name):
        if(input("Would you like to collect data by "+name+" again: ").lower() == "yes"):
            return True
        else:
            return False

    def check_load_files(self):
        matchesbypermno = False
        up = False
        for file in os.listdir("."):
            if(file == ".matchesbypermno"):
                matchesbypermno = True
            elif(file == ".up"):
                up = True
        if(not matchesbypermno):
            self.main.data.match_by_permno_and_date_wrds_and_xls_or_txt("permno", "permno", "crsp.wrds", "final.xls")
            up = False
        elif(self.new_matches("permno and date")):
            self.main.data.match_by_permno_and_date_wrds_and_xls_or_txt("permno", "permno", "crsp.wrds", "final.xls")
            up = False
        if(not up):
            self.main.under.wrds_and_xml_or_txt_under(self.config, self.data)
        elif(self.new_up("Under Pricing?")):
            self.main.under.wrds_and_xml_or_txt_under(self.config, self.data)
def instantiate():
    main = Main()
    main.main(main)

if __name__ == '__main__':
    instantiate()
