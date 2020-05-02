Rebekah Westerlind, Emily Sine
NetIDs: rw537, ejs345

# Backend Final Project API Specification
Due Date: Sunday, May 10

## Get all patients

```
GET /api/patients/
```
Response
    
    {
        "success": true,
        "data": [
            {
                "id": 1,
                "name": "Bonnie",
                "nurse": [ <SERIALIZED NURSE WITHOUT PATIENT FIELD>],
                "hormones": [ <SERIALIZED HORMONE WITHOUT PATIENT FIELD>, ... ]
            },
            {
                "id": 2,
                "name": "Sally",
                "nurse": [ <SERIALIZED NURSE WITHOUT PATIENT FIELD>],
                "hormones": [ <SERIALIZED HORMONE WITHOUT PATIENT FIELD>, ... ]
            },
            ...
        ]
    }


```
Example.png
```
## Create a patient
```
POST /api/patients/
```
Request

    {
        "name": <USER INPUT>
    }
    
Response

    {
        "success": true,
        "data": {
                "id": <ID>,
                "name": <USER INPUT>,
                "nurse": [],
                "hormones": []
        }
    }

## Get a specific patient
```
GET /api/patients/{id}/
```
Response

    {
        "success": true,
        "data": {
                "id": <ID>,
                "name": <USER INPUT>,
                "nurse": [ <SERIALIZED NURSE WITHOUT PATIENT FIELD>],
                "hormones": [ <SERIALIZED HORMONE WITHOUT PATIENT FIELD>, ... ]
        }
    }


## Delete a specific patient
```
DELETE /api/patients/{id}/
```
Response

    {
        "success": true,
        "data": {
                "id": <ID>,
                "name": <USER INPUT>,
                "nurse": [ <SERIALIZED NURSE WITHOUT PATIENT FIELD>],
                "hormones": [ <SERIALIZED HORMONE WITHOUT PATIENT FIELD>, ... ]
        }
    }

## Get all nurses
```
GET /api/nurses/
```
Response

    {
        "success": true,
        "data": [
            {
                "id": 1,
                "name": "Franny",
                "patients": [ <SERIALIZED PATIENT WITHOUT NURSE FIELD,...>],
            },
            {
                "id": 2,
                "name": "Bob",
                "patients": [ <SERIALIZED PATIENT WITHOUT NURSE FIELD,...>],
            },
            ...
        ]
    }

## Get a specific nurses
```
GET /api/nurses/{id}/
```
Response

    {
        "success": true,
        "data": {
                "id": <ID>,
                "name": <USER INPUT>,
                "patients": [ <SERIALIZED PATIENT WITHOUT NURSE FIELD,...>],
        }
    }
## Assign a patient to a nurse
```
POST /api/patients/{id}/addnurse/
```
Request

    {
        "nurse_id": <USER INPUT>
    }

Response

    {
        "success": true,
        "data": <SERIALIZED PATIENT>
    }    

## Get all hormones
```
GET /api/hormones/
```
Response

    {
        "success": true,
        "data": {
                "id": <ID>,
                "name": <USER INPUT>,
                "patients": [ <SERIALIZED PATIENT WITHOUT NURSE FIELD,...>],
        }
    }

## Assign a hormone to a patient
```
POST /api/patients/{id}/addhormone/
```
Request

    {
        "hormone_id": <USER INPUT>
    }

Response

    {
        "success": true,
        "data": <SERIALIZED PATIENT>
    }   



