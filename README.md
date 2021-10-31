# Simple Elevator Scheduling Problem/Sorting

#### This is a simple practice of a reading file and sorting the given location and commands.

#### The problem description

1. Command format: (location, command)

2. Definitions:
   2.1 location={1,2,3,4,5,6,7,8,9,10,11)
    
       % 1-10 stand for floor number, 11 stands for user within the elevator
       
   2.2 command={1,2,3,4,5,6,7,8,9,10,11,12) 
       
       %1-10 stand for the floor the user would like to go. 11 for upstairs, 
       
       12 for downstair
       
3. Output the stops of this elevator to a file named as elevator_stop.txt

Command format description:

1,11 -> a user is on floor 1 and press upstairs

11, 8 -> a user is in car and press 8F

1, 2(1-10) -> invalid command


Example of input file: <**Not the actual input file contents**>

The initial position of elevator is on floor 1
  
11, 5
  
11, 3
  
2, 11
  
8, 12
  
9, 12
  
  
**However, you can still test with the above combination.**
