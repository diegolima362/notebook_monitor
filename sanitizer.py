from typing import Dict
import parse_to_label as parser

classification_to_int: Dict[str, int] = {
    "Negligible": 1,
    "Minor": 2,
    "Serious": 3,
    "Critical": 4,
    "Catastrophical": 5,
}

int_to_classification: Dict[int, str] = {
    1: "Negligible",
    2: "Minor",
    3: "Serious",
    4: "Critical",
    5: "Catastrophical",
}

configuration_to_int: Dict[str, int] = {
    "BBNGeNIeHandler_Config1": 1,
    "BBNGeNIeHandler_Config2": 2,
    "BBNGeNIeHandler_Config3": 3,
}

int_to_configuration: Dict[int, str] = {
    1: "BBNGeNIeHandler_Config1",
    2: "BBNGeNIeHandler_Config2",
    3: "BBNGeNIeHandler_Config3",
}

drug_amount_to_int: Dict[str, int] = {
    "Low": 1,
    "Moderate": 2,
    "High": 3,
}

int_to_drug_amount: Dict[int, str] = {
    1: "Low",
    2: "Moderate",
    3: "High",
}

lockoutInterval_to_int: Dict[str, int] = {
    "Low": 1,
    "Medium": 2,
    "High": 3,
}

int_to_lockoutInterval: Dict[int, str] = {
    1: "Low",
    2: "Medium",
    3: "High",
}

o2_supplement_to_int: Dict[str, int] = {
    "None": 0,
    "Minimal": 1,
    "Medium": 2,
    "High": 3,
}

int_to_o2_supplement: Dict[int, str] = {
    0: "None",
    1: "Minimal",
    2: "Medium",
    3: "High",
}

weight_to_int: Dict[str, int] = {
    "Underweight": 1,
    "Normal": 2,
    "Overweight": 3,
    "Obesity_I": 4,
    "Obesity_II": 5,
    "Obesity_III": 6,
}

int_to_weight: Dict[int, str] = {
    1: "Underweight",
    2: "Normal",
    3: "Overweight",
    4: "Obesity_I",
    5: "Obesity_II",
    6: "Obesity_III",
}


def sanitize(d: dict, date=False, string=False):
    # monitor data
    if not string:
        d["classification"] = classification_to_int[d["classification"]]
        d["configuration"] = configuration_to_int[d["configuration"]]
        d["drugAmount"] = drug_amount_to_int[d["drugAmount"]]
        d["lockoutInterval"] = lockoutInterval_to_int[d["lockoutInterval"]]

    # context data
    d["takingOtherMedications"] = 1 if d["context"][0]["takingOtherMedications"] else 0
    d["o2Supplement"] = o2_supplement_to_int[d["context"][0]["o2Supplement"]]

    # history data
    d["apnea"] = 1 if d["history"][0]["apnea"] else 0
    d["riskAge"] = 1 if d["history"][0]["riskAge"] else 0
    d["weight"] = weight_to_int[d["history"][0]["weight"]]

    if d['configuration'] == 2 or d['configuration'] == 'BBNGeNIeHandler_Config2':
        if not string:
            del d['heartRate']
            del d['spo2']
        else:
            d['heartRate'] = 0
            d['spo2'] = 0
    elif d['configuration'] == 1 or d['configuration'] == 'BBNGeNIeHandler_Config1':
        if not string:
            del d['etCO2']
            del d['respirationRate']
        else:
            d['etCO2'] = 0
            d['respirationRate'] = 0

    # remove object datatype items
    del d["_id"]
    if not date:
        del d["date"]
    del d["patientContextId"]
    del d["history"]
    del d["context"]

    return d


def sanitize_naive_bayes(d: dict, date=False):
    # context data
    d["takingOtherMedications"] = 'yes' if d["context"][0]["takingOtherMedications"] else 'no'
    d["o2Supplement"] = d["context"][0]["o2Supplement"]

    # history data
    d["apnea"] = 'yes' if d["history"][0]["apnea"] else 'no'
    d["riskAge"] = 'yes' if d["history"][0]["riskAge"] else 'no'
    d["weight"] = d["history"][0]["weight"]

    if d['configuration'] == 'BBNGeNIeHandler_Config2':
        d['configuration'] = 'cfg_2'
        d['etCO2'] = parser.etco2_to_label(d['etCO2'])
        d['respirationRate'] = parser.rr_to_label(d['respirationRate'])

        d['heartRate'] = 'no_data'
        d['spo2'] = 'no_data'

    elif d['configuration'] == 'BBNGeNIeHandler_Config1':
        d['configuration'] = 'cfg_1'
        d['heartRate'] = parser.hr_to_label(d['heartRate'])
        d['spo2'] = parser.spo2_to_label(d['spo2'])

        d['etCO2'] = 'no_data'
        d['respirationRate'] = 'no_data'
    else:
        d['configuration'] = 'cfg_3'
        d['heartRate'] = parser.hr_to_label(d['heartRate'])
        d['spo2'] = parser.spo2_to_label(d['spo2'])
        d['etCO2'] = parser.etco2_to_label(d['etCO2'])
        d['respirationRate'] = parser.rr_to_label(d['respirationRate'])

    d['riskValue'] = parser.risk_to_label(d['riskValue'])

    # remove object datatype items
    del d["_id"]
    if not date:
        del d["date"]
    del d["patientContextId"]
    del d["history"]
    del d["context"]

    return d


def detailed_data(d: dict):
    # monitor data
    d["classification"] = int_to_classification[d["classification"]]
    d["configuration"] = int_to_configuration[d["configuration"]]
    d["drugAmount"] = int_to_drug_amount[d["drugAmount"]]
    d["lockoutInterval"] = int_to_lockoutInterval[d["lockoutInterval"]]

    # context data
    d["takingOtherMedications"] = d["takingOtherMedications"] == 1
    d["o2Supplement"] = int_to_o2_supplement[d["o2Supplement"]]

    # history data
    d["apnea"] = d["apnea"] == 1
    d["riskAge"] = ["riskAge"] == 1
    d["weight"] = int_to_weight[d["weight"]]

    return d
