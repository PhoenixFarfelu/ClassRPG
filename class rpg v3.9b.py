from random import randint
import tkinter as tk
from time import sleep

evo = 0.25
class perso:
    #stat de base
    def __init__(self):
        self.arg = 1500
        self.xpmax = 200
        self.xp = 0
        self.lvl = 1
        self.age = 20
        self.hp = 100
        self.pos = 0
        self.inv = {
    'armure':[
        {'type':'armure','nom':'tunique en cuire','rareté':'commun','stat':[0,0,10,0,0,0],'prix':100}],
    'bouclier':[
        {'type':'bouclier','nom':'marmite','rareté':'commun','stat':[0,0,5,0,0,0],'prix':50}],
    'arme':[
        {'type':'arme','nom':'gourdin','rareté':'commun','stat':[0,10,0,0,0,0],'prix':100}],
    'anneau':[
        {'type':'anneau','nom':'anneau rouillé','rareté':'commun','stat':[10,10,0,0,0,0],'prix':200}]
    }
        self.inv_2 = {
    'armure':[
        {'type':'armure','nom':'tunique en cuire','rareté':'commun','stat':[0,0,10,0,0,0],'prix':100},
        {'type':'armure','nom':'tunique légère','rareté':'peu commun','stat':[0,0,10,0,5,0],'prix':125}],
    'bouclier':[
        {'type':'bouclier','nom':'marmite','rareté':'commun','stat':[0,0,5,0,0,0],'prix':50}],
    'arme':[
        {'type':'arme','nom':'gourdin','rareté':'commun','stat':[0,10,0,0,0,0],'prix':100}],
    'anneau':[
        {'type':'anneau','nom':'anneau rouillé','rareté':'commun','stat':[10,10,0,0,0,0],'prix':200}]
    }
        self.hpmax_base = 100
        self.str_base = 15
        self.arm_base = 0
        self.stam_base = 100
        self.speed_base = 10
        self.int_base = 10

        self.hpmax = self.hpmax_base
        self.str = self.str_base
        self.arm = self.arm_base
        self.stam = self.stam_base
        self.speed = self.speed_base
        self.int = self.int_base
        pass

    #update les valeurs en fonction du stuff
    def update_val(self):
        self.hpmax = self.hpmax_base + get_item('armure',0) + get_item('bouclier',0) + get_item('arme',0) + get_item('anneau',0)
        self.str = self.str_base     + get_item('armure',1) + get_item('bouclier',1) + get_item('arme',1) + get_item('anneau',1)
        self.arm = self.arm_base     + get_item('armure',2) + get_item('bouclier',2) + get_item('arme',2) + get_item('anneau',2)
        self.stam = self.stam_base   + get_item('armure',3) + get_item('bouclier',3) + get_item('arme',3) + get_item('anneau',3)
        self.speed = self.speed_base + get_item('armure',4) + get_item('bouclier',4) + get_item('arme',4) + get_item('anneau',4)
        self.int = self.int_base     + get_item('armure',5) + get_item('bouclier',5) + get_item('arme',5) + get_item('anneau',5)

    #degat au joueur
    def degat(self,dps,battle):
        #degat réduit selon l'armure
        dps = dps - (self.arm/2)
        #esquive selon la vitesse
        a = randint(1,100)
        if a < self.speed:
            tk.Label(battle, text="     le monstre a esquivé     ").grid(column=4, row=2)
            battle.update()
            battle.update_idletasks()
        if a >= self.speed:
            self.hp -= dps
            if self.hp < 0:
                self.hp=0
            print('tu as perdu ',dps,'hp')
            print('hp actuel ',self.hp)
        pass

    #gain d'xp pour le joueur
    def gainxp(self,gain):
        self.xp += gain
        print('vous avez gagnez :',gain,'xp')
        pass

    #heal pour le joueur
    def heal(self,he,battle):
        self.hp += he
        #limite par l'hpmax du joueur
        if self.hp >= self.hpmax:
            self.hp = self.hpmax
        tk.Label(battle, text=f'Il vous reste maintenant {p1.hp} hp').grid(column=1, row=1)
        tk.Label(battle, text=f"     Vous buvez une potion     ").grid(column=1, row=2)
        battle.update()
        battle.update_idletasks()

    #augmentation des stats du joueur / monte de niveau
    def lvup(self):
        if p1.xp >= p1.xpmax :
            lvup = tk.Tk()
            lvup.title("Niveau Supérieur")
            lvup.grid()
            lvup.geometry('%dx%d+%d+%d' % (250, 350, 1075, 260))
            tk.Label(lvup, text=f"Vous êtes passé niveau : {p1.lvl+1}").grid(column=0, row=0)
            tk.Label(lvup, text=f"Argent : {p1.arg}").grid(column=0, row=1)
            tk.Label(lvup, text=f"Xp pour le prochain niveau :{p1.xpmax}+100").grid(column=0, row=2)
            tk.Label(lvup, text=f"hpmax : {p1.hpmax_base} +5").grid(column=0, row=6)
            tk.Label(lvup, text=f"Stamina : {p1.stam_base} +2").grid(column=0, row=8)
            tk.Label(lvup, text=f"Armure : {p1.arm_base} +1").grid(column=0, row=9)
            tk.Label(lvup, text=f"Vitesse : {p1.speed_base} +1").grid(column=0, row=10)
            tk.Label(lvup, text=f"Force : {p1.str_base} +1").grid(column=0, row=11)
            tk.Label(lvup, text=f"Intelligence : {p1.int_base} +1").grid(column=0, row=12)
            tk.Button(lvup, text="Ok", command=lvup.destroy).grid(column=0, row=14)
            #lvup.mainloop()
            self.xp -= self.xpmax
            self.xpmax += 100
            self.lvl += 1
            self.age = 20
            self.hpmax += 5
            self.hp = self.hpmax
            self.stam += 2
            self.arm += 1
            self.speed += 1
            self.str += 1
            self.int += 1
        else:
            pass


    #fait vieillir le joueur
    def vieillir(self,val):
        self.age += val
        pass

    #useless
    def nommer(self, nom):
        self.nom = nom

