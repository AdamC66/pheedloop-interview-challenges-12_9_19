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

from collections import defaultdict

def print_comments(list_of_comments):

    def send_comments(sorted_comments, key, comments, n):
        for comment_id in sorted_comments[key]:
            display_comments(comment_id, n, comments)
            send_comments(sorted_comments, comment_id, comments, n+1)

    def display_comments(comment_id, n, comments):
        print(n*"    ", get_comment_text(comments, comment_id)[0])

    def get_comment_text(comments, my_id):
        return [item['comment'] for item in comments if item['id'] == my_id]

    c = defaultdict(list)
    for comment in list_of_comments:
        c[comment['parentCommentId']].append(comment['id'])
    send_comments(c, None, comments, 0)


print_comments(comments)


