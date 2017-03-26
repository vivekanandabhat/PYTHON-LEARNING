""" Simple calculation of mileage based on Odometer start & end readings ?
"""

def calculate_stops(miles,gasoline,gasoline_start):
    """ Distance travelled from bangalore to Goa = 560 Kms.
        Function to calculate the refuelling stops required for the trip
    """
    km=560
    stops = 0
    dist_cvrd = 0
    if (gasoline_start==gasoline) :
        dist_cvrd = gasoline*miles
        while (dist_cvrd < km) :
            stops+=1
            dist_cvrd = dist_cvrd + (gasoline*miles)
            
    else :

        dist_cvrd = gasoline_start*miles
        while (dist_cvrd < km) :
            gasoline_start=gasoline
            stops+=1
            dist_cvrd = dist_cvrd + (gasoline_start*miles)
            
            
    print "The number of stops required between bangalore and Goa is : ", stops
    

def get_fuel_data():
    """  This function requests user to input the fuel tank capacity & mileage of vehicle
    """
    avg_mileage = raw_input("Enter the average mileage of your vehicle : ")
    tank = raw_input("Enter the tank capacity of the vehicle : ")
    tank_start = raw_input("Enter the amount of fuel available in vehicle tank at the start of the journey : ")
    return float(avg_mileage), float(tank), float(tank_start)


# Main starts from here
mileage, gas, gas_start = get_fuel_data()
calculate_stops(mileage,gas,gas_start)

print


    
