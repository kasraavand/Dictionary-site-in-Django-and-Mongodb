from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context,RequestContext
from django.template.loader import get_template
from persdicapp.forms import *
from django.shortcuts import render_to_response
import sqlite3 as lite
from django.core.context_processors import csrf
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from pymongo import Connection
from pymongo.errors import ConnectionFailure

class mongo:
 try:
  client = Connection(host="localhost", port=27017)
 except ConnectionFailure, e:
  sys.stderr.write("Could not connect to MongoDB: %s" % e)
  sys.exit(1)
 dbh = client["mydb3"]
#assert dbh.connection == client
 def ins(self,word,mean):
  dic={"word":word,
      "mean":mean}
  self.dbh.users.insert(dic, safe=True)
   #self.dbh.users.insert(self.user_doc2, safe=True)
   #print "Successfully inserted document: %s" % user_doc
 def prin(self,word):
  #print self.dbh.users.find_one({"word":"example"})# for find a dictionary 
  users = self.dbh.users.find({"word":word})
  for user in users:
   return user.get("mean")
 def update(self,word,mean):
  new_user_doc={"word":word,"mean":mean}
  self.dbh.users.update({"word":word}, new_user_doc, safe=True)
 def find(self,case):
   #print self.dbh.users.find_one({"word":"example"})# for find a dictionary 
  if self.dbh.users.find({"word":case}) :
   return True
  return False

def register_page(request):
 if request.method == 'POST':
  form = RegistrationForm(request.POST)
  if form.is_valid():
   user = User.objects.create_user(
username=form.cleaned_data['username'],
password=form.cleaned_data['password1'],
email=form.cleaned_data['email']
)
   return HttpResponseRedirect('/register/success/')
 else:
  form = RegistrationForm()
 variables =RequestContext(request, {
'form': form
})
 return render_to_response(
'registration/register.html',
variables
)

def login(request):
 c={}
 c.update(csrf(request))
 if request.method == 'POST':
    form=loginform(request.POST)
    user = authenticate(username=request.POST.get('username', ''),password= request.POST.get('password', ''))    
    if user is not None:
        if user.is_active:
            c['user']=user
            #c.update(csrf(request))
            return render_to_response('index.html',RequestContext(request,c))
    else:
      messages.error(request, u'Invalid credentials')
 else:
  form = loginform()
 variables =RequestContext(request, {
'form': form 
})
 return render_to_response(
'registration/login.html',
variables
)

 return render_to_response('registration/login.html',c)

def loggedin(requetst):
    form=loginform(request.POST)
    if form.is_valid():
     #username = request.POST['username']
     #password = request.POST['password']
     #user = authenticate(username=username, password=password)
     if user is not None:
        if user.is_active:
            login(request,form.get_user())
            return render_to_response('index.html')
            # Redirect to a success page.
@csrf_exempt
def main_page(request):
 
 MON=mongo()
 #print(MON.database.names())
 item=1
 dic1={}
 con = lite.connect('G.m2')
 with con:    
    cur = con.cursor()    
    cur.execute("SELECT * FROM word")
    rows = cur.fetchall()
    for row in rows:
      for i in range(len(row)):
       if isinstance(row[i], unicode):
        if item>0:
         val=row[i].encode('utf8')
         item=-item
        else :
         dic1[val]=row[i].encode('utf8')
         item=-item
#request.user=None
 lito=dic1.keys()
 form=loginform()
 if request.method== 'POST':
   form=loginform(request.POST)
   user = authenticate(username=request.POST.get('username', ''),password= request.POST.get('password', '')) 
   request.user =user
 else:
   user = authenticate(username='username',password='password') 
   request.user =user
 template = get_template('index.html')
 athlete_list='Enter a word !'
 athlete_list2=''
 m=''
 se=[1,2,3,4,5,6,7,8,'mazdak','kasra','mehdi','babak']
 if 'word' in request.GET:
  athlete_list='your last word is:'
  athlete_list2=request.GET['word']
  for i in lito:
   if i==request.GET['word']:
    m=MON.prin(str(i))
  #m=request.GET['word']
 variables = Context({'user': request.user,'form': form,'head_title': 'Persan-English dictionary free !','page_title': 'Welcome to PersDic','mean':m,'page_body': 'Thanks of all persons those who improve and enrich the database with edit words and meanings of words Including the Literature and English Language alumni at Universitys of Shirazs and Malayer! (In future software updates ,the names will be added!)-Finally, I have to say that the software has many shortcomings that I will fix them with the whole shebang and I ask all readers of this text that have a expertise, However at low levels help to improve the code ,even by suggestions or censure!Thank you!!','athlete':athlete_list,'athlete2':athlete_list2,'select_list':se})
#request.user.username=None
 output = template.render(variables)
 return HttpResponse(output)
