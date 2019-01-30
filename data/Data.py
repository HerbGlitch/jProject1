import pandas as pd

class Data:
    config = None

    def data(self, config):
        self.config = config

    def match(self, keyword_for_data1, keyword_for_data2, data_table1_name, data_table2_name):
        data_table1 = None
        data_table2 = None
        for table in self.config.databases:
            if(table.title == "databases/" + data_table1_name):
                data_table1 = table
            if(table.title == "databases/" + data_table2_name):
                data_table2 = table
        file = open("test.txt", "w+")
        for id1, data1 in data_table1.table.iterrows():
            for id2, data2, in data_table2.table.iterrows():
                if(int(data1[keyword_for_data1]) == int(data2[keyword_for_data2])):
                    if(self.match_month(data1["date"], data2["date"])):
                        text = data_table1_name + " and " + data_table2_name + " have the same value at: Data1 - " + str(id1) + ", Data2 - " + str(id2) + "; with the value of: " + str(data1[keyword_for_data1] + " and dates of: Data1 - " + str(data1["date"]) + ", Data2 - " + str(data2["date"]) + "\n")
                        file.write(text)
        # file.write("\n" + data_table1.table.loc[32441]['date'])
        file.close()

    def match_month(self, date1, date2):
        date1 = self.check_convert_date(date1)
        date2 = self.check_convert_date(date2)
        if(int(str(date1)[:6]) == int(str(date2)[:6])):
            return True

    def check_convert_date(self, date):
        date = str(date).strip()
        if("/" in date):
            temp_date = date.split("/")
            if(len(temp_date[0]) == 1):
                temp_date = int("0" + str(temp_date[0]))
            date = int(str(temp_date[2]) + str(temp_date[0]) + str(temp_date[1]))
            return date
        elif(len(date) == 8):
            return int(date)
        else:
            print("error")
            return 00000000
