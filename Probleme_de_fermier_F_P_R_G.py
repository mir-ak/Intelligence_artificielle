from random import randrange  
initial=[0,0,0,0]
buts=[[1,1,1,1]]
trace=False

interdits=[[F,P,R,G] for F in [0,1] for P in [0,1] for R in [0,1]
               for G in [0,1] if P!=F and (P==G or R==P)]

if trace:
    print('interdits :', interdits)

def successeurs(etat):
    fermier=etat[0]
    destination=1-fermier
    fermier_seul=etat.copy()
    fermier_seul[0]=destination
    candidats=[fermier_seul]
    for indice in range(1,len(etat)):
        if etat[indice]==fermier:
            candidat=etat.copy()
            candidat[0]=destination
            candidat[indice]=destination
            candidats.append(candidat)
    if trace:
        print('successeurs de', etat, ':', [candidat for candidat in candidats if candidat not in interdits])
    return [candidat for candidat in candidats if candidat not in interdits]


successeurs([1,1,1,0])
def Aleatoir():
	e0 = initial 
	B = buts 
	E = [initial]
	P = [initial]
	e = e0
	while( e not in B ):
		s = [e1 for e1 in successeurs(e) if e1  not in E]
		if len(s) == 0:
			if len(P) == 0:
				return 0
			else:
				e = P.pop()
		else: 
				e1 = s[randrange(len(s))]
				P.append(e1)
				e = e1 
		if not e in E:
			E.append(e)
		
	return P
print("F,P,R,G")
print("solution en Aleatoir")
[print(l) for l in Aleatoir()]
def profondeur(G,e):
	G.append(e)
	if e in buts:
		return G
	for e1 in successeurs(e):
		if not e1 in G:
			return profondeur(G,e1)

print("solution en Profondeur")
[print(l) for l in profondeur([] , initial)]

def largeur(G,e):
	F = []
	F.append(e)
	while(len(F)): 
		x = F[0]
		F.remove(x)
		a = successeurs(x)
		while (len(a)):
			y = a[0]
			a.remove(y)
			if not y in G : 
				G.append(y)
				F.append(y)
	return G
print("solution en largeur")
[print(l) for l in largeur([] , initial)]	

class Etat:
    def __init__(self, liste, h, nbr_coup, verfier):
        self.h = h
        self.nbr_coup = nbr_coup
        self.f = h+nbr_coup
        self.verfier = verfier
        self.liste = liste


def h(e):
	return 4-sum(e)

def petit_cout(f):
	indix = 0 

	for i in range (len(f)):
		if (f[indix].f > f[i].f):
			indix = i 
	return indix 
	
def A_etoil():
	e0 = Etat(initial,h(initial),0,None)
	F = []
	v = []
	F.append(e0)
	e = e0
	while(e.h > 0 and len(F)):
		e = F[petit_cout(F)]
		F.remove(e)
		v.append(e)
		for s in successeurs(e.liste):
			F.append(Etat(s,h(s),e.nbr_coup+1,e))
	if (e.h == 0 ):
		l =[]
		while(e.verfier != None):
			l.insert(0,e.liste)
			e = e.verfier
		l.insert(0,e.liste)
		return l 
	else :
		return [] 
print("solution en A*")
print(A_etoil())
		
		
	
	
	
