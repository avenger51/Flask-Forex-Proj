### Conceptual Exercise
(I don't understand the Markdown part of this assessment..)

Answer the following questions below:

- What are important differences between Python and JavaScript?
Python is mainly used for server-side communications, data analytics, etc, 
while JS is used for web development. JS uses {} to seperate code statements while
Python does not.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
1.  my_dict = {"a": 1, "b": 2}
    value = my_dict.get("c", 0) 
    print(value)
2. my_dict = {"a": 1, "b": 2}
   key = "c"

    if key in my_dict:
        value = my_dict[key]
    else:
        value = None

- What is a unit test?
A unit test is testing the individual components of software rather than all of the components.  Used to check
indvidual code pieces themselves.

- What is an integration test?
An integration test is a test of how components of code function together.

- What is the role of web application framework, like Flask?
Flask provides templates for creating routes, rendering templates, capturing sessions, redirecting routes, and 
for starting and running a web server.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
Using a route would be preferable for usability and ensuring conformity to REST standards.  Using a URL
query would be used if there were more particular query parameters involved.


- How do you collect data from a URL placeholder parameter using Flask?
Flask gets these data via a route.

- How do you collect data from the query string using Flask?
Via request.args.get

- How do you collect data from the body of the request using Flask?
request.form

- What is a cookie and what kinds of things are they commonly used for?
A cookie is used by the web server to provide the web browser with session data such as # page views,
user auth, tracking, etc.

- What is the session object in Flask?
A session is a way to implement cookie functionality in a cleaner way

- What does Flask's `jsonify()` do?
Converts Python lists, dicts, etc. into URL readable that can be sent as HTTP.
