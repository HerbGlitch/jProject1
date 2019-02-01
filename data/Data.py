import pandas as pd

class Data:
    config = None

    def data(self, config):
        #allowes config.databases to be called
        self.config = config

    def match_by_permno_and_date_wrds_and_xls_or_txt(self, keyword_for_data1, keyword_for_data2, wrds_data_table_name, data_table_name):
        #gets the tables from the databases in config to check permno and date
        data_table1 = None
        data_table2 = None
        for table in self.config.databases:
            if(table.title == "databases/" + wrds_data_table_name):
                data_table1 = table
            if(table.title == "databases/" + data_table_name):
                data_table2 = table
        #loops throught the table
        file = open(".matchesbypermno", "w+")
        for id, data in data_table2.table.iterrows():
            if(self.check_int(str(data[keyword_for_data2]))):
                #checks permno and date
                new_table = data_table1.database.raw_sql("SELECT * FROM "+data_table1.library+"."+data_table1.table+" WHERE (date >= '"+str(data["date"]).strip().split(" ")[0]+"') AND ("+keyword_for_data1+" IN ("+str(data[keyword_for_data2]).strip()+"))")
                for id1, data1 in new_table.iterrows():
                    #saves matching data to text file
                    text = "databases/" + wrds_data_table_name + "," + str(id) + "," + str(data1["date"]) + "," + str(data1["prc"]) +"," + "databases/" + data_table_name + "," + str(id1) + "," + str(data["date"]).split(" ")[0] + "," + str(data["prc"]) +"\n"
                    file.write(text)
        file.close()

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
