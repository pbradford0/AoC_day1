#Author: Phil Bradford

import sys

#loads the file into a string
def load_file(filename):
  f = open(filename, 'rU').read()
  return f

def main():
  
  #exit at the start if there is no specified file
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)

  #read the input to a variable
  directions = load_file(sys.argv[1])
  #start at floor 0
  floor = 0
  #loop over input, +1 per ( and -1 per )
  for f in directions:
    if f == '(':
      floor = floor +1
    elif f == ')':
      floor = floor -1
    #any input other than ( or ) is unacceptable
    else:
      print "Error: Input must be ( or ) only!"
      sys.exit(0)
  #output results
  print "Santa is looking for floor " + str(floor) + "."

if __name__ == '__main__':
  main()
