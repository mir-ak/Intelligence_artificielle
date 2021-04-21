import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

np.random.seed(50)

# distance euclidean 
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2)**2))

class KMeans():

    def __init__(self, K=5, max_iters=100, plot_steps=False):
        self.K = K
        self.max_iters = max_iters
        self.plot_steps = plot_steps

        # liste d'exemples d'indices pour chaque cluster       
        self.clusters = [[] for _ in range(self.K)]
        # les centres (vecteur caractéristique moyen) pour chaque cluster
        self.centers = []

    def predict(self, X):
        self.X = X
        self.n_points, self.n_features = X.shape
        
        random_point_idxs = np.random.choice(self.n_points, self.K, replace=False)
        self.centers = [self.X[idx] for idx in random_point_idxs]

        for _ in range(self.max_iters):
            # créer des clusters
            self.clusters = self.create_clusters(self.centers)
            if self.plot_steps:
                self.plot()

            # Calculer de nouveaux centres de gravité à partir des clusters
            Old_centers = self.centers
            self.centers = self.get_centers(self.clusters)
            
            # vérifier si les clusters ont changé
            if self.is_converged(Old_centers, self.centers):
                break

            if self.plot_steps:
                self.plot()

        # Classer les point comme l'index de leurs clusters
        return self.get_cluster_labels(self.clusters)

    def get_cluster_labels(self, clusters):
        # chaque point recevra le libellé du cluster auquel il a été attribué
        labels = np.empty(self.n_points)
        for cluster_idx, cluster in enumerate(clusters):
            for point_index in cluster:
                labels[point_index] = cluster_idx
        return labels

    def create_clusters(self, centers):
        # Définir des point aux centres de gravité les plus proches pour créer des clusters
        clusters = [[] for _ in range(self.K)]
        for idx, point in enumerate(self.X):
            centroid_idx = self.centers_closest(point, centers)
            clusters[centroid_idx].append(idx)
        return clusters

    def centers_closest(self, sample, centers):
        # distance des point actuel à chaque centroïde
        distances = [euclidean_distance(sample, point) for point in centers]
        # Renvoie indices des distances minimales
        closest_index = np.argmin(distances)
        return closest_index

    def get_centers(self, clusters):
        # attribuer la valeur moyenne des clusters aux centres de gravité
        centers = np.zeros((self.K, self.n_features))
        for cluster_idx, cluster in enumerate(clusters):
            cluster_mean = np.mean(self.X[cluster], axis=0)
            centers[cluster_idx] = cluster_mean
        return centers

    def is_converged(self, Old_centers, centers):
        # distances entre chaque ancien et nouveau centre de gravité, pour tous les centres de gravité
        distances = [euclidean_distance(Old_centers[i], centers[i]) for i in range(self.K)]
        return sum(distances) == 0

    def plot(self):
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_title('K_means')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        for i, index in enumerate(self.clusters):
            point = self.X[index].T
            ax.scatter(*point)
        for point in self.centers:
            ax.scatter(*point, marker="*", color='yellow', linewidth=2,s=150)
        plt.show()
        
def main():
    x, y = make_blobs(centers=5, n_samples=500, shuffle=True, random_state=40)      
    clusters = len(np.unique(y))
    print("nb_clusters ",clusters)
    k = KMeans(K=clusters, max_iters=150, plot_steps=True)
    k.predict(x)


main()
        
