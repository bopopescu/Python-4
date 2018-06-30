import requests

# response = requests.get("http://delhihighcourt.nic.in/case.asp")
# print(response.text)

"""url = "http://delhihighcourt.nic.in/dhc_case_status_list_new.asp"
data = {"sno":2,"party":"Rahul","pyear":2018}
response = requests.post(url=url,data=data)

print(response.text)"""

response = requests.get("https://twitter.com/dna")
