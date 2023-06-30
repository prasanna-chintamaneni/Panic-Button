from twilio.rest import Client
import keys
import geocoder

client = Client(keys.account_sid, keys.auth_token)

# Get the location coordinates of the 'from' phone number
from_number = keys.twilio_number  # Replace with your Twilio phone number
from_location = geocoder.ip('me').latlng  # Use geolocation to get the current user's coordinates

# Generate the Google Maps link
google_maps_link = f"https://maps.google.com/?q={from_location[0]},{from_location[1]}"

# Create the message with the location link
message_body = f"Hello Prasanna, how are you?\n\nHere's my location: {google_maps_link}"

# Send the message
message = client.messages.create(
    body=message_body,
    from_=keys.twilio_number,
    to=keys.my_phone_number
)

print(message.body)
