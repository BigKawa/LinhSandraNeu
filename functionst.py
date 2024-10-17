
# Define Age Group 
def age_group(x):
    if x < 13:
        return "child"
    elif x < 21:
        return "teen"
    elif x < 65:
        return "adult"
    else:
        return "senior"