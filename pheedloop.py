
# Absent Attendees

# Given a list of attendee ids for attendees who have registered for an event and a list of attendee ids 
# for attendees who have checked into an event, return the list of attendees who have not checked in.




# absentAttendees(registeredAttendees, checkedInAttendees)
# // [509, 672]


registeredAttendees = [195, 294, 329, 441, 509, 672, 701, 873, 920]
checkedInAttendees = [195, 294, 329, 441, 701, 873, 920]


def check_checked_in(registered, checkedin):
    result = []
    for attendee in registered:
        # if attendee not in checkedin:
        #     result.append(attendee)
        is_in_list = False
        for checkin in checkedin:
            if attendee == checkin:
                is_in_list = True
                break
            else:
                is_in_list = False

        if not is_in_list:
            result.append(attendee)
    return result

print(check_checked_in(registeredAttendees, checkedInAttendees))