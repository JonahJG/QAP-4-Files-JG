def ValDigOnly(Value):
    # Validate for digits only
    IsValid = True
    if Value.isdigit() == False:
        IsValid = False
    elif len(Value) != 10:
        IsValid = False
    return IsValid

def ValPostal(Value):
    # Validate the postal code in the form L0L0L0
    IsValid = True
    if Value[0].isalpha() == False or Value[1].isdigit() == False or Value[2].isalpha() == False:
        IsValid = False
    elif len(Value) != 6:
        IsValid = False
    return IsValid