import pandas as pd
import wrds
import os

class Database:
    title = None
    db = None
    table = None
    main = None

    def database_txt(self, main, txt_file, titles = None):
        file = open(txt_file, 'r')
        lines = file.read().splitlines(True)
        file.close()
        if(titles == None):
            titles = lines[0].split(', ')
        tempfile = open("temp.txt", "a")
        for line in lines[1:]:
            tempfile.write(line)
        tempfile.close()
        i = 0
        while i < len(titles):
            if(titles[i].find("\n")):
                titles[i] = titles[i].replace("\n", "")
            i += 1
        self.table = pd.read_fwf("temp.txt", header=None, names=titles)
        os.remove("temp.txt")
        self.title = txt_file

    def database_wrds(self, main, library, table):
        self.main = main
        self.db = wrds.Connection()
        self.table = self.db.get_table(library=library, table=table)
        self.title = table + " in " + library

    def database_xls(self, main, xls_file):
        self.main = main
        temp_file = pd.ExcelFile(xls_file)
        self.table = pd.read_excel(xls_file, sheet_name=temp_file.sheet_names[0])
        self.title = xls_file

    def database_get_titles(self, small_databases_names):
        file = open(small_databases_names[0], 'r')
        lines = file.read().splitlines(True)
        file.close()
        titles = lines[0].split(', ')
        return titles
