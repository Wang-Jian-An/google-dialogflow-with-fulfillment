from datetime import datetime
from flask import Flask, request
import imbalanced_data_concept_question
import question_about_the_concept_of_transfer_learning

app = Flask(__name__)

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillmentText = ""
    query_result = req.get("queryResult")
    if query_result.get("action") == "imbalance_data_concept_question":
        fulfillmentText = imbalanced_data_concept_question.generate_answer_text()
    elif query_result.get("action") == "precision_equation":
        fulfillmentText = "Precision相關問題"
    elif query_result.get("action") == "question_about_the_concept_of_transfer_learning":
        fulfillmentText = question_about_the_concept_of_transfer_learning.generate_answer_text()
    return {
        "fulfillmentText":fulfillmentText,
        "source":"webhookdata"
    }

if __name__ == "__main__":
    app.run()