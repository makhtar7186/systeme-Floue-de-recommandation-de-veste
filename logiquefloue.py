# marquage pour les modification
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl 

def antecedant():
    """ Cette fonction declare les antecedants"""

    # La tour de taille est située dans un intervalle 
    tour_taille = ctrl.Antecedent(np.arange(52, 93, 2), 'tour_taille')
    # La tour de poitrine est située dans un intervalle
    tour_poitrine = ctrl.Antecedent(np.arange(70, 111, 2), 'tour_poitrine')
    # La longueur des manches
    longueur_manche = ctrl.Antecedent(np.arange(67, 90, 1), 'longueur_manche')
    # Longueur dos    
    taille_dos = ctrl.Antecedent(np.arange(68, 73, 1), 'taille_dos')
    # Hanche
    hanche = ctrl.Antecedent(np.arange(88, 108, 0.5), 'hanche')
    # Longueur jambe
    longueur_jambe = ctrl.Antecedent(np.arange(73, 83, 1), 'longueur_jambe')

    return tour_taille, tour_poitrine, taille_dos, hanche, longueur_jambe, longueur_manche

def consequence():
    """ Declaration de la conséquence """
    choix_taille = ctrl.Consequent(np.arange(0, 100, 2), 'choix_taille')
    return choix_taille

def defuzzification(x):
    if x >= 0 and x < 20:
        return 'XS'
    elif x >= 20 and x < 40:
        return 'S'
    elif x >= 40 and x < 60:
        return 'M'
    elif x >= 60 and x < 80:
        return 'L'
    elif x >= 80 and x <= 100:
        return 'XL'

