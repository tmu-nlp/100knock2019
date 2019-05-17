##タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

import re

filename = r"\Users\Koya\Documents\Lab\100knock2019\Eguchi\chapter02\hightemp.txt"
file = open(filename, "r",encoding="utf-8" )
readfile = file.read()

refile  = readfile.replace("\t", " ")

print( refile)

file.close()