#creer le perso
p1 = perso()

#creer le monstre de base
class monstre:

    #stat de base du monstre évoluant selon la case actuelle
    def __init__(self):
        self.hpmax = 100 + (p1.pos*randint(1,3))
        self.hp = 100 + (p1.pos*randint(1,3))
        self.stam = 100 + (p1.pos)
        self.arm = int(10 + (p1.pos/2))
        self.speed = int(8 + (p1.pos/2))
        self.str = int(10 + (p1.pos/2))
        self.int = int(10 + (p1.pos/2))
        pass

    #degat sur le monstre
    def degat(self,dps,battle):
        #reduction des degats selon l'armure
        dps = dps - (self.arm/2)
        #esquive selon la vitesse du monstre
        a = randint(1,100)
        if a < self.speed:
            tk.Label(battle, text=f"                    le monstre a esquivé                    ").grid(column=4, row=2)
            battle.update()
            battle.update_idletasks()

        if a >= self.speed:
            self.hp -= dps
            if self.hp < 0:
                self.hp=0
            tk.Label(battle, text=f"     hp actuel du monstre : {self.hp}     ").grid(column=4, row=1)
            tk.Label(battle, text=f"                le monstre a perdu {dps} hp               ").grid(column=4, row=2)
            battle.update()
            battle.update_idletasks()
        pass

    #heal du monstre
    def heal(self,he,battle):
        self.hp += he

        #limitation par l'hpmax
        if self.hp >= self.hpmax:
            self.hp = self.hpmax
        tk.Label(battle, text=f"     hp actuel du monstre : {self.hp}     ").grid(column=4, row=1)
        tk.Label(battle, text=f"                    le monstre se soigne                    ").grid(column=4, row=2)
        battle.update()
        battle.update_idletasks()