def definitionRegleVest():
    rule1 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XS'] & tour_taille['XS'], choix_taille['XS'])
    rule2 = ctrl.Rule(taille_dos['S'] & tour_poitrine['S'] & tour_taille['S'], choix_taille['S'])
    rule3 = ctrl.Rule(taille_dos['M'] & tour_poitrine['M'] & tour_taille['M'], choix_taille['M'])
    rule4 = ctrl.Rule(taille_dos['L'] & tour_poitrine['L'] & tour_taille['L'], choix_taille['L'])
    rule5 = ctrl.Rule(taille_dos['XL'] & tour_poitrine['XL'] & tour_taille['XL'], choix_taille['XL'])

    rule6 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XS'] & tour_taille['S'], choix_taille['S'])
    rule7 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XS'] & tour_taille['M'], choix_taille['M'])
    rule8 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XS'] & tour_taille['L'], choix_taille['L'])
    rule9 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XS'] & tour_taille['XL'], choix_taille['XL'])

    rule10 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['M'] & tour_taille['XS'], choix_taille['M'])
    rule11 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['L'] & tour_taille['XS'], choix_taille['L'])
    rule12 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['S'] & tour_taille['XS'], choix_taille['S'])
    rule13 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XL'] & tour_taille['XS'], choix_taille['XL'])

    rule14 = ctrl.Rule(taille_dos['S'] & tour_poitrine['XS'] & tour_taille['S'], choix_taille['S'])
    rule15 = ctrl.Rule(taille_dos['S'] & tour_poitrine['XS'] & tour_taille['M'], choix_taille['M'])
    rule16 = ctrl.Rule(taille_dos['S'] & tour_poitrine['XS'] & tour_taille['L'], choix_taille['L'])
    rule17 = ctrl.Rule(taille_dos['S'] & tour_poitrine['XS'] & tour_taille['XL'], choix_taille['XL'])

    rule18 = ctrl.Rule(taille_dos['S'] & tour_poitrine['M'] & tour_taille['XS'], choix_taille['M'])
    rule19 = ctrl.Rule(taille_dos['S'] & tour_poitrine['L'] & tour_taille['XS'], choix_taille['L'])
    rule20 = ctrl.Rule(taille_dos['S'] & tour_poitrine['S'] & tour_taille['XS'], choix_taille['S'])
    rule21 = ctrl.Rule(taille_dos['S'] & tour_poitrine['XL'] & tour_taille['XS'], choix_taille['XL'])

    rule22 = ctrl.Rule(taille_dos['M'] & tour_poitrine['XS'] & tour_taille['S'], choix_taille['S'])
    rule23 = ctrl.Rule(taille_dos['M'] & tour_poitrine['XS'] & tour_taille['M'], choix_taille['M'])
    rule24 = ctrl.Rule(taille_dos['M'] & tour_poitrine['XS'] & tour_taille['L'], choix_taille['L'])
    rule25 = ctrl.Rule(taille_dos['M'] & tour_poitrine['XS'] & tour_taille['XL'], choix_taille['XL'])

    rule26 = ctrl.Rule(taille_dos['M'] & tour_poitrine['M'] & tour_taille['XS'], choix_taille['M'])
    rule27 = ctrl.Rule(taille_dos['M'] & tour_poitrine['L'] & tour_taille['XS'], choix_taille['L'])
    rule28 = ctrl.Rule(taille_dos['M'] & tour_poitrine['S'] & tour_taille['XS'], choix_taille['S'])
    rule29 = ctrl.Rule(taille_dos['M'] & tour_poitrine['XL'] & tour_taille['XS'], choix_taille['XL'])

    rule30 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['S'] & tour_taille['S'], choix_taille['S'])
    rule31 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['S'] & tour_taille['M'], choix_taille['M'])
    rule32 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['S'] & tour_taille['L'], choix_taille['L'])
    rule33 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['S'] & tour_taille['XL'], choix_taille['XL'])

    rule34 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['M'] & tour_taille['S'], choix_taille['M'])
    rule35 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['M'] & tour_taille['M'], choix_taille['M'])
    rule36 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['M'] & tour_taille['L'], choix_taille['L'])
    rule37 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['M'] & tour_taille['XL'], choix_taille['XL'])

    rule38 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['L'] & tour_taille['S'], choix_taille['L'])
    rule39 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['L'] & tour_taille['M'], choix_taille['L'])
    rule40 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['L'] & tour_taille['L'], choix_taille['L'])
    rule41 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['L'] & tour_taille['XL'], choix_taille['XL'])

    rule42 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XL'] & tour_taille['S'], choix_taille['XL'])
    rule43 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XL'] & tour_taille['M'], choix_taille['XL'])
    rule44 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XL'] & tour_taille['L'], choix_taille['XL'])
    rule45 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XL'] & tour_taille['XL'], choix_taille['XL'])

    return [rule1, rule2, rule3, rule4, rule5, 
          rule6, rule7, rule8, rule9, rule10,
          rule11, rule12, rule13, rule14,
          rule15, rule16, rule17, rule18,
          rule19, rule20, rule21, rule22,
          rule23, rule24, rule25, rule26,
          rule27, rule28, rule29, rule30,
          rule31, rule32, rule33, rule34,
          rule35, rule36, rule37, rule38,
          rule39, rule40, rule41, rule42,
          rule43, rule44, rule45]


