from io import open
'''
fichero=open('fichero.txt','r')
texto1=fichero.read()
print(texto1)
#fichero.seek(0)
print(texto1)
fichero.close()

fichero=open('fichero.txt','r')
texto1=fichero.readlines()
print(texto1)
print(type(texto1))
fichero.close()
for i in texto1:
    print(i)
'''

fichero=open('fichero.txt','r')
texto1=fichero.readline()
print(texto1)
print(type(texto1))
fichero.close()
for i in texto1:
    print(i)