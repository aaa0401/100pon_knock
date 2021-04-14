from math import *
from copy import *

def q_1(from_str):
    to_str = ""
    for i in from_str:
        to_str = i + to_str
    return to_str


def q_2(from_str):
    return from_str[0] + from_str[2] + from_str[4] + from_str[6]


def q_3(from_str1, from_str2):
    to_str = ""
    for i in range(len(from_str1)):
        to_str += from_str1[i] + from_str2[i]
    return  to_str


def q_4(statement):
    words = statement.split()
    ans = []
    for i in words:
        ans += [len(i)]
    return ans


def q_5(statement):
    words = statement.split()
    target = [1, 5, 6, 7, 8, 9, 15, 16, 19]


def q_6_word(statement, n):
    unigram = []
    for i in statement:
        unigram += [i]
    ans = copy(unigram)
    for i in range(n-1):
        for j in range(len(unigram)-1-i):
            ans[j] += unigram[j+i+1]
        ans.pop()
    return ans


def q_7(statement1, statement2):
    bi1 = set(q_6_word(statement1, 2))
    bi2 = set(q_6_word(statement2, 2))
    orset = bi1 | bi2
    andset = bi1 & bi2
    subset = bi1 - bi2
    return orset, andset, subset


def q_8(x, y, z):
    return str(x) + "時の" + str(y) + "は" + str(z)


def q_9(statement):
    converted = ""
    for i in statement:
        chr_code = ord(copy(i))
        if chr_code <= 90:
            converted += i
        else:
            converted += chr(219 - chr_code)
    return converted

def q_11(file_name):
    hightemap = open(file_name, "r", encoding="utf-8")
    lines = hightemap.readlines()
    return len(lines)

def q_20(file_name):
    import gzip, json
    with gzip.open(file_name, "r") as gf:
        data = json.load(gf, "r")
    for i in data:
        print(i)


def main():
    # print(q_1("stressed"))
    # print(q_2("パタトクカシー"))
    # print(q_3("パトカー", "タクシー"))
    # print(q_4("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."))
    # print(q_6_word("I am an NLPer", 2))
    # or_set, and_set, sub_set = q_7("paraparaparadise", "paragraph")
    # print(str(or_set), str(and_set), str(sub_set))
    # print(q_8("15", "ゴリラ", "気性が荒い"))
    # print(q_9("abcABC"))
    # print(q_9("zyxABC"))
    # print(q_11("popular_name.txt"))
    q_20("jawiki-country.json.gz")



if __name__ == '__main__':
    main()
