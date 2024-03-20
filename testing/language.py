from survey import AnonymousSurvey

question = 'What language did you first learn to speak?'
language_survey = AnonymousSurvey(question)

language_survey.show_question()
print('Enter q at anytime to quit')

while True:
    response = input('Language: ')
    if response == 'q':
        break
    language_survey.store_response(response)

print('Thank you to everyone who participated in the survey!')

language_survey.show_results()
