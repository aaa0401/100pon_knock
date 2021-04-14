from math import *
from copy import *

from math import *
from copy import *

def q_0(from_str):
    to_str = ""
    for i in from_str:
        to_str = i + to_str
    return to_str


def q_1(from_str):
    return from_str[0] + from_str[2] + from_str[4] + from_str[6]


def q_2(from_str1, from_str2):
    to_str = ""
    for i in range(len(from_str1)):
        to_str += from_str1[i] + from_str2[i]
    return  to_str


def q_3(statement):
    words = statement.split()
    ans = []
    for i in words:
        ans += [len(i)]
    return ans


def q_4(statement):
    words = statement.split()
    target = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    element = dict()
    for i in range(len(words)):
        if i in target:
            head = words[i][0]
        else:
            head = words[i][0:1]
        element[head] = i+1
    return element


def q_5_word(statement, n):
    unigram = []
    for i in statement:
        unigram += [i]
    ans = copy(unigram)
    for i in range(n-1):
        for j in range(len(unigram)-1-i):
            ans[j] += unigram[j+i+1]
        ans.pop()
    return ans


def q_6(statement1, statement2):
    bi1 = set(q_5_word(statement1, 2))
    bi2 = set(q_5_word(statement2, 2))
    orset = bi1 | bi2
    andset = bi1 & bi2
    subset = bi1 - bi2
    return orset, andset, subset


def q_7(x, y, z):
    return str(x) + "時の" + str(y) + "は" + str(z)


def q_8(statement):
    converted = ""
    for i in statement:
        chr_code = ord(copy(i))
        if chr_code <= 90:
            converted += i
        else:
            converted += chr(219 - chr_code)
    return converted


def q_9(statement):
    return statement


def q_10(file_name):
    hightemap = open(file_name, "r", encoding="shift_jis")
    lines = hightemap.readlines()
    return len(lines)


def q_11(file_name):
    hightemap = open(file_name, "r", encoding="shift_jis")
    lines = hightemap.readlines()
    for i in lines:
        if(i == "\t"):
            i = " "
    hightemap.close()
    return lines[0]


def q_12(file_name):
    hightemap = open(file_name, "r", encoding="utf-8")
    col1 = open("col1.txt", "w", encoding="utf-8")
    col2 = open("col2.txt", "w", encoding="utf-8")
    lines = hightemap.readlines()
    for aline in lines:
        columned_line = aline.split()
        col1.write(columned_line[0] + "\n")
        col2.write(columned_line[1] + "\n")
    hightemap.close()
    col1.close()
    col2.close()


def q_13(col1_name, col2_name, marge_file_name):
    col1 = open(col1_name, "r")
    col2 = open(col2_name, "r")
    marge_file = open(marge_file_name, "w")
    col1_lines = col1.readlines()
    col2_lines = col2.readlines()
    for i in range(len(col1_lines)):
        print(col1_lines[i].strip("\n"))
        marge_file.write(col1_lines[i].strip("\n") + "\t" + col2_lines[i])
    col1.close()
    col2.close()
    marge_file.close()


# def q_13_revised(col1_name, col2_name, marge_file_name):
#   with open("col1.txt") as col1_f, open("col2.txt") as col2_f, open("marge.txt") as marge_f:
#      for col1_f, col2_f in zip(col1_f, col2_f):
#         marge_f.write(col1_f.)

def q_14(file_name, N):
    with open(file_name) as f:
        lines = f.readlines()
        for i in range(N):
            print(lines[i].strip("\n"))


def q_15(file_name, N):
    with open(file_name) as f:
        lines = f.readlines()
        for i in range(N):
            print(lines[len(lines) - i - 1].strip("\n"))


def q_16(file_name, N):
    with open(file_name) as f, open("parsed_file.txt", "w") as d:
        lines = f.readlines()
        if N < 1 or N > len(lines):
            N = 1
        mark_index = len(lines) / N
        for i in len(lines):
            d.write(lines[i])
            if i == mark_index:
                d.write("\n")


def q_20(file_name):
    # JSONデータが複数ある場合json.loads
    import gzip, json
    data = []
    with gzip.open(file_name, "r") as gf:
        for i in gf:
            line = json.loads(i)
            if line["title"] == "イギリス":
                target = line["text"]
                break
    return target


def q_21(text):
    # searchは一個のみ、findallは文字列のみ, finaiterでsearchの複数版、 ()で囲むと取り出せる
    import re
    match = re.findall(r"\[\[Category:.+\]\]", text)
    for i in match:
        print(i)


def q_22(text):
    # searchは一個のみ、findallは文字列のみ, finaiterでsearchの複数版、 ()で囲むと取り出せる
    import re
    match = re.finditer(r"\[\[Category:(.+)\]\]", text)
    # ()で囲んだ場合はそのままでも出せる .group(0)で元の文字列、　複数の()は1から順番に取り出せる
    for i in match:
        print(i.group(1))


def main():
    # print(q_0("stressed"))
    # print(q_1("パタトクカシー"))
    # print(q_2("パトカー", "タクシー"))
    # print(q_3("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."))
    # print(q_4("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."))
    # print(q_5_word("I am an NLPer", 2))
    # or_set, and_set, sub_set = q_6("paraparaparadise", "paragraph")
    # print(str(or_set), str(and_set), str(sub_set))
    # print(q_7("15", "ゴリラ", "気性が荒い"))
    # print(q_8("abcABC"))
    # print(q_8("zyxABC"))
    # print(q_10("popular_name.txt"))
    # print(q_11("popular_name.txt"))
    # q_12("popular_name.txt")
    # q_13("col1.txt", "col2.txt", "marge.txt")
    # q_14("popular_name.txt", 3)
    # q_15("popular_name.txt", 3)
    # q_16("popular_name.txt", 4)
    uk = q_20("jawiki-country.json.gz")
    q_21(uk)
    q_22(uk)

if __name__ == '__main__':
    main()
