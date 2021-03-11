import json

with open("output/sentiment.txt","r", encoding="utf-8") as file:
    file = '{"root":[' + file.read().strip() + ']'

    # file = file.replace("'", '"')
    # json = json.loads(file)
    # print(json[0]["sentiment"])

    i = 0
    for element in file:
        if i < 270450:
            print(element, end='')
            i += 1
        else:
            break
    print()
