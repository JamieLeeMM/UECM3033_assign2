import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy.linalg as sp

img=mpimg.imread('Garden.tiff')
[r,g,b] = [img[:,:,i] for i in range(3)]


fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(r, cmap = 'Reds')
ax3.imshow(g, cmap = 'Greens')
ax4.imshow(b, cmap = 'Blues')
plt.show()


#Lower resolution picture
img=mpimg.imread('Garden.tiff')
[r1,g1,b1] = [img[:,:,i] for i in range(3)]

Ur1,Sr1,Vr1=sp.svd(r,full_matrices=False)
Sr1 = np.diag(Sr1)

Ug1,Sg1,Vg1=sp.svd(g,full_matrices=False)
Sg1 = np.diag(Sg1)

Ub1,Sb1,Vb1=sp.svd(b,full_matrices=False)
Sb1 = np.diag(Sb1)

SrNew1 = np.zeros_like(Sr1)
SrNew1[0:30] = Sr1[0:30]
Rnew1 = Ur1.dot(SrNew1).dot(Vr1)

SgNew1 = np.zeros_like(Sg1)
SgNew1[0:30] = Sg1[0:30]
Gnew1 = Ug1.dot(SgNew1).dot(Vg1)

SbNew1 = np.zeros_like(Sb1)
SbNew1[0:30] = Sb1[0:30]
Bnew1 = Ub1.dot(SbNew1).dot(Vb1)

img[:,:,0]=Rnew1
img[:,:,1]=Gnew1
img[:,:,2]=Bnew1

fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(r, cmap = 'Reds')
ax3.imshow(g, cmap = 'Greens')
ax4.imshow(b, cmap = 'Blues')
plt.show()

#higher resolution picture
img_2=mpimg.imread('Garden.tiff')
[r2,g2,b2] = [img_2[:,:,i] for i in range(3)]

Ur2,Sr2,Vr2=sp.svd(r2,full_matrices=False)
Sr2 = np.diag(Sr2)

Ug2,Sg2,Vg2=sp.svd(g2,full_matrices=False)
Sg2 = np.diag(Sg2)

Ub2,Sb2,Vb2=sp.svd(b2,full_matrices=False)
Sb2 = np.diag(Sb2)

SrNew2 = np.zeros_like(Sr2)
SrNew2[0:200] = Sr2[0:200]
Rnew2 = Ur2.dot(SrNew2).dot(Vr2)

SgNew2 = np.zeros_like(Sg2)
SgNew2[0:200] = Sg2[0:200]
Gnew2 = Ug2.dot(SgNew2).dot(Vg2)

SbNew2 = np.zeros_like(Sb2)
SbNew2[0:200] = Sb2[0:200]
Bnew2 = Ub2.dot(SbNew2).dot(Vb2)

img_2[:,:,0]=Rnew2
img_2[:,:,1]=Gnew2
img_2[:,:,2]=Bnew2

fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img_2)
ax2.imshow(r2, cmap = 'Reds')
ax3.imshow(g2, cmap = 'Greens')
ax4.imshow(b2, cmap = 'Blues')
plt.show()

np.count_nonzero()