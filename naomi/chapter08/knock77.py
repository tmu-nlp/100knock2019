# 77. 正解率の計測
# 76の出力を受け取り，予測の正解率，正例に関する適合率，再現率，F1スコアを求めるプログラムを作成せよ．

def main():
    with open('lables.txt', 'r', encoding='utf-8') as fin:

        corr = 0
        pos = 0
        pos_corr = 0
        counts = 0
        
        for line in fin:
            (lbl, prd, prob) = line.rstrip().split()
            if lbl == prd:
                corr += 1
            if lbl == '+1':
                pos += 1
                if prd == '+1':
                    pos_corr += 1
            counts += 1
        accuracy = corr/counts
        precision = pos_corr/pos

    print(f'正解率： {accuracy}')
    print(f'正例の適合率： {precision}')

if __name__ == '__main__':
    main()
