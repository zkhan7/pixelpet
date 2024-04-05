from twilio.rest import Client

account_sid = 'ACae2ba0cf82d4757541a081f987060921'
auth_token = 'd02f4bc67e4436af570dab11edeaedf1'
client = Client(account_sid, auth_token)

def sendSMS(type, data):
  if 10 <= data <= 50:
       message_body = "The temperature measured by RPi is {:.1f}°C. Pet likes the temperature.".format(data)
  else:
       message_body = "The temperature measured by RPi is {:.1f}°C. Pet hates the temperature.".format(data)
  message = client.messages.create(
   from_='+12513334882',
   body=message_body,
   to='+16476226132'
  )
  print("Message successfully sent!")
