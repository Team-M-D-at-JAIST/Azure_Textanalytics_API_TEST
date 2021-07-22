key = "388c1df1197743a7bd965709e2161a2e"
endpoint = "https://new-defination.cognitiveservices.azure.com/"

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, credential=ta_credential)
    return text_analytics_client


client = authenticate_client()
#
#
# def sentiment_analysis_example(client):
#     documents = ["I had the best day of my life. I wish you were there with me."]
#     response = client.analyze_sentiment(documents=documents)[0]
#     print("Document Sentiment: {}".format(response.sentiment))
#     print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
#         response.confidence_scores.positive,
#         response.confidence_scores.neutral,
#         response.confidence_scores.negative,
#     ))
#     for idx, sentence in enumerate(response.sentences):
#         print("Sentence: {}".format(sentence.text))
#         print("Sentence {} sentiment: {}".format(idx + 1, sentence.sentiment))
#         print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
#             sentence.confidence_scores.positive,
#             sentence.confidence_scores.neutral,
#             sentence.confidence_scores.negative,
#         ))
#
#
# sentiment_analysis_example(client)
#
#
#
# def entity_recognition_example(client):
#     try:
#         documents = ["I had a wonderful trip to Seattle last week."]
#         result = client.recognize_entities(documents=documents)[0]
#
#         print("Named Entities:\n")
#         for entity in result.entities:
#             print("\tText: \t", entity.text, "\tCategory: \t", entity.category, "\tSubCategory: \t", entity.subcategory,
#                   "\n\tConfidence Score: \t", round(entity.confidence_score, 2), "\n")
#
#     except Exception as err:
#         print("Encountered exception. {}".format(err))
#
#
# entity_recognition_example(client)
#
#
# def entity_linking_example(client):
#     try:
#         documents = ["""駅から滝まではどのぐらいの時間がかかるんですか"""]
#         result = client.recognize_linked_entities(documents=documents)[0]
#
#         print("Linked Entities:\n")
#         for entity in result.entities:
#             print("\tName: ", entity.name, "\tId: ", entity.data_source_entity_id, "\tUrl: ", entity.url,
#                   "\n\tData Source: ", entity.data_source)
#             print("\tMatches:")
#             for match in entity.matches:
#                 print("\t\tText:", match.text)
#                 print("\t\tConfidence Score: {0:.2f}".format(match.confidence_score))
#
#     except Exception as err:
#         print("Encountered exception. {}".format(err))
#
#
# entity_linking_example(client)


def key_phrase_extraction_example(client):
    try:
        documents = [{
        "id": "1",
        "language": "ja",
        "text": """最寄り駅からどのくらいかかるかは知りたいです。"""
    }]

        response = client.extract_key_phrases(documents=documents)[0]

        if not response.is_error:
            print("\tKey Phrases:")
            for phrase in response.key_phrases:
                print("\t\t", phrase)
        else:
            print(response.id, response.error)

    except Exception as err:
        print("Encountered exception. {}".format(err))


key_phrase_extraction_example(client)