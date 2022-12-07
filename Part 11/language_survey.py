from survey import AnonymousSurvey

language_survey = AnonymousSurvey("What language did you first learn to speak? ")

language_survey.show_question()

while True:
    response = input("Language: ")
    if response.lower() == "quit":
        break
    language_survey.store_responses(response)

language_survey.show_results()