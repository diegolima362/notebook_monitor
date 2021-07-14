from typing import Mapping


def risk_to_label(value):
    if value >= 0 and value < 25:
        return 'Negligible'
    elif value >= 25 and value < 45:
        return 'Minor'
    elif value >= 45 and value < 65:
        return 'Serious'
    elif value >= 65 and value < 85:
        return 'Critical'
    elif value >= 85:
        return 'Catastrophic'
    else:
        return 'Value not defined'


def spo2_to_label(value):
    if value > 93:
        return 'Negligible'
    elif value > 90:
        return 'Minor'
    elif value > 84:
        return 'Serious'
    elif value > 74:
        return 'Critical'
    else:
        return 'Catastrophic'


def hr_to_label(value):
    if value > 49 and value < 101:
        return 'Negligible'
    elif (value > 44 and value < 51) or (value > 100 and value < 111):
        return 'Minor'
    elif (value > 39 and value < 46) or (value > 110 and value < 131):
        return 'Serious'
    elif (value > 34 and value < 40) or (value > 130 and value < 171):
        return 'Critical'
    elif value < 35 or value > 170:
        return 'Catastrophic'
    else:
        return 'Value not defined'


def rr_to_label(value):
    if value > 10 and value < 20:
        return 'Negligible'
    elif value == 10 or value == 20 or value == 21:
        return 'Minor'
    elif value == 8 or value == 9 or (value > 21 and value < 26):
        return 'Serious'
    elif value == 6 or value == 7 or (value > 25 and value < 36):
        return 'Critical'
    elif value < 6:
        return 'Catastrophic'
    else:
        return 'Value not defined'


def etco2_to_label(value):
    if value > 35 and value < 46:
        return 'Negligible'
    elif (value > 45 and value < 50) or (value > 30 and value < 35):
        return 'Minor'
    elif (value > 49 and value < 56) or (value > 24 and value < 31):
        return 'Serious'
    elif (value > 55 and value < 61) or (value > 20 and value < 26):
        return 'Critical'
    else:
        return 'Catastrophic'
