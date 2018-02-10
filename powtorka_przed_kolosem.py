# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 15:33:15 2017

@author: maciej
"""
####################LABY NR 1 ##########################33
#a=int(input("Podaj dlugosc podstawy"))
#h=int(input("Podaj wysokosc trojkata"))
#print(a*h/2)
#------------------------------
#    a=int(input("Podaj dlugosc pierwszego boku"))
#    b=int(input("Podaj dlugosc drugiego boku"))
#    c=int(input("Podaj dlugosc trzeciego boku"))
#    p=0.5 *(a+b+c)
#    S=(p*(p-a)*(p-b)*(p-c))**(1/2)
#    print(S)
#----------------------------------------------
#import random
#n=random.randint(0,9)
#while True:
#    a=int(input("Zgadnij liczbe od 0-9  "))
#    if a==n:
#        print("Wygrałeś")
#        break
#    elif a>n:
#        print("Za duzo")
#    elif a<n:
#        print("Za malo")
#    else:
#        print("Dziwna liczba")
#n=int(input("Podaj wysokosc choinki >=2    "))
#if n>=2:
#    for i in range(1,n):
#        for j in range(i+1):
#            for k in range(j+1):
#                print("X",end="")
#            print("")
#----------------------------------------------
#n=int(input("Podaj liczbe wieksza od 1 "))
#if n>=1:
#    for i in range(1,n+1):
#        for j in range(i+1):
#            for k in range(n-j):
#                print(" ",end="")
#            for k in range(2*j+1):
#                print("X",end="")
#            print("")
#------------------LABORATORIUM NR 2 ----------------------------------------
#while True:
#    print("1.Dodawanie")
#    print("2.Odejmowanie")
#    print("3.Mnożenie")
#    print("4.Dzielenie")
#    print("5.Potęgowanie")
#    print("6.Wyjscie")
#    a=int(input("""Podaj ktore dzialanie chcesz wykonac
#    """))
#    if a==6:
#        break
#    b=int(input("Podaj liczbe 1   "))
#    c=int(input("Podaj liczbe 2   "))
#    if a==1:
#        print(c+b)
#    elif a==2:
#        print(b-c)
#    elif a==3:
#        print(b*c)
#    elif a==4:
#        if c==0:
#            print("Nie wolno dzielic przez zero!")
#        else:
#            print(b/c)
#    elif a==5:
#        print(b**c)
#    else:
#        print("Nie ma takiej opcji w menu")
#------------------------------------------------------
#n=int(input("Podaj liczbe w systemie dwojkowych"))
#a=n
#y=0
#wynik=0
#while a>0:
#    tmp=a%10
#    a=a//10
#    if tmp !=0 and tmp!=1 :
#        y=1
#if y==0:
#    i=0
#    while n>0:
#        wynik = wynik + (n%10)*(2**(i))
#        n=n//10
#        i+=1
#    print(wynik)
#else:
#    print("To nie jest liczba w systemie dwojkowym")
#----------------------------------------------------
#dec=int(input("Podaj liczbe dziesietna  "))
#sys=int(input("Podaj na jaki system chcesz zamienić liczbe "))
#numbers="0123456789"
#alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#tab=[]
#while dec > 0:
#    tmp = dec % sys
#    for i in range(len(numbers)):
#        if tmp==i:
#            tab.append(numbers[i])
#            break
#    for i in range(len(alpha)):
#        if tmp==10+i:
#            tab.append(alpha[i])
#            break
#    dec=dec//sys
#i=len(tab)-1
#while i>=0:
#    print(tab[i],end="")
#    i-=1
#---------------------------------------------------------------
#num_1=str(input("Podaj liczbe "))    
#sys_1=int(input("W jakim systemie podałeś liczbe? "))
#sys_2=int(input("Na jaki system ja przekonwertować ? "))
#numbers="0123456789"
#alpha="ABCDEFGHIJKLMNOPQRUSTYVWXYZ"
#result=[]
#for i in range(len(num_1)):
#    y=0
#    if sys_1<=9:
#        for j in range(sys_1):
#            if num_1[i]==numbers[j]:
#                y=1
#                break
#    else:
#        for j in range(9):
#            if num_1[i]==numbers[j]:
#                y=1
#                break
#        for j in range(sys_1-9):
#            if num_1[i]==alpha[j]:
#                y=1
#                break
#    if y==0:
#        print("Podales liczbe nie do zadeklarowanego systemu , lub za duzego zakresu :)))")
#        break
#wynik=0
#for i in range(len(num_1)):
#    for j in range(sys_1):
#        if j<=9:
#            if num_1[len(num_1)-i-1]==numbers[j]:
#                wynik=wynik + j*((sys_1)**(i))
#        if j>=10:
#            if num_1[len(num_1)-i-1]==alpha[j-10]:
#                wynik=wynik+ (j)*(sys_1**(i))
#print(wynik)
#while wynik>0:
#    tmp=wynik%sys_2
#    wynik=wynik//sys_2
#    for i in range(10):
#        if tmp==i:
#            result.append(numbers[i])
#    for i in range(10,10+len(alpha)):
#        if tmp==i:
#            result.append(alpha[i-10])
#for i in range(len(result)):
#    print(result[len(result)-i-1],end="")
#---------------------------LABORATORIUM NR 3-----------------------
#import random
#import time
#n=20
#tab=[]
#for i in range(n):
#    tab.append(0)
#
#for i in range(20):
#    while True:
#        x=random.randrange(n)
#        if tab[x]!=1:
#            print(x*"-",end="")
#            print("x",end="")
#            print((n-x-1)*"-")
#            time.sleep(0.3)
#            tab[x]=1
#            break
#    if i%n==0:
#        for j in range(n):
#            tab[j]=0
#-------------------------------------------------------------------
#import time
#n=int(input("Podaj dlugosc animowanego kwadratu " ))
#if n%2==1:
#    while True:
#        for i in range(n//2+1):
#            for j in range(n+1):
#                if j==n//2+1-i or j==n//2+1+i:
#                    print((n//2-i)*"-",end="")
#                    print((2*i+1)*"X",end="")
#                    print((n//2-i)*"-")
#                elif j>n//2+1-i and j<n//2+1+i:
#                    print((n//2-i)*"-",end="")
#                    print("X",end="")
#                    print((2*i-1)*"-",end="")
#                    print("X",end="")
#                    print((n//2-i)*"-")
#                else:
#                    print(n*"-")
#            time.sleep(0.3)
#        k=n//2-1
#        while(k>=0):
#            for j in range(n):
#                 if j==n//2+1-k or j==n//2+1+k:
#                    print((n//2-k)*"-",end="")
#                    print((2*k+1)*"X",end="")
#                    print((n//2-k)*"-")
#                 elif j>n//2+1-k and j<n//2+1+k:
#                    print((n//2-k)*"-",end="")
#                    print("X",end="")
#                    print((2*k-1)*"-",end="")
#                    print("X",end="")
#                    print((n//2-k)*"-")
#                 else:
#                    print(n*"-")
#            k-=1      
#            time.sleep(0.3)
#        break    jezeli chcesz w nsk to usun breaka :)
#else:
#    print("Dlugosc kwadratu musi byc nieparysta")
#-----------------------------LABORATORIUM NR 4------------------
#n=int(input("Podaj liczbe z silni jaka chcesz obliczyć " ))
#def silnia__iter(n):
#    result=1
#    for i in range(1,n+1):
#        result=result*i
#    return result
#def silnia__reku(n):
#    if n==1:
#        return 1
#    else:
#        return silnia__reku(n-1)*n
#res_1=silnia__iter(n)
#res_2=silnia__reku(n)
#print(res_1)
#print(res_2)
#-----------------------------------------------------------------
#n=int(input("Podaj liczbe "))
#def fibo__iter(n):
#    tab=[1,1]
#    if n==1:
#        return 1
#    elif n==2:
#        return 1
#    else:
#        for j in range(2,n):
#            tab.append(tab[j-1]+tab[j-2])
#        return tab[n-1]
#def fibo__reku(n):
#    if n==1:
#        return 1
#    elif n==2:
#        return 1
#    else:
#        return fibo__reku(n-2)+fibo__reku(n-1)
#res_1=fibo__iter(n)
#res_2=fibo__reku(n)
#print(res_1)
#print(res_2)
#----------------------------------------------------------------
#n=int(input("Podaj wysokosc trojkata pascala " ))
#def Pascal_Triangle(row,position):
#    if position==1 or position==row:
#        return 1
#    if row==1:
#        return 1
#    else:
#        return Pascal_Triangle(row-1,position) + Pascal_Triangle(row-1,position-1)
#print((n-2)*" ","1")
#for i in range(2,n+1):
#    print((n-i)*" ",end="")
#    for j in range(1,i+1):
#        print(Pascal_Triangle(i,j),end=" ")
#    print("")
#-------------------------LABORATORIUM NR 5------------------------
#n=1000000
#tab=[]
#for i in range(n):
#    tab.append(1)
#def pierwiastek(n):
#    a=1
#    while a*a<n:
#        a+=1
#    return a
#def Sito_Erastotenesa(tab,n):
#    for i in range(2,pierwiastek(n)):
#        if tab[i]==0:
#            continue
#        else:
#            tmp=2
#            result=tmp*i
#            while result<n:
#                tab[result]=0
#                tmp+=1
#                result=tmp*i
#Sito_Erastotenesa(tab,n)
#for i in range(2,n):
#    if tab[i]==1:
#        print(i)
#---------------------LABORATORIUM NR 6-------------------------------
#shift=5
#code=str(input("Podaj wiadomosc do zaszyfrowania" ))
#tab=[]
#def Cezar(code,shift):
#    for i in range(len(code)):
#        tmp=ord(code[i])
#        if tmp==32:
#            tab.append(chr(tmp))
#        elif tmp+shift <=122:
#            tab.append(chr(tmp+shift))
#        else:
#            tmp_2=tmp+shift - 122
#            tab.append(chr(97 + tmp_2))
#Cezar(code,shift)
#print(code)
#print(tab)
#def Brutus(tab,shift):
#    for i in range(len(code)):
#        tmp=ord(tab[i])
#        if tmp==32:
#            tab[i]=(chr(tmp))
#        elif tmp-shift >=97:
#            tab[i]=chr(tmp-shift)
#        else:
#            tmp_2=97-(tmp-shift)
#            tab[i]=chr(122 - tmp_2)
#Brutus(tab,shift)
#print(tab)   
#--------------------------------------------------------------------
#alpha="abcdefghijklmnopqrstuvwxyz"
#cihper="zkjhfdpqoiwlvxybcmaegnrstu"
#string=str(input("Podaj wiadomosc do zaszyfrowania"))
#tab=[]
#for i in range(len(string)):
#    tab.append(string[i])
#    
#def Coding(cipher,tab):
#    for i in range(len(tab)):
#        for j in range(len(cipher)):
#            if ord(tab[i])==j+97:
#                tab[i]=cipher[j]
#                break
#print(tab)
#Coding(cihper,tab)
#print(tab)
#def deCoding(cipher,tab):
#    for i in range(len(tab)):
#        for j in range(len(cihper)):
#            if  tab[i]==cipher[j]:
#                tab[i]=chr(97+j)
#                break
#deCoding(cihper,tab)
#print(tab)
#---------------------------------------------------------------
#import random
#string=str(input("Podaj wiadomosc do zaszyfrowania "))
#tab=[]
#klucz=[]
#for i in range(len(string)):
#    klucz.append(random.randint(1,25))
#    tab.append(string[i])
#
#def Klucz(klucz,tab):
#    for i in range(len(tab)):
#        if ord(tab[i])==32:
#            continue
#        elif ord(tab[i])+klucz[i]>=122:
#            tmp_2=ord(tab[i])+klucz[i]-122
#            tab[i]=chr(97+tmp_2)
#        else:
#            tab[i]=chr(ord(tab[i])+klucz[i])
#print(tab)
#Klucz(klucz,tab)
#print(tab)
#def deKlucz(klucz,tab):
#    for i in range(len(tab)):
#        if ord(tab[i])==32:
 #           continue
