from Bio.PDB import *
import re
from skbio import DistanceMatrix

parser = PDBParser()
io=PDBIO()
chainz = []
coords = []
labels = []
fileName = ""

valid = 1
while valid > 0:
    try:
        fileName = input("Enter name of PDB file:")
        structure = parser.get_structure('4HHB', fileName + '.pdb')
        break
    except:
        print("Invalid file name, try again")

getAlphaCarbons(fileName)
# getCoordinates()

def getAlphaCarbons(fileName):
    fw = open('ac.txt', 'w')
    fr = open(fileName + '.pdb', 'r')

    for line in fr:
        if(re.search(r'^ATOM\s+\d+\s+CA\s+', line)):
            fw.write(line)

    fw.close()
    fr.close()

# def getCoordinates():
fh = open('ac.txt', 'r')    
for line in fh:
    items = line.split()
    coords.append([items[6], items[7], items[8]])
    labels.append(items[5])
    
    
print(labels)
    
    
    