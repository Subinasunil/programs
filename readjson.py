import json

with open("blogs.json",encoding="utf-8")as f:
    data=json.load(f)
    print(data)
print(len(data))

# number of post by userid=1
postnum=[post for post in data if post["userId"]==1]
print(len(postnum))
# total number of likes for postid 6
total=[len(like["liked_by"]) for like in data if like["postId"]==6]
print(total)
# number of post liked by user=2
num_post=len([post for post in data if 2 in post["liked_by"]])
print(num_post)