from flask import Flask, jsonify, request
from services.scoreboard_service import get_match_scoreboard

app = Flask(__name__)

@app.route('/scoreboard/<match_id>', methods=['GET'])
def scoreboard(match_id):
    try:
        result = get_match_scoreboard(match_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
