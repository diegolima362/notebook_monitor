from typing import Dict

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


def sanitize(d: dict):
    # monitor data
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
    
    if d['configuration'] == 2:
        del d['heartRate']
        del d['spo2']
    elif d['configuration'] == 1:
        del d['etCO2']
        del d['respirationRate']

    # remove object datatype items
    del d["_id"]
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
