# CSC301 Assignment 2 

# Demo and Website Link
Checkout Price Calculator Web App Demo:
https://youtu.be/Lo8NAMPbsk0

Link to the website:
https://assignment-2-101-agamjot-saini.herokuapp.com/
# Decisions Report

## Front-End Options:

1.) React.js -- I have some experience with this, so I initially wanted to use react for this project. 
However, I thought it may be overkill, since the checkout price calculator did not really need to
have a lot of complex functionality. We just needed a way of inputting items, and a way to display them.


2.) Angular -- Similar to react, I felt like this may be overkill. There are many different aspects to Angular, 
and it seemed like there would be a steep learning curve to becoming familiar with it. If I had more time to develop
the application, I may have considered learning Angular. However, since I was doing this assignment without 
a partner and was using Flask as my backend (which i had to learn as well, since i am new to that), I thought
it would be best to use a technology that I am familiar with for the front end.


3.) ***HTML/JS*** -- I chose to use HTML/JS for the front end of the web app. 
The checkout price calculator just
had to have a way of inputting items, and showing the list of items. 
Since the app did not require a lot of complex functionality on top of that, 
I thought using HTML with some nice CSS styling should be sufficient for our purposes. 




## Back-End Options:

1.) Node.js -- I have some experience using node.js in some of my past projects, so I was initially considering using
node.js for the backend of the web app. However, this would require high maintenance, compared to using something 
like Flask. Thus, I decided on not using node.js, since I thought it may be overkill. 


2.) Django -- I considered using django for this project because I am aware of its popularity among developers. 
I have not used django before, but I am familiar with python, which is why I considered using it. I also thought
it may be good for the checkout calculator backend, since it supports dynamic HTML pages. It is also very fast,
which would have been a bonus, even though speed is not a major concern for this app, as it is a relatively simple
one. This would have also been a great choice for the checkout price calculator, but I chose Flask because I found it to be lighter,
and better suited to the simple nature of the app.


3.) ***Flask (with Jinja)*** -- I was completely new to Flask, but it was easy to pickup since I am familiar with python. 
It is very Lightweight, which is perfect for the checkout price calculator. Additionally, our group will be using
Flask for our team project, so I thought learning Flask now would be a bonus. It would give me a head start which
would allow me to help out my team quicker.

Flask does not support dynamic HTML pages, so I used Jinja to add dynamic components to the HTML template.
I found Flask very easy to set up and use. I used it with Jinja, which was also new to me. It very fascinating 
using Flask in the backend in conjunction with Jinja. Having the logic in the Flask backend, and using Jinja to
unpack it in the frontend was very cool to me, and I learnt a lot about these technologies.

Flask supports SQLAlchemy, which would be sufficient for our web app. We just need to store the information
the user inputs in a table, which can be done using SQLAlchemy. 




## Database Options:

1.) ***SQLAlchemy*** -- Works with Flask. Sufficient for our web app. Pretty much the only option with Flask. Easy integration with Flask. 
*I would like to use SQLAlchemy as the next step in development. I can store the items the user inputs into the form in a table in SQLAlchemy.*

2.) PostgreSQL -- Familiar with this from csc343. Easy to store tables. Could work well for our app.

3.) MongoDB -- Better to use a relational database for our application, since we want to store the items inputted as rows. MongoDB is not ideal for our app.



## Final Product Summary

Checkout Price Calculator Web App Demo:
https://youtu.be/Lo8NAMPbsk0

Link to the website:
https://assignment-2-101-agamjot-saini.herokuapp.com/

I built a web app using HTML/JS in the front-end and Flask in the back-end. I also used the templating system Jinja to make the HTML page dynamic. 
It allowed me to change the HTML when changes would be made in the back-end.  

In the web app, we can add and remove items. As we add and remove items to the list, they show up in a table below the input form. 
The input fields have certain requirements:
- the item name cannot be more than 20 characters long
- the price must be greater than 0, and less than or equal to 1000000 (2 decimal place accuracy)
- the quantity must be at least one, and no more than 50 (whole number quantity required 
- the discount (%) must be 0 at the very least, and 100 at most (the default is 0, with 2 decimal place accuracy)
- the tax (%) must be 0 at the very least, and 100 at most (the default is 13, with 2 decimal place accuracy)

We can also clear the form completely by clicking the "Clear Item List" button.

The deployed application has small bugs relating to removing and clearing, which I am trying to fix. The application runs mostly fine locally.



### Next Steps:

Fix the back-end code of the removeItem function. 

Implement sqlalchemy database and store the items as rows. 



# Testing
I wanted to use the flask-testing library for unit testing, but it is not being maintained anymore. I was going to use it to check if the template was used
and if the variables (Jinja) were used to render it. However, I was not able to do that.

As a solution, I set up unit tests for the logic of my app. I copy-pasted my backend functions into my tests.py file, and changed the return values of my functions.
This way, I could at least check if my functions were doing what they were supposed to, by using assertions. 



I would like to explore PyTesting next, as it is well supported. I feel like this is the next step to take with testing.

# Testing Instructions

To run the tests: 
- have python installed
- download the tests.py file 
- open terminal and navigate to the directory containing tests.py
- type this command: python tests.py




The output should look like this:  

PS D:\checkout\assignment-2-101-agamjot-saini>  python tests.py 

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK



