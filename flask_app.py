import requests
from flask import Flask,json,render_template

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template("main_page.html",house_count=count_house(),senate_count=count_senate(),senateRCount=partyCount('R','Senate'),senateDCount=partyCount('D','Senate'),senateICount=partyCount('I','Senate'),HORRCount=partyCount('R','House'),HORDCount=partyCount('D','House'),HORICount=partyCount('I','House'))



@app.route('/congress/house/members/count')
def count_house():
    return len(get_members('House'))

@app.route('/congress/house/members')
def house_members():
    return str(get_members('House'))

@app.route('/congress/senate/members')
def senate_members():
    return str(get_members('Senate'))

@app.route('/congress/senate/members/count')
def count_senate():
    return len(get_members('Senate'))

@app.route('/test')
def countSenateRepublicans():
    return str(partyCount('R','Senate'))

def partyCount(party,branch):
    members= get_members(branch)
    currentPartyMembers = list(filter(lambda x: x['in_office'] == True and x['party'] == party, members))
    return len(currentPartyMembers)


def get_members(branch):
    url = 'https://api.propublica.org/congress/v1/115/'+branch+'/members.json'
    headers = {'X-API-Key': 'hiqnP0QhmhuWnLwxtllo2NmUf1irHPNdgZINhbjn'}
    membersRequest = requests.get(url, headers=headers)
    jsonToPython=json.loads(membersRequest.text)
    members=jsonToPython['results'][0]['members']
    return members
