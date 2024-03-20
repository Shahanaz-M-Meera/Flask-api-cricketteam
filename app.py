from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data for cricketers and their teams
cricketers = {
    "Ricky Ponting": "Australia",
    "Rahul Dravid": "India",
    "Shane Bond": "New Zealand",
    "Craig Kieswetter": "England"
}

@app.route('/cricketer-team', methods=['GET'])
def get_cricketer_team():
    cricketer_name = request.args.get('name')
    if cricketer_name in cricketers:
        return jsonify({"name": cricketer_name, "team": cricketers[cricketer_name]})
    else:
        return jsonify({"error": "Cricketer is not in the database"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
