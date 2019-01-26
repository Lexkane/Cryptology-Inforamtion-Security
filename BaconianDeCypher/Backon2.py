def main():
 pass

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'   

import sys
#methods
def rebase(a):
 if len(a)%5==0:
  return a
 else :
  return  a[:(len(a)-len(a)%5)]
         
def decode(a):
 return chr(97+key.find(a))
 #main
a=sys.argv[1].replace(" ","")
b=rebase(a)
#k=b.translate({ord(x): y for (x, y) in zip(alphabet2, translateall)})
e=['a' if 96<ord(i)<123  else "b" for i in b]
c="".join(e)
d=[decode(c[i:i+5]) for i in range(0, len(c),5)]
p="".join(d)
print(str(p))
 

