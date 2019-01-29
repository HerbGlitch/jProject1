import wrds
from data.Data import Data
from data.Database import Database
import pandas as pd


#sdc -- ['_malookup_', 'chars', 'ma_advisors', 'ma_details', 'ma_events', 'ma_names', 'names', 'ni_details', 'ni_names']

#commands:
#db.list_libraries()
#db.list_tables(library='library name')
#db.describe_table(library='library name', table='table name')
#database_variable = db.get_table(library='library name', table='table name') # the type returned is DataFrame


#will delete below comments in future, they will be currently used for reference:

#test = stocknames.iloc[1]
#print(test)

class Config:
    #build all of the objects
    db = None
    main = None

    def config(self, main):

        #for data, value in data_set.iterrows():
            #print("crsp", data, value["cusip"], value["namedt"], value["comnam"], value["siccd"], value["permno"], value["permco"], value["shrcd"], value["prc"], value["ret"], value["shrout"]) #prc, ret, shrout
            #data = Data()
            #order fo items data.data(data_type, data_id, cusip, date, issuer, sic, permno, permco, shrcd, prc, ret, shrout)
            #main.data.append(data.data("crsp", data, value["cusip"], value["date"], value["issuer"], value["sic"], value["permno"], value["permco"], value["shrcd"], value["prc"], value["ret"], value["shrout"]))
            #data.print_data()
