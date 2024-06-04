def km_to_miles(km):
    
    conversion_factor = 0.621371
   
    miles = km * conversion_factor
    return miles


km_input = float(input("Enter distance in kilometers: "))


miles_output = km_to_miles(km_input)
print(f"{km_input} kilometers is equal to {miles_output} miles.")
