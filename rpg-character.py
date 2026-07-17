full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    # 1. Validate name type
    if not isinstance(name, str):
        return "The character name should be a string"
    
    # 2. Validate empty name
    if name == "":
        return "The character should have a name"
        
    # 3. Validate name length
    if len(name) > 10:
        return "The character name is too long"
        
    # 4. Validate spaces in name
    if " " in name:
        return "The character name should not contain spaces"
        
    # 5. Validate stats are integers
    # We check the type of each stat specifically to avoid boolean edge cases (since isinstance(True, int) is True)
    if type(strength) is not int or type(intelligence) is not int or type(charisma) is not int:
        return "All stats should be integers"
        
    # 6. Validate stats minimum value
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
        
    # 7. Validate stats maximum value
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
        
    # 8. Validate sum of points
    if (strength + intelligence + charisma) != 7:
        return "The character should start with 7 points"
        
    # 9. Build the visual representation string if all checks pass
    str_dots = (full_dot * strength) + (empty_dot * (10 - strength))
    int_dots = (full_dot * intelligence) + (empty_dot * (10 - intelligence))
    cha_dots = (full_dot * charisma) + (empty_dot * (10 - charisma))
    
    return f'{name}\nSTR {str_dots}\nINT{int_dots}\nCHA{cha_dots}'


print(create_character('ren', 4, 2, 1)) 
  