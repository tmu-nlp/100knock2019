from scipy import io
import sklearn.decomposition


def main():
    x = io.loadmat('knock_x')['x']
    # 次元圧縮
    clf = sklearn.decomposition.TruncatedSVD(300)
    x300 = clf.fit_transform(x)
    io.savemat('knock_x300', {'x300': x300})


if __name__ == "__main__":
    main()