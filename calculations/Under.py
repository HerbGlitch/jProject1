#Computes the under pricing
import pandas as pd
import math

class Under:
    config = None
    data = None
    def under(self, config, data):
        self.config = config
        self.data = data
        data_table = open(".matchesbypermno", "r")
        data_lines = data_table.readlines()
        table = []
        for data_items in data_lines:
            data = data_items.split(",")
            i = 0
            while i < len(data):
                if(data[i].find("\n")):
                    data[i] = data[i].replace("\n", "")
                i += 1
            inner_table = [data[0], data[1], data[2], data[3]]
            table.append(inner_table)
        file = open(".test", "w+")
        up = .0001
        for inner_table in table:
            data_table1 = None
            data_table2 = None
            for fetch_table in self.config.databases:
                if(fetch_table.title == inner_table[0]):
                    data_table1 = fetch_table
                if(fetch_table.title == inner_table[2]):
                    data_table2 = fetch_table
            if(self.data.match_month(data_table1.table.loc[int(inner_table[1])]["date"], data_table2.table.loc[int(inner_table[3])]["date"])):
                prc = data_table1.table.loc[int(inner_table[1])]["prc"]
                offer_prc = data_table2.table.loc[int(inner_table[3])]["prc"]
                if(self.data.check_float(str(prc)) and self.data.check_float(str(offer_prc))):
                    print(prc,offer_prc)
                    up = (math.fabs(float(prc))/float(offer_prc)) - 1
                    file.write(data_table1.title + "," + inner_table[1] + "," + data_table2.title + "," + inner_table[2] + "," + str(up) + "\n")
        file.close()
            # file.write("\n" + data_table1.table.loc[32441]['date'])
