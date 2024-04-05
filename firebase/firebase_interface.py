import pyrebase
config = {
"apiKey": "AIzaSyBV50OdFZyStNg6ExwPDuu2WnfLPY5FnAI",
"authDomain": "sysc-3010-l2g2.firebaseapp.com",
"databaseURL": "https://sysc-3010-l2g2-default-rtdb.firebaseio.com/",
"storageBucket": "sysc-3010-l2g2.appspot.com"
}


def read_database(dataType, log=False):
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    dataset_data = db.child(dataType).get()
    data_array = []

    if dataset_data is not None:
        key = 0
        for dataPoint in dataset_data.each():
            data_array.append({"key": key, "value": dataPoint.val()})
            key+=1
            
    # If no data found, return null
    if not data_array:
        if log:
            print("Reading from database failed!")
        return None
    
    elif dataType == "Temperature":
        data_array.sort(key = lambda x: x["key"])
        # return the last temperature data
        if log:
            print("Read Temperature from firebase: ", data_array[-1],"\n")
        return data_array[-1]["value"]
    
    elif dataType == "Feedings":
        if log:
            print("Read Feedings from firebase: ", data_array[-1],"\n")
        return data_array[-1]["value"]
    
    elif dataType == "LitterClean":
        if log:
            print("Read LitterClean from firebase: ", data_array[-1],"\n")
        return data_array[-1]["value"]
    
    elif dataType == "MoodScore":
        if log:
            print("Read MoodScore from firebase: ", data_array[-1],"\n")
        return data_array[-1]["value"]

    elif dataType == "PetClean":
        if log:
            print("Read PetClean from firebase: ", data_array[-1],"\n")
        return data_array[-1]["value"]
    
    elif dataType == "Steps":
       if log:
           print("Read Steps from firebase: ", data_array[-1],"\n")
       return data_array[-1]["value"]
    
    else:
        if log:
            print("Invalid data type","\n")

    return None

def write_database(table, data, log=False):
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    # Determine the key
    last_data = db.child(table).order_by_key().limit_to_last(1).get().val()
    if last_data:
        last_key = int(list(last_data.keys())[0])
        key = str(last_key + 1)
    else:
        key = "1"

    if table == "Temperature":
        if isinstance(data, list):
            for idx, item in enumerate(data, start=1):
                rounded_data = round(item, 2)  
                db.child(table).child(key).set(rounded_data) 
                print(f"Temperature: {key}: {rounded_data} written to database")
                key = str(int(key) + 1) 
        else:
            rounded_data = round(data, 2)  # Round the value to two decimal places 
            db.child(table).child(key).set(rounded_data)
            print("Temperature: ",key,":", rounded_data, "written to database","\n")

    elif table == "Feedings":
        if isinstance(data, list):
            for idx, item in enumerate(data, start=1):
                db.child(table).child(key).set(item) 
                print(f"Feedings: {key}: {item} written to database")
                key = str(int(key) + 1) 
        else:
            db.child(table).child(key).set(data)
            print("Feedings: ",key,":", data, "written to database","\n")

    elif table == "LitterClean":
        if isinstance(data, list):
            for idx, item in enumerate(data, start=1):
                db.child(table).child(key).set(item) 
                print(f"LitterClean: {key}: {item} written to database")
                key = str(int(key) + 1) 
        else:
            db.child(table).child(key).set(data)
            print("LitterClean: ",key,":", data, "written to database","\n")

    elif table == "MoodScore": 
        if isinstance(data, list):
            for idx, item in enumerate(data, start=1):
                db.child(table).child(key).set(item) 
                print(f"MoodScore: {key}: {item} written to database")
                key = str(int(key) + 1) 
        else:
            db.child(table).child(key).set(data)
            print("MoodScore: ",key,":", data, "written to database","\n")

    elif table == "PetClean":
        if isinstance(data, list):
            for idx, item in enumerate(data, start=1):
                db.child(table).child(key).set(item) 
                print(f"PetClean: {key}: {item} written to database")
                key = str(int(key) + 1) 
        else:
            db.child(table).child(key).set(data)
            print("PetClean: ",key,":", data, "written to database","\n")

    elif table == "Steps":
        if isinstance(data, list):
            for idx, item in enumerate(data, start=1):
                db.child(table).child(key).set(item) 
                print(f"Steps: {key}: {item} written to database")
                key = str(int(key) + 1) 
        else:
            db.child(table).child(key).set(data)
            print("Steps: ",key,":", data, "written to database","\n")

    else:
        print("Invalid data type","\n")
    
