import sys

def main():
 #inputdata
 key = 'aaaaabbbbbabbbaabbababbaaababaab'
 alphabet = 'abcdefghijklmnopqrstuvwxyz'   
 alphabet2=alphabet+'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 translatea='aaaaaaaaaaaaaaaaaaaaaaaaaa'
 translateb='bbbbbbbbbbbbbbbbbbbbbbbbbb'
 translateall=translatea+translateb
 #methods
 def rebase(a):
  if len(a)%5==0:
   return a
  else :
   return  a[:(len(a)-len(a)%5)]
 
 def find_str(inputstr,strtofind):
    index=0
    if strtofind in inputstr:
         c=strtofind[0]
         for ch in inputstr:
          if ch==c:
           if inputstr[index:index+len(strtofind)]==strtofind:
            return index
    else:return -1               
 
 def decode(a):
  return chr(97+key.find(a))

 #main
 a=sys.argv[1].replace(' ','')
 b=rebase(a)
 c=b.translate({ord(x): y for (x, y) in zip(alphabet2, translateall)})
 d=[decode(c[i:i+5]) for i in range(0, len(c),5)]
 p="".join(d)
 print(p)
 


if  __name__=="__main__":
    main()