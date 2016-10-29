#Author: Phil Bradford

import sys

#loads the file into a string
def load_file(filename):
  f = open(filename, 'rU').read()
  return f

def find_destination(filename):
  directions = load_file(filename)
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
  return floor

def find_basement(filename):
  directions = load_file(filename)
  #loop over the directions until position is -1
  floor = 0
  #keep track of which instruction we're on
  instr = 0
  for f in directions:
    if f == '(':
      floor = floor +1
    elif f == ')':
      floor = floor -1
    #any input other than ( or ) is unacceptable
    else:
      print "Error: Input must be ( or ) only!"
      sys.exit(0)
    #debug: print where santa is on each step
    #print str(floor) + ", ",
    #debug: print instr before incrementing
    #print str(instr) + ", ",
    instr = instr +1
    #exit the loop as soon as santa enters the basement
    if floor < 0:
      break
  return instr

def main():
  #exit at the start if there is no specified file
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)

  #get the floor santa ends at for part 1
  floor = find_destination(sys.argv[1])
  #output results for part 1
  print "Santa is looking for floor " + str(floor) + "."
  #get the first basement floor instruction for part 2
  basement = find_basement(sys.argv[1])
  if basement > -1:
    print "Santa entered the basement at instruction " + str(basement)
  else:
    print "Santa did not enter the basement."

if __name__ == '__main__':
  main()
