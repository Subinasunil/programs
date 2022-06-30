from blog.models import users,posts
# print(users)
# username="akhil"
# password="Password@123"
session={}
def signin_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("invalid session u must login")
    return wrapper


def authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user=[user for user in users if user["username"]==username and user["password"]==password]
    return user
# print(authenticate(username="akhil",password="Password@123" ))
class LoginView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]

        print(session)

class PostlistView:
    @signin_required
    def get(self,*args,**kwargs):
        return posts
    @signin_required
    def post(self,*args,**kwargs):
        print(kwargs)
        my_post=kwargs.get("data")
        userId=session["user"]["id"]
        my_post["userId"]=userId
        posts.append(my_post)
        print(posts[-1])



class MypostListView:

    @signin_required
    def get(self,*args,**kwargs):
        userId=session["user"]["id"]
        mypost=[post for post in posts if post["userId"]==userId]
        return mypost
class AddLike:
    @signin_required
    def post(self,*args,**kwargs):
        postid=kwargs.get("postid")
        post=[post for post in posts if post["postId"]==postid]
        if post:
            post=post[0]
            userid=session["user"]["id"]
            post["liked_by"].append(userid)
            print(post["liked_by"])


log_in=LoginView()
log_in.post(username="akhil",password="Password@123")
all_post=PostlistView()
my_post={
    "postId":9,"title":"hello good morning","content":"my content","liked by":[]
}
all_post.post(data=my_post)
mypost=MypostListView()
like=AddLike()
like.post(postid=1)

# print(mypost.get())
# print(all_post.get())