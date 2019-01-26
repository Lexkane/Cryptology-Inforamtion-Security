#Cracking brute force caesar cipher for English words
#using euristics algorithm of % occurence

def main():
 message = input('Please input ciphertext')
 LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 for key in range(len(LETTERS)):
      translated = ''
      for symbol in message:
         if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
               num = num + len(LETTERS)
            translated = translated + LETTERS[num]
         else:
            translated = translated + symbol
      #print('Cracking #%s: %s' % (key, translated))
      if ((translated.count('E')/len(translated) >= 0.10) and (translated.count('A')/len(translated) >=0.08)\
      or (translated.count('R')/len(translated) >=0.07)):
       print('Euristic key is #%s: %s' % (key, translated))
      else:pass


if __name__=="__main__":
      main()