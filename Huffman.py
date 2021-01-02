import math
print("-" * 50)
string = input("Enter message : ") #Kullanıcıdan alınan harfler bütünü ("TESTTEST")
encodeString = input("Enter to encode binary :") #Çözülmesi istenen binary kod ("110011011010")


class myDict(dict): # Yeni sözlük sınıfı oluşturuldu

    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

class NodeTree(object): # Ağaç düğümleri sınıfı oluşturuldu

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)

def huffman_code_tree(node, left=True, binString=''): # Ana kodun Huffman kodlamasına uyarlanması
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    dictionary = dict()

    dictionary.update(huffman_code_tree(l, True, binString + '1')) # Ağaç sola 0 / sağa 1 seklinde düzenlendi
    dictionary.update(huffman_code_tree(r, False, binString + '0'))
    return dictionary

freq = {}
for c in string: # Frekans hesaplaması
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True) # Frekansların sıralaması
nodes = freq

while len(nodes) > 1:  # Ağaç düğümleri ???
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])
huffmanDict = myDict()

for (char, frequency) in freq:
    huffmanDict.add(char, huffmanCode[char])

tmp = ''
decodeString = ''
decodeStringHarfli = ''

for i in encodeString:
    tmp += i
    for key, value in huffmanDict.items():
        if value == tmp:
            decodeString += tmp
            decodeStringHarfli += key
            tmp = ''
# Değişkenler oluşturuldu
first = 0
second = 0
halfAverage = 0
entropiHuffman = 0
everyHuffmanCode = []
totalAverageHuffman = 0
totalFreqHuffmanCode = 0
totalCompressingValue = 0
totalEntropiHuffman = 0.0
totalAverageHuffmanNextValue = 0

print("-" * 50)
print("Decoded String = ", decodeString)
print("Decoded Letters = ", decodeStringHarfli)
print("-" * 50)

for first in range(len(freq)):

    print("Index = ", str(first+1))
    print("Symbol = ", str(freq[first][0]))
    print("Frequence = ", str(freq[first][1]))
    print("Code = ", huffmanCode[str(freq[first][0])])
    print("Code Lenght = ", str(len(huffmanCode[str(freq[first][0])])))
    print("-" * 50)

    lenHuffmanCode = len(huffmanCode[str(freq[first][0])]) #Ortalama Sozluk Uzunlugu ilk kismi
    freqHuffmanCode = freq[first][1]
    totalFreqHuffmanCode += freqHuffmanCode
    halfAverage += lenHuffmanCode * freqHuffmanCode
    everyHuffmanCode.append(freqHuffmanCode)


for second in range(len(everyHuffmanCode)): #Entropi
    entropiHuffman = -((everyHuffmanCode[second]/totalFreqHuffmanCode)*(math.log2(everyHuffmanCode[second]/totalFreqHuffmanCode)))
    totalEntropiHuffman += entropiHuffman

AverageHuffman = (halfAverage / totalFreqHuffmanCode) #Ortalama Sozluk Uzunlugu Bulma
totalAverageHuffman += AverageHuffman
totalAverageHuffmanNextValue = (totalAverageHuffman +1) -( (totalAverageHuffman) % 1)
totalCompressingValue = 1 -(totalAverageHuffman / totalAverageHuffmanNextValue)

#Average Dictionary Length  = lenght1 * (freq1 /total freq) * n2 *n3
#sıkıstırma oranı = 1 - (ort sozluk uzunlugu / en anlamlı bit)
#en anlamlı bit = (ort sozluk uzunlugu + 1 ) - (ort sozluk uzunlugu  ) % 1
print('Average Dictionary Length = ', str(totalAverageHuffman))

#-[(freq / total freq )* log2(freq / total freq)+ n2 + n3 ]
print('Compression Ratio = ', str(totalCompressingValue))
print('Entropy = ', str(totalEntropiHuffman))

