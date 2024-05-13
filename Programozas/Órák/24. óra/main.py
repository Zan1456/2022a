l = ["Géza", "Ivett"]

# r - read, w - write, a - append
f = open("file.txt", "a", encoding="utf-8")
for i in range(len(l)):
    f.write(f"{l[i]}\n")

for i in range(len(l)):
    f.write(f"{i+1}.név: {l[i]}\n")

f.close()