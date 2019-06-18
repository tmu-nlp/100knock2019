'''
75. 素性の重み
73で学習したロジスティック回帰モデルの中で，重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．
'''

from knock73 import serialize, deserialize


def feature_weights():
    model = deserialize("model")
    names = deserialize("names")
    weights = model.coef_[0].tolist()
    weights_name = list(zip(weights, names))
    weights_name.sort()
    print("highest")
    for weight, name in weights_name[-1:-10:-1]:
        print(f"{weight:.5} {name}")
    print("\nlowest")
    for weight, name in weights_name[:9]:
        print(f"{weight:.5} {name}")
    


if __name__ == "__main__":
    feature_weights()
