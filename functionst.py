
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def filter_complete_visit(df):
    """This functions checks if the visit ids have gone through 
    all the required process steps to count as a confirmed state"""
    all_steps = ['step_3', 'step_2', 'step_1', 'start', 'confirm']

    
    visit_check = df.groupby("visit_id")["process_step"].apply(lambda x:all((step in x.values for step in all_steps)))
    return visit_check[visit_check == True].index.tolist()
    
    
    
    
    
    
    
    
    
    
    
