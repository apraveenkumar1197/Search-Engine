import os
from collections import OrderedDict

#######   Important Userdefined Paramaters    #########

path="E:\src"
searchword= "Applet";

########################
count=0
searchwordlist=[]
carrysubfolder=[]
carryfiles =[]
tempfolders=[]
mastertempfolders=[]
def isfile(f):
	if ((f).find('.') > 0):
		return 1
	else:
		return 0

		
subfolders = [f.path for f in os.scandir(path) if f.is_dir()]
mastertempfolders = subfolders
carrysubfolder= subfolders
while 1:
	for subfolder in mastertempfolders:		
		subfolders = [f.path for f in os.scandir(subfolder) if f.is_dir()]
		#templist=[]
		#for fold in subfolders:
		#	templist.add(fold.replace("\\","\"));
		tempfolders.extend(subfolders)
		carrysubfolder.extend(subfolders)
	mastertempfolders = tempfolders
	if len(mastertempfolders) < 1:
		break;
	tempfolders=[]
carrysubfolder.sort()
#for carry in carrysubfolder:
#	print(carry)

for path in carrysubfolder:
	files = [path+"\\"+f for f in os.listdir(path) if isfile(f)]
	carryfiles.extend(files);
carryfiles.sort();

contents = ""
for carry in carryfiles:
	count += 1
	print(str(count)+" / "+str(len(carryfiles)),end="\r")
	with open(carry) as f:
		contents = f.read()
		if(contents.find(searchword) > -1):
			count += 1
			searchwordlist.append(carry);
			
#searchwordlist = list(OrderedDict.fromkeys(searchwordlist))
index=1;
print("\n\nSNo  Count   File\n")
for i in searchwordlist:
	count = searchwordlist.count(i)	
	print(str(index)+".   "+str(count)+"    "+i)
	searchwordlist.remove(i)
	index += 1 
