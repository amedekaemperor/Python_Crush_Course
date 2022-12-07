from survey import AnonymousSurvey

def test_store_single_response():
    language_survey = AnonymousSurvey("What language did you first learn to speak? ")
    language_survey.store_responses("ewe")
    assert 'ewe' in language_survey.responses