class ceaserCipher :
    def encrypt(self, text, k) :
        res = ''
        for char in text :
            num = ord(char) - 97
            num += k
            num = num % 26
            newKey = 97 + num
            res += chr(newKey)
        return res.upper()
    
    def decrypt(self, text, k) :
        text = text.lower()
        res = ''
        for char in text :
            num = ord(char) - 97
            num -= k
            num = ((26 + num) % 26) + 97
            res += chr(num)
        return res


if __name__ == "__main__" :
    text  = 'yaswanth'
    k = 3
    print(ceaserCipher().encrypt(text, k))
    print(ceaserCipher().decrypt('BDVZDQWK', k))