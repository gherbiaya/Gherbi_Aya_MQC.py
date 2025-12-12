print (" *****MQC , Master 01 , (11/12/2025***** ") 
print ("**** GROUPE MEMBRE ****")
print ("GHERBI Aya , chef de group")
print ("Ali salah")
print ("Grita nesrine")
print ("Benichou Abdelwaheb")
print ("Ben moumane yasmine")
print("\n","\n")


print("Gherbi aya""\n")
import pandas as pd

# Données : séquence ADN , longueur , pourcentage de GC "
data = {
    "séquence" : ["ATGCGTACGTA","GCTAGCTAGGCC","ATGCGCGTAAGT","TACGATCGTA","ATGAAAGGCTT","CGTACGTAGC","TTAACCGGAT"],
    "longueur" : [11,12,12,10,11,10,10],
    "pourcentage GC" : [50,66.67,58.33,40,40.45,60,50]
}
# création d'un dataframe (tableau pandas)
df =pd.DataFrame (data)
print("*****************création et affichage*****************")
"# Affichage du tableau"
print("tableau des séquences ADN :""\n")
print(df,"\n" "\n")


#1) opérations sur les tableaux :
print("*******opérations******","\n","\n")

#2) Sélecionner la colonne "longueur"
longueur = df["longueur"]
print(longueur, "\n" , "\n")
 
#3)filtration les dont la longueur est supérieur à 10
print("********** filtrage avec la longueur **********","\n")

filtred_df = df[df["longueur"] > 10]
print(filtred_df,"\n" , "\n")

#4) calculer la moyenne du pourcentage de GC avec 3 chiffres aprés la virgule
print("********** filtrege avec pourcentage % *********","\n")

average_GC = df["pourcentage GC"]. mean()
print(f"pourcentage moyen de GC : {average_GC:.3f}%","\n" , "\n")


print("ALI SALAH""\n")
# ALI SALAH

#5) Ajouter une colonne "categorie GC"
def categorize(gc):
    if gc > 55:
        return 'Riche'
    elif 45 <= gc <= 55:
        return 'Moyen'
    elif gc < 45:
        return 'Faible'
df['categorie GC'] = df["pourcentage GC"] .apply(categorize)
print ("\n Tableau avec Categorie GC:")
print(df , "\n" , "\n") 





print("Grita Nesrine""\n")
# Grita Nesrine

#6) ajouter une colone donnant le nombre de "G" dans chaque séquence 
df["nombre de G"] = df["séquence"].str.count("G") 
print("**** G) Nombre de G ajoutés *****")
print(df, "\n")