#Si on veut mettre en % c'est (p1.nom*x) | donc (p1.arm*0.1)
#ordre pour les valeurs :
#0. hpmax p1.hpmax_base
#1. str p1.str_base
#2. arm p1.arm_base
#3. stam p1.stam_base
#4. speed p1.speed_base
#5. int p1.int_base    
inventaire = {
    'armure':[
        {'type':'armure','nom':'tunique en cuire','rareté':'commun','stat':[0,0,10,0,0,0],'prix':100},
        {'type':'armure','nom':'tunique légère','rareté':'peu commun','stat':[0,0,10,0,5,0],'prix':125}],
    'bouclier':[
        {'type':'bouclier','nom':'marmite','rareté':'commun','stat':[0,0,5,0,0,0],'prix':50},
        {'type':'bouclier','nom':'bouclier en bois','rareté':'peu commun','stat':[0,0,10,0,0,0],'prix':100}],
    'arme':[
        {'type':'arme','nom':'gourdin','rareté':'commun','stat':[0,10,0,0,0,0],'prix':100},
        {'type':'arme','nom':'épée en bois','rareté':'peu commun','stat':[0,15,0,0,0,0],'prix':150}],
    'anneau':[
        {'type':'anneau','nom':'anneau rouillé','rareté':'commun','stat':[10,10,0,0,0,0],'prix':200},
        {'type':'anneau','nom':'anneau de legende','rareté':'épique','stat':[(p1.hpmax_base*0.1),(p1.str_base*0.1),(p1.arm_base*0.1),(p1.stam_base*0.1),(p1.speed_base*0.1),(p1.int_base*0.1)],'prix':1500}],
    }

def get_item(nom,n):
    if len(p1.inv[nom]) > 0:
        valeur = p1.inv[nom][0]['stat'][n]
        return valeur
    else:
        return 0

def equipe_item_achat(item):
    #p1.inv_2[item['type']].append(p1.inv[item['type']])
    p1.inv[item['type']].insert(0,item)
    p1.update_val()

def equipe_item_inv(nom,n,main_inv):
    p1.inv[nom].insert(0,p1.inv_2[nom][n])
    update_inv_aff(main_inv)

def vente_item(nom,n,main_vente):
    p1.arg += int((p1.inv_2[nom][n]['prix'])/2)
    if p1.inv_2[nom][n] == p1.inv[nom][0]:
        p1.inv[nom].pop(0)
    p1.inv_2[nom].pop(n)
    update_vente_aff(main_vente)

def selec_al():
    v_al = randint(1,4)
    if v_al == 1:
        return selec_al_2('armure')
    if v_al == 2:
        return selec_al_2('bouclier')
    if v_al == 3:
        return selec_al_2('arme')
    if v_al == 4:
        return selec_al_2('anneau')
      
def selec_al_2(nom):
    global inventaire
    v_al_2 = randint(0,len(inventaire[nom])-1)
    return inventaire[nom][v_al_2]

def ajuste_item(item,v,prix):
    global evo
    l=[]
    item['nom'] += '+'+str(v)
    for i in item['stat']:
        l.append(int(i + (i*evo)*v))
    item['stat'] = l
    item['prix'] = prix
    return item

def update_inv_aff(main_inv):
    if len(p1.inv['armure']) > 0:
        tk.Label(main_inv, text=f"   Votre armure : {p1.inv['armure'][0]['nom']} {p1.inv['armure'][0]['stat']}          ").grid(column=1, row=1)
    else :
        tk.Label(main_inv, text=f"   Votre armure : Rien                                                                ").grid(column=1, row=1)
    if len(p1.inv['bouclier']) > 0:
        tk.Label(main_inv, text=f"   Votre bouclier : {p1.inv['bouclier'][0]['nom']} {p1.inv['bouclier'][0]['stat']}    ").grid(column=1, row=2)
    else :
        tk.Label(main_inv, text=f"   Votre bouclier : Rien                                                              ").grid(column=1, row=2)
    if len(p1.inv['arme']) > 0:
        tk.Label(main_inv, text=f"   Votre arme : {p1.inv['arme'][0]['nom']} {p1.inv['arme'][0]['stat']}                ").grid(column=1, row=3)
    else :
        tk.Label(main_inv, text=f"   Votre arme : Rien                                                                  ").grid(column=1, row=3)
    if len(p1.inv['anneau']) > 0:
        tk.Label(main_inv, text=f"   Votre anneau : {p1.inv['anneau'][0]['nom']} {p1.inv['anneau'][0]['stat']}          ").grid(column=1, row=4)
    else :
        tk.Label(main_inv, text=f"   Votre anneau : Rien                                                                ").grid(column=1, row=4)
    tk.Label(main_inv, text=f"Armures en stock :").grid(column=1, row=5)
    aff_inv_2(main_inv,'armure',1)
    tk.Label(main_inv, text=f"Boucliers en stock :").grid(column=2, row=5)
    aff_inv_2(main_inv,'bouclier',2)
    tk.Label(main_inv, text=f"Armes en stock :").grid(column=3, row=5)
    aff_inv_2(main_inv,'arme',3)
    tk.Label(main_inv, text=f"Anneaux en stock :").grid(column=4, row=5)
    aff_inv_2(main_inv,'anneau',4)
    main_inv.update()
    main_inv.update_idletasks()
    p1.update_val()

