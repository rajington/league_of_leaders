from riotwatcher import RiotWatcher
from API_KEY import API_KEY

w = RiotWatcher(API_KEY)

# check if we have API calls remaining
print(w.can_make_request())

me = w.get_summoner(name='rajington')
print(me)

recent = w.get_match_history(summoner_id=me['id'])

for match in recent['matches']:
    print(match['participants'][0]['stats']['goldEarned'])
