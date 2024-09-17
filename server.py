from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
	# This is your healthcheck endpoint, returning a JSON response with a status message.
	return jsonify({"status": "Memory backend service is running"}), 200

if __name__ == '__main__':
	# You can run the server in debug mode to catch any errors during development.
	app.run(debug=True)
