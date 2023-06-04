
import pandas as pd 

# getting the data from exfcel sheet
l1 = pd.read_excel('french_ligue_1_2022_2023.xlsx')

# sorting clubs using stadium names
ajaccio = l1[l1['stadium'] == 'Stade Francois Coty']
angers = l1[l1['stadium'] == 'Stade Raymond Kopa']
auxerre = l1[l1['stadium'] == 'Stade de l’Abbe-Deschamps']
brestois = l1[l1['stadium'] == 'Stade Francis-Le Ble']
clermont = l1[l1['stadium'] == 'Stade Gabriel Montpied']
lens = l1[l1['stadium'] == 'Stade Bollaert Delelis']
lille = l1[l1['stadium'] == 'Stade Pierre Mauroy']
lorient = l1[l1['stadium'] == 'Stade Yves Allainmat']
lyonnais = l1[l1['stadium'] == 'Groupama Stadium']
marseille = l1[l1['stadium'] == 'Velodrome']
monaco = l1[l1['stadium'] == 'Stade Louis II']
montpellier = l1[l1['stadium'] == 'Stade de la Mosson']
nantes = l1[l1['stadium'] == 'Stade de la Beaujoire']
nice = l1[l1['stadium'] == 'Allianz Riviera']
psg = l1[l1['stadium'] == 'Parc des Princes']
rennais = l1[l1['stadium'] == 'Roazhon Park']
reims = l1[l1['stadium'] == 'Stade Auguste-Delaune']
strasbourg = l1[l1['stadium'] == 'Stade de la Meinau']
toulouse = l1[l1['stadium'] == 'Stade de Toulouse']
troyes = l1[l1['stadium'] == 'Stade de l’Aube']


