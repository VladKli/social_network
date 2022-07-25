<h1>Social Network</h1>
Object of this task is to create a simple REST API. You can use one framework from this list (Django 
Rest Framework, Flask or FastAPI) and all libraries which you are prefer to use with this frameworks.

<h3>Basic models:</h3> 

● User

● Post (always made by a user)

<h3>Basic Features:</h3>

● user signup

● user login

● post creation

● post like

● post unlike

● analytics about how many likes was made. Example url 
/api/analitics/?date_from=2020-02-02&date_to=2020-02-15 . API should return analytics aggregated 
by day.

● user activity an endpoint which will show when user was login last time and when he mades a last 
request to the service. - not inmplemented

<h3>Requirements:</h3>

● Implement token authentication (JWT is prefered)
