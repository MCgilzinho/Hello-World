# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.



fname = input("Enter file name: ")  #solicita entrada
fh = open(fname)                    #abre arquivo
lista=list()                        #cria lista

#encontra o números solicitados no enúnciado
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") : #examina se a linha possui a string
        b=line.find(':')            #encontra ':'
        a=line[b+1:] 	            #constroi string         
        lista.append(float(a))      #adiciona 'a' na lista e transforma em float

w=len(lista)                        #quantidade de elemntos na lista

#efetua a conta da média 
total=0
for index in lista:
    total=total+index
    
media=float(total/w)
print('Average spam confidence:',media)

