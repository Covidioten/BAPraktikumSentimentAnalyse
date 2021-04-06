import json
import re

with open("../output/sentiment.txt", "r", encoding="utf-8") as file:

    text = file.read()
    # print(int(len(text)-1))
    endIndex = int(len(text) - 1)

    text = text[0 : endIndex]


    text = '{"root":[' + text + ']}'

    text = text.replace("'", '"')

    text = re.sub(r'\s+', '', text)
    text = text.strip()

    arr = []
    # digit_arr = []
    arr = re.findall('\d\d\d\d-\d\d-\d\d', text)
    print(sorted(arr))



    # digit_arr = []
    # for entry in arr:
    #     digit_arr.append(int(re.findall('\d+', entry)[0]))
    #
    # print(sum(digit_arr))

    # for entry in digit_arr[0]:
    #     entry = int(entry)

    # for entry in digit_arr[0]:
    #     digit_arr = map(int, entry)
    #
    # print(sum(digit_arr))

    # arr = map(int, arr)

    # for entry in


    #
    # json = json.loads(text).decode("utf-8")
    #
    # print(json[0]["sentiment"])

    # i = 0
    # for element in text:
    #     if i == 178430:
    #         print(element)
    #         i += 1
    #     if i == 1784331:
    #         print(element)
    #         # if i == 4693:
    #         # print("!!!")
    #         i += 1
    #
    #     if i == 178433:
    #         break
    #
    #     i += 1
