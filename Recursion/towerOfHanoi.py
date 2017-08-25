#The following program solves the tower of hanoi problem by the use of recursion method

def towersofhanoi(disks,start_tower,end_tower):
    if disks:
        towersofhanoi(disks-1,start_tower,6-start_tower-end_tower)
        print("Disk number {} moved from {} to {}".format(disks,start_tower,end_tower))
        towersofhanoi(disks-1,6-start_tower-end_tower,end_tower)

#Let's check this problem for number of disks=6,start_tower=1,end_tower=3
towersofhanoi(disks=3,start_tower=1,end_tower=3)