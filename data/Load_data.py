from data.Data import Data
import pandas as pd

#sdc -- ['_malookup_', 'chars', 'ma_advisors', 'ma_details', 'ma_events', 'ma_names', 'names', 'ni_details', 'ni_names']

class Load_data:
    main = None
    config = None

    # lists
    crsp_name = ["databases/CRSP Total0.txt"]
    sdc_name = [""]

    def load_data(self, main, config):
        self.main = main
        self.config = config
        for database in self.config.databases:
            self.load_table(database)

    def load_table(self, database):
        if(database.title == self.crsp_name[0]):
            for id, data in database.table.iterrows():
                data_object = Data()
                main.data_object.data_crsp("crsp", id, data["cusip"], data["date"], data["comnam"], data["siccd"], data["permno"], data["permco"], data["shrcd"], data["prc"], data["ret"], data["shrout\n"])
                data_object.print_data()
