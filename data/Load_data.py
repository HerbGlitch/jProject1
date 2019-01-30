from data.Data import Data
import pandas as pd

#this is a reference class
class Load_data:
    main = None
    config = None

    # lists
    crsp_name = ["databases/CRSP Total0.txt"]
    sdc_name = [""]

    # def load_data(self, main, config):
    #     self.main = main
    #     self.config = config
    #     for database in self.config.databases:
    #         self.load_table(database)
    #
    # def load_table(self, database):
    #     if(database.title == self.crsp_name[0]):
    #         for id, data in database.table.iterrows():
    #             print("crsp", id, data["cusip"], data["date"], data["comnam"], data["siccd"], data["permno"], data["permco"], data["shrcd"], data["prc"], data["ret"], data["shrout"])
