from datetime import datetime
from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillmentText = ""
    query_result = req.get("queryResult")
    if query_result.get("action") == "imbalance_data_concept_question":
        fulfillmentText = "不平衡資料的問題"
    return {
        "fulfillmentText":fulfillmentText,
        "source":"webhookdata"
    }

if __name__ == "__main__":
    app.run()