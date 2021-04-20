import math
from math import *
from copy import *

from math import *
from copy import *
import re

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
    # with内でreturnしても大丈夫大宰府天満宮
    with open(file_name, "r",) as f:
        return len(f.readlines())


def q_11(file_name):
    with open(file_name, "r") as f:
        # for文のiに代入はできない
        lines = f.readlines()
        before = lines[0]
        for i in range(len(lines)):
            lines[i] = " ".join(lines[i].split("\t"))
        print(before + "→" + lines[0])


def q_12(file_name):
    popular_name = open(file_name, "r")
    col1 = open("col1.txt", "w")
    col2 = open("col2.txt", "w")
    for i in popular_name:
        columned_line = i.split()
        col1.write(columned_line[0] + "\n")
        col2.write(columned_line[1] + "\n")
    popular_name.close()
    col1.close()
    col2.close()


def q_13(col1_name, col2_name, marge_file_name):
    with open(col1_name, "r") as col1, open(col2_name, "r") as col2, open(marge_file_name, "w") as marge_file:
        for i, j in zip(col1, col2):
            marge_file.write(i.strip("\n") + "\t" + j)


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
    with open("q_16test.txt") as f, open("parsed_file.txt", "w") as d:
        lines = f.readlines()
        if N < 1 or N > len(lines):
            N = 1
        mark_index = math.ceil(len(lines) / N)
        for i in range(len(lines)):
            d.write(lines[i])
            if (i+1) % mark_index == 0 and i != 0:
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
    match = re.findall(r"\[\[Category:.+\]\]", text)
    for i in match:
        print(i)


def q_22(text):
    # searchは一個のみ、findallは文字列のみ, finaiterでsearchの複数版、 ()で囲むと取り出せる
    match = re.finditer(r"\[\[Category:(.+)\]\]", text)
    # ()で囲んだ場合はそのままでも出せる .group(0)で元の文字列、　複数の()は1から順番に取り出せる
    for i in match:
        print(i.group(1))


def q_23(text):
    match = re.finditer(r"(=+).+=+", text)
    for i in match:
        print(i.group(0) + ":" + str(len(i.group(1))))


def q_24(text):
    # ファイルは[[ファイル:Wikipedia-logo-v2-ja.png|thumb|説明文]]という形式。知らんがな
    match = re.finditer(r"\[\[ファイル:(.+)\|", text)
    for i in match:
        print(i.group(0) + ":" + i.group(1))


def q_25(text):
    # MULTILINE 複数行 DOTALL 改行無視
    match = re.finditer(r"^\{\{基礎情報.*$(.*)^\}\}", text, re.MULTILINE + re.DOTALL)
    result = dict()
    for i in match:
        pattern =r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'
        result(re.findall(pattern, i.group(0), re.MULTILINE + re.DOTALL))
    for i, j in result.items():
        print(i + ":" + j)

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
    print(q_10("popular_name.txt"))
    print(q_11("popular_name.txt"))
    q_12("popular_name.txt")
    q_13("col1.txt", "col2.txt", "marge.txt")
    q_14("popular_name.txt", 3)
    q_15("popular_name.txt", 3)
    q_16("popular_name.txt", 3)
    uk = q_20("jawiki-country.json.gz")
    # print(uk)
    # q_21(uk)
    # q_22(uk)
    # q_23(uk)
    # q_24(uk)
    # q_25(uk)

if __name__ == '__main__':
    main()
