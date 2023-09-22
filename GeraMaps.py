import pandas as pd
import folium
from folium.plugins import MarkerCluster

maps = pd.read_excel('localizacoes.xlsx')
maps

mapa = folium.Map(
    location=[-29.713735225021466, -53.71281461789054],
    tiles="OpenStreetMap",
    zoom_start=12
)

iconeGabrieli = folium.features.CustomIcon('https://raw.githubusercontent.com/LeonardoFdSantos/map-gabrieli-tcc/main/Localizacao_Gabrieli.png',icon_size=(75,75), icon_anchor=(37.5, 72), popup_anchor=(0,-70))

folium.Marker(location= [-29.713735225021466, -53.71281461789054],
    popup="Prédio 26D - CCS - Terapia Ocupacional - UFSM",
    tooltip='Prédio 26D - CCS - Terapia Ocupacional - UFSM',
    icon=(iconeGabrieli)
    ).add_to(mapa)

for index, creche in maps.iterrows():
      folium.Marker(location= [creche['Latitude'], creche['Longetude']],
                  popup = str(creche['Localizacao']),
                  tooltip = str(creche['Localizacao']),
                  icon=(folium.features.CustomIcon('https://raw.githubusercontent.com/LeonardoFdSantos/map-gabrieli-tcc/main/Localizacao_Gabrieli.png',icon_size=(75,75), icon_anchor=(37.5, 72), popup_anchor=(0,-70)))).add_to(mapa)

mapa.save(outfile="index.html")