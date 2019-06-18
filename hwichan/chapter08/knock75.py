from knock74 import create_model
from collections import defaultdict


def main():
    vectorizer, model = create_model()

    weights = model.coef_[0]  # 重み
    names = vectorizer.get_feature_names() # 名前

    weight_list = sorted(list(zip(weights, names)))

    print('Top 10')
    for w in reversed(weight_list[-10:]):
        print(f'{w[1]}\t{w[0]}')

    print('Worst 10')
    for w in weight_list[:10]:
        print(f'{w[1]}\t{w[0]}')

if __name__ == "__main__":
    main()

# 結果
#
# Top 10
# beauti  3.0394149995402278
# refresh 2.780843933992421
# perform 2.593971638186186
# enjoy   2.515050467777645
# entertain       2.387982917314859
# solid   2.371026978624689
# best    2.3356335717964996
# still   2.312221458313934
# fun     2.2895744522475145
# engross 2.263142017921292
#
# # Worst 10
# bad     -3.7150401372785224
# bore    -3.2958760909672105
# dull    -3.171941446145977
# fail    -2.6149759569184923
# lack    -2.5863780424366367
# worst   -2.526162987192001
# neither -2.4648398311488293
# wast    -2.180203916552519
# thing   -2.157040080851157
# mediocr -2.1097236310014553