def definitionRegleChem():
    rule1 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XS'] & tour_taille['XS'] & longueur_manche['XS'], choix_taille['XS'])
    rule2 = ctrl.Rule(taille_dos['S'] & tour_poitrine['S'] & tour_taille['S'] & longueur_manche['S'], choix_taille['S'])
    rule3 = ctrl.Rule(taille_dos['M'] & tour_poitrine['M'] & tour_taille['M'] & longueur_manche['M'], choix_taille['M'])
    rule4 = ctrl.Rule(taille_dos['L'] & tour_poitrine['L'] & tour_taille['L'] & longueur_manche['L'], choix_taille['L'])
    rule5 = ctrl.Rule(taille_dos['XL'] & tour_poitrine['XL'] & tour_taille['XL'] & longueur_manche['XL'], choix_taille['XL'])

    rule6 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XS'] & tour_taille['S'] & longueur_manche['S'], choix_taille['S'])
    rule7 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XS'] & tour_taille['S'] & longueur_manche['M'], choix_taille['M'])

    rule8 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XS'] & tour_taille['M'] & longueur_manche['M'], choix_taille['M'])
    rule9 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XS'] & tour_taille['M'] & longueur_manche['L'], choix_taille['L'])

    rule10 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XS'] & tour_taille['L'] & longueur_manche['L'], choix_taille['L'])
    rule11 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XS'] & tour_taille['XL'] & longueur_manche['XL'], choix_taille['XL'])

    rule12 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['M'] & tour_taille['XS'] & longueur_manche['M'], choix_taille['M'])
    rule13 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['M'] & tour_taille['XS'] & longueur_manche['L'], choix_taille['L'])

    rule14 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['L'] & tour_taille['XS'] & longueur_manche['L'], choix_taille['L'])
    rule15 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['L'] & tour_taille['XS'] & longueur_manche['XL'], choix_taille['XL'])

    rule16 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['S'] & tour_taille['XS'] & longueur_manche['L'], choix_taille['S'])
    rule17 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['S'] & tour_taille['XS'] & longueur_manche['M'], choix_taille['M'])

    rule18 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XL'] & tour_taille['XS'] & longueur_manche['L'], choix_taille['XL'])
    rule19 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XL'] & tour_taille['XS'] & longueur_manche['XL'], choix_taille['XL'])

    rule20 = ctrl.Rule(taille_dos['S'] & tour_poitrine['XS'] & tour_taille['S'] & longueur_manche['S'] , choix_taille['S'])
    rule21 = ctrl.Rule(taille_dos['S'] & tour_poitrine['XS'] & tour_taille['S'] & longueur_manche['M'] , choix_taille['M'])

    rule22 = ctrl.Rule(taille_dos['S'] & tour_poitrine['XS'] & tour_taille['M'] & longueur_manche['M'], choix_taille['M'])
    rule23 = ctrl.Rule(taille_dos['S'] & tour_poitrine['XS'] & tour_taille['M'] & longueur_manche['L'], choix_taille['L'])

    rule24 = ctrl.Rule(taille_dos['S'] & tour_poitrine['XS'] & tour_taille['L'] & longueur_manche['L'], choix_taille['L'])
    rule25 = ctrl.Rule(taille_dos['S'] & tour_poitrine['XS'] & tour_taille['L'] & longueur_manche['XL'], choix_taille['XL'])

    rule26 = ctrl.Rule(taille_dos['S'] & tour_poitrine['XS'] & tour_taille['XL'] & longueur_manche['XL'], choix_taille['XL'])

    rule27 = ctrl.Rule(taille_dos['S'] & tour_poitrine['M'] & tour_taille['XS'] & longueur_manche['M'], choix_taille['M'])
    rule28 = ctrl.Rule(taille_dos['S'] & tour_poitrine['M'] & tour_taille['XS'] & longueur_manche['L'], choix_taille['L'])

    rule29 = ctrl.Rule(taille_dos['S'] & tour_poitrine['L'] & tour_taille['XS'] & longueur_manche['L'], choix_taille['L'])
    rule30 = ctrl.Rule(taille_dos['S'] & tour_poitrine['L'] & tour_taille['XS'] & longueur_manche['XL'], choix_taille['XL'])

    rule31 = ctrl.Rule(taille_dos['S'] & tour_poitrine['S'] & tour_taille['XS'] & longueur_manche['S'], choix_taille['S'])
    rule32 = ctrl.Rule(taille_dos['S'] & tour_poitrine['S'] & tour_taille['XS'] & longueur_manche['M'], choix_taille['M'])

    rule33 = ctrl.Rule(taille_dos['S'] & tour_poitrine['XL'] & tour_taille['XS'] & longueur_manche['XL'], choix_taille['XL'])

    rule34 = ctrl.Rule(taille_dos['M'] & tour_poitrine['XS'] & tour_taille['S'] & longueur_manche['S'], choix_taille['S'])
    rule35 = ctrl.Rule(taille_dos['M'] & tour_poitrine['XS'] & tour_taille['S'] & longueur_manche['M'], choix_taille['M'])
    rule36 = ctrl.Rule(taille_dos['M'] & tour_poitrine['XS'] & tour_taille['M'] & longueur_manche['M'], choix_taille['M'])
    rule37 = ctrl.Rule(taille_dos['M'] & tour_poitrine['XS'] & tour_taille['M'] & longueur_manche['L'], choix_taille['L'])


    rule38 = ctrl.Rule(taille_dos['M'] & tour_poitrine['XS'] & tour_taille['L'] & longueur_manche['L'], choix_taille['L'])
    rule39 = ctrl.Rule(taille_dos['M'] & tour_poitrine['XS'] & tour_taille['L'] & longueur_manche['XL'], choix_taille['XL'])

    rule40 = ctrl.Rule(taille_dos['M'] & tour_poitrine['XS'] & tour_taille['XL'] & longueur_manche['XL'], choix_taille['XL'])

    rule41 = ctrl.Rule(taille_dos['M'] & tour_poitrine['M'] & tour_taille['XS'] & longueur_manche['M'], choix_taille['M'])
    rule42 = ctrl.Rule(taille_dos['M'] & tour_poitrine['M'] & tour_taille['XS'] & longueur_manche['L'], choix_taille['L'])
    
    rule43 = ctrl.Rule(taille_dos['M'] & tour_poitrine['L'] & tour_taille['XS'] & longueur_manche['L'], choix_taille['L'])
    rule44 = ctrl.Rule(taille_dos['M'] & tour_poitrine['L'] & tour_taille['XS'] & longueur_manche['XL'], choix_taille['L'])
    
    rule45 = ctrl.Rule(taille_dos['M'] & tour_poitrine['S'] & tour_taille['XS'] & longueur_manche['S'], choix_taille['S'])
    rule46 = ctrl.Rule(taille_dos['M'] & tour_poitrine['S'] & tour_taille['XS'] & longueur_manche['M'], choix_taille['M'])

    rule47 = ctrl.Rule(taille_dos['M'] & tour_poitrine['XL'] & tour_taille['XS'] & longueur_manche['XL'], choix_taille['XL'])

    rule48 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['S'] & tour_taille['S'] & longueur_manche['S'], choix_taille['S'])
    rule49 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['S'] & tour_taille['S'] & longueur_manche['M'], choix_taille['M'])
    
    rule50 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['S'] & tour_taille['M'] & longueur_manche['M'], choix_taille['M'])
    rule51 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['S'] & tour_taille['M'] & longueur_manche['L'], choix_taille['L'])
    
    rule52 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['S'] & tour_taille['L'] & longueur_manche['L'], choix_taille['L'])
    rule53 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['S'] & tour_taille['L'] & longueur_manche['XL'], choix_taille['XL'])
    
    rule54 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['S'] & tour_taille['XL'] & longueur_manche['XL'], choix_taille['XL'])

    rule55 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['M'] & tour_taille['S'] & longueur_manche['M'], choix_taille['M'])
    rule56 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['M'] & tour_taille['S'] & longueur_manche['L'], choix_taille['L'])
    
    rule57 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['M'] & tour_taille['M'] & longueur_manche['M'], choix_taille['M'])
    rule58 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['M'] & tour_taille['M'] & longueur_manche['L'], choix_taille['L'])
    
    rule59 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['M'] & tour_taille['L'] & longueur_manche['L'], choix_taille['L'])
    rule60 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['M'] & tour_taille['L'] & longueur_manche['XL'], choix_taille['XL'])

    rule61 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['M'] & tour_taille['XL'] & longueur_manche['XL'], choix_taille['XL'])

    rule62 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['L'] & tour_taille['S'] & longueur_manche['L'], choix_taille['L'])
    rule63 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['L'] & tour_taille['S'] & longueur_manche['XL'], choix_taille['XL'])

    rule64 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['L'] & tour_taille['M'] & longueur_manche['L'], choix_taille['L'])
    rule65 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['L'] & tour_taille['M'] & longueur_manche['XL'], choix_taille['XL'])
    
    rule66 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['L'] & tour_taille['L'] & longueur_manche['L'], choix_taille['L'])
    rule67 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['L'] & tour_taille['L'] & longueur_manche['XL'], choix_taille['XL'])
    
    rule68 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['L'] & tour_taille['XL'] & longueur_manche['XL'], choix_taille['XL'])

    rule69 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XL'] & tour_taille['S'] & longueur_manche['XL'], choix_taille['XL'])
    rule70 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XL'] & tour_taille['M'] & longueur_manche['XL'], choix_taille['XL'])
    rule71 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XL'] & tour_taille['L'] & longueur_manche['XL'], choix_taille['XL'])
    rule72 = ctrl.Rule(taille_dos['XS'] & tour_poitrine['XL'] & tour_taille['XL'] & longueur_manche['XL'], choix_taille['XL'])
    
    #j'ecrit le return de cette fonction qui renvoir les rule
    return [rule1, rule2, rule3, rule4, rule5, 
          rule6, rule7, rule8, rule9, rule10,
          rule11, rule12, rule13, rule14,
          rule15, rule16, rule17, rule18,
          rule19, rule20, rule21, rule22,
          rule23, rule24, rule25, rule26,
          rule27, rule28, rule29, rule30,
          rule31, rule32, rule33, rule34,
          rule35, rule36, rule37, rule38,
          rule39, rule40, rule41, rule42,
          rule43, rule44, rule45,rule46,
          rule47, rule48, rule49,rule50,
          rule51, rule52, rule53,rule54,
          rule55, rule56, rule57,rule58,
          rule59, rule60, rule61,rule62,
          rule63, rule64, rule65,rule66,
          rule67, rule68, rule69,rule70,
          rule71, rule72]
    


