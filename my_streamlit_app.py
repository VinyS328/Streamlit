import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns
import plotly.express as px

st.title('Analyse du dataset Voiture')

# Import de la dataframe

df_voiture = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv',sep=',')



###################################
#### SIDE BAR ET RADIO BUTTON #####
###################################

## Obtenir la liste des regions
region = df_voiture['continent'].unique()

# Création d'un radio bouton

continent = ['All','US.','Europe.','Japan.']

region_f = st.sidebar.radio('Choisir votre filtre pour la region',continent)
 
if region_f == 'All':
    filtered_data = df_voiture
else:
    filtered_data = df_voiture.loc[df_voiture['continent'].str.contains(region_f)]
    
filtered_data
##########################
###### GRAPHIQUES#########
##########################

filtered_data1 = filtered_data.select_dtypes(include='number')

# création d'une heatmap fitrable

plt.subplots(figsize=(10,5))
st.subheader("Heatmap")
viz_correlation = sns.heatmap(filtered_data1.corr(), annot =True, center=0,cmap = sns.color_palette("vlag", as_cmap=True))
plt.xticks(rotation=45)
st.pyplot(viz_correlation.figure)


expander = st.expander("Analyse:")
expander.write(
    "En général nous voyons un forte corrélation positive entre les colonnes 'weigth lbs' et 'cubicinches' , mais aussi la colonne 'cylinders' et 'cubicinches'. "
    "Il y a aussi une forte corrélation négative entre les colonnes 'hp' et 'mpg'. Plus le vehicule est puissant plus il consomme de carburant"
)

# Création d'un scatterplot 

plt.subplots(figsize=(10,5))
st.subheader("Histogram")
viz_hist = sns.histplot(filtered_data1, x="weightlbs")

st.pyplot(viz_hist.figure)

expander = st.expander("Analyse:")
expander.write(
    "Aux US: nous voyons que la majorité des voitures ont un poids compris entre 2500 et 4600 lbs. "
    "En Europe: la majorité des voitures ont un poids compris entre 1800 et 2400 lbs. "
   "Au Japon: on compte 12 voitures ayant un poids entre 1950 et 2150 lbd mais en général,il y a des voitures de tout poids mais qui ne dépassent pas les 3000 lbs. "
    "On peut en conclure qu'au US, les voitures sont fidèles à leur image c'est à dire très imposantes et consommatrices en carburant. En europe les voitures sont quant à elles plus légères et au japon nous voyons que les poids des voitures ne dépasse pas les 3000 lbs qui peut faire penser qu'il y a beaucoup de petites voitures." 
)

#Creation d'un boxplot

plt.subplots(figsize=(10,5))
st.subheader("Boxplot")
viz_box = px.box(filtered_data1, x='hp')
st.plotly_chart(viz_box)
     
         
expander = st.expander("Analyse:")
expander.write(
"Aux US: nous avons 75% des voitures de ce dataset qui ont un hp inférieur à 150 et 25% des voitures qui ont un hp supérieure à 150. "
"En Europe: nous avons 75% des voitures de ce dataset qui ont un hp inférieur à 90.5 et 25% des voitures qui ont un hp supérieure à 90.5. "
"Au Japon: nous avons 75% des voitures de ce dataset qui ont un hp inférieur à 95 et 25% des voitures qui ont un hp supérieure à 95. "
"On peut en conclure que les voitures américaines sont plus puissance en terme de chevaux que les voiture Japonnaises ou européennes "   
)


