import re
import logging
import json
import nltk
from bs4 import BeautifulSoup
import azure.functions as func

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    html_body = req.params.get('html_body')
    if not html_body:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            html_body = req_body.get('html_body')

    if html_body:
        result = run(html_body)
        return func.HttpResponse(result, mimetype="application/json")
    else:
        return func.HttpResponse(
            "Please pass html_body in the query string or in the request body.",
            status_code=400
        )

def run(html_body):
    soup = BeautifulSoup(html_body, 'html.parser')
    sentence_dict = {}
    index = 0

    for div in soup.find_all("div"):
        for br in div.find_all("br"):
            br.replace_with(" ")
        
        text = div.get_text()
        sentences = nltk.sent_tokenize(text)

        for sentence in sentences:
            clean_sentence = re.sub(r'[^a-zA-Z0-9\s]', '', sentence)
            tokens = nltk.word_tokenize(clean_sentence)
            token_tags = nltk.pos_tag(tokens)
            tags = [x[1] for x in token_tags]

            if any([x[:2] == 'VB' for x in tags]) and any([x[:2] == 'NN' for x in tags]):
                sentence_dict[index] = clean_sentence
                index += 1

    return json.dumps(sentence_dict)
