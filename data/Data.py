import pandas as pd

class Data:
    config = None

    def data(self, config):
        #allowes config.databases to be called
        self.config = config

    def match_by_permno_and_date(self, keyword_for_data1, keyword_for_data2, data_table1_name, data_table2_name):
        #gets the tables from the databases in config to check permno and date
        data_table1 = None
        data_table2 = None
        for table in self.config.databases:
            if(table.title == "databases/" + data_table1_name):
                print(data_table1, table)
                data_table1 = table
            if(table.title == "databases/" + data_table2_name):
                data_table2 = table
        #creates a file to write final data to make looping through every run not necessary
        #file = open(".matchesbypermno", "w+")
        #loops throught the table
        test = data_table1.database.raw_sql("SELECT "+data_table1.library+";")
        test = data_table1.database.raw_sql("SELECT "+keyword_for_data1+" FROM "+data_table1.table+" WHERE FIND_IN_SET('10240', "+keyword_for_data1+");")
        # for id1, data1 in data_table1.table.iterrows():
        #     for id2, data2, in data_table2.table.iterrows():
        #         #check to see if the data is an integer
        #         if(self.check_int(str(data1[keyword_for_data1])) and self.check_int(str(data2[keyword_for_data2]))):
        #             #strips data of whitespace and compares permno
        #             if(int(str(data1[keyword_for_data1]).strip()) == int(str(data2[keyword_for_data2]).strip())):
        #                 #checks date to see after the company was created
        #                 if(self.check_recent_date(data1["date"], data2["date"])):
        #                     #writes to file making mutiple looping not needed to save time
        #                     text = "databases/" + data_table1_name + "," + str(id1) + "," + "databases/" + data_table2_name + "," + str(id2) + "\n"
        #                     file.write(text)
        #saves the file
        #file.close()

    def match_month(self, date1, date2):
        #checks if the months and years are the same
        date1 = self.check_convert_date(date1)
        date2 = self.check_convert_date(date2)
        if(int(str(date1)[:6]) == int(str(date2)[:6])):
            return True
        else:
            return False

    def check_convert_date(self, date):
        date = str(date).strip()
        #splits date format mm/dd/yyyy to yyyymmdd
        if("/" in date):
            temp_date = date.split("/")
            if(len(temp_date[0]) == 1):
                temp_date = int("0" + str(temp_date[0]))
            date = int(str(temp_date[2]) + str(temp_date[0]) + str(temp_date[1]))
            return date
        #splits date format yyyy-mm-dd 00:00:00 to yyyymmdd
        elif("-" in date):
            temp_date = date.split("-")
            temp_day = temp_date[2].split(" ")
            date = int(str(temp_date[0] + temp_date[1] + temp_day[0]))
            return date
        #returns date because it should be correct
        elif(len(date) == 8):
            return int(date)
        #does not have a correct format
        else:
            print("error")
            return 0

    def check_recent_date(self, date1, date2):
        #checks if the date is after the company was made
        date1 = str(self.check_convert_date(date1))
        date2 = str(self.check_convert_date(date2))
        if(date1[:6] >= date2[:6]):
            return True
        else:
            return False

    def check_int(self, number):
        #checks to see if number is an integer, can be negative
        if number[0] in ('-', '+'):
            return number[1:].isdigit()
        return number.isdigit()

    def check_float(self, number):
        try:
            float(number)
            return True
        except ValueError:
            return False
