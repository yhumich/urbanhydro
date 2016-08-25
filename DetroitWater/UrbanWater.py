# Select WWTP, RTB, CSO and SWMA
# WWTP: wastewater treatment plant or wastewater plant (another acronyms: WTP)


import csv

keywords = ['wastewater', 'wasterwater plant', 'wastewater treatment plant', 'wtp', 'wwtp']

# read csv file
filepath = '/Users/huya/Work/Detroit_Water/Data/Point_Source/'
ifile = filepath + 'urban_pointsource.csv'
ofile1 = filepath + 'wwtp_ps.csv'
ofile2 = filepath + 'other_ps.csv'

# save the results to file
f1 = open(ofile1, 'wt')
f2 = open(ofile2, 'wt')

try:
    csvwriter1 = csv.writer(f1)
    csvwriter2 = csv.writer(f2)
    try:
        with open(ifile, 'rb') as csvfile:
            csvreader = csv.reader(csvfile)
            headers = csvreader.next()
            csvwriter1.writerow(headers)
            csvwriter2.writerow(headers)
            for row in csvreader:
                facility = row[1].lower()
                keyflag = 0
                for key in keywords:
                    if ~facility.find(key):
                        keyflag = 1
                        break
                # select the matching row
                if keyflag:
                    csvwriter1.writerow(row)
                else:
                    csvwriter2.writerow(row)

    except IOError:
        print 'cannot open', ifile

except IOError:
    print 'cannot open', f1

finally:
    f1.close()
    f2.close()

# save results


