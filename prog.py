from Bio.PDB import *
from mpl_toolkits import mplot3d
import re
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import *
from matplotlib.pyplot import *
import matplotlib.cm as cm
from matplotlib.colorbar import Colorbar

parser = PDBParser()
io=PDBIO()
coords = []
labels = []
xdata = []
ydata = []
zdata = []

# Getting PDB Filename to Extract from User
fileName = ""
valid = 1
while valid > 0:
    try:
        fileName = input("Enter name of PDB file:")
        structure = parser.get_structure('4HHB', fileName + '.pdb')
        break
    except:
        print("Invalid file name, try again")

#Extracts Alpha Carbon Atoms from PDB file and places into ac.txt
def getAlphaCarbons(fileName):
    fw = open('ac.txt', 'w')
    fr = open(fileName + '.pdb', 'r')

    for line in fr:
        if(re.search(r'^ATOM\s+\d+\s+CA\s+', line)):
            fw.write(line)

    fw.close()
    fr.close()

#Takes xyz coordinates of ac atoms from ac.txt and puts them into arrays
def getCoordinates():
    fh = open('ac.txt', 'r')    
    for line in fh:
        items = line.split()
        coords.append([float(items[6]), float(items[7]), float(items[8])])
        labels.append(items[5])
        
    for coord in coords:
        xdata.append(coord[0])
        ydata.append(coord[1])
        zdata.append(coord[2])

#Gets cutoff distance from user        
def getCutoff():
    return int(input("Cutoff Distance: "))

#Generates a C-Alpha Trace by plotting and connecting data
def cAlpha(xdata, ydata, zdata):
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.plot3D(xdata, ydata, zdata, "green")
    ax.scatter3D(xdata, ydata, zdata, s=1, c="r", cmap='hsv')
    plt.show()

#Generates a C-Alpha Trace, colored by number of CA within cutoff distance for each CA
def cAlphaColor(xdata, ydata, zdata, cutOff):
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.plot3D(xdata, ydata, zdata, c="black", alpha=0.5)
    p = ax.scatter3D(xdata, ydata, zdata, s=5, c=withinDistance(cutOff), cmap='hsv')
    fig.colorbar(p)
    plt.show()

#Generates a Pairwise Distance Matrix Plot    
def pdMatrix(coords):
    pd = pairwise_distances(coords, Y=None, metric='euclidean', n_jobs=None, force_all_finite=True)
    
    plt.imshow(pd)
    plt.colorbar()
    plt.show()

#For each CA returns count of other CA within a distance cutoff
def withinDistance(cutOff):
    output = []

    pd = pairwise_distances(coords, Y=None, metric='euclidean', n_jobs=None, force_all_finite=True)
    for point in pd:
        count = 0
        for dist in point:
            if dist < cutOff:
                count += 1
        output.append(count)
        
    return np.array(output)

# def distanceColor(cutOff):
    
#     fig = plt.figure()
#     ax = plt.axes()
    
#     ax.axhline(y=0, xmin=0, xmax=len(coords), c=withinDistance(cutOff), cmap='hsv')
    
#     # ax.plot(labels, withinDistance(cutOff))
#     # fig.colorbar(cm.ScalarMappable(cmap='autumn'), ax=ax)    
    
#     plt.show()

#Main Procedure
getAlphaCarbons(fileName)
getCoordinates()
cutOff = getCutoff()

# cAlpha(xdata, ydata, zdata)
# cAlphaColor(xdata, ydata, zdata, cutOff)
# pdMatrix(coords)
# print(withinDistance(cutOff))
# distanceColor(cutOff)