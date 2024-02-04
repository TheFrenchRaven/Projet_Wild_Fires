import pandas as pd
import numpy as np
import streamlit as st
# Librairie Sklearn nécessaires
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
# Modèle de classification que l'on va utiliser
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn import tree
clf = tree.DecisionTreeClassifier()

# Pour évaluer nos modèles
from sklearn.metrics import classification_report, accuracy_score, roc_curve, auc

# Pour afficher le(s) arbre(s) de décision ou dans notre forêt aléatoire
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Pour optimiser les performances de nos modèles
from sklearn.model_selection import GridSearchCV

# Chargeaons notre dataset
df = pd.read_csv("C:/Users/alexa/OneDrive/PowerBI/Projet_Wild_Fires/wildfire_base_clean.csv",
                 sep = ",", index_col = 'OBJECTID')


st.sidebar.title("Sommaire")



pages = ["Introduction au projet","Compréhension et manipulation des données","Pre-processing et feature engineering","Visualisations et Statistiques"]

page = st.sidebar.radio("Allez vers la page : ", pages)


if page == pages[0] :
    
     st.write("Introduction au projet" )
     
     st.write("Contexte d’insertion du projet dans votre métier. 1 Perfectionnement, 1 Curiosité personnelle et 3 Reconversions professionnelles." )
     
     st.write("Du point de vue technique.Majoritairement novices, nous apprenons au fur et à mesure des sprints et de l’état d’avancement du projet." )
     
     st.write("Du point de vue économique.Montée en compétences et opportunité d’un emploi d’avenir." )
     
     st.write("Du point de vue scientifique.3 membres du groupe travaillent déjà avec des données. 2 autres membres découvrent cet univers." )

elif page == pages[1]:
    
    st.write("Compréhension et manipulation des données")
    st.write("Quel(s) jeu(x) de donnée(s) avez-vous utilisé pour atteindre les objectifs de votre projet ?")
    st.write("Le lien initialement donné pour le projet était l’édition 4 de ce jeu de données qui est régulièrement mis à jour.")
    st.write("Nous avons décidé de travailler à partir de l’édition 6 du jeu de données")
    st.write("Voici la liste des jeux de données utilisés : ")
    
    
    
    st.dataframe(df.head())

