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



