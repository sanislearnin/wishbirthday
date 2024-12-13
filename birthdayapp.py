from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

# Define the file name
file_name = "birthday_wishes.csv"

# Define the headers for the CSV file
headers = ["Name", "Message Length", "Tone", "Gift Given"]

# Ensure the CSV file has headers if it doesn't exist
if not os.path.exists(file_name):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

@app.route('/add_wish', methods=['POST'])
def add_wish():
    data = request.json

    # Extract data from the JSON payload
    name = data.get('name', '').strip()
    message = data.get('message', '').strip()
    tone = data.get('tone', '').strip()
    gift = "Yes" if data.get('gift', '').lower() == 'yes' else "No"

    # Calculate message length
    message_length = len(message)

    # Append the data to the CSV file
    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([name, message_length, tone, gift])

    return jsonify({"message": "Wish saved successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
