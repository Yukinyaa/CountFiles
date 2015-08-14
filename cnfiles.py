import os


num_lines=0
num_words=0
num_chars=0
    
def dostuff (fle):
    global num_lines
    global num_words
    global num_chars
    if (fle[-4:]==".cpp" or fle[-2:]==".h" or fle[-3:]==".cs" or fle[-5:]==".java"):
        print(fle)
        with open(fle, 'r') as f:
            for line in f:
                words = line.split()
                num_lines += 1
                num_words += len(words)
                num_chars += len(line)

def rec_cnt (dir):
    for i in os.listdir(dir):
        if os.path.isdir(dir+"/"+i):
            rec_cnt(dir+"/"+i)
        else: dostuff(dir+"/"+i)




rec_cnt(".")


print "num_lines :",num_lines
print "num_words :",num_words
print "num_chars :",num_chars



print "press any key to exit"
os.system('pause')
