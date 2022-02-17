places = {0: "", 3: "K", 6: "M", 9: "B", 12: "T", 15: "Qa", 18: "Qi", 21: "Sx", 24: "Sp", 27: "Oc", 30: "No", 33: "Dc", 36: "Ud", 39: "Dd", 42: "Td", 45: "Qad", 48: "Qid", 51: "Sxd", 54: "Spd", 57: "Ocd", 60: "Nod", 63: "Vg", 66: "Uvg", 69: "Dvg", 72: "Tvg", 75: "Qavg", 78: "Qivg", 81: "Sxvg", 84: "Spvg", 87: "Ocvg", 90: "Novg", 93: "Tg", 96: "Qatg", 99: "Qitg", 100: " Googol", 102: "Sxtg", 105: "Sptg", 108: "Octg", 111: "Notg", 114: "Tr", 117: "Qatr", 120: "Qitr", 123: "Sxtr", 126: "Sptr", 129: "Octr", 132: "Notr", 135: "Qadtr", 138: "Qidtr", 141: "Sxdtr", 144: "Spdtr", 147: "Ocdtr", 150: "Nodtr", 153: "Qadtg", 156: "Qidtg", 159: "Sxdtg", 162: "Spdtg", 165: "Ocdtg", 168: "Nodtg", 171: "Qadt", 174: "Qidt", 177: "Sxdt", 180: "Spdt", 183: "Ocdt", 186: "Nodt", 189: "Qadq", 192: "Qidq", 195: "Sxdq", 198: "Spdq", 201: "Ocdq", 204: "Nodq", 207: "Qads", 210: "Qids", 213: "Sxds", 216: "Spds", 219: "Ocds", 222: "Nods", 225: "Qadqd", 228: "Qidqd", 231: "Sxdqd", 234: "Spdqd", 237: "Ocdqd", 240: "N"}


def closest_value(input_list, input_value):
    if input_value >= max(input_list):
        return max(input_list)
    return max(i for i in input_list if i <= input_value)


def prettify(number):
    if number < 10 ** min(i for i in places if i > 0):
        return str(number)
    num_places = len(str(number)) - 1
    cv = closest_value(list(places.keys()), num_places)
    if int(number / (10 ** cv)) == number / (10 ** cv):
        return str(int(number / (10 ** cv))) + places[cv]
    else:
        return str(number / (10 ** cv)) + places[cv]


if __name__ == "__main__":
    print(prettify(-1))
    print(prettify(0))
    print(prettify(1))
    print(prettify(10))
    print(prettify(100))
    print(prettify(1000))
    print(prettify(10000))
    print(prettify(100000))
    print(prettify(1000000))
    print(prettify(10000000))
    print(prettify(100000000))
    print(prettify(1000000000))
    print(prettify(10000000000))
    print(prettify(100000000000))
    print(prettify(1000000000000))
    print(prettify(int(str(1)+"0"*100)))
