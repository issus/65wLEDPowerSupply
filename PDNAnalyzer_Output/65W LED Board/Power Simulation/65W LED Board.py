designFile = "C:/Users/Public/Documents/Altium/Projects/65wLEDPowerSupply/PDNAnalyzer_Output/65W LED Board/odb.tgz"

powerNets = ["VIN", "NetIC1_1", "NetC13_2", "VIN_DRV", "UVHS", "UVLO", "12V", "12FB", "NetD3_1", "IADJ", "LEDVCC"]

groundNets = ["CN_GND", "GND", "LEDVSS"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("J1", "1") ],
"ground_pins": [ ("J1", "2") ],
"voltage": 48,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("R2", "1") ],
"ground_pins": [ ("R2", "2") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("R8", "2") ],
"ground_pins": [ ("R8", "1") ],
"resistance": 1E-09,
"Rpin": 770,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("R12", "2") ],
"ground_pins": [ ("R12", "1") ],
"resistance": 1E-09,
"Rpin": 62000,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("D3", "1") ],
"ground_pins": [ ("D3", "2") ],
"current": 0.02,
"Rpin": 5,
}
,
{
"id": "5",
"type": "load",
"power_pins": [ ("J4", "1") ],
"ground_pins": [ ("J4", "2") ],
"current": 0.15,
"Rpin": 0.666666666666667,
}
,
{
"id": "6",
"type": "load",
"power_pins": [ ("J5", "1") ],
"ground_pins": [ ("J5", "2") ],
"current": 0.15,
"Rpin": 0.666666666666667,
}
,
{
"id": "7",
"type": "load",
"power_pins": [ ("J6", "1") ],
"ground_pins": [ ("J6", "2") ],
"current": 0.15,
"Rpin": 0.666666666666667,
}
,
{
"id": "8",
"type": "load",
"power_pins": [ ("R10", "2") ],
"ground_pins": [ ("R10", "1") ],
"resistance": 1E-09,
"Rpin": 4880,
}
,
{
"id": "9",
"type": "load",
"power_pins": [ ("J3", "1") ],
"ground_pins": [ ("J3", "2") ],
"current": 1.8,
"Rpin": 0.0555555555555556,
}
,
{
"id": "10",
"type": "source",
"power_pins": [ ("L2", "2") ],
"ground_pins": [ ("IC4", "11"), ("IC4", "10"), ("IC4", "9"), ("IC4", "3") ],
"voltage": 12,
"Rpin": 0,
}
,
{
"id": "11",
"type": "load",
"power_pins": [ ("IC4", "7"), ("IC4", "2") ],
"ground_pins": [ ("IC4", "11"), ("IC4", "10"), ("IC4", "9"), ("IC4", "3") ],
"current": 0.128307505545986,
"Rpin": 2.07834035531999,
}
,
{
"id": "12",
"type": "source",
"power_pins": [ ("L1", "2") ],
"ground_pins": [ ("R6", "2") ],
"voltage": 36,
"Rpin": 0,
}
,
{
"id": "13",
"type": "load",
"power_pins": [ ("IC2", "2") ],
"ground_pins": [ ("IC2", "9"), ("IC2", "11") ],
"current": 1.40670416419292,
"Rpin": 0.0947842031944444,
}
]


voltage_regulators = [
{
"id": "14",
"type": "linear",

"in": [ ("IC1", "2") ],
"out": [ ("IC1", "3") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.058,
}
,
{
"id": "15",
"type": "linear",

"in": [ ("R1", "2") ],
"out": [ ("R1", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 16500,
}
,
{
"id": "16",
"type": "linear",

"in": [ ("FB2", "2") ],
"out": [ ("FB2", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.075,
}
,
{
"id": "17",
"type": "linear",

"in": [ ("FB1", "2") ],
"out": [ ("FB1", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.025,
}
,
{
"id": "18",
"type": "linear",

"in": [ ("R4", "2") ],
"out": [ ("R4", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 25500,
}
,
{
"id": "19",
"type": "linear",

"in": [ ("IC3", "3") ],
"out": [ ("IC3", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.046,
}
,
{
"id": "20",
"type": "linear",

"in": [ ("R6", "1") ],
"out": [ ("R6", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.075,
}
,
{
"id": "21",
"type": "linear",

"in": [ ("R11", "2") ],
"out": [ ("R11", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 550000,
}
,
{
"id": "22",
"type": "linear",

"in": [ ("R14", "1") ],
"out": [ ("R14", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 340,
}
,
{
"id": "23",
"type": "linear",

"in": [ ("R7", "1") ],
"out": [ ("R7", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 31700,
}
]


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.8, 'Thickness': 1E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.6E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.6, 'Thickness': 0.0002},
        {'name': 'LAYER_1', 'Conductivity': 47000000, 'Thickness': 1.8E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.8, 'Thickness': 0.001065},
        {'name': 'LAYER_2', 'Conductivity': 47000000, 'Thickness': 1.8E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.6, 'Thickness': 0.0002},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.6E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.8, 'Thickness': 1E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
