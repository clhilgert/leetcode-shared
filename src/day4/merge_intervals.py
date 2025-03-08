# 56. Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[100,100],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.


# Constraints just for clay:

# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4

def merge(intervals):
    intervals.sort()
    result = []
    prev_start = intervals[0][0]
    prev_end = intervals[0][1]
    curr_start = None
    curr_end = None
    for i in range(1, len(intervals)):
        curr_start = intervals[i][0]
        curr_end = intervals[i][1]
        if curr_start < prev_end:
            prev_end = max(prev_end, curr_end)
        if curr_start > prev_end:
            result.append([prev_start, prev_end])
            prev_start = curr_start
            prev_end = curr_end
    result.append([prev_start, curr_end])
    return result