def definitionReglePant():
    rule1 = ctrl.Rule(hanche['XS'] & longueur_jambe['XS'], choix_taille['XS'])
    rule2 = ctrl.Rule(hanche['S'] & longueur_jambe['S'], choix_taille['S'])
    rule3 = ctrl.Rule(hanche['M'] & longueur_jambe['M'], choix_taille['M'])
    rule4 = ctrl.Rule(hanche['L'] & longueur_jambe['L'], choix_taille['L'])
    rule5 = ctrl.Rule(hanche['XL'] & longueur_jambe['XL'], choix_taille['XL'])
    rule6 = ctrl.Rule(hanche['XS'] & longueur_jambe['S'], choix_taille['XS'])
    rule7 = ctrl.Rule(hanche['XS'] & longueur_jambe['M'], choix_taille['M'])
    rule8 = ctrl.Rule(hanche['XS'] & longueur_jambe['L'], choix_taille['M'])
    rule9 = ctrl.Rule(hanche['XS'] & longueur_jambe['XL'], choix_taille['L'])
    rule10 = ctrl.Rule(hanche['S'] & longueur_jambe['XS'], choix_taille['S'])
    rule11 = ctrl.Rule(hanche['S'] & longueur_jambe['M'], choix_taille['M'])
    rule12 = ctrl.Rule(hanche['S'] & longueur_jambe['L'], choix_taille['M'])
    rule13 = ctrl.Rule(hanche['S'] & longueur_jambe['XL'], choix_taille['L'])
    rule14 = ctrl.Rule(hanche['L'] & longueur_jambe['XS'], choix_taille['M'])
    rule15 = ctrl.Rule(hanche['L'] & longueur_jambe['S'], choix_taille['M'])
    rule16 = ctrl.Rule(hanche['L'] & longueur_jambe['M'], choix_taille['L'])
    rule17 = ctrl.Rule(hanche['L'] & longueur_jambe['XL'], choix_taille['L'])
    rule18 = ctrl.Rule(hanche['XL'] & longueur_jambe['XS'], choix_taille['M'])
    rule19 = ctrl.Rule(hanche['XL'] & longueur_jambe['S'], choix_taille['M'])
    rule20 = ctrl.Rule(hanche['XL'] & longueur_jambe['M'], choix_taille['L'])
    rule21 = ctrl.Rule(hanche['XL'] & longueur_jambe['L'], choix_taille['L'])
    rule22 = ctrl.Rule(hanche['M'] & longueur_jambe['XS'], choix_taille['S'])
    rule23 = ctrl.Rule(hanche['M'] & longueur_jambe['S'], choix_taille['M'])
    rule24 = ctrl.Rule(hanche['M'] & longueur_jambe['L'], choix_taille['M'])
    rule25 = ctrl.Rule(hanche['M'] & longueur_jambe['XL'], choix_taille['L'])

    return [rule1, rule2, rule3, rule4, rule5, 
          rule6, rule7, rule8, rule9, rule10,
          rule11, rule12, rule13, rule14,
          rule15, rule16, rule17, rule18,
          rule19, rule20, rule21, rule22,
          rule23, rule24, rule25]

