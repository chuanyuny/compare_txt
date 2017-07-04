import difflib
import time
def read_txt(path):
	fo=open(path,'r')
	content=fo.readlines()
	return content

def aa(filename):
	diffmkfile = open('diff.%f.html' % time.time(),'w')
	diffmkfile.write("<meta charset='UTF-8'>")
	diffmkfile.write(filename)
	diffmkfile.close()

txt1=read_txt('read.txt')
txt2=read_txt('read1.txt')

d=difflib.HtmlDiff()
aa(d.make_file(txt1,txt2))

