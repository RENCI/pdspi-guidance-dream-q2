import os
import requests

from api.utils import generate_time_series_data


pds_host = os.getenv("PDS_HOST", "localhost")
pds_port = os.getenv("PDS_PORT", "8080")
pds_version = os.getenv("PDS_VERSION", "v1")

config = {
    "title": "COVID guidance",
    "piid": "pdspi-guidance-dream-q2",
    "pluginType": "g",
    "settingsDefaults": {
            "pluginSelectors": [ {
            "title": "COVID",
            "id": "PDS:covid",
                "selectorValue": {
                "value": "PDS:covid:treatment",
                "title": "Treatment" }
        },
        {
            "title": "COVID",
            "id": "PDS:covid",
            "selectorValue": {
                "value": "PDS:covid:resource",
                "title": "Resource" }
        } ],
        "modelParameters": [
        {
         "id": "pdspi-guidance-dream-q2:loc",
         "title": "Hospital location (State)",
         "parameterDescription": "Please choose a state to indicate the hospital location for which you would like to get triage guidance.",
         "parameterValue": { "value": "NC" },
         "legalValues": {
            "type": "string",
            "enum": ["NC","NY","PA","SC","VA"]}
        }],
        "patientVariables": [ {
            "id": "LOINC:30525-0",
            "title": "Age",
            "legalValues": { "type": "number", "minimum": "0" },
            "group": "Profile",
            "why": "Age is used to assess patient risk for COVID."
        }, {
            "id": "LOINC:21840-4",
            "title": "Sex",
            "legalValues": { "type": "string", "enum": ['female', 'male'] },
            "group": "Profile",
            "why": "Sex is used to assess patient risk for COVID."
        }, {
            "id": "LOINC:39156-5",
            "title": "BMI",
            "group": "Profile",
            "legalValues": { "type": "number", "minimum": "0" },
            "why": "BMI is used to assess patient risk for COVID."
        }, {
            "id": "LOINC:LP21258-6",
            "title": "Oxygen saturation",
            "group": "Profile",
            "legalValues": { "type": "number", "minimum": "0" },
            "why": "Oxygen saturation is used to assess patient risk for COVID."
        }, {
            "id": "LOINC:56799-0",
            "title": "Address",
            "group": "Profile",
            "legalValues": { "type": "string" },
            "why": "Address of the patient's residence is used to assess patient risk for COVID."
        }, {
            "id": "LOINC:LP172921-1",
            "title": "Cardiovascular disease",
            "group": "Pre-existing Condition",
            "legalValues": { "type": "boolean" },
            "why": "cardiovascular disease pre-existing condition is used to assess patient risk for COVID."
        }, {
            "id": "LOINC:54542-6",
            "title": "Pulmonary disease",
            "group": "Pre-existing Condition",
            "legalValues": { "type": "boolean" },
            "why": "pulmonary disease pre-existing condition is used to assess patient risk for COVID."
        }, {
            "id": "LOINC:LP128504-0",
            "title": "Autoimmune disease",
            "group": "Pre-existing Condition",
            "legalValues": { "type": "boolean" },
            "why": "Autoimmune disease pre-existing condition is used to assess patient risk for COVID."
        }, {
            "id": "LOINC:45701-0",
            "title": "Fever",
            "legalValues": { "type": "boolean"},
            "group": "Symptom",
            "why": "Fever is one major symptom of COVID"
        }, {
            "id": "LOINC:LP212175-6",
            "title": "Date of fever onset",
            "legalValues": { "type": "string"},
            "group": "Symptom",
            "why": "Date of fever onset info is important for COVID patient risk assessment"
        }, {
            "id": "LOINC:64145-6",
            "title": "Cough",
            "legalValues": { "type": "boolean"},
            "group": "Symptom",
            "why": "Cough is one major symptom of COVID"
        }, {
            "id": "LOINC:85932-2",
            "title": "Date of cough onset",
            "legalValues": { "type": "string"},
            "group": "Symptom",
            "why": "Date of cough onset info is important for COVID patient risk assessment"
        }, {
            "id": "LOINC:54564-0",
            "title": "Shortness of breath",
            "legalValues": { "type": "boolean"},
            "group": "Symptom",
            "why": "Shortness of breath is one major symptom of COVID"
           } 
        ]
    }
}


