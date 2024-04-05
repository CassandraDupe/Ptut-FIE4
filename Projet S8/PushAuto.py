import requests
import json
import copy

api_url = "http://localhost:8081/capteur"
donnéesString='{"patient":"Jean-Guy CEMY","mesures":[{"jour":"2024-03-11","releves":[{"heure":"7:30:00","value":"95","unit":"mg/dL"},{"heure":"9:30:00","value":"145","unit":"mg/dL"},{"heure":"12:30:00","value":"99","unit":"mg/dL"},{"heure":"14:30:00","value":"112","unit":"mg/dL"},{"heure":"19:30:00","value":"75","unit":"mg/dL"},{"heure":"21:30:00","value":"164","unit":"mg/dL"},{"heure":"22:30:00","value":"150","unit":"mg/dL"}]}]}'
donnéesJson=json.loads(donnéesString)

while len(donnéesJson['mesures'][0]['releves'])!=0:
    temp=copy.deepcopy(donnéesJson)
    donnée=temp["mesures"][0]['releves'][0]
    for i in range (0, len(donnéesJson["mesures"][0]['releves'])-1):
        temp["mesures"][0]['releves'].pop()
        
    response = requests.post(api_url, json=temp)
    print(temp['mesures'][0]['releves'][0])
    for mesure in donnéesJson["mesures"]:
        for releve in mesure["releves"]:
            if "heure" in releve and releve["heure"] == temp["mesures"][0]['releves'][0]['heure']:
                mesure["releves"].remove(releve)