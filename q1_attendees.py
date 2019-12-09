
# Absent Attendees

# Given a list of attendee ids for attendees who have registered for an event and a list of attendee ids 
# for attendees who have checked into an event, return the list of attendees who have not checked in.

# absentAttendees(registeredAttendees, checkedInAttendees)
# // [509, 672]

registeredAttendees = [195, 294, 329, 441, 509, 672, 701, 873, 920]
checkedInAttendees = [195, 294, 329, 441, 701, 873, 920]

def check_checked_in(registered, checkedin):
    checkedin_set = set(checkedin)
    registered_set = set(registered)
    
    #O(len(registered_set))
    return list(registered_set-checkedin_set)

print(check_checked_in(registeredAttendees, checkedInAttendees))