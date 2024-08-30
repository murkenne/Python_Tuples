'''
1. Tuple Mastery in Python
Objective: The aim of this assignment is to deepen your understanding of tuples in Python.

Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. 
Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
The function should format and return a string that lists each itinerary. 
For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, the output should be a string formatted as:
'''

def format_itineraries(itineraries):
    for itinerary in itineraries:
        traveler_name, origin, destination = itinerary
        print(f"{traveler_name} is flying from {origin} to {destination}")
    




def main():
    itineraries = [
        ("Alice", ("FL123", "New York", "London"), ("FL456", "London", "Paris")),
         ("Bob", ("FL789", "Tokyo", "San Francisco"), ("FL321", "San Francisco", "New York")),
         # Additional itineraries....
    ]
    
    
    
    
    format_itineraries(itineraries)
    
    
if __name__ == "__main__":
    main()
    

    
