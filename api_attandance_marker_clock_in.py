# importing the requests library 
import requests 

# api-endpoint 
host = "example"
email="example@example.com"
password="example"

def authToken(host,email,password):
	api_url = 'https://'+host+'.snaphrm.com/api/v1/auth/login'

	body = {"email":email,"password":password,"remember_me":"false"}
 
	headers = {'X-SNAPHRM-HOST':host+'.snaphrm.com'}
	r = requests.post(url = api_url, params = body,headers=headers) 

	data = r.json() 


	print(data['message'])
	print('') 
	return data['data']['token']

def clock_in(host,token):
	api_url = 'https://'+host+'.snaphrm.com/api/v1/attendance/clock-in'

	body = {"working_from": "home"}
 
	headers = {'X-SNAPHRM-HOST':host+'.snaphrm.com','Authorization':'Bearer '+token}
	r = requests.post(url = api_url, params = body,headers=headers) 

	data = r.json() 


	print(data)
	print('') 


print('Auto Clock-In SnapHRM') 
print('by github.com/4nkitd') 
print('') 

token = authToken(host,email,password)

clock_in(host,token)