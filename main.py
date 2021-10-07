import random as r
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans



def random_boja():
    return 'black'
    #return (r.random(), r.random(), r.random())

def generisi_tacku(xmin = 0, xmax = 1000, ymin = 0, ymax = 1000):
    x = r.uniform(xmin, xmax)
    y = r.uniform(ymin, ymax)
    return [x, y]

def generisi_tacke(n = 100, xmin = 0, xmax = 1000, ymin = 0, ymax = 1000):
    tacke = []
    for _ in range(n):
        tacke.append(generisi_tacku(xmin, xmax, ymin, ymax))

    return tacke

def razdvoji_tacke(tacke):
    x = []
    y = []

    for e in tacke:
        x.append(e[0])
        y.append(e[1])
    return x, y,

tacke = generisi_tacke(30)
x, y = razdvoji_tacke(tacke)


df = DataFrame(tacke,columns=['x','y'])
kmeans = KMeans(n_clusters=3).fit(df)
centroids = kmeans.cluster_centers_

plt.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='black', s=50)
plt.show()