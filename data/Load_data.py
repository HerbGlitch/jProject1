from data.Data import Data

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
        for data_table in self.config.databases:
            self.load_table(data_table)

    def load_table(self, table):
        print(table)
        #print("crsp", data, value["cusip"], value["namedt"], value["comnam"], value["siccd"], value["permno"], value["permco"], value["shrcd"], value["prc"], value["ret"], value["shrout"]) #prc, ret, shrout
            #     data = Data()
            #     order for items data.data(data_type, data_id, cusip, date, issuer, sic, permno, permco, shrcd, prc, ret, shrout)
            #     main.data.append(data.data("crsp", data, value["cusip"], value["date"], value["issuer"], value["sic"], value["permno"], value["permco"], value["shrcd"], value["prc"], value["ret"], value["shrout"]))
            #     data.print_data()
