class Data:
    #type variable
    data_type = None

    #same data variables
    data_id = None
    cusip = None
    date = None
    issuer = None
    sic = None

    #crsp
    permno = None
    permco = None
    shrcd = None
    prc = None
    ret = None
    shrout = None

    #sdc
    offer_price = None
    ipo_flag = None
    cusip9 = None
    sdc_id = None
    deal_number = None
    total_shares_offered_in_this_market = None
    primary_shares_offered_in_this_market = None
    total_revenues_before_offering = None
    date_founded = None
    lead_managers_long_name = None
    venture_backed = None
    original_high_filing_price = None
    origional_low_filing_price = None
    units = None
    add_l_class_of_common_stock = None
    percent_of_shares_offered_abroad = None
    auditor = None

    def data_crsp(self, data_type, data_id, cusip, date, issuer, sic, permno, permco, shrcd, prc, ret, shrout):
        self.data_type = data_type
        self.data_id = data_id
        self.cusip = cusip
        self.date = date
        self.issuer = issuer
        self.sic = sic
        self.permno = permno
        self.permco = permco
        self.shrcd = shrcd
        self.prc = prc
        self.ret = ret
        self.shrout = shrout

    def data_sdc(self, data_type, data_id, cusip, date, issuer, sic, offer_price, ipo_flag, cusip9, sdc_id, deal_number, total_shares_offered_in_this_market, primary_shares_offered_in_this_market, total_revenues_before_offering, date_founded, lead_managers_long_name, venture_backed, original_high_filing_price, origional_low_filing_price, units, add_l_class_of_common_stock, percent_of_shares_offered_abroad, auditor):
        self.data_type = data_type
        self.data_id = data_id
        self.cusip = cusip
        self.date = date
        self.issuer = issuer
        self.sic = sic
        self.offer_price = None
        self.ipo_flag = ipo_flag
        self.cusip9 = cusip9
        self.sdc_id = sdc_id
        self.deal_number = deal_number
        self.total_shares_offered_in_this_market = total_shares_offered_in_this_market
        self.primary_shares_offered_in_this_market = primary_shares_offered_in_this_market
        self.total_revenues_before_offering = total_revenues_before_offering
        self.date_founded = date_founded
        self.lead_managers_long_name = lead_managers_long_name
        self.venture_backed = venture_backed
        self.original_high_filing_price = original_high_filing_price
        self.origional_low_filing_price = origional_low_filing_price
        self.units = units
        self.add_l_class_of_common_stock = add_l_class_of_common_stock
        self.percent_of_shares_offered_abroad = percent_of_shares_offered_abroad
        self.auditor = auditor

    def print_data(self):
        print("----------------------------------")
        print(self.data_type)
        print(self.data_id)
        print(self.cusip)
        print(self.date)
        print(self.issuer)
        print(self.sic)
        if(self.data_type == "crsp"):
            print(self.permno)
            print(self.permco)
            print(self.shrcd)
            print(self.prc)
            print(self.ret)
            print(self.shrout)
