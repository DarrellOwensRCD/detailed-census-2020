# Calculates the race differences from 2020 Detailed Ethnic Groups against 2010 Summary File 2
import csv
import re
# This returns a list of 2020 strings equal of the 2010 entry race
def finder(race, dic20, dic10):
    if race not in dic10:
        return None
    num = dic10[race]
    races = []
    if num in dic20:
        races.append(dic20[num])
    else:
        #this means the digit is a split
        num = float(num) + 0.1
        #print(str(num))
        races.append(dic20[str(num)])
        num = num + 0.1
        if str(num) in dic20:
            #print(str(num))
            races.append(dic20[str(num)])
            num = num + 0.1
            if str(num) in dic20:
                #print(str(num))
                races.append(dic20[str(num)])
    return races
def is_float(value):
    try:
        float_value = float(value)
        return True
    except ValueError:
        return False
filedata20 = '/Users/darrell/Desktop/DetailedCensus/DetailedCensus2020/DECENNIALDDHCA2020.T01001-Data.csv'
filedata10 = '/Users/darrell/Desktop/DetailedCensus/DetailedCensus2010/DECENNIALSF22010.PCT1-Data.csv'
filename10 = '/Users/darrell/Desktop/DetailedCensus/DetailedCensus2010/unique2010.csv'
filename20 = '/Users/darrell/Desktop/DetailedCensus/DetailedCensus2020/unique2020.csv'
destfile = '/Users/darrell/Desktop/DetailedCensus/NetChange.csv'
with open(filename10, 'r') as f1, open(filename20, 'r') as f2, open(filedata10, 'r') as f3, open(filedata20, 'r') as f4:
    data1 =  csv.reader(f1, delimiter=',')
    data2 =  csv.reader(f2, delimiter=',')
    data3 =  csv.reader(f3, delimiter=',')
    data4 =  csv.reader(f4, delimiter=',')
    d1 = list(data1)
    d2 = list(data2)
    d3 = list(data3)
    d4 = list(data4)
    f1.close()
    f2.close()
    f3.close()
    f4.close()
print("Starting...")
# Make a race dictionary of 2010 info
dic20 = {}
dic10 = {}
for unique in d1:
    if unique[1].isnumeric():
        dic10[unique[0]] = unique[1]
# Make an inverted race dictionary of 2020 info
for unique in d2:
    if unique[1].isnumeric() or '.' in unique[1]:
        dic20[unique[1]] = unique[0]
# Make a header based off the 2020 file with 3 new catagories
header = []
start = True
second = True
for line in d3:
    if start:
        start = False
        line.append("POPGROUP_NET")
        line.append("POPGROUP_BOOL")
    elif second:
        second = False
        line.append("Popgroup Change")
        line.append("Flag if Change Was Calculated")
    else:
        # 0500000US02220 | Sitka City and Borough, Alaska | 106	| White | 567
        # Calculate Change for this race in this county
        # Find the appropriate string equal in 2020 via the dictionary ID number system
        race = (re.split(r'\(', line[3], 1))[0]
        if line[4].isnumeric():
            count10 = int(line[4])
            races2020 = finder(race, dic20, dic10)
            diff = 0
            # Usually just 1 item but accounts for multiple split racial groups in 2020 for 1 of 2010
            if races2020:
                for ethnicname in races2020:
                    # Iterate the 2020 file and find the string of the 2020 race group
                    for race20 in d4:
                        if race20[4] == ethnicname and line[1] == race20[1]:
                            count20 = int(race20[2])
                            if diff > 0 :
                                diff += count20
                            else :
                                diff = count20 - count10
                            break
                # With the diff calculated, add the stat and flag
                line.append(diff)
                line.append("TRUE")
                if 'Chinese' in line[3] and 'Alameda' in line[1]:
                    print(line)
with open('/Users/darrell/Desktop/DetailedCensus/DetailedCensus2010/finalcalc.csv', 'w') as fp:
    writer = csv.writer(fp)
    writer.writerows(d3)
    fp.close()
print("done")
