print("hello")

#  ​import requests
#  headers = {
#    'Content-Type': 'application/json',
#    'Authorization': 'Bearer rT1NsCRn3HlFi8FA6P3nWwvFqbCi'
#  }
#  ​
#  payload = {
#      "BusinessShortCode": 174379,
#      "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjUxMTEyMTMxNjQ3",
#      "Timestamp": "20251112131647",
#      "TransactionType": "CustomerPayBillOnline",
#      "Amount": 1,
#      "PartyA": 254743942226,
#      "PartyB": 174379,
#      "PhoneNumber": 254743942226,
#      "CallBackURL": "https://mydomain.com/path",
#      "AccountReference": "CompanyXLTD",
#      "TransactionDesc": "Payment of X" 
#    }
#  ​
#  response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, data = payload)
#  print(response.text.encode('utf8'))