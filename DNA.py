file_text = open ("x.txt.") .read()
X = len(file_text)
C = 0
G = 0

for i in range (0,X):
    if file_text[i] == 'C':
        C = C + 1
    else:
        C = C + 0
    if file_text[i] == 'G':
        G = G + 1
    else:
        G = G + 0
    
    Y = C + G

print "The length of the DNA is", len(file_text)
print "The number of C's is", C
print "The number of G's is", G
print "The percentage of C+G is", (100.0*Y)/X