def configurationVest():
    """ Configuration des variables et des règles pour le choix de la taille de la veste """
    global tour_taille, tour_poitrine, taille_dos,choix_taille
    #Antécedants et conséquence
    tour_taille, tour_poitrine, taille_dos = antecedant()[0], antecedant()[1], antecedant()[2]
    choix_taille = consequence()

    # Configuration longueur du dos
    taille_dos_XS = fuzz.trapmf(taille_dos.universe, [68, 69, 70, 70])
    taille_dos_S = fuzz.trapmf(taille_dos.universe, [69, 70, 71, 71])
    taille_dos_M = fuzz.trapmf(taille_dos.universe, [70, 71, 72, 72])
    taille_dos_L = fuzz.trapmf(taille_dos.universe, [71, 72, 73, 73])
    taille_dos_XL = fuzz.trapmf(taille_dos.universe, [72, 73, 74, 74])
    taille_dos['XS'] = taille_dos_XS
    taille_dos['S'] = taille_dos_S
    taille_dos['M'] = taille_dos_M
    taille_dos['L'] = taille_dos_L
    taille_dos['XL'] = taille_dos_XL

    # Configuration de la tour de TAILLE
    tour_taille_XS = fuzz.trapmf(tour_taille.universe, [52, 52, 60, 61])
    tour_taille_S = fuzz.trapmf(tour_taille.universe, [60, 61, 68, 69])
    tour_taille_M = fuzz.trapmf(tour_taille.universe, [68, 69, 76, 77])
    tour_taille_L = fuzz.trapmf(tour_taille.universe, [76, 77, 84, 85])
    tour_taille_XL = fuzz.trapmf(tour_taille.universe, [84, 85, 92, 93])
    tour_taille['XS'] = tour_taille_XS
    tour_taille['S'] = tour_taille_S
    tour_taille['M'] = tour_taille_M
    tour_taille['L'] = tour_taille_L
    tour_taille['XL'] = tour_taille_XL

    # Configuration du tour de poitrine
    tour_poitrine_XS = fuzz.trapmf(tour_poitrine.universe, [70, 70, 78, 79])
    tour_poitrine_S = fuzz.trapmf(tour_poitrine.universe, [78, 79, 86, 87])
    tour_poitrine_M = fuzz.trapmf(tour_poitrine.universe, [86, 87, 94, 95])
    tour_poitrine_L = fuzz.trapmf(tour_poitrine.universe, [94, 95, 102, 103])
    tour_poitrine_XL = fuzz.trapmf(tour_poitrine.universe, [102, 103, 110, 110])
    tour_poitrine['XS'] = tour_poitrine_XS
    tour_poitrine['S'] = tour_poitrine_S
    tour_poitrine['M'] = tour_poitrine_M
    tour_poitrine['L'] = tour_poitrine_L
    tour_poitrine['XL'] = tour_poitrine_XL

    # Configuration du Choix
    choix_XS = fuzz.trapmf(choix_taille.universe, [0, 0, 19, 19])
    choix_S = fuzz.trapmf(choix_taille.universe, [20, 20, 39, 39])
    choix_M = fuzz.trapmf(choix_taille.universe, [40, 40, 59, 59])
    choix_L = fuzz.trapmf(choix_taille.universe, [60, 60, 79, 79])
    choix_XL = fuzz.trapmf(choix_taille.universe, [80, 80, 100, 100])
    choix_taille['XS'] = choix_XS
    choix_taille['S'] = choix_S
    choix_taille['M'] = choix_M
    choix_taille['L'] = choix_L
    choix_taille['XL'] = choix_XL


    # Configuration des règles
    choix_regles = ctrl.ControlSystem(definitionRegleVest())
    choisir = ctrl.ControlSystemSimulation(choix_regles)

    return choisir


