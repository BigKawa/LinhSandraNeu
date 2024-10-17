
# Define Age Group (min: 17, max: 96)

def age_group(x):
    if x < 24:
        return "teens"
    elif x >= 24 and x < 34:
        return "young adults"
    elif x >= 34 and x < 44:
        return "adults"
    elif x >= 44 and x < 54:
        return "older adults"
    elif x >= 54 and x < 64:
        return "old adults"
    elif x >= 64 and x < 74:
        return "young senior"
    elif x >= 74 and x < 84:
        return "senior"
    else:
        return "old senior"
