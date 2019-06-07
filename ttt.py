import pull_data
def compare(File1,File2):
    with open(File1,'r') as f:
        d=set(f.readlines())
    with open(File2,'r') as f:
        e=set(f.readlines())

    with open(File1,'a') as f:
        for line in list(e-d):
            f.write(line)
category = ["science", "business", "health"]
for c in category:
    print(c)
    pull_data.pull_data(c)
    compare("{}.txt".format(c), "{}-test.txt".format(c))
