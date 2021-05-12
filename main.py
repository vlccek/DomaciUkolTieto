import json

pathtoFile = 'oecd.json'

def loadFiles():
    with open(pathtoFile) as f:
        data = json.load(f)
    return data

def main():
    print(loadFiles())

if __name__ == "__main__":
    main()