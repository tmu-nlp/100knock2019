import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from knock76 import create_model
from knock77 import score
from sklearn.metrics import precision_recall_curve


def main():
    labels, features, model = create_model('sentiment.txt')

    '''
        precision_recall_curve()
            第１引数に正解ラベル、第２引数に予測ラベルの予測確率を指定することにより
            precision : 閾値, recall : 再現率 関係を得られる
            [:, 1] は閾値の範囲？

        参考
            https://ohke.hateblo.jp/entry/2017/08/25/230000
    '''
    precision, recall, thresholds = precision_recall_curve(labels, model.predict_proba(features)[:, 1])

    plt.plot(precision, recall, color="red")

    fp = FontProperties(fname=r'/mnt/c//Windows/Fonts/ipaexg.ttf')
    plt.xlabel('閾値', fontproperties=fp)
    plt.ylabel('再現率', fontproperties=fp)

    plt.show()

    '''
    正解に対する再現率 : 正解が1だったものに対して予測も1であるものの割合
    であるから閾値が高くなると予測が1になる確率が低くなるため再現率は下がる
    '''


if __name__ == "__main__":
    main()