def update_vente_aff(main_vente):
    for child in main_vente.winfo_children(): child.destroy()
    if len(p1.inv['armure']) > 0:
        tk.Label(main_vente, text=f"   Votre armure : {p1.inv['armure'][0]['nom']} {p1.inv['armure'][0]['stat']}          ").grid(column=1, row=1)
    else :
        tk.Label(main_vente, text=f"   Votre armure : Rien                                                                ").grid(column=1, row=1)
    if len(p1.inv['bouclier']) > 0:
        tk.Label(main_vente, text=f"   Votre bouclier : {p1.inv['bouclier'][0]['nom']} {p1.inv['bouclier'][0]['stat']}    ").grid(column=1, row=2)
    else :
        tk.Label(main_vente, text=f"   Votre bouclier : Rien                                                              ").grid(column=1, row=2)
    if len(p1.inv['arme']) > 0:
        tk.Label(main_vente, text=f"   Votre arme : {p1.inv['arme'][0]['nom']} {p1.inv['arme'][0]['stat']}                ").grid(column=1, row=3)
    else :
        tk.Label(main_vente, text=f"   Votre arme : Rien                                                                  ").grid(column=1, row=3)
    if len(p1.inv['anneau']) > 0:
        tk.Label(main_vente, text=f"   Votre anneau : {p1.inv['anneau'][0]['nom']} {p1.inv['anneau'][0]['stat']}          ").grid(column=1, row=4)
    else :
        tk.Label(main_vente, text=f"   Votre anneau : Rien                                                                ").grid(column=1, row=4)
    tk.Label(main_vente, text=f"Armures en stock :").grid(column=1, row=5)
    aff_vente_2(main_vente,'armure',1)
    tk.Label(main_vente, text=f"Boucliers en stock :").grid(column=2, row=5)
    aff_vente_2(main_vente,'bouclier',2)
    tk.Label(main_vente, text=f"Armes en stock :").grid(column=3, row=5)
    aff_vente_2(main_vente,'arme',3)
    tk.Label(main_vente, text=f"Anneaux en stock :").grid(column=4, row=5)
    aff_vente_2(main_vente,'anneau',4)
    main_vente.update()
    main_vente.update_idletasks()
    p1.update_val()
    



#systeme de combat
#actions du joueur
def attaque_legere(m1,battle,v):
    tk.Label(battle, text="Vous faites une attaque légère").grid(column=1, row=2)
    battle.update()
    battle.update_idletasks()
    m1.degat(p1.str,battle)
    attaque_monstre(m1,battle,v)
def attaque_lourde(m1,battle,v):
    tk.Label(battle, text="Vous faites une attaque lourde").grid(column=1, row=2)
    battle.update()
    battle.update_idletasks()
    m1.speed = m1.speed+20
    m1.degat(p1.str*2,battle)
    m1.speed = m1.speed-20
    attaque_monstre(m1,battle,v)
