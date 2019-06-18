# rt-polarity.pos: 5331 lines
# rt-polarity.neg: 5331 lines


# 1, -1をそれぞれ挿入
# コマンド　LC_ALL=C sed -e "s/^/1 /" rt-polarity.pos > pos.txt
# コマンド　LC_ALL=C sed -e "s/^/-1 /" rt-polarity.neg > neg.txt
# 注：LC_ALL=Cがないと、RE error: illegal byte sequence
# neg.txt, pos.txt 共に5331 linesと確認

# ２つのファイルを連結
# cat pos.txt neg.txt > sent.txt
# sent.txt 10662 linesと確認

# シャッフル
# cat sent.txt  | LC_ALL=C sort -R > sentiment.txt
# sentiment.txt 10662 linesと確認

# '1 'で始まる行を数える
# grep -c '^+1 ' sentiment.txt
# 5328
# grep -e ^+1 sentiment.txt |wc -l
# 5331
