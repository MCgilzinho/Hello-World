'''
ENUNCIADO
Open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the split() method.
The program should build a list of words.
For each word on each line check to see if the word is
already in the list and if not append it to the list.
When the program completes, sort and print the resulting words in
alphabetical order.
'''

fname = input("Enter file name: ")
fh = open(fname)
PrimeiraLista = list()
SegundaLista = list()

'''cria a PrimeiraLista com as posições em formato listas de strings'''
'''exemplo de saída: [['bla','bla','bla'],['ok','ok']]'''
for line in fh:
    PrimeiraLista.append(line.split())

'''ajusta a PrimeiraLista em uma única lista'''
'''exemplo de saída: ['bla','bla','bla','ok','ok']'''
for l in PrimeiraLista:
    for i in l:
        SegundaLista.append(i)

'''procura item repetido e o elimina'''
i=0
while i < len(SegundaLista):
    j=i+1
    while j < len(SegundaLista):
        if SegundaLista[i]==SegundaLista[j]:
            SegundaLista.pop(j)
        else :
            j+=1

    i+=1

'''coloca a SegundaLista em ordem alfabetica'''
SegundaLista.sort()  
       
'''resposta desejada'''
print(SegundaLista)
fh.close()