def boire_potion(m1,battle,v):
    b = randint(10,p1.hpmax/2)
    p1.heal(b,battle)
    tk.Label(battle, text=f'     Il vou reste maintenant {p1.hp} hp     ').grid(column=1, row=1)
    tk.Label(battle, text="          Vous buvez une potion          ").grid(column=1, row=2)
    battle.update()
    battle.update_idletasks()
    attaque_monstre(m1,battle,v)
def fuir(m1,battle,v):
    b = randint(1,100)
    if b < p1.speed*3 :
        tk.Label(battle, text="Vous arrivez à fuir").grid(column=1, row=2)
        # COMMANDE DE FIN DE COMBAT A INSERER ICI
        battle.update()
        battle.update_idletasks()
    if b > p1.speed*3 :
        tk.Label(battle, text="Vous n'arrivez pas à fuir").grid(column=1, row=2)
        # COMMANDE A INSERER ICI
        battle.update()
        battle.update_idletasks()
        attaque_monstre(m1,battle,v)

#actions du monstre
def attaque_monstre(m1,battle,v):
    global evo
    sleep(1)
    if m1.hp <= 0:
        val1 = 200 + (evo*200) * v #xp gagne
        val2 = 50 + (evo *100) * v #p gagne
        p1.xp += val1
        p1.arg += val2
        battle_end = tk.Tk()
        battle_end.title("Class rpg - Combat Terminé")
        battle_end.grid()
        #battle_end.geometry(100, 100)
        tk.Label(battle_end, text='Vous avez gagné le combat !').grid(column=1, row=0)
        tk.Label(battle_end, text=f'Vous optenez {val1} xp').grid(column=1, row=1)
        tk.Label(battle_end, text=f'Vous optenez {val2} pièces').grid(column=1, row=2)
        tk.Button(battle_end, text='Ok',command=lambda: [battle_end.destroy(),battle.destroy(),change_pos(p1.pos+1),p1.vieillir(0.25),p1.lvup(),partir()]).grid(column=3, row=5)
        center_window(250,100,battle_end)
        battle_end.mainloop()
    a = randint(1,100)
    if a <= 70:
        p1.degat(m1.str,battle)
        tk.Label(battle, text='le monstre fait une attaque normale').grid(column=4, row=2)
        tk.Label(battle, text=f'Il vou reste maintenant {p1.hp} hp').grid(column=1, row=1)
        battle.update()
        battle.update_idletasks()
    if a > 70 and a <= 85:
        p1.degat((m1.str)*1.5,battle)
        tk.Label(battle, text='le monstre fait une attaque lourde').grid(column=4, row=2)
        tk.Label(battle, text=f'Il vou reste maintenant {p1.hp} hp').grid(column=1, row=1)
        battle.update()
        battle.update_idletasks()
    if a > 85:
        m1.heal(m1.hp/2,battle)
        tk.Label(battle, text="                    le monstre se soigne                    ").grid(column=4, row=2)
        tk.Label(battle, text=f" hp actuel du monstre : {m1.hp}").grid(column=4, row=1)
        battle.update()
        battle.update_idletasks()


def combat(v):  #boucle de combat principale
    m1 = monstre()

    battle = tk.Tk()
    battle.title("Class rpg - Combat")
    battle.grid()
    battle.geometry("750x250")
    tk.Label(battle, text="Vous faites face à un montre").grid(column=1, row=0)
    tk.Label(battle, text="     ").grid(column=3, row=0)
    tk.Label(battle, text="Etat actuel du monstre :").grid(column=4, row=0)
    tk.Label(battle, text=" ").grid(column=1, row=1)
    tk.Label(battle, text="Que voulez vous faire ?").grid(column=1, row=2)
    tk.Button(battle, text="Attaque légère", command=lambda: [attaque_legere(m1,battle,v)]).grid(column=0, row=3)
    tk.Button(battle, text="Attaque lourde", command=lambda: [attaque_lourde(m1,battle,v)]).grid(column=1, row=3)
    tk.Button(battle, text="Se soigner", command=lambda: [boire_potion(m1,battle,v)]).grid(column=2, row=3)
    tk.Button(battle, text="Fuite", command=lambda: [fuir(m1,battle,v)]).grid(column=1, row=4)
    center_window(750,250,battle)
    battle.mainloop()

    if m1.speed >= p1.speed:
        attaque_monstre(m1,battle,v)

    #fin du combat
    if p1.hp <= 0:
        print('vous avez perdu')

