# Session Comments

# Let's say we are building a way to allow users to leave comments on sessions. Users may also reply to other comments.

# Given that we receive the following response from our Comments API:

comments = [
    { "id": 1, "parentCommentId": 4,"comment": "Wrong! Y is better than X" },
    { "id": 2, "parentCommentId": 4, "comment": "Add me on LinkedIn" },
    { "id": 3, "parentCommentId": None,"comment": "Fake news" },
    { "id": 4, "parentCommentId": None,"comment": "Great session! Have you considered X?" },
    { "id": 5, "parentCommentId": 3,"comment": "+1" },
    { "id": 6, "parentCommentId": 2,"comment": "no" }
]

# Print out the following:

# Fake news
#     +1
# Great session! Have you considered X?
#     Add me on LinkedIn
#         No
#     Wrong! Y is better than X



# # for key, value in dict:
#     if key = parent: print
#     if key = child 1: print ('   '), print (comment)
#     if key = 

#     dict{
#         parent comment id: [list of children _ id s]
#     }

def print_comments(i, comment_dict, n):
    for comment in comments:
        if comment['id'] == i:
            print( n*'  ', comment['comment'])
            for x in comment_dict[i]:
                print_comments(x , comment_dict, n+1)

def make_comments(list_of_comments):
    current_comments = list_of_comments
    comment_dict = {}
    for comment in list_of_comments:
        comment_dict[comment['id']] = []
        
    for comment in list_of_comments:    
        if comment['parentCommentId']:
            comment_dict[comment['parentCommentId']].append(comment['id'])
    # print (comment_dict) 

    for comment in comments:
        if comment["parentCommentId"] == None:
            print_comments(comment['id'], comment_dict, 0)

    return comment_dict       
    
        
comment_ids = make_comments(comments)



# for key, value in comment_ids.items():
#     if len(value) == 0: 
#         pass
#     if len(value) >= 1:
#         print_comments(key)
#         for x in value:
#             print_comments(x)