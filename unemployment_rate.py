from pyjstat import pyjstat
import requests
from collections import OrderedDict

def loadFile():
    EXAMPLE_URL = 'https://json-stat.org/samples/oecd.json'
    data = requests.get(EXAMPLE_URL)
    results = pyjstat.from_json_stat(data.json(object_pairs_hook=OrderedDict))
    return results

def getSortedDataLow():
    df = loadFile()
    sortedData = df[0].sort_values(by='value')
    return sortedData

def main():
    sortedData = getSortedDataLow()
    print('countries with the lowest:')
    print(sortedData[0:3])

    print('countries with the highest:')
    print(sortedData[-3:])

if __name__ == "__main__":
    main()