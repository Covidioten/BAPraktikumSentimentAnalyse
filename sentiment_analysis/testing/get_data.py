import json
import re

with open("../output/sentiment.txt", "r", encoding="utf-8") as file:
    file = '{"root":[' + file.read() + ']}'

    # file = file.replace("'", '"')
    # file = file.replace("}}}}", '}}}},')
    #
    # file = re.sub(r'\s+', '',file)
    #
    # json = json.loads(file).decode("utf-8")
    #
    # print(json[0]["sentiment"])

    i = 0
    for element in file:
        if i < 4702:
            print(element, end='')
            # if i == 4693:
            # print("!!!")
            i += 1
        else:
            break
