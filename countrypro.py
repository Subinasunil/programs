# print total no of country details
import json

with open("country.json",encoding="utf-8") as f:
    data=json.load(f)
print(len(data))

# print lang of Ukraine

lang_ukraine=[lang["languages"] for lang in data if lang["name"]=="Ukraine"]
for lan in lang_ukraine[0]:
    print(lan["name"])
# print(lang_ukraine[0])

# print currency in china

currency_details=[cur["currencies"] for cur in data if cur["name"].startswith("Palestine")]
currency=[cur["name"]for cur in currency_details[0]]
print(currency)

# print population of india

india_popu=[p["population"] for p in data if p["name"]=="India"]
print(india_popu)
def get_country_data(country_name):
    return [country for country in data if country["name"].lower().startswith(country_name)]
country_data=get_country_data("india")
country_borders=country_data[0].get("borders")
print(country_data[0].get("border"))
sharing_borders=[ country.get("name") for country in data if country["alpha3Code"] in country_borders]
print(sharing_borders)
populated_country=max(data,key=lambda d:d.get("population"))
print(populated_country["name"])
low_pop=min(data,key=lambda d:d.get("population"))
print(low_pop["name"])