#        elif ord(tab[i])-klucz[i]<97:
#            tmp_2=97-ord(tab[i])+klucz[i]
#           tab[i]=chr(122-tmp_2)
#        else:
#            tab[i]=chr(ord(tab[i])-klucz[i])
#deKlucz(klucz,tab)
#print(tab)           
#--------------------LABORATORIUM NR 7--------------------------
#import random
#n = 100
#b = 10
#numbers = []
#tab = []

#def Sito(numbers,b):
#    for i in range(2,pierwiastek(b)):
#        if numbers[i] != 1:
#            k = i
#            result = 1
#            while result < b:
#                numbers[result] = 1
#                result = i * k
#                k = k + 1
#def pierwiastek(n):
#    a=1
#    while a*a < n:
#        a += 1
#    return a
#
#for i in range(n):
#    tab.append(random.randint(1,b))
#
#for i in range(b):
#    numbers.append(i)
#
#Sito(numbers,b)
#print(tab)
#for i in range(2,len(numbers)):
#    tmp = 0
#    if numbers[i] != 1:
#        for j in range(n):
#            if tab[j] == numbers[i]:
#                tmp += 1
#        if tmp%2==0:
#            for j in range(n):
#                if tab[j]==numbers[i]:
#                    tab[j] = -1

#print(tab)
#for i in range(n):
#    if tab[i] != -1:
#        print(tab[i],end=" ")       
#------------------------------------------------------------
money = [1, 5 ,8 , 9, 10, 16, 17, 20, 24, 26]
length = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
efficient=[]

rank=[]

def most_efficient(money,length):
    for i in range(len(length)):
        efficient.append(money/length)
        
def sort(efficient):
    max_val=length[0]
    for i in range(len(efficient)-1):
        if efficient[i+1] > efficient[i]:
            max_val=length[i+1]
    rank.append(max_val)





























        
        
            
            
        
    
        



































