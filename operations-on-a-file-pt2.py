import os

#line split
with open('filename1.txt', 'r') as f:
    for line in f:
        words = line.split()
        print(len(words), "words --> ", line.strip())
print()


#strip method 
with open('filename2.txt', 'r') as f:
    for line in f:
        print(line.strip())
print()


print("Downtown Central Park West (A) (B) (C) (D) ")

content = ''

with open ('filename1.txt', 'r') as f:
	content += '--- filename1.txt--- \n'
	content += f.read() + '\n'

#repeat this same snippet for filename2.txt
with open ('filename2.txt', 'r') as f:
	content += '--- filename2.txt--- \n'
	content += f.read() + '\n'

#then do this:

with open ('filecombination.txt', 'w') as out:
	out.write(content)


if os.path.exists("filecombination.txt"):
      print("This file already exists and will be overwritten.")
else:
      print("This file does not exist. Creating the file now.")

if os.path.exists("rinse.txt"):
    os.remove("rinse.txt")
    print("File deleted")
else:
      print("Can't remove file: (does not exist or is not in the correct folder)")