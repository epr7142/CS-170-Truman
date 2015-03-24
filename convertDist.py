# convertDist.py
# A program to convert Kilometer Distances into miles.
# by: Eli P. Riekeberg
# Date: September 2nd, 2014


def main():
    # Ask the user for the input distance in kilometers.
    km = float(input("What is the distance in kilometers? "))
    
    # Calculate the equivalent distance in miles.
    mile = (0.6241)* km

    # Print the results.
    print ("The distance is", mile, "miles.")

main()
