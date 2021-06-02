import json

labels = "C:/Users/felix/OneDrive/Bureau/test/out/dataset_preparation/META/labels.json"
sizes = "C:/Users/felix/OneDrive/Bureau/test/out/dataset_preparation/META/sizes.json"
nb_apparition_2018 = {'nb_parcelles': 0}
nb_apparition_2019 = {}
nb_apparition_2020 = {}
small_parcels = {}
with open(labels) as f:
    data = json.load(f)
    for key, value in data['CODE9_2018'].items():
        nb_apparition_2018['nb_parcelles'] += 1
        if value in nb_apparition_2018:
            nb_apparition_2018[value] += 1
        else:
            nb_apparition_2018[value] = 0

    for key, value in data['CODE9_2019'].items():
        if value in nb_apparition_2019:
            nb_apparition_2019[value] += 1
        else:
            nb_apparition_2019[value] = 0

    for key, value in data['CODE9_2020'].items():
        if value in nb_apparition_2020:
            nb_apparition_2020[value] += 1
        else:
            nb_apparition_2020[value] = 0

with open('C:/Users/felix/OneDrive/Bureau/test/out/dataset_preparation/META/stats/nb_apparition_2018.json',
          'w') as file:
    file.write(json.dumps(nb_apparition_2018, indent=4))
with open('C:/Users/felix/OneDrive/Bureau/test/out/dataset_preparation/META/stats/nb_apparition_2019.json',
          'w') as file:
    file.write(json.dumps(nb_apparition_2019, indent=4))
with open('C:/Users/felix/OneDrive/Bureau/test/out/dataset_preparation/META/stats/nb_apparition_2020.json',
          'w') as file:
    file.write(json.dumps(nb_apparition_2020, indent=4))

with open(sizes) as f:
    data = json.load(f)
    for key, value in data.items():
        if value < 50:
            small_parcels[key] = value

with open('C:/Users/felix/OneDrive/Bureau/test/out/dataset_preparation/META/stats/small_parcels.json',
          'w') as file:
    file.write(json.dumps(small_parcels, indent=4))
