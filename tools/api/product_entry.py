import json

import pip._vendor


class EntryHandler:

	def generate_entry(self):
		response = pip._vendor.requests.get(
			'https://ourfarms.herokuapp.com/apiRest/product/?format=json',
			auth=('GR1', 'gr1234567890')
		)

		if response.status_code != 200:
			return -1

		list_dic = json.loads(response.content.decode('utf-8'))
		return list_dic
