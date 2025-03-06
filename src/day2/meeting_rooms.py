# Meeting Rooms
# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

# Example 1:

# Input: intervals = [(0,30),(5,10),(15,20)]

# Output: false
# Explanation:

# (0,30) and (5,10) will conflict
# (0,30) and (15,20) will conflict
# Example 2:

# Input: intervals = [(5,8),(9,15)]

# Output: true

def intervals(interval):
    interval.sort()
    prev_end = 0      

    for start, end in interval:
        if prev_end > start:
            return False

        prev_end = end
    return True