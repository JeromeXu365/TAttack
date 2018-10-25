
import numpy as np
np.random.seed(1337)  # for reproducibility
import matplotlib.pyplot as plt

'''
#1.2 baseline attack
# give X,Y axis name below
plt.xlabel('Datasets')
plt.ylabel('Accuracy')
labels = ['Adult', 'CIFAR-10', 'CIFAR-100', 'MNIST']

# plot data
Y1 = [0.50,0.79,0.92,0.51]
Y2 = [0.50,0.79,0.92,0.51]
Y3 = [0.46,0.79,0.92,0.50]
# plot type
plt.bar(np.arange(4), Y1, label = "Precision", color = "R", width = 0.25)
plt.bar(np.arange(4) + 0.25, Y2, label = 'Recall', color = 'G', width = 0.25)
plt.bar(np.arange(4) + 0.5, Y3, label = 'F1-Score', color = 'B', width = 0.25)
plt.xticks(np.arange(4)+ 0.25,labels)
#plt.scatter(X, Y)
plt.legend()
plt.show()
'''

'''
# 1.3 target precision comparison
# give X,Y axis name below
plt.xlabel('Epoches')
plt.ylabel('Attack accuracy')
#labels = ['Adult', 'CIFAR-10', 'CIFAR-100', 'MNIST']

# plot data
X1 = [  100,  200,  300,  400,  500,  600,  700,  800,  900, 1000]
Y1 = [0.503,0.509,0.509,0.507,0.515,0.508,0.513,0.511,0.518,0.509]

X2 = [ 100, 200, 300, 400, 500, 600, 700, 800, 900,1000]
Y2 = [0.61,0.66,0.69,0.71,0.76,0.74,0.78,0.80,0.76,0.79]

X3 = [ 100, 200, 300, 400, 500, 600, 700, 800, 900,1000]
Y3 = [0.58,0.65,0.70,0.72,0.77,0.78,0.79,0.81,0.84,0.83]
# plot type
plt.ylim(0.45,0.85)
dot1, = plt.plot(X1, Y1, color = 'blue', marker = '*')
dot2, = plt.plot(X2, Y2, color = 'green', marker = '8')
dot3, = plt.plot(X3, Y3, color = 'red', marker = '4')

plt.legend(handles=[dot1,dot2,dot3], labels =['MNIST','CIFAR-10','CIFAR-100'],loc='best')
plt.show()
'''

'''
# 1.4.1 overfitting vs accuracy
# give X,Y axis name below
plt.xlabel('Target overfitting level')
plt.ylabel('Attack accuracy')
#labels = ['Adult', 'CIFAR-10', 'CIFAR-100', 'MNIST']

# plot data
X1 = [ 0.17,0.18,0.23,0.23,0.26,0.4,0.47,0.51,0.51,0.54,
       0.56,0.56,0.56,0.59,0.59,0.59,0.61,0.61,0.61]
Y1 = [0.57,0.58,0.60,0.58,0.61,0.66,0.69,0.71,0.72,0.75,
       0.76,0.74,0.75,0.78,0.76,0.77,0.80,0.79,0.79]

X2 = [ 0.26,0.42,0.48,0.52,0.55,0.56,0.58,0.67,0.68,0.71,
       0.71,0.72,0.74,0.76,0.77,0.77,0.78,0.79,0.79,0.83,0.84,0.86]
Y2 = [0.58,0.65,0.69,0.70,0.70,0.71,0.72,0.77,0.78,0.78,
       0.79,0.80,0.81,0.82,0.83,0.83,0.84,0.84,0.85,0.88,0.88,0.92]

X3 = [0.03,0.02,0.02,0.03,0.03,0.03,0.04,0.03,0.04,0.04,0.04,0.03,
       0.02,0.02,0.02,0.03,0.02,0.02,0.03,0.03,0.03,0.02]
Y3 = [0.503,0.503,0.509,0.509,0.507,0.515,0.508,0.513,0.511,0.518,
   0.509,0.510,0.504,0.510,0.504,0.509,0.506,0.509,0.507,0.510,0.509,0.510]

X4 = np.linspace(0,1,50)
Y4 = X4/2+0.5

# plot type
plt.xlim(0,1)
plt.ylim(0.45,1)
plt.scatter(X1,Y1,c='r',marker='o',s=40,label='CIFAR 10')
plt.scatter(X2,Y2,c='b',marker='o',s=60,label='CIFAR 100')
plt.scatter(X3,Y3,c='g',marker='o',s=20,label='MNIST')
plt.plot(X4,Y4)
plt.grid(linestyle='-.')
plt.legend()

plt.show()
'''


# 1.4.2 complexity vs accuracy
# give X,Y axis name below
plt.xlabel('Network complexity,hidden points')
plt.ylabel('Attack accuracy')
#labels = ['Adult', 'CIFAR-10', 'CIFAR-100', 'MNIST']

# plot data
X1 = [  50,   100,  200,  300,  400,  500,  600,  700,  800]
Y1 = [0.515,0.510,0.510,0.509,0.506,0.509,0.507,0.510,0.509]

X2 = [50,100,200, 500, 800]
Y2 = [0.79,0.77,0.74,0.75,0.75]

X3 = [50,100,200, 500, 800]
Y3 = [0.83,0.84,0.82,0.80,0.78]

col_labels = ['50','100','200','500','800']
row_labels = ['Parameters']
table_vals = [[158750,317400,634700,1586600,2538500]]
my_table = plt.table(cellText=table_vals, colWidths=[0.1]*5,
                     rowLabels=row_labels, colLabels=col_labels, loc='upper center')

# plot type
plt.ylim(0.45,1)
dot1, = plt.plot(X1, Y1, color = 'blue', marker = '*')
dot2, = plt.plot(X2, Y2, color = 'green', marker = '8')
dot3, = plt.plot(X3, Y3, color = 'red', marker = 's')
plt.legend(handles=[dot1,dot2,dot3], labels =['MNIST','CIFAR-10','CIFAR-100'],loc='best')
plt.grid(linestyle='-.')

plt.show()
