print("Hello 10E! (World)!")
#end: a sor végi karakter, alapértelmezetten SorvégeKocsivissza (Enter)\n
print("Szia Én!", end=" *** ")
print("Programozni királyságos", end=" *** ") 
print("Üdv a programomban!")
print()
#NAGYON SZÉPEN MEGÍRT ÜZENET XD
#
"""
Comment XD
Comment XD
print() \"""
"""

print("Tej", "Sör", "Kakaó", "Kenyér", "Macisajt", "Koffeinmentes KV", sep="\t")

print("Tej", "Sör", "Kakaó", "Kenyér", "Macisajt", "Koffeinmentes KV", sep="; ")
#szintaktikai hiba a nyelvhelyességére vonatkozó hiba
#szemantikai hiba amikor logikai hibát vétünk és nem azt csinálja a program amit akarunk

#1.
print("Hello World")

#2.

print("Kedves Tamás")
print("    Isten hozott a Python világában!")
print("        Üdv: a program")

print("Kedves Tamás!", "\n", "Isten hozott a Python világában!", "\n \t", "Üdv: a program", sep="\t")

#3
print('"Ha meg tudod álmodni, meg is tudod tenni!"', end=" ")
print("Walt Disney")

print('"Ha meg tudod álmodni, meg is tudod tenni!"', end="-")
print("Walt Disney")

print('"Walt Disney"', end=": \t")
print("Ha meg tudod álmodni, meg is tudod tenni!")

#4.

print("tej", "kenyér", "vaj", "sajt", sep=",")
print("tej", "kenyér", "vaj", "sajt", sep="\t")
print("tej", "kenyér", "vaj", "sajt", sep="***")

#5.

print(""" "A 'white space' vagy 'whitespace' angol szóösszetétel, jelentése fehér tér , \n \n Az informatikában, elsősorban a \n \t programozásban és \n \t szövegszerkesztésben \n használatos kifejezés. \n \n alapvetően azokat a karaktereket értjük alatta, amelyek nem láthatóak a szövegben, \n viszont valamilyen egyedi funkcióval bírnak." """ "\n",  """A Wikipédiából, (a szabad encyklopédia) """, sep="--",)
# A közelébe se menjek rá se nézzek mert működik!!!!!!! 

#6 Tudom, hogy nem kell de unatkozom lol

nev = "Tamás"
eletkor = 16
magassag = 1.69 #nem tudom pontos-e
print("A nevem:", nev, "Az életkorom:", eletkor, "A magasságom:", magassag,"m",)

#7 dsnssdfkjnfdfhfgddf

nev_leng = len(nev)
#print(nev_leng) debug lol

print((2+nev_leng)*"*", "\n", "*", nev, "*", "\n", (2+nev_leng)*"*", sep="")

#8

a = 5
b = 10

print(f"a={a}", f"b={b}", sep=", ")
print(f"a={a*2}", f"b={b*2}", sep=", ")
print(f"a={a*2}", f"b={b*2}", sep=", ")
print(f"a={a+1}", f"b={b-1}", sep=", ")
a = 69
osszeg = 0
osszeg = a+b
print(f"a={a+1}", f"b={b-1}", f"összeg={osszeg}", sep=", ")


#9 fdnndfjndgfjdfg

a = 1
b= 7
c= -3

print(f"#(a-b)/c=({a}-{b})/{c}=", (a-b)/c)
print(f"#(a+b)*(2a-c)=({a}+{b})*({2*a}-({c}))=", (a+b)*(2*a-c))
print(f"#(3a-3b)/c=({3*a}-{3*b})/{c}=", (3*a-3*b)/c)
print(f"#2ac+4b={2*a*c}+{4*b}=", 2*a*c+4*b)

#10