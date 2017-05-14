import codecs
import re
import string
import os

def read():
    dir = os.getcwd()
    files = os.listdir(dir + "/data/nuc/")   
    for file in files:
        testdir = "data/nuc/"
        with codecs.open(testdir + file, "r", "euc-jp", "ignore") as f:
            current_line = f.readline()
            w = codecs.open("data/train_data.txt", "a", "utf-8")
            w.write("\n")
            while current_line:
                current_line = edit_line(current_line)
                w.write(current_line)
                current_line = f.readline()
            w.write(current_line)

def edit_line(one_line):
    #％ｃｏｍ：
    if ("％ｃｏｍ：" in one_line):
        one_line = one_line.replace("％ｃｏｍ：", "")
    #＊と＠は行ごと削除
    if ("＊" in one_line or "＠" in one_line):
        return ""

    # FとM：
    regexf = u'F...：'
    regexm = u'M...：'
    one_line = re.sub(regexf, "", one_line)
    one_line = re.sub(regexm, "", one_line)

    regexca = u'F...'
    regexmtanaka = u'M...'

    one_line = re.sub(regexca, "キャサリン", one_line)
    one_line = re.sub(regexmtanaka, "田中さん", one_line)

    # （）
    regexp = u'（.*）'
    one_line = re.sub(regexp, "", one_line)

    regexp = u'＜.*＞'
    one_line = re.sub(regexp, "", one_line)

    return one_line
        
        
if __name__ == "__main__":
  read()