guidance = {
    "piid": "pdspi-guidance-dream-q2",
    "patientId": "38",
    "settingsRequested": {
    "timestamp": "2020-04-03T13:41:09.942+00:00",
    "modelParameters": [ {
                            "id": "pdspi-guidance-dream-q2:loc",
                            "title": "Hospital location (State)",
                            "parameterDescription": "Please choose a state to indicate the hospital location for which you would like to get triage guidance.",
                            "parameterValue": { "value": "NC" }
                         } 
                       ],
    "patientVariables": [ {
                            "id": "LOINC:30525-0",
                            "title": "Age",
                            "variableValue": {
                            "value": "0.5",
                            "units": "years"
                            },
                            "how": "The value was specified by the end user.",
                            "timestamp": "2020-04-03T13:41:09.942+00:00"
                            }, 
                            {
                            "id": "LOINC:21840-4",
                            "title": "Sex",
                            "variableValue": {
                            "value": "female"
                            },
                            "how": "The value was specified by the end user.",
                            "timestamp": "2020-04-03T13:41:09.942+00:00"
                          },
                          {
                            "id": "LOINC:39156-5",
                            "title": "BMI",
                            "variableValue": {
                            "value": "23.2"
                            },
                            "how": "The value was specified by the end user.",
                            "timestamp": "2020-04-03T13:41:09.942+00:00"
                          },
                          {
                            "id": "LOINC:45701-0",
                            "title": "Fever",
                            "variableValue": {
                            "value": true
                            },
                            "how": "The value was specified by the end user.",
                            "timestamp": "2020-04-03T13:41:09.942+00:00"
                          },
                          {
                            "id": "LOINC:64145-6",
                            "title": "Cough",
                            "variableValue": {
                            "value": true
                            },
                            "how": "The value was specified by the end user.",
                            "timestamp": "2020-04-03T13:41:09.942+00:00"
                          },
                          {
                            "id": "LOINC:54564-0",
                            "title": "Shortness of breath",
                            "variableValue": {
                            "value": true
                            },
                            "how": "The value was specified by the end user.",
                            "timestamp": "2020-04-03T13:41:09.942+00:00"
                          } 
                    ]
            }
    }

def generate_vis_spec(typeid, x_axis_title, y_axis_title, chart_title, chart_desc):
    json_post_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    vega_spec_input = {
        "typeid": typeid,
        "x_axis_title": x_axis_title,
        "y_axis_title": y_axis_title,
        "chart_title": chart_title,
        "chart_description": chart_desc
    }
    url_str = "http://{}:{}/{}/plugin/tx-vis/vega_spec".format(pds_host, pds_port, pds_version)
    resp = requests.post(url_str, headers=json_post_headers, json=vega_spec_input)
    # resp = requests.post("http://tx-vis:8080/vega_spec", headers=json_post_headers, json=vega_spec_input)
    if resp.status_code == 200:
        return resp.json()
    else:
        return {}


def generate_vis_outputs(age=None, weight=None, bmi=None, dose=None, tau=None, num_cycles=None):
    outputs = [
        {
            "id": "oid-1",
            "name": "Time-series data",
            "description": "Information about time-series data",
            "data": generate_time_series_data(50),
            "specs": [
                generate_vis_spec("line_chart", "X Axis", "Y Axis", "Line chart", "Time-series line chart"),
                generate_vis_spec("area_chart", "X Axis", "Y Axis", "Area chart", "Time-series area chart")
            ]
        }
        
    ]
    return outputs


def get_config():
    return config


def get_guidance(body):
    def extract(var, attr, type="patientVariables"):
        return var.get(attr, next(filter(lambda rpv: rpv["id"] == var["id"], config["settingsDefaults"][type]))[attr])

    inputs = []
    age = None
    weight = None
    bmi = None
    dose = None
    tau = None
    num_cycles = None
    ret_input = {}
    input_dose = None
    input_tau = None
    input_num_cycles = None
    ret_guidance = []
    for body_item in body:
        for var in body_item['settingsRequested']["patientVariables"]:
            if var['id'] == 'LOINC:30525-0':
                age = var["variableValue"]['value']
            elif var['id'] == 'LOINC:29463-7':
                weight = var["variableValue"]['value']
            elif var['id'] == 'LOINC:39156-5':
                bmi = var["variableValue"]['value']
            inputs.append({
                "id": var["id"],
                "title": extract(var, "title"),
                "how": var["how"],
                "why": extract(var, "why"),
                "variableValue": var["variableValue"],
                "legalValues": extract(var, "legalValues"),
                "timestamp": var.get("timestamp", "2020-02-18T18:54:57.099Z")
            })

        ret_guidance.append({
            **guidance,
            "settingsRequested": body_item['settingsRequested'],
            "settingsUsed": {'patientVariables': inputs,
                              'modelParameters': ret_input}
        })
    return ret_guidance