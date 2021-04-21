import numpy as np
import matplotlib.pyplot as plt
import time
import random

centre1=np.array([3,3])
centre2=np.array([-3,-3])
sigma1=np.array([[1.5,0],[0,1.5]])
sigma2=np.array([[1.5,0],[0,1.5]])
taille1=200
taille2=200
cluster1=np.random.multivariate_normal(centre1,sigma1,taille1)
cluster2=np.random.multivariate_normal(centre2,sigma2,taille2)

plt.scatter([point[0] for point in cluster1], [point[1] for point in cluster1], color="pink")
plt.scatter([point[0] for point in cluster2], [point[1] for point in cluster2], color="blue")
plt.scatter(centre1[0], centre1[1], color="red")
plt.scatter(centre2[0], centre2[1], color="red")

def f(x,w):
    if not w[2]:
        w[2] = 1
    return -(w[0]+w[1]*x)/w[2] 

def perceptron(a,b):
	v_apprentissage = 0.1
	w = np.array([0,0,0])
	nb_apprentissage = 1
	for x in range(nb_apprentissage):
		for i in range(len(a)):#pour i vers N
			y1 = np.array([1,a[i][0],a[i][1]])
			y2 = np.array([1,b[i][0],b[i][1]])
			if 1 * np.dot(w,y1) <= 0:#verifie les cas rose 
				w = w + v_apprentissage * y1 * 1 
			if -1 * np.dot(w,y2) <= 0:#verifie les cas blue 
				w = w + v_apprentissage * y2 * -1
			
			#if(i % 40 == 0):#on dessine avec quelque iteration 
				plt.scatter([point[0] for point in cluster1], [point[1] for point in cluster1], color ="pink")
				plt.scatter([point[0] for point in cluster2], [point[1] for point in cluster2], color ="blue")
				plt.scatter(centre1[0], centre1[1], color="red")
				plt.scatter(centre2[0], centre2[1], color="red")
				plt.plot([x for x in range(-5,5)],[f(x,w) for x in range(-5,5)],label='line')
				print(w)
				#plt.show()
				
	return w

def perceptron_random(A,B):#Aléatoire 
    v_apprentissage = 0.1
    w = np.array([0,0,0])
    nb_apprentissage = 1
    for i in range(150):
        t = random.randint(0,1) 
        nb_t = random.randint(0,len(A)-1) 
        p_t = np.array([1,0,0])
        if(t):
            p_t[1],p_t[2] = A[nb_t][0],A[nb_t][1]
            Y = 1
        else:
            p_t[1],p_t[2] = B[nb_t][0],B[nb_t][1]
            Y  = -1
        if( Y * np.dot(w,p_t) <= 0):
            w = w + v_apprentissage * p_t * Y
        
        if (Y * np.dot(w,p_t) <= 0 ):
            w = w + v_apprentissage * p_t * Y

        if(i % 40 == 0):#on dessine avec quelque iteration 
            print(i)
            plt.scatter([point[0] for point in cluster1], [point[1] for point in cluster1], color ="pink")
            plt.scatter([point[0] for point in cluster2], [point[1] for point in cluster2], color ="blue")
            plt.scatter(centre1[0], centre1[1], color="red")
            plt.scatter(centre2[0], centre2[1], color="red")
            plt.plot([x for x in range(-5,5)],[f(x,w) for x in range(-5,5)],label='line')
            print(w)
            #plt.show()
    return w

w = perceptron(cluster1,cluster2)
#w = perceptron_random(cluster1,cluster2)
print(w)
plt.scatter([point[0] for point in cluster1], [point[1] for point in cluster1], color="pink")
plt.scatter([point[0] for point in cluster2], [point[1] for point in cluster2], color="blue")
plt.scatter(centre1[0], centre1[1], color="red")
plt.scatter(centre2[0], centre2[1], color="red")
plt.plot([x for x in range(-5,5)],[f(x,w) for x in range(-5,5)],label='line')
plt.show()


