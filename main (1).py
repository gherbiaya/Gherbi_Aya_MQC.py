#Pandas with (gherbi aya , (11/12/2025))
#for biology master tlemcen" 
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
print(df)