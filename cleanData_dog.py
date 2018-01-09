import csv
__author__ = 'Shih-Ting Huang', 'Wei-Yao Ku'

"""
CSCI-630: Final Project
Author: Shih-Ting Huang (sh3964), Wei-Yao Ku(wxk6489)

re-define variables
"""


def intakeType(var):
    """
    re-category intake type into 6 types
    :param var: original type
    :return: new type
    """
    dead = ['ET REQUES', 'EUTH REQ', 'DISPOSAL']
    takeover = ['CONFISCAT', 'EVACUEE', 'INVESTIGAT']
    temporary = ['FOR TRANSP', 'TRANSFER']
    medical = ['MED OBSERV', 'OUTSURGERY', 'QUARANTINE']
    street = ['FOUND', 'KHS', 'LOST', 'STRAY']
    abandon = ['OWNER SUR', 'RETURN', 'FOSTER']
    if var in dead:
        return 'DEAD'
    elif var in takeover:
        return 'TAKEOVER'
    elif var in temporary:
        return 'TEMPORARY'
    elif var in medical:
        return 'MEDICAL'
    elif var in street:
        return 'STREET'
    elif var in abandon:
        return 'ABANDON'
    else:
        return 'OTHER'


def primaryColor(var):
    """
    re-category color type.
    :param var: original color
    :return: new color
    """
    color = ['BLACK', 'BROWN', 'WHITE', 'TAN', 'TRICOLOR', 'RED', 'GRAY', 'BLUE', 'YELLOW', 'CHOCOLATE', 'FAWN',
             'CREAM', 'GOLD', 'BUFF', 'SILVER', 'SABLE', 'APRICOT']
    var = var.split()
    if len(var) > 1:
        mark = 'mark'
    else:
        mark = 'no_mark'

    if len(var) > 0:
        if var[0] in color:
            return var[0], mark
        else:
            return 'OTHER', mark
    else:
        return 'UNKNOWN', 'UNKNOWN'


def primaryBreed(var):
    """
    re-category breed type
    :param var: original breed
    :return: new breed
    """
    breed = ['PIT BULL TERRIER', 'LABRADOR RETRIEVER', 'GERMAN SHEPHERD DOG', 'BEAGLE', 'BOXER',
             'CHIHUAHUA - SMOOTH COATED', 'AMERICAN PIT BULL TERRIER', 'ROTTWEILER', 'CHOW CHOW',
             'BORDER COLLIE', 'SHIH TZU', 'JACK RUSS TER', 'SIBERIAN HUSKY', 'POODLE - MINIATURE',
             'YORKSHIRE TERRIER', 'COCKER SPANIEL', 'AUSTRALIAN SHEPHERD', 'DACHSHUND',
             'GOLDEN RETRIEVER', 'POMERANIAN']
    if var in breed:
        return var
    else:
        return 'OTHER'


def outcomeAsilomarStatus(var):
    """
    re-category outcomeAsilomarStatus
    :param var: original outcomeAsilomarStatus
    :return: new outcomeAsilomarStatus
    """
    if var == 'HEALTHY':
        return 'HEALTHY'
    elif var == 'TREATABLE/MANAGEABLE':
        return 'TREATABLE/MANAGEABLE'
    elif var == 'UNHEALTHY/UNTREATABLE':
        return 'UNHEALTHY/UNTREATABLE'
    else:
        return 'unknown'


def gender(var):
    """
    re-category gender
    :param var: original gender
    :return: new gender
    """
    male = ['MALE', 'NEUTERED MALE']
    female = ['FEMALE', 'SPAYED FEMALE']
    if var in male:
        return 'MALE'
    elif var in female:
        return 'FEMALE'
    else:
        return 'unknown'


def reproductiveStatusAtOutcome(var):
    """
    re-category reproductiveStatusAtOutcome
    :param var: original reproductiveStatusAtOutcome
    :return: new reproductiveStatusAtOutcome
    """
    if var == 'ALTERED':
        return 'ALTERED'
    elif var == 'FERTILE':
        return 'FERTILE'
    else:
        return 'unknown'


def stayTime(inDate, outDate):
    """
    Caculate stay in shelter time
    :param inDate: intake date
    :param outDate: outcome date
    :return: stay time category
    """
    if inDate is '' or outDate is '':
        return 'unknown'
    else:
        intake_date, intake_time = inDate.split()
        in_yyyy, in_mm, in_dd = intake_date.split('-')
        outcome_date, outcome_time = outDate.split()
        out_yyyy, out_mm, out_dd = outcome_date.split('-')
        if intake_date == outcome_date:
            return '<1 day'
        else:
            days = abs(
                (int(out_yyyy) - int(in_yyyy)) * 365 + (int(out_mm) - int(in_mm)) * 30 + int(out_dd) - int(in_dd))
            if days <= 180:
                return '1-0.5y'
            elif days <= 700:
                return '0.5-2y'
            else:
                return '>2y'


def age(DOB, outDate):
    """
    Caculate age
    :param DOB: birthday
    :param outDate: outcome date
    :return: age category
    """
    if DOB is '' or outDate is '':
        return 'UNKNOWN'
    else:
        intake_date, intake_time = DOB.split()
        in_yyyy, in_mm, in_dd = intake_date.split('-')
        outcome_date, outcome_time = outDate.split()
        out_yyyy, out_mm, out_dd = outcome_date.split('-')
        days = abs((int(out_yyyy) - int(in_yyyy)) * 365 + (int(out_mm) - int(in_mm)) * 30 + int(out_dd) - int(in_dd))
        if days <= 90:
            return 'PUPPY'
        elif days <= 365:
            return 'YOUNG'
        elif days <= 2555:
            return 'ADULT'
        else:
            return 'OLD'


def outcome(out_type):
    """
    re-category outcome into binary (1: adopted, 0: others)
    :param out_type: original outcome type
    :return: new outcome label
    """
    if out_type == 'ADOPTION':
        return '1'
    else:
        return '0'


def main():
    """
    The main function.
    Read in file.
    Re-category wanted variables.
    Output result.
    :return: None
    """
    i = 0
    data = []
    with open('dog.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if i is 0:
                row[4] = 'PrimaryColor'
                row[5] = 'ColorMark'
                row[2] = 'StayTime'
                row[10] = 'Age'
                row[11] = 'ReproductiveStatus'  # at outcome
                row[12] = 'AsilomarStatus'      # at outcome
                row[13] = 'Outcome'
                data.append(row[2:])
                i += 1
            else:
                row[2] = stayTime(row[2], row[15])
                row[3] = intakeType(row[3])
                row[4], row[5] = primaryColor(row[5])
                row[6] = primaryBreed(row[6])
                row[7] = 'no' if len(row[7]) is 0 else 'MIX'    # SecondaryBreed
                row[8] = gender(row[8])
                row[9] = 'no' if len(row[9]) is 0 else 'MIX'    # SecondaryColor
                row[10] = age(row[10], row[15])
                row[11] = reproductiveStatusAtOutcome(row[21])
                row[12] = outcomeAsilomarStatus(row[20])
                row[13] = outcome(row[16])
                data.append(row[2:])

    with open('DOG_data.csv', "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for i in range(len(data)):
            writer.writerow(data[i][:12])


if __name__ == '__main__':
    main()
