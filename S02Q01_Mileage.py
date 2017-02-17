""" Simple calculation of mileage based on Odometer start & end readings ?
"""

def calculate_mileage(distance,gasoline):
    """ Function to calculate the final mileage of the vehicle.
    """
    mileage = distance/gasoline
    print "The mileage of the vehicle used is : ", mileage
    

def get_odo_readings():
    """ This function reads user input for odometer start & end readings
        It also requests user to input the total fuel consumed for the journey
    """
    begin = raw_input("Enter the odometer reading at the start of the journey : ")
    end = raw_input("Enter the odometer reading at the end of the journey : ")
    fuel = raw_input("Enter the fuel consumed for the journey : ")
    return float(begin), float(end), float(fuel)

# Main starts from here
start, end, gas = get_odo_readings()
total = end - start
calculate_mileage(total,gas)



    
