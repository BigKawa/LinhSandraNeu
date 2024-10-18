
# Define Age Group (min: 17, max: 96)

def age_group(x):
    if x < 24:
        return "teens"
    elif x < 34:
        return "young adults"
    elif x < 44:
        return "adults"
    elif x < 54:
        return "older adults"
    elif x < 64:
        return "old adults"
    elif x < 74:
        return "young senior"
    elif x < 84:
        return "senior"
    else:
        return "old senior"


# Define client tenure

def client_tenure(x):
    if x < 11:
        return "short term user"
    else:
        return "long term user"

