from flask import Flask, jsonify, request
import logging
import redis

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

# Redis connection setup
###TODO: load credentials securely from an ENV var before public release
REDIS_URL = 'redis://default:AefTAAIjcDExMDY1YjFiYmRjNGY0MzM0YjM5OGIzY2E4ZmZjNTk0MnAxMA@thorough-kangaroo-59347.upstash.io:6379'
redis_client = redis.StrictRedis.from_url(REDIS_URL, decode_responses=True)

def compute_meta():
	pass
	# stub - static in DB for now

def to_llm_english():
	pass
	# stub - will dress up records returned in proper English

@app.route('/health', methods=['GET'])
def health_check():
	return jsonify({"status": "Memory backend service is running"}), 200

@app.route('/memories/<string:application>/<string:namespace>/', methods=['GET'])
def get_memories(application, namespace):
	# UUID is hardcoded for now
	###TODO: extract from future oauth2 headers
	UUID = '807193e7-8104-4759-bdd5-dbcf96974e84'

	redis_key = f"{UUID}_{application}_{namespace}"

	#Fetch memories
	memories = redis_client.lrange(redis_key, 0, -1)

	if not memories:
		logging.debug(f"No memories found under namespace {redis_key}")
		return jsonify({"memories": []}), 200

	# Return the list of memories as JSON
	logging.debug(f"Found memories for under namespace {redis_key}")
	return jsonify({"memories": memories}), 200

if __name__ == '__main__':
	# You can run the server in debug mode to catch any errors during development.
	app.run(debug=True)
