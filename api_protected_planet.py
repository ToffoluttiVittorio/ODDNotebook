import requests
import pandas as pd
import json

#url = 'https://api.protectedplanet.net/v3/countries/:FRA?token=0a694f50ddc7a276fccc40d80aa1556e&with_geometry=true'
#
#response = requests.get(url)
#data = response.json()
#
#print(data)

test = requests.get('https://api.protectedplanet.net/v3/countries/NAM?token=0a694f50ddc7a276fccc40d80aa1556e&page=10&with_geometry=false')

api_data = test.json()

#print(api_data)


def convert_json_to_csv(json_data, csv_filename='namibia.csv'):
    # Création d'un DataFrame pandas
    df = pd.DataFrame({
        'Name': [json_data['country']['name']],
        'ISO_3': [json_data['country']['iso_3']],
        'ID': [json_data['country']['id']],
        'PA_Land_Area': [json_data['country']['statistics']['pa_land_area']],
        'PA_Marine_Area': [json_data['country']['statistics']['pa_marine_area']],
        'Land_Area': [json_data['country']['statistics']['land_area']],
        'Percentage_PA_Land_Cover': [json_data['country']['statistics']['percentage_pa_land_cover']],
        'Percentage_PA_Marine_Cover': [json_data['country']['statistics']['percentage_pa_marine_cover']],
        'Marine_Area': [json_data['country']['statistics']['marine_area']],
        'Polygons_Count': [json_data['country']['statistics']['polygons_count']],
        'Points_Count': [json_data['country']['statistics']['points_count']],
        'OECM_Polygon_Count': [json_data['country']['statistics']['oecm_polygon_count']],
        'OECM_Point_Count': [json_data['country']['statistics']['oecm_point_count']],
        'Protected_Area_Polygon_Count': [json_data['country']['statistics']['protected_area_polygon_count']],
        'Protected_Area_Point_Count': [json_data['country']['statistics']['protected_area_point_count']],
        'Percentage_OECMs_PA_Marine_Cover': [json_data['country']['statistics']['percentage_oecms_pa_marine_cover']],
        'OECMs_PA_Land_Area': [json_data['country']['statistics']['oecms_pa_land_area']],
        'OECMs_PA_Marine_Area': [json_data['country']['statistics']['oecms_pa_marine_area']],
        'Percentage_OECMs_PA_Land_Cover': [json_data['country']['statistics']['percentage_oecms_pa_land_cover']],
        'Assessments': [json_data['country']['pame_statistics']['assessments']],
        'Assessed_PAs': [json_data['country']['pame_statistics']['assessed_pas']],
        'PAME_PA_Land_Area': [json_data['country']['pame_statistics']['pame_pa_land_area']],
        'PAME_Percentage_PA_Land_Cover': [json_data['country']['pame_statistics']['pame_percentage_pa_land_cover']],
        'PAME_PA_Marine_Area': [json_data['country']['pame_statistics']['pame_pa_marine_area']],
        'PAME_Percentage_PA_Marine_Cover': [json_data['country']['pame_statistics']['pame_percentage_pa_marine_cover']],
        'Pas_Count': [json_data['country']['pas_count']],
        'Pas_National_Count': [json_data['country']['pas_national_count']],
        'Pas_Regional_Count': [json_data['country']['pas_regional_count']],
        'Pas_International_Count': [json_data['country']['pas_international_count']],
        'Pas_With_IUCN_Category_Count': [json_data['country']['pas_with_iucn_category_count']],
        'Pas_With_IUCN_Category_Percentage': [json_data['country']['pas_with_iucn_category_percentage']],
        'Protected_Planet_Link': [json_data['country']['links']['protected_planet']],
        # ... Ajoutez d'autres attributs selon votre structure de données
    })

    # Ajout des données des designations dans le DataFrame
    for designation in json_data['country']['designations']:
        df[f'{designation["name"]} (Count)'] = [designation['pas_count']]
        df[f'{designation["name"]} (Percentage)'] = [designation.get('pas_percentage', None)]

    # Ajout des données des catégories IUCN dans le DataFrame
    for iucn_category in json_data['country']['iucn_categories']:
        df[f'{iucn_category["name"]} (Count)'] = [iucn_category['pas_count']]
        df[f'{iucn_category["name"]} (Percentage)'] = [iucn_category.get('pas_percentage', None)]

    # Ajout des données des gouvernances dans le DataFrame
    for governance in json_data['country']['governances']:
        df[f'{governance["name"]} (Count)'] = [governance['pas_count']]
        df[f'{governance["name"]} (Percentage)'] = [governance.get('pas_percentage', None)]

    # Enregistrement du DataFrame dans un fichier CSV
    df.to_csv(csv_filename, index=False)

#convert_json_to_csv(api_data)

geom = requests.get('https://api.protectedplanet.net/v3/countries/NAM?token=0a694f50ddc7a276fccc40d80aa1556e&page=10&with_geometry=true')

#print(geom.json())

def replace_apostrophe_with_double_quote(input_string):
    # Remplace ' par "
    modified_string = input_string.replace("'", '"')
    return modified_string

# Exemple d'utilisation
original_string = "{'type': 'Feature', 'properties': {'fill-opacity': 0.7, 'stroke-width': 0.05, 'stroke': '#40541b', 'fill': '#83ad35', 'marker-color': '#2B3146'}, 'geometry': {'type': 'Polygon', 'coordinates': [[[11.718, -28.959], [11.718, -16.951], [25.26, -16.951], [25.26, -28.959], [11.718, -28.959]]]}}"
modified_string = replace_apostrophe_with_double_quote(original_string)

print(f"Original : {original_string}")
print(f"Modifié : {modified_string}")

# Convertir la chaîne JSON en dictionnaire
dictionary_data = json.loads(modified_string)

# Afficher le dictionnaire résultant
#print(dictionary_data)


ulr_geojson_nam = 'https://api.protectedplanet.net/v3/protected_areas/search?tok  en=0a694f50ddc7a276fccc40d80aa1556e&marine=true&country=NAM&with_geometry=true'