#affiche les stats
def aff():
    lvl = tk.Tk()
    lvl.title("Stats")
    lvl.grid()
    lvl.geometry('%dx%d+%d+%d' % (250, 350, 1075, 260))
    tk.Label(lvl, text="Stats").grid(column=0, row=0)
    tk.Label(lvl, text=f"Argent : {p1.arg}").grid(column=0, row=1)
    tk.Label(lvl, text=f"Xp requis : {p1.xpmax}").grid(column=0, row=2)
    tk.Label(lvl, text=f"Xp : {p1.xp}").grid(column=0, row=3)
    tk.Label(lvl, text=f"Niveau : {p1.lvl}").grid(column=0, row=4)
    tk.Label(lvl, text=f"Age : {p1.age}").grid(column=0, row=5)
    tk.Label(lvl, text=f"hpmax : {p1.hpmax}").grid(column=0, row=6)
    tk.Label(lvl, text=f"hp : {p1.hp}").grid(column=0, row=7)
    tk.Label(lvl, text=f"Stamina : {p1.stam}").grid(column=0, row=8)
    tk.Label(lvl, text=f"Armure : {p1.arm}").grid(column=0, row=9)
    tk.Label(lvl, text=f"Vitesse : {p1.speed}").grid(column=0, row=10)
    tk.Label(lvl, text=f"Force : {p1.str}").grid(column=0, row=11)
    tk.Label(lvl, text=f"Intelligence : {p1.int}").grid(column=0, row=12)
    tk.Label(lvl, text=f"Position : {p1.pos}").grid(column=0, row=13)
    tk.Button(lvl, text="Ok", command=lvl.destroy).grid(column=1, row=14)
    lvl.mainloop()

def aff_inv():
    main_inv = tk.Tk()
    main_inv.title("inventaire")
    main_inv.grid()
    main_inv.geometry('%dx%d+%d+%d' % (950, 350, 1075, 260))
    if len(p1.inv['armure']) > 0:
        tk.Label(main_inv, text=f"   Votre armure : {p1.inv['armure'][0]['nom']} {p1.inv['armure'][0]['stat']}          ").grid(column=1, row=1)
    else :
        tk.Label(main_inv, text=f"   Votre armure : Rien                                                                ").grid(column=1, row=1)
    if len(p1.inv['bouclier']) > 0:
        tk.Label(main_inv, text=f"   Votre bouclier : {p1.inv['bouclier'][0]['nom']} {p1.inv['bouclier'][0]['stat']}    ").grid(column=1, row=2)
    else :
        tk.Label(main_inv, text=f"   Votre bouclier : Rien                                                              ").grid(column=1, row=2)
    if len(p1.inv['arme']) > 0:
        tk.Label(main_inv, text=f"   Votre arme : {p1.inv['arme'][0]['nom']} {p1.inv['arme'][0]['stat']}                ").grid(column=1, row=3)
    else :
        tk.Label(main_inv, text=f"   Votre arme : Rien                                                                  ").grid(column=1, row=3)
    if len(p1.inv['anneau']) > 0:
        tk.Label(main_inv, text=f"   Votre anneau : {p1.inv['anneau'][0]['nom']} {p1.inv['anneau'][0]['stat']}          ").grid(column=1, row=4)
    else :
        tk.Label(main_inv, text=f"   Votre anneau : Rien                                                                ").grid(column=1, row=4)
    tk.Label(main_inv, text=f"Armures en stock :").grid(column=1, row=5)
    aff_inv_2(main_inv,'armure',1)
    tk.Label(main_inv, text=f"Boucliers en stock :").grid(column=2, row=5)
    aff_inv_2(main_inv,'bouclier',2)
    tk.Label(main_inv, text=f"Armes en stock :").grid(column=3, row=5)
    aff_inv_2(main_inv,'arme',3)
    tk.Label(main_inv, text=f"Anneaux en stock :").grid(column=4, row=5)
    aff_inv_2(main_inv,'anneau',4)
    main_inv.mainloop()

