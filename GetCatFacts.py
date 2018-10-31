import requests, json,time, urllib.request as urllib, datetime
from PIL import Image
from twilio.rest import Client

account_sid = 'AC1b4b3c094b29a01776c9d3026ea48b8d'
auth_token = 'b0c80c516be3a35d532f7936c8bd2337'

client = Client(account_sid, auth_token)

url = "https://cat-fact.herokuapp.com/facts/random?animal=cat&amount=1"
r = requests.get(url)
people = {}
data = json.loads(r.text)
print(data)
times = 0

people['JoelsGoogle'] = '+13253302734' 
people['Joel']        = '+13304856523'
people['Sara']        = '+12544318572'
people['Erik']        = '+12549793318'
people['Chloe']       = '+12544138684' 
# people['Sterling']    = '+16822296627' 
# people['Valeria']     = '+13253303239' 
people['Chris']       = '+17122024715' 
people['Rhett']       = '+12545927226' 
people['Diana']       = '+19034402010' 
people['Alex']       = '+13253560123' 

print(people)
while(1):
	for person in people:
		fact = data['text']
		
		t = datetime.datetime.time(datetime.datetime.now())
		if (t >= datetime.time(10,0)) and (t <= datetime.time(14,45)) and (times <= len(people)):
			message = client.messages.create(
				body = fact,
				from_= '+15153798158',
				to=people[person]
			)
			print (people[person])
			times += 1
				
		if t >= datetime.time(14,45):
			times = 0

		if times >= len(people):
			time.sleep(1500)







