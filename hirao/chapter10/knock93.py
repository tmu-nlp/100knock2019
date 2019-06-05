with open("family.txt") as f, open("pca_family.txt") as f_pca:
    n = 0
    count = 0
    for line1, line2 in zip(f, f_pca):
        if line1.rstrip().split()[-1] == line2.rstrip().split()[-1]:
            count +=1
        n += 1
    print(f"PCA Accuracy: {count/n * 100:.2f}%")

with open("family.txt") as f, open("w2v_family.txt") as f_pca:
    n = 0
    count = 0
    for line1, line2 in zip(f, f_pca):
        if line1.rstrip().split()[-1] == line2.rstrip().split()[-1]:
            count +=1
        n += 1
    print(f"Word2Vec Accuracy: {count/n * 100:.2f}%")

# PCA Accuracy: 0.20%
# Word2Vec Accuracy: 21.34%