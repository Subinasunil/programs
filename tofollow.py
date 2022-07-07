import json
import random
try:
    with open("followers.json",encoding="utf-8")as f:
        data=json.load(f)
        print(data)
        all_users=[user["id"] for user in data]
        print(all_users)
        my_followings=[user["followers"] for user in data if user["username"]=="akhil"][0]
        my_id=[user["id"] for user in data if user["username"]=="akhil"][0]
        print(my_followings)
        tofollow=set(all_users)-set(my_followings)
        tofollow.remove(my_id)
        print(tofollow)
        suggestions=random.sample([*tofollow],2)
        print(suggestions)
        lst = [1, 2, 3, 4]
        st = {*lst}
        print(st)

except Exception as e:
    print(e)

