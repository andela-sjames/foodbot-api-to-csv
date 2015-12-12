import requests

sample = requests.get('http://slack-foodbot.herokuapp.com/api/rating/',)

api_result = sample.json()
headers = 'DATE, RATE, COMMENT, DAY, FOOD, MEAL\n'


def readfile():
    return_string = []
    resp = ''
    for results in api_result['results']:
        return_string = [str(results['date']), str(results['rate']),
                         str(results['comment']), str(results['menu']['day']),
                         str(results['menu']['food']),
                         str(results['menu']['meal'])]

        resp += ', '.join(return_string) + '\n'
    return resp

with open("food.csv", "w") as outputfile:
    outputfile.write(headers)
    outputfile.write(readfile())
