# importing the requests library 
import requests 
import psycopg2

# api-endpoint 
URL = "GRAPHQL_URL"

email = "testpairgamming@yopmail.com"
phone = "+62812288291240"

query = '''
mutation {
  signUpCompanyTest(input: {
     email: "''' + email + '''"
     companyName: "PT. Testing Programming"
     password: "DATABASE_PW"
     phoneNumber: "''' + phone + '''"
     role: "transporter"
  }) {
     body
     statusCode
  }
}
'''

r = requests.post(URL, json={'query': query})
if r.status_code == 200:
    print('Request Success!')
    data = r.json()
    if "errors" in data:
        print(data['errors'][0]['message'])
    else:    
        print(data['data'])
else:
    print('Request Error!')

host="DATABASE_HOST"
dbname="DATABASE_NAME"
user="DATABASE_USER"
password="DATABASE_PASSWORD"
conn = psycopg2.connect(host=host, database=dbname, user=user, password=password)
cur = conn.cursor()

query = """
select * from users
where phone_number = '""" + phone + """'
and email = '""" + email + """';
"""

cur.execute(query)

query = " delete from users where phone_number = '" + phone + "';"

cur.execute(query)
conn.commit()

cur.close()
conn.close()