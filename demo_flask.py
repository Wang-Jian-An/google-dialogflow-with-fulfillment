from datetime import datetime
from flask import Flask, request
import question_about_imbalanced_data_handle
import question_about_imbalanced_data_concept
import question_about_the_concept_of_transfer_learning
import query_text_store

app = Flask(__name__)

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillmentText = ""
    query_result = req.get("queryResult")
    text = query_result.get("queryText")
    query_text_store.store_text(text)
    if query_result.get("action") == "question_about_imbalanced_data_handle":
        fulfillmentText = question_about_imbalanced_data_handle.generate_answer_text()
    elif query_result.get("action") == "question_about_imbalanced_data_concept":
        fulfillmentText = question_about_imbalanced_data_concept.generate_answer_text()
    elif query_result.get("action") == "precision_equation":
        fulfillmentText = "Precision相關問題"
        with open("query_text_store_precision.txt", "r") as f:
            file = f.readlines()
    elif query_result.get("action") == "question_about_the_concept_of_transfer_learning":
        fulfillmentText = question_about_the_concept_of_transfer_learning.generate_answer_text()
    return {
        "fulfillmentText":fulfillmentText,
        "source":"webhookdata"
    }

if __name__ == "__main__":
    app.run()


