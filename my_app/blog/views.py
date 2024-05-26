from django.shortcuts import render

posts =[{
    'author':'CoreyMS',
    'title': 'Blog Post 1',
    'content':'first post content',
    'date_posted':'august 21,2018'   
},{
'author':'jane doe',
    'title': 'Blog Post 2',
    'content':'second post content',
    'date_posted':'august 21,2078'   
}
]
def home(request):
    context={
         'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
      return render(request,'blog/about.html',{'title':'About'})


