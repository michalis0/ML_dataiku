
from flask import Flask, render_template, jsonify, request
from transformers import AutoModelForSequenceClassification, AutoTokenizer

app = Flask(__name__)

model_name = './tiny'
label2id = {
    "A1": 0,
    "A2": 1,
    "B1": 2,
    "B2": 3,
    "C1": 4,
    "C2": 5
}

id2label = {
    0: "A1",
    1: "A2",
    2: "B1",
    3: "B2",
    4: "C1",
    5: "C2"
}

model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=6, id2label=id2label, label2id=label2id)
tokenizer = AutoTokenizer.from_pretrained(model_name)


def preprocess_function(string):
    model_inputs = tokenizer([string], truncation=True, return_tensors='pt')
    return model_inputs


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        string = request.form.get('text_input')  # Get the user input from the form
        inputs = preprocess_function(string)
        result = model(**inputs)

        predictions = result.logits.argmax().item()
        predicted_label = id2label[predictions]

        return jsonify({'predicted_label': predicted_label})

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)

