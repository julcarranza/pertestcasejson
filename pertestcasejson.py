# name:        pertestcasejson.py
# Version      0.1
# Date:        May 8, 2017
# Author:      Julio Carranza
#
# Description:
#              Script to split the EZ JSON Main Result file
#              into per test cases keeping the structure
#              of the headers. The "test_cases" key
#              in the dictionary stores the per test case
#              array. The script will generate json files
#              in the format jsonfile-view_id.json per test
#              case.
#
# Usage:       python pertestcasejson.py jsonfile.json

import sys, json


jsonfile =sys.argv[1]

with open(jsonfile) as data_file:
    data = json.load(data_file)
testnumber = jsonfile.split('.')[0]

for i in data["test_cases"]:
    for x in i:

        testpercase = testnumber + '-'+ i[x]['view_id'] + '.json'
        print testpercase
        datapercase = {}

        datapercase["test_cases"] = [i,]
        with open(testpercase, 'w') as f:
            json.dump(datapercase, f)
