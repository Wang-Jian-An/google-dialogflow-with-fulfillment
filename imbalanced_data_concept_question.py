import pandas as pd

def generate_answer_text():
    qa_data = pd.read_csv("Cupoy_QA問答集_不平衡資料.csv")

    answer_text = "使用者你好，在網路上有專家為您解答您的問題囉，在此附上連結，並建議您參考以下資訊："
    # for one_row in range(qa_data.shape[0]):
    #     answer_text = answer_text + "主題：" + qa_data.loc[one_row, "QA主題"] + "參考連結：" + qa_data.loc[one_row, "QA連結"]
    return answer_text