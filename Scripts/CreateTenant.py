import requests

url = "http://192.168.10.1/api/node/mo/uni/tn-testtenant.json"

payload = "{\r\n\t\"fvTenant\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-testtenant\",\r\n\t\t\t\"name\": \"testtenant\",\r\n\t\t\t\"rn\": \"tn-testtenant\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}"
cookie = {"APIC-cookie": "0a8sUgNVtPlJfDuV7+pPSLvIT0oAT7xOSSoUuATE6iLSk0lG8iPjp6xqTu4nXjYuSNqVaSnz45170a8VzjNSCJPJAsShHXOuuQAjjTqsc4bn2dATH+wq2e51+2G2zGajHrQzWrXYHsadS/0aaYEyHbdOBPGCOVtrgW9m9bInqwg="}
response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)
