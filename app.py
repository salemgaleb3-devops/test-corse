from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return jsonify(
            message="Please subscribe, like, and comment on this video, TY!!!",
            status="success"
        )

    @app.route("/health")
    def health_check():
        return jsonify(status="healthy"), 200

    @app.errorhandler(404)
    def not_found(_):
        return jsonify(error="Route not found"), 404

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
