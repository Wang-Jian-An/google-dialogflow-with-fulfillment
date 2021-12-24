from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillment = ""
    query_result = req.get("queryResult")
    if query_result.get("action") == "tomorrow_order_or_not":
        fulfillmentText = "You can order."
    return {
        "fulfillmentText":fulfillmentText,
        "source":"webhookdata"
    }

if __name__ == "__main__":
    app.run()