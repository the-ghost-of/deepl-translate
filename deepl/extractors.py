def extract_translated_sentences(json_response):
    translations = json_response["result"]["translations"]
    return [
        translation["beams"][0]["postprocessed_sentence"]
        for translation in translations
    ]


def extract_split_sentences(json_response):
    return json_response["result"]["splitted_texts"][0]
