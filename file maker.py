import os
path = "G:\\py\\12"

for i in range(1,6):
    file = f"{i}.txt"
    fpath =os.path.join(path, file)
    
    with open(fpath,'w') as f:
        f.write("this is a file")