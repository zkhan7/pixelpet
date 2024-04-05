TEMP_FACTOR = 0.4
STEP_FACTOR = 0.2
FEEDING_FACTOR = 0.1
PET_CLEAN_FACTOR = 0.2
LITTER_CLEAN_FACTOR = 0.1

prev_temperature_score = 0
def calculate(temp, steps, feeding, pet_clean, litter_clean):
    # each score is out of 100
    temp_score = 0
    steps_score = 0
    feeding_score = 0
    pet_clean_score = 0
    litter_clean_score = 0

    # Temperature
    if temp is not None:
        if 18 <= temp <= 24:
            temp_score = 100
        elif 10 <= temp <= 17 or 24 <= temp <= 28:
            temp_score = 50

    # Steps
    if steps is not None:
        if steps >= 100:
            steps_score = 100
        else:
            steps_score = steps

    # feedings
    if feeding is not None:    
        if (feeding >= 4):
            feeding_score = 100
        elif (feeding == 3):
            feeding_score = 75
        elif (feeding == 2):
            feeding_score = 50
        elif (feeding == 1):
            feeding_score = 25


    # pet cleaning
    if pet_clean is not None:
        if pet_clean == 1:
            pet_clean_score = 100

    # litter cleaning
    if litter_clean is not None:
        if litter_clean == 1:
            litter_clean_score = 100

    return (temp_score*TEMP_FACTOR) + (steps_score*STEP_FACTOR) + (feeding_score*FEEDING_FACTOR) + (pet_clean_score*PET_CLEAN_FACTOR) + (litter_clean_score*LITTER_CLEAN_FACTOR) 
