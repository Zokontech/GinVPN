#Alexander Krasny
round_constants=(0x01, 0x02, 0x04,0x08,0x10,0x20,0x40)

#array for s_box permutation transformation
s_box = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)
#array for reversed s_box permutation transformation
inv_s_box = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)
#array for mix_colum operation permutation transformation
column_mix=[
    [2,3,1,1],
    [1,2,3,1],
    [1,1,2,3],
    [3,1,1,2]]

#array for reversing mix_colum operation permutation transformation
inv_column_mix=[
    [0x0e,0x0b,0x0d,0x09],
    [0x09,0x0e,0x0b,0x0d],
    [0x0d,0x09,0x0e,0x0b],
    [0x0b,0x0d,0x09,0x0e]]

class InvalidKey(Exception):
    pass

class AES:
    def __init__(self, master_key): #generates round keys for encryption/decryption give 32byte master key
        if(len(master_key)!=32):
            raise InvalidKey("Invald Key Length")
        if type(master_key) is str:
            mk=bytearray(master_key, 'utf-8')
        elif type(master_key) is bytes:
            mk=bytearray(master_key)
        else:
            raise InvalidKey("Invald Key Types")
        self.num_rounds=14
        self.round_keys=[]
        word_array=[]
        self.key_expansion(mk,word_array)
        for i in range(0,self.num_rounds+1):
            self.round_keys.append(self.word_keys(word_array[4*i:4*i+4]))

    #key expansion functions 
    def xor_bytes(self, a,b):#returns a bytes object containing a xor b
        return bytes(i^j for i, j in zip(a, b))
    def sub_word(self, word):#returns the s_box transformation on the bytes in word
        return bytes(s_box[i] for i in word)
    def rot_word(self, word):#returns the word rotated left one position
        return bytes([word[1]])+bytes([word[2]])+bytes([word[3]])+bytes([word[0]])

    
    #generates 60 words from the master key and stores them in word array by modifying the last word with the previous 3 methods as specified by AES standards.
    def key_expansion(self, key, word_array):
        key_length=int(len(key)/4)
        for i in range(0,key_length):
            word_array.append(bytes(key[i*4:i*4+4]))
        for i in range(key_length, 4 * (self.num_rounds+1)):
            temp=word_array[-1]
            if (i % key_length == 0):
                temp = self.xor_bytes(self.sub_word(self.rot_word(temp)), bytes([round_constants[int(i/key_length)-1]])+bytes([0])+bytes([0])+bytes([0]))
            elif (key_length > 6 and i % key_length == 4):
                temp = self.sub_word(temp)
            word_array.append(self.xor_bytes(word_array[i-key_length], temp))

    #encryption functions
    def add_round_key(self, txt, key):#returns txt xor-ed with key
        return bytearray([txt[i]^key[i] for i in range(0,len(txt))])
    def sub_bytes(self, msg):#returns the s_box transformation of msg
        return bytearray([s_box[i] for i in msg])
    def shift_rows(self, msg):#returns msg with rows shifted as specified by AES standards
        return bytearray(
        [msg[0],msg[5],msg[10],msg[15],
        msg[4],msg[9],msg[14],msg[3],
        msg[8],msg[13],msg[2],msg[7],
        msg[12],msg[1],msg[6],msg[11]])

    #inspired by https://stackoverflow.com/questions/45442396/a-pure-python-way-to-calculate-the-multiplicative-inverse-in-gf28-using-pytho
    def multiply(self, b,a): #return galios multiplication of b and a
        res = 0
        for i in range(0,8):
            if b & 1: 
                res ^= a
            hi_set = a & 0x80
            a <<= 1
            a &= 0xFF
            if hi_set:
                a ^= 0x1b
            b >>= 1
        return res

    def mix_col(self, col):# returns col galios multiplied by the column_mix array.
        b=bytearray()
        for j in range(0,4):
            tmp=0x00
            for i in range(0,4):
                tmp^=self.multiply(column_mix[j][i], col[i])
            b+=bytes([tmp])
        return b

    def mix_cols(self, msg):#return an bytearray made from concatenation of each column of message after mix_col
        b=bytearray()
        for i in range (0,4):
            b+=self.mix_col(msg[4*i:4*i+4])
        return(b)


    #decryption functions
    def inv_sub_bytes(self, msg):#returns the msg after the application of the inverse s_box transformation
        return bytearray([inv_s_box[i] for i in msg])

    def inv_shift_rows(self, msg):#returns msg with row shifts of shift_rows reversed as specified by AES standards
        return bytearray(
        [msg[0],msg[13],msg[10],msg[7],
        msg[4],msg[1],msg[14],msg[11],
        msg[8],msg[5],msg[2],msg[15],
        msg[12],msg[9],msg[6],msg[3]])

    def inv_mix_col(self, col):#returns col galios multiplied by the inv_column_mix array.
        b=bytearray()
        for j in range(0,4):
            tmp=0x00
            for i in range(0,4):
                tmp^=self.multiply(inv_column_mix[j][i], col[i])
            b+=bytes([tmp])
        return b

    def inv_mix_cols(self, msg):#return an bytearray made from concatenation of each column of message after inv_mix_col
        b=bytearray()
        for i in range (0,4):
            b+=self.inv_mix_col(msg[4*i:4*i+4])
        return(b)

    def pad(self, msg): #returns the msg padded to a multiple of 16 bytes with the byte representing the number of pad characters
        if (len(msg))%16!=0:
            pad=16-(len(msg))%16
            for i in range(0, pad):
                msg.append(pad)
        return msg
    def un_pad(self, msg):#returns the reverse of the padding process
        pad=msg[-1]
        for i in range(0, pad):
            if msg[-1-i]==pad:
                continue
            else:
                return(msg)
        return(bytearray(msg[0:len(msg)-pad]))

    def word_keys(self, words):#returns the concatenation of array words
        return bytearray(words[0]+words[1]+words[2]+words[3])
    
    
    def cipher(self, plaintext): #returns the result of the AES encryption algorithms rounds on one block of the full message using the mutation functions
        msg=self.add_round_key(plaintext, self.round_keys[0]) #initial whitening
        for i in range(1, self.num_rounds): #13 rounds
            msg=self.sub_bytes(msg)
            msg=self.shift_rows(msg)
            msg=self.mix_cols(msg)
            msg=self.add_round_key(msg,self.round_keys[i])
        #final round, no mix_col
        msg=self.sub_bytes(msg)
        msg=self.shift_rows(msg)
        msg=self.add_round_key(msg,self.round_keys[-1])
        return(msg)
    def inv_cipher(self, ciphertext):
        msg=self.add_round_key(ciphertext, self.round_keys[-1]) #initial reverse whitening
        for i in range(self.num_rounds-1, 0, -1): #13 rounds
            msg=self.inv_shift_rows(msg)
            msg=self.inv_sub_bytes(msg)
            msg=self.add_round_key(msg, self.round_keys[i])
            msg=self.inv_mix_cols(msg)
        #final round, no inv_mix_col
        msg=self.inv_shift_rows(msg)
        msg=self.inv_sub_bytes(msg)
        msg=self.add_round_key(msg,self.round_keys[0])
        return(msg)

    #returns the result of inv_cipher on all blocks of msg
    def decrypt(self, msg):
        output=bytearray()
        for i in range(0,int(len(msg)/16)):      
            output+=self.inv_cipher(msg[16*i:16*i+16])
        output=self.un_pad(output)
        return output#.decode('utf-8')

    #returns the result of encrypt on all blocks of msg. if string is True, encrypt expects a string, and if false it expects bytes.
    def encrypt(self, msg, string=True):
        if string:
            msg_bytes=bytearray(msg, 'utf-8')
        else:
            msg_bytes=bytearray(msg)
        msg_bytes=self.pad(msg_bytes)
        output=bytearray()
        for i in range(0,int(len(msg_bytes)/16)):      
            output+=self.cipher(msg_bytes[16*i:16*i+16])
        return output

if __name__=="__main__":
    key="Vrz19NDnmgmqvJw0fm4R3Zadi7OLLVoA"
    msg="hello how's it going"
    aes=AES(key)
    output=aes.encrypt(msg)
    print(output)
    print(aes.decrypt(output))