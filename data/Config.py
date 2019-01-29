from data.Data import Data
from data.Database import Database
import os

class Config:
    #build all of the objects
    db = None
    main = None

    #lists
    databases = []

    def file_split(self, file):
        lines_per_file = 60000
        smallfile = None
        x = 0;
        small_databases_names = []
        with open(file) as bigfile:
            for lineno, line in enumerate(bigfile):
                if lineno % lines_per_file == 0:
                    if smallfile:
                        smallfile.close()
                    small_filename = file.split(".")[0] + '{}.txt'.format(x)
                    small_databases_names.append(small_filename)
                    x += 1
                    smallfile = open(small_filename, "w")
                smallfile.write(line)
            if smallfile:
                smallfile.close()
            return small_databases_names

    def config(self, main):
        self.main
        for name in main.databases_names:
            database = Database()
            if(os.path.getsize(name) > 10000000):
                small_databases_names = self.file_split(name)
                titles = database.database_get_titles(small_databases_names)
                for small_name in small_databases_names:
                    new_database = Database()
                    new_database.database_txt(self.main, small_name, titles)
                    os.remove(small_name)
                    self.databases.append(new_database)
            elif(name.split(".")[-1] == "txt"):
                database.database_txt(self.main, name)
            elif(name.split(".")[-1] == "xls"):
                database.database_xls(self.main, name)
            else:
                print("functionality not available yet")
            if(database.title != None):
                self.databases.append(database)
