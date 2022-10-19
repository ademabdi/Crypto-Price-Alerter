# importing twilio
import twilio
import twilio.rest
from twilio.rest import Client
  
# Your Account Sid and Auth Token from twilio.com / console
account_sid = 'AC300cde4f76dca131da5733a026429c64'
auth_token = '5f555497025d3fd69a99bd9845762a11'
  
client = Client(account_sid, auth_token)
  
''' Change the value of 'from' with the number 
received from Twilio and the value of 'to'
with the number in which you want to send message.'''
message = client.messages.create(
                              from_='+14255417271',
                              body ='Hi guess who sent this message (Python)!!!',
                              to ='+14168364718'
                          )
  
print(message.sid)