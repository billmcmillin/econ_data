import csv, sys
from datetime import datetime

def get_econ_dict(econ_file, col):
    econ_dict = {}
    with open(econ_file) as cf:
        rd = csv.reader(cf)
        next(rd)
        for row in rd:
            date = datetime.strptime(row[0], '%Y-%m-%d')
            econ_dict.update({date: row[col]})
    return econ_dict

def update_econ_file(econ_file):
    with open(econ_file) as cf:
        with open('econ_percentages.csv', 'w', newline='\n') as csvout:
            outwriter = csv.writer(csvout, delimiter=',',quoting=csv.QUOTE_MINIMAL)
            rd = csv.reader(cf)
            prev1 = 1
            prev2 = 1
            prev6 = 1
            out_data = []
            for row in rd:
                cur_val1 = float(row[1])
                diff1 = ((cur_val1 - prev1) / prev1)
                row.append(diff1)
                prev1 = cur_val1
                cur_val2 = float(row[2])
                diff2 = ((cur_val2 - prev2) / prev2)
                row.append(diff2)
                prev2 = cur_val2
                cur_val6 = float(row[6])
                diff6 = ((cur_val6 - prev6) / prev6)
                row.append(diff6)
                prev6 = cur_val6
                outwriter.writerow(row)

def get_sales_percent_chg(dc_file):
    dc_dict = {}
    return dc_dict

def get_percent_change(fact_file, econ_file, col):
    col = col-5
    eco_dc = get_econ_dict(econ_file, col)
    print(eco_dc)
    with open(fact_file) as ff:
        ffrd = csv.reader(ff)
        next(ffrd)
        for row in ffrd:
            try:
                date = datetime.strptime(row[0], '%Y-%m-%d')
                print(row[0],eco_dc[date])
            except:
                pass

def get_unempl(econ_file):
    with open(econ_file) as cf:
        with open('unempl_percentages.csv', 'w', newline='\n') as csvout:
            outwriter = csv.writer(csvout, delimiter=',',quoting=csv.QUOTE_MINIMAL)
            rd = csv.reader(cf)
            for row in rd:
                print(row)
                #calculate rate of change over 12-month moving average

fact_file = "data/trends.csv"
econ_file = "data/company_perf.csv"
col = int(sys.argv[1])

if __name__ == "__main__":
    #get_percent_change(fact_file, econ_file, col)
    #update_econ_file(econ_file)
    get_unempl(econ_file)
