import json
import requests
import pprint
import tablib


r = requests.get(
    "https://api.tatts.com/sales/vmax/web/data/racing/2017/09/16/SR/full")
pp = pprint.PrettyPrinter(indent=2)
data = r.json()
# pp.pprint(data
# attrs = ['Number','NameForm','TrackRating','Distance']
# for item in data["RaceDay"]['Meetings'][0]:
#     for att in attrs:
#         print(item[att])

# pp.pprint(data["RaceDay"]['Meetings'][0]['Races'][0]['FixedPriceSummary']['FixedPrices'][0]['MeetingId'])
# pp.pprint(data["RaceDay"]['Meetings'][0]['Races'][0]['RacingFormGuide']['Event']['Race'])
# ['Runners']['RacingFormGuide'])

raceItems = ['Name', 'Number', 'Distance']

raceData = []

for item in data["RaceDay"]['Meetings'][0]['Races']:
    raceDetails = item['RacingFormGuide']['Event']['Race']
    raceData.append((raceDetails['Name'],raceDetails['Number'],raceDetails['Distance']))
    # raceData.extend(raceDetails['Name'],raceDetails['Number'],raceDetails['Distance'])

data = tablib.Dataset(*raceData, headers=raceItems)

print(data)
# print(raceData)
# headers = ('Name', 'Number', 'Distance')
# data = (raceDetails['Name'],raceDetails['Number'],raceDetails['Distance'])
# data = tablib.Dataset(*data, headers=headers)


    # print("Race called {0} over {1} and its race number {2}.".format(raceDetails['Name'],
    #                                                                  raceDetails['Distance'],
    #                                                                  raceDetails['Number']))