def configurationChemise():
    """ Configuration des variables et des règles pour le choix de la taille de la chemise """
    global tour_taille, tour_poitrine, taille_dos, longueur_manche, choix_taille
    # Antécedants et conséquence
    tour_taille, tour_poitrine, taille_dos, longueur_manche = antecedant()[0], antecedant()[1], antecedant()[2], antecedant()[5]
    choix_taille = consequence()

      # Configuration longueur du dos
    taille_dos_XS = fuzz.trapmf(taille_dos.universe, [68, 69, 70, 70])
    taille_dos_S = fuzz.trapmf(taille_dos.universe, [69, 70, 71, 71])
    taille_dos_M = fuzz.trapmf(taille_dos.universe, [70, 71, 72, 72])
    taille_dos_L = fuzz.trapmf(taille_dos.universe, [71, 72, 73, 73])
    taille_dos_XL = fuzz.trapmf(taille_dos.universe, [72, 73, 74, 74])
    taille_dos['XS'] = taille_dos_XS
    taille_dos['S'] = taille_dos_S
    taille_dos['M'] = taille_dos_M
    taille_dos['L'] = taille_dos_L
    taille_dos['XL'] = taille_dos_XL
    # configuration longueur manche
    longueur_manche_XS = fuzz.trapmf(longueur_manche.universe, [67, 68, 72, 72])
    longueur_manche_S = fuzz.trapmf(longueur_manche.universe, [71, 72, 74, 74])
    longueur_manche_M = fuzz.trapmf(longueur_manche.universe, [73, 74, 79, 79])
    longueur_manche_L = fuzz.trapmf(longueur_manche.universe, [78, 79, 84, 84])
    longueur_manche_XL = fuzz.trapmf(longueur_manche.universe, [83, 84, 90, 90])
    longueur_manche['XS'] = longueur_manche_XS
    longueur_manche['S'] = longueur_manche_S
    longueur_manche['M'] = longueur_manche_M
    longueur_manche['L'] = longueur_manche_L
    longueur_manche['XL'] = longueur_manche_XL


    # Configuration de la tour de TAILLE
    tour_taille_XS = fuzz.trapmf(tour_taille.universe, [52, 52, 60, 61])
    tour_taille_S = fuzz.trapmf(tour_taille.universe, [60, 61, 68, 69])
    tour_taille_M = fuzz.trapmf(tour_taille.universe, [68, 69, 76, 77])
    tour_taille_L = fuzz.trapmf(tour_taille.universe, [76, 77, 84, 85])
    tour_taille_XL = fuzz.trapmf(tour_taille.universe, [84, 85, 92, 93])
    tour_taille['XS'] = tour_taille_XS
    tour_taille['S'] = tour_taille_S
    tour_taille['M'] = tour_taille_M
    tour_taille['L'] = tour_taille_L
    tour_taille['XL'] = tour_taille_XL

    # Configuration du tour de poitrine
    tour_poitrine_XS = fuzz.trapmf(tour_poitrine.universe, [70, 70, 78, 79])
    tour_poitrine_S = fuzz.trapmf(tour_poitrine.universe, [78, 79, 86, 87])
    tour_poitrine_M = fuzz.trapmf(tour_poitrine.universe, [86, 87, 94, 95])
    tour_poitrine_L = fuzz.trapmf(tour_poitrine.universe, [94, 95, 102, 103])
    tour_poitrine_XL = fuzz.trapmf(tour_poitrine.universe, [102, 103, 110, 110])
    tour_poitrine['XS'] = tour_poitrine_XS
    tour_poitrine['S'] = tour_poitrine_S
    tour_poitrine['M'] = tour_poitrine_M
    tour_poitrine['L'] = tour_poitrine_L
    tour_poitrine['XL'] = tour_poitrine_XL

    # Configuration du Choix
    choix_XS = fuzz.trapmf(choix_taille.universe, [0, 0, 19, 19])
    choix_S = fuzz.trapmf(choix_taille.universe, [20, 20, 39, 39])
    choix_M = fuzz.trapmf(choix_taille.universe, [40, 40, 59, 59])
    choix_L = fuzz.trapmf(choix_taille.universe, [60, 60, 79, 79])
    choix_XL = fuzz.trapmf(choix_taille.universe, [80, 80, 100, 100])
    choix_taille['XS'] = choix_XS
    choix_taille['S'] = choix_S
    choix_taille['M'] = choix_M
    choix_taille['L'] = choix_L
    choix_taille['XL'] = choix_XL


    # Configuration des règles
    choix_regles = ctrl.ControlSystem(definitionRegleChem())
    choisir = ctrl.ControlSystemSimulation(choix_regles)

    return choisir


