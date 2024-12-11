def minMovesToSeat(seats, students):

    seats.sort()
    students.sort()
    output = sum(abs(x-y) for x,y in zip(seats, students))
    
    return output


seats = [3, 1, 5]
students = [2, 7, 4]
print(minMovesToSeat(seats, students))
