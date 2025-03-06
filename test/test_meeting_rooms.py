from src.day2.meeting_rooms import intervals

def test_intervals():
    assert intervals([(0,30),(5,10),(15,20)]) == False
    assert intervals([(9,15),(5,8)]) == True
