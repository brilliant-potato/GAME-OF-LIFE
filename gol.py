import sys
import time


def create_start_array(size,ran): #placeholder!!!
	line = [0]*size
	field = line*size
	return field
	

def printarr(pf): #placeholder!!!
	print ("nothing to see here!")

def update_field(pf): #placeholder!!!
	return pf


def main():
	if len(sys.argv) != 5:
		print ("\nusage: gol size number_of_gens timeout choose_start (only use integer values!)")
		sys.exit() 
		

				
	size = int(sys.argv[1])	
	number_of_gens = int(sys.argv[2])
	timeout = int(sys.argv[3])
	ran = int(sys.argv[4])
	
	play_field = create_start_array(size,ran)
	for i in range(0,number_of_gens):
		play_field = update_field(play_field)
		time.sleep(timeout)
		printarr(play_field)


if __name__ == "__main__":
    # execute only if run as a script

    main()