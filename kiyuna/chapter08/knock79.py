'''
79. 適合率-再現率グラフの描画
ロジスティック回帰モデルの分類の閾値を変化させることで，適合率-再現率グラフを描画せよ．
'''
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.metrics import precision_recall_curve
from scipy.stats import hmean
from knock72 import load

model = load("model")
labels = load("labels")
features = load("features")

model.classes_  # => array([-1,  1])
probs = model.predict_proba(features)[:, 1]
pre, rec, th = precision_recall_curve(labels, probs)

plt.plot(pre, rec)
plt.xlabel("precision")
plt.ylabel("recall")
plt.savefig("out79_2d.png")

x1, x2, y = zip(*[(p, r, hmean([p, r])) for p, r in zip(pre, rec) if p and r])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(x1, x2, y)
ax.set_xlabel("precision")
ax.set_ylabel("recall")
ax.set_zlabel("f1")
plt.savefig("out79_3d.png")
