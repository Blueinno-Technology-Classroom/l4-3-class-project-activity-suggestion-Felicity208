
########################### Template Code ################################
# Import the libraries to make HTTP requests
import requests
from pprint import pprint

# You don't need to understand how this function works for now
def get_activity(preference=None) -> dict:
    if preference is None:
        url = "https://bored.api.lewagon.com/api/activity/"
        url = "https://bored.api.lewagon.com/api/activity/"
    else:
        url = f"https://bored.api.lewagon.com/api/activity?type={preference}"

    response = requests.get(url)
    return response.json()
########################################################################
print("Don't know what to do? Pick a number below and I will suggest something for you:  0: education  1: recreational  2: social  3: diy  4: charity  5: cooking  6: relaxation  7: music  8: busywork 9: no preference")
activity = input()

if activity == 9:
    resp_dict1 = get_activity()
if activity == 0:
    resp_dict1 = get_activity("education")
if activity == 1:
    resp_dict1 = get_activity("recreational")
if activity == 2:
    resp_dict1 = get_activity("social")
if activity == 3:
    resp_dict1 = get_activity("diy")
if activity == 4:
    resp_dict1 = get_activity("charity")
if activity == 5:
    resp_dict1 = get_activity("cooking")
if activity == 6:
    resp_dict1 = get_activity("relaxation")
if activity == 7:
    resp_dict1 = get_activity("music")
if activity == 8:
    resp_dict1 = get_activity("busywork")
print(f"You may {resp_dict1['activity']}?")
if resp_dict1['link'] != "":
    print(f"This could be helpful {resp_dict1['link']}")
########################### Example Code #################################
# calling get_activity without parameter
#resp_dict1 = get_activity()
#pprint(resp_dict1)

# calling get_activity with parameter
#resp_dict2 = get_activity('music')
#pprint(resp_dict2)
########################################################################



