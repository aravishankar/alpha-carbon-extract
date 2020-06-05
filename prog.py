from Bio.PDB import *
from mpl_toolkits import mplot3d
import re
import numpy as np
import matplotlib.pyplot as plt
# from skbio import DistanceMatrix

parser = PDBParser()
io=PDBIO()
chainz = []
coords = []
labels = []
xdata = []
ydata = []
zdata = []

fileName = ""

valid = 1
while valid > 0:
    try:
        fileName = input("Enter name of PDB file:")
        structure = parser.get_structure('4HHB', fileName + '.pdb')
        break
    except:
        print("Invalid file name, try again")

# getCoordinates()

def getAlphaCarbons(fileName):
    fw = open('ac.txt', 'w')
    fr = open(fileName + '.pdb', 'r')

    for line in fr:
        if(re.search(r'^ATOM\s+\d+\s+CA\s+', line)):
            fw.write(line)

    fw.close()
    fr.close()

def getCoordinates():
    fh = open('ac.txt', 'r')    
    for line in fh:
        items = line.split()
        coords.append([float(items[6]), float(items[7]), float(items[8])])
        labels.append(items[5])

getAlphaCarbons(fileName)
getCoordinates()


for coord in coords:
    xdata.append(coord[0])
    ydata.append(coord[1])
    zdata.append(coord[2])
        
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(xdata, ydata, zdata, "green")
ax.scatter3D(xdata, ydata, zdata, s=1, c="r", cmap='hsv')

plt.show()