def configurationPantalon():
    global hanche, longueur_jambe, choix_taille
    hanche, longueur_jambe = antecedant()[3], antecedant()[4]
    choix_taille = consequence()

     #configuration longueur de hanche
    hanche_XS = fuzz.trapmf(hanche.universe, [88, 88, 92, 93])
    hanche_S = fuzz.trapmf(hanche.universe, [92, 93, 96, 97])
    hanche_M = fuzz.trapmf(hanche.universe, [96, 97, 100, 101])
    hanche_L = fuzz.trapmf(hanche.universe, [100, 101, 104, 105])
    hanche_XL = fuzz.trapmf(hanche.universe, [104, 105, 108, 109])

    hanche['XS'] = hanche_XS
    hanche['S'] = hanche_S
    hanche['M'] = hanche_M
    hanche['L'] = hanche_L
    hanche['XL'] = hanche_XL

    #Configuration longueur de jambe
    longueur_jambe_XS = fuzz.trapmf(longueur_jambe.universe, [73, 74, 75, 76])
    longueur_jambe_S = fuzz.trapmf(longueur_jambe.universe, [75, 76, 77, 78])
    longueur_jambe_M = fuzz.trapmf(longueur_jambe.universe, [77, 78, 79, 80])
    longueur_jambe_L = fuzz.trapmf(longueur_jambe.universe, [79, 80, 81, 82])
    longueur_jambe_XL = fuzz.trapmf(longueur_jambe.universe, [81, 82, 83, 84])

    longueur_jambe['XS'] = longueur_jambe_XS
    longueur_jambe['S'] = longueur_jambe_S
    longueur_jambe['M'] = longueur_jambe_M
    longueur_jambe['L'] = longueur_jambe_L
    longueur_jambe['XL'] = longueur_jambe_XL

    # Configuration du Choix
    choix_XS = fuzz.trapmf(choix_taille.universe, [0, 0, 19, 19])
    choix_S = fuzz.trapmf(choix_taille.universe, [20, 20, 39, 39])
    choix_M = fuzz.trapmf(choix_taille.universe, [40, 40, 59, 59])
    choix_L = fuzz.trapmf(choix_taille.universe, [60, 60, 79, 79])
    choix_XL = fuzz.trapmf(choix_taille.universe, [80, 80, 100, 100])
    choix_taille['XS'] = choix_XS
    choix_taille['S'] = choix_S
    choix_taille['M'] = choix_M
    choix_taille['L'] = choix_L
    choix_taille['XL'] = choix_XL

    # Configuration des règles
    choix_regles = ctrl.ControlSystem(definitionReglePant())
    choisir = ctrl.ControlSystemSimulation(choix_regles)

    return choisir

def tailleVeste(tt_entry,tp_entry,td_entry):
    try:
        veste = configurationVest()
        veste.input['tour_taille'] = tt_entry
        veste.input['tour_poitrine'] = tp_entry
        veste.input['taille_dos'] = td_entry
        veste.compute()
        veste_taille = defuzzification(veste.output['choix_taille'])
        return veste_taille
    except :
        return None


def tailleChemise(tt_entry,tp_entry,td_entry,lm_entry):
    try:
        chemise = configurationChemise()
        chemise.input['tour_taille'] = tt_entry
        chemise.input['tour_poitrine'] = tp_entry
        chemise.input['taille_dos'] = td_entry
        chemise.input['longueur_manche'] = lm_entry
        chemise.compute()
        chemise_taille = defuzzification(chemise.output['choix_taille'])
        return chemise_taille
    except :
        return None

def taillePantalon(lj_entry,lh_entry):
    try:
        pantalon = configurationPantalon()
        pantalon.input['longueur_jambe'] = lj_entry
        pantalon.input['hanche'] = lh_entry
        pantalon.compute()
        pantalon_taille = defuzzification(pantalon.output['choix_taille'])
        return pantalon_taille
    except :
        return None
