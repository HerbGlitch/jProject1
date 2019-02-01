#Computes the under pricing
import pandas as pd
import math

class Under:
    config = None
    data = None
    def wrds_and_xml_or_txt_under(self, config, data):
        self.config = config
        self.data = data
        data_table = open(".matchesbypermno", "r")
        table = data_table.readlines()
        j = 0
        for data_items in table:
            data = data_items.split(",")
            i = 0
            while i < len(data):
                if(data[i].find("\n")):
                    data[i] = data[i].replace("\n", "")
                i += 1
            table[j] = data
            j += 1
        file = open(".test", "w+")
        up = .0001
        for inner_table in table:
            data_table1 = None
            data_table2 = None
            for fetch_table in self.config.databases:
                if(fetch_table.title == inner_table[0]):
                    data_table1 = fetch_table
                if(fetch_table.title == inner_table[4]):
                    data_table2 = fetch_table
            if(self.data.match_month(inner_table[2], inner_table[6])):
                prc = inner_table[3]
                offer_prc = inner_table[7]
                if(self.data.check_float(str(prc)) and self.data.check_float(str(offer_prc))):
                    up = (math.fabs(float(prc))/float(offer_prc)) - 1
                    try:
                        file.write(str(data_table2.table.loc[int(inner_table[5])]["permno"]) + "," + data_table1.title + "," + inner_table[1] + "," + data_table2.title + "," + inner_table[5] + "," + str(up) + "," + data_table2.table.loc[int(inner_table[5])]["issuer"] + "\n")
                    except:
                        print("hi")
        file.close()
            # file.write("\n" + data_table1.table.loc[32441]['date'])
