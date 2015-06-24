import sys
import re
import json
import os
import fnmatch

def get_file_names(year):
    list_of_files = []
    for file in os.listdir('/home/ms/systems/analytics/analytics-service/analytics/'):
        if fnmatch.fnmatch(file, '*'+ re.escape(year) + '*.txt'):
            list_of_files.append(file)
#    print list_of_files
    return list_of_files

def extract_data(year):
    year = year
    files = get_file_names(year);
    dict_list = {}
    str1 = "TotalVisits"
    str2 = "TotalUnique"
    for i in files:
        f = open(i)
        for line in f: 
            if re.match(r'^TotalVisits',line):
#                print line.strip() 
#                print (i.lstrip('awstats.')).rstrip('.txt')
#                Json = json.dumps({ (i.lstrip('awstats.')).rstrip('.txt'): (line.strip('TotalVisits ')).rstrip() })  
                 dict_list[(i.lstrip('awstats.')).rstrip('.txt')] = (line.strip('TotalVisits ')).rstrip()

    print dict_list
    name_of_datafile = "data-" + re.escape(year) + ".json"
    print name_of_datafile 
    with open('data-2014.json', 'w') as outfile:
        json.dump(dict_list, outfile, sort_keys= True, indent = 4)

# get_file_names("2015");

extract_data("2014");



