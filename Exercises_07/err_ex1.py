"""
err_ex1.py  : diesel generator error
"""
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"


def endurance(fuel_in_litre: float, fuel_burn_per_min: float) -> float:
   
    try:
        # input validation
        if fuel_in_litre < 0 or fuel_burn_per_min < 0:
            raise Exception("Values must be > 0")

        # divide by zero condition
        if fuel_burn_per_min == 0:
            return 999999.9999 #return a long time for idling  

        #  time left
        time_left = fuel_in_litre / fuel_burn_per_min
        return time_left

    except Exception as e:
        print(f"valueerror: {e}")
        return 0  # invalid inputs


fuel_in_litre = 70  
fuel_burn_per_min = 0  # idling

time_to_stop = endurance(fuel_in_litre, fuel_burn_per_min)
print(f"Remaining time: {time_to_stop} minutes")  


fuel_in_litre = 70  
fuel_burn_per_min = 2  

time_to_stop = endurance(fuel_in_litre, fuel_burn_per_min)
print(f"Remaining time: {time_to_stop} minutes") 


