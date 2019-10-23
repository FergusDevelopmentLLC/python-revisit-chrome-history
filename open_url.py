import webbrowser
import json
import datetime

new = 2 # open in a new tab, if possible

ignore = []
#ignore.append(".google.com")
ignore.append("localhost")
ignore.append("linkedin")
ignore.append("reddit")

#or, define ur own ignore words
# text_file = open("private/ignore.csv", "r")
# ignore = text_file.read().split(',')

print(ignore)

#with open('private/history_will.json') as history_json:
with open('sample.json') as history_json:
    history = json.load(history_json)
    
    startDisplay = 0
    endDisplay = 3

    index = 0
    for item in history:

        if index >= startDisplay:

            found = False
            for word in ignore:
                if word in item["url"]:
                    found = True

            if found == False:
                print(item["lastVisitTime"] + "|" + item["url"])
                webbrowser.get(using='google-chrome').open(item["url"],new=new)
            
        index += 1
        if index == endDisplay:
            break