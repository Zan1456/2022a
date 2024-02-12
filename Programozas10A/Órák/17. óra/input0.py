import fv

rows = fv.read("input0.txt")
print(fv.process_space(rows[0], first=1))

rows = fv.read("input1.txt")
print(fv.process_space(rows[0], first=1, last=1))

rows = fv.read("input2.txt")
print(fv.process_space(rows[1], first=1, last=1))

rows = fv.read("input3.txt")
print(fv.process_space(rows[1], first=1, last=1, dataseparator=";"))