import re
from calendar import isleap

def date_detection(date :str) -> bool:
    year_rejex=re.compile(r'(\d{4})')
    
    leap_year_rejex=re.compile(r'((([0-2][0-9]|30)/(0[469]|11))|(([0-2][0-9]|3[01])/(0[13578]|1[02])|([0-2][0-9])/(02)))/(\d{4})')
    non_leap_year_rejex=re.compile(r'((([0-2][0-9]|30)/(0[469]|11))|(([0-2][0-9]|3[01])/(0[13578]|1[02])|([0-2][0-8])/(02)))/(\d{4})')
    if isleap(int(year_rejex.search(date).group())):
        match_obj=leap_year_rejex.findall(date)
        if match_obj:
            return True
    else:
        match_obj=non_leap_year_rejex.findall(date)
        if match_obj:
            return True
    return False


date="29/04/2016"
print(date_detection(date))
