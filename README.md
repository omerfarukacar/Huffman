# TICARET UNIVERSITESI

AÇIKLAMA

Huffman
 Huffman kodlamasý veri sýkýþtýrmak için kullanýlan yöntemlerden biridir.
 Temel amaç veriyi kayýpsýz olarak sýkýþtýrýp geri açmaktýr.
 En büyük avantajý en sýk kullanýlan karakterlerin frekansýna göre sýralama yapýlýp, 
en az alaný en sýk kullanýlan karaktere ayýrmasýdýr.

Huffman Çözücü
 Mevcut bitlere karþýlýk gelen karakterleri bulmak amacý ile kullanýlýr.
 
Entropi
 Olabilecek en yüksek sýkýþtýrma oranýný belirtir.

Ortalama Sözlük Uzunluðu
 Oluþturulan sözlüðün kelimelerinin ortalama uzunluðunu belirtir.

Sýkýþtýrma Oraný
 Huffman kodlama yaptýktan sonra oluþan sözlüðün sýkýþtýrma oranýný belirtir.

GEREKLÝLÝKLER
Python 3.9
math kütüphanesi 

ÖRNEK
--------------------------------------------------
Enter message : HUFFMANTESTCODE
Enter to encode binary :101110101010111010101
--------------------------------------------------
Decoded String =  10111010101011101010
Decoded Letters =  TMETME
--------------------------------------------------
Index =  1
Symbol =  F
Frequence =  2
Code =  100
Code Lenght =  3
--------------------------------------------------
Index =  2
Symbol =  T
Frequence =  2
Code =  101
Code Lenght =  3
--------------------------------------------------
Index =  3
Symbol =  E
Frequence =  2
Code =  010
Code Lenght =  3
--------------------------------------------------
Index =  4
Symbol =  H
Frequence =  1
Code =  111
Code Lenght =  3
--------------------------------------------------
Index =  5
Symbol =  U
Frequence =  1
Code =  1100
Code Lenght =  4
--------------------------------------------------
Index =  6
Symbol =  M
Frequence =  1
Code =  1101
Code Lenght =  4
--------------------------------------------------
Index =  7
Symbol =  A
Frequence =  1
Code =  0010
Code Lenght =  4
--------------------------------------------------
Index =  8
Symbol =  N
Frequence =  1
Code =  0011
Code Lenght =  4
--------------------------------------------------
Index =  9
Symbol =  S
Frequence =  1
Code =  0000
Code Lenght =  4
--------------------------------------------------
Index =  10
Symbol =  C
Frequence =  1
Code =  0001
Code Lenght =  4
--------------------------------------------------
Index =  11
Symbol =  O
Frequence =  1
Code =  0110
Code Lenght =  4
--------------------------------------------------
Index =  12
Symbol =  D
Frequence =  1
Code =  0111
Code Lenght =  4
--------------------------------------------------
Average Dictionary Length =  3.533333333333333
Compression Ratio =  0.1166666666666667
Entropy =  3.5068905956085183
--------------------------------------------------

License and Citation
The software is licensed under the MIT License.