def aff_inv_2(main_inv,nom,col):
    for i in range(len(p1.inv_2[nom])):
        tk.Button(main_inv, text=f"{i}. {p1.inv_2[nom][i]['nom']} {p1.inv_2[nom][i]['stat']}", command=lambda i=i: equipe_item_inv(nom,i,main_inv)).grid(column=col, row=6+i)
        

def aff_vente():
    main_vente = tk.Tk()
    main_vente.title("inventaire")
    main_vente.grid()
    main_vente.geometry('%dx%d+%d+%d' % (950, 350, 1075, 260))
    tk.Label(main_vente, text=f"   Votre armure : {p1.inv['armure'][0]['nom']} {p1.inv['armure'][0]['stat']}          ").grid(column=1, row=1)
    tk.Label(main_vente, text=f"   Votre bouclier : {p1.inv['bouclier'][0]['nom']} {p1.inv['bouclier'][0]['stat']}    ").grid(column=1, row=2)
    tk.Label(main_vente, text=f"   Votre arme : {p1.inv['arme'][0]['nom']} {p1.inv['arme'][0]['stat']}                ").grid(column=1, row=3)
    tk.Label(main_vente, text=f"   Votre anneau : {p1.inv['anneau'][0]['nom']} {p1.inv['anneau'][0]['stat']}          ").grid(column=1, row=4)
    tk.Label(main_vente, text=f"Armures en stock :").grid(column=1, row=5)
    aff_vente_2(main_vente,'armure',1)
    tk.Label(main_vente, text=f"Boucliers en stock :").grid(column=2, row=5)
    aff_vente_2(main_vente,'bouclier',2)
    tk.Label(main_vente, text=f"Armes en stock :").grid(column=3, row=5)
    aff_vente_2(main_vente,'arme',3)
    tk.Label(main_vente, text=f"Anneaux en stock :").grid(column=4, row=5)
    aff_vente_2(main_vente,'anneau',4)
    main_vente.mainloop()

def aff_vente_2(main_vente,nom,col):
    for i in range(len(p1.inv_2[nom])):
        tk.Button(main_vente, text=f"{i}. {p1.inv_2[nom][i]['nom']} {p1.inv_2[nom][i]['stat']} ({(p1.inv_2[nom][i]['prix'])/2} p)", command=lambda i=i: vente_item(nom,i,main_vente)).grid(column=col, row=6+i)

def achat_main(v):
    global evo
    item_1 = selec_al()
    item_2 = selec_al()
    item_1_prix = item_1['prix'] + (evo*item_1['prix'])*v
    item_2_prix = item_2['prix'] + (evo*item_2['prix'])*v
    tachat = tk.Tk()
    tachat.grid()
    tachat.title("Class rpg - Marchand")
    tachat.geometry('%dx%d+%d+%d' % (660, 150, 350, 50))
    tk.Label(tachat, text="Marchand").grid(column=1, row=0)
    tk.Label(tachat, text=f"Que voulez achetez ? Vous avez : {p1.arg} p").grid(column=1, row=1)
    tk.Button(tachat, text=f"{item_1['nom']} +{v} ({item_1_prix} p)", command=lambda *args: lance_achat(v,tachat,item_1_prix,item_1)).grid(column=0, row=2)
    tk.Button(tachat, text=f"{item_2['nom']} +{v} ({item_2_prix} p)", command=lambda *args: lance_achat(v,tachat,item_2_prix,item_2)).grid(column=1, row=2)
    tk.Button(tachat, text=f"une potion de vie ({25+(evo*20)*v} p)", command=lambda *args: lance_achat(v,tachat)).grid(column=2, row=2)
    tk.Button(tachat, text=f"Vendre vos objets", command=lambda *args: aff_vente()).grid(column=1, row=3)
    tk.Button(tachat, text="Quit", command=lambda: tachat.destroy()).grid(column=2, row=4)
    tachat.mainloop()
