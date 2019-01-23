# import json

# file_object = open('smartgrid_data.json', 'w' )

# data = {}
# data['key'] = 'value'
# json_data = json.dumps(data)

# file_object.write(json_data)

import json

file_object = open('smartgrid_data.json', 'w' )

data = {'reading':[], 'region':[], 'aggregator':[], 'neighborhood':[], 'house':[]}

data['reading'].append({'date': 'datetime.datetime(2019, 11, 30, 05, 37, 41.239789)', 
						'consumption': 8139, 
						'consumption_units': 'kWh',
						'temperature': 66, 
						'temperature_units': 'F', 
						'cost': 10, 
						'currency': 'USD', 
						'region': "Molestiae sapient", 
						'aggregator': "Molestiae sapient/Aspe",
						'neighborhood': "Molestiae sapient/Aspe/Expl",
						'house': "Molestiae sapient/Aspe/Expl/Aliquam magnam nam, mol"
						})

data['region'].append({'region':'Molestiae sapient'})

data['aggregator'].append({'region':'Molestiae sapient', 'aggregator': 'Aspe'})

data['neighborhood'].append({'region':'Molestiae sapient', 'aggregator': 'Aspe', 'neighborhood': 'Expl'})

data['house'].append({'region':'Molestiae sapient', 'aggregator': 'Aspe', 'neighborhood': 'Expl', 'house''Aliquam magnam nam, mol'})

json_data = json.dump(data, fp=file_object, indent=4, sort_keys=True, default=str)