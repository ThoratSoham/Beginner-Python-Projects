import os
path = "G:\\py\\12"
file = os.listdir(path)

for count, filename in enumerate(file):
    if filename.endswith('.txt'):
        nn=f"file_{count+1}.txt"
        oldp = os.path.join(path, filename)
        newp = os.path.join(path, nn)
        os.rename(oldp, newp)
    