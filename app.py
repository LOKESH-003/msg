from flask import Flask, request, jsonify
from twilio.rest import Client

app = Flask(__name__)

@app.route('/send_whatsapp_message', methods=['POST'])
def send_whatsapp_message():
    phone_number = request.form.get('phone_number')

    # Twilio credentials
    account_sid = 'ACb9195ee49a5fddf63130178973ed4185'
    auth_token = 'f3ab8a6c7674a31c55b57d6c4de6ce1c'  # Replace with your Twilio Auth Token
    client = Client(account_sid, auth_token)

    message_body = "Hello from your Flutter app! This is a test WhatsApp message."

    try:
        message = client.messages.create(
            body=message_body,
            from_='whatsapp:+14155238886',  # Your Twilio WhatsApp number
            to=f'whatsapp:{phone_number}'
        )
        print(f"WhatsApp message sent: {message.sid}")
        return jsonify({'status': 'Message sent'}), 200
    except Exception as e:
        print(f"Failed to send WhatsApp message: {e}")
        return jsonify({'status': 'Failed to send message'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
