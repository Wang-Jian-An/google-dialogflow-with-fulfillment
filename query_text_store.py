
def store_text(text):
    with open("query_text_store_precision_equation.txt", "a") as f:
        f.write(text + "\n")
    return

store_text("precision")