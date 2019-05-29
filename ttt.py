def compare(File1,File2):
	with open(File1,'r') as f:
		d=set(f.readlines())
	with open(File2,'r') as f:
		e=set(f.readlines())

    	with open('file1','a') as f:
        	for line in list(e-d):
        		f.write(line)
compare("file1", "file2")