def lance_achat(v,tachat,prix,item):
    if p1.arg >= prix:
        p1.arg -= prix #argent depensee
        item_f = ajuste_item(item,v,prix)
        equipe_item_achat(item_f)
        #p1.inv_2[item['type']].append(item_f)
        tk.Label(tachat, text=f"   Vous avez acheté un(e) {item['nom']} ({prix} p)   ").grid(column=1, row=3)
        tk.Label(tachat, text=f"     Que voulez achetez ? Vous avez : {p1.arg} p     ").grid(column=1, row=1)
        p1.update_val()
        tachat.update()
        tachat.update_idletasks()
    else:
        tk.Label(tachat, text=f"     Que voulez achetez ? Vous avez : {p1.arg} p     ").grid(column=1, row=1)
        tk.Label(tachat, text="               pas assez d'argent               ").grid(column=1, row=3)
        tachat.update()
        tachat.update_idletasks()

def change_rep():
    global rep
    rep = al()
def change_hp(v):
    p1.hp = v
def change_action(v):
    global action
    action = v
lvequipement = 0
def change_pos(v):
    p1.update_val()
    global lvequipement
    p1.pos = v
    if p1.pos%5 == 0 :
        lvequipement += 1
    p1.vieillir(0.25)
def change_pp(v):
    global pp
    pp = v
def partir():
    global rep
    rep = al()
    tk.Label(main, text=f"  Vous êtes sur à la position {p1.pos} il y a un {rep[1]} sur votre route  ").grid(column=1, row=0)
    main.update()
    main.update_idletasks()
    



#fonction qui envoie vers le choix fait
#c est si la personne passe la case ou non ( 1 = elle la jouer, 2 = ne joue pas )
#t est le type de la case defini sur 100 selon la fonction al()
#v est le niveau du loot, donc +1 niveau toutes les 5 cases
def choix(c,t_,v):
    global tachat
    if c == 2 :
        print('vous passez sans rien faire')
#combat
    if t_ >= 20 and c == 1:
        combat(v)
#coffre
    if t_ >= 10 and t_ < 20 and c == 1:
        p1.arg += 100
        tcoffre = tk.Tk()
        tcoffre.title("Class rpg - coffre")
        tcoffre.grid()
        tk.Label(tcoffre, text=f"Vous trouvez 100 pièces dans le coffre").grid(column=1, row=1)
        tk.Button(tcoffre, text="Ok", command=tcoffre.destroy).grid(column=1, row=2)
        center_window(275,75,tcoffre)

#marchand
    if t_ < 10 and c == 1:
        achat_main(v)
    fin = True
    return fin



#lance l'aleatoire de la case
def al():
    a = randint(1,100)
    if a >= 20:
        b = 'un monstre'
        return a,b
    if a >= 10 and a < 20:
        b = 'un coffre'
        return a,b
    if a < 10:
        b = 'un marchand'
        return a,b

def center_window(width, height,window):
    # get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

#boucle principale du jeu
lvequipement = 0
while p1.hp > 0:
    rep = al()
    main = tk.Tk()
    main.grid()
    main.title("Class rpg")
    main.geometry("750x250")
    tk.Label(main, text=f"Vous êtes sur à la position {p1.pos} il y a un {rep[1]} sur votre route").grid(column=1, row=0)
    tk.Label(main, text="Que voulez vous faire ?").grid(column=1, row=1)
    tk.Button(main, text="s'en approcher", command=lambda: [choix(1,rep[0],lvequipement),main.destroy()]).grid(column=0, row=2)
    tk.Button(main, text="partir", command=lambda: [change_pos(p1.pos+1),partir()]).grid(column=1, row=2)
    tk.Button(main, text="statistiques", command=lambda *args: aff()).grid(column=2, row=2)
    tk.Button(main, text="inventaire", command=lambda *args: aff_inv()).grid(column=3, row=2)
    tk.Button(main, text="Quit", command=lambda: [change_hp(-50),main.destroy()]).grid(column=2, row=3)
    center_window(750, 250,main)
    main.mainloop()

print('perdu')