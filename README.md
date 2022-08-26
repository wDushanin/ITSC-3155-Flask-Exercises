# ITSC-3155-Flask-Exercises

Exercise Instructions: 

Each of your exercises should use either Bootstrap, another CSS framework, or custom CSS so that your pages do not use the default HTML styling.

1. Write a flask app with a single route at "GET /" which shows the current date and time when the user opens the page. This means that when you reload the page, the time should change to be the next current time when the page was loaded.

2. Write a flask app where a user can enter an integer with a GET form. When the user submits the form, the page you route to should show whether the number was an even number, odd number, or not an integer at all. In this resultant page, you should have a link that brings the user back home. Because you are using a GET form, this resultant page should still work if you navigate to it directly, but with an error message if no query parameter was included. Remember to extract the common template HTML code to a layout.

3. Write a flask app that allows users to register for different student organizations. The home page should have a simple POST form that allows users to enter their name and then select one of five student organizations. When the user registers, they should be added to a global dictionary in the server where the key is the student's name and the value is the organization. After the user is saved, redirect to a page that shows the list of all registered users. This other page should also be accessible from the home page and vice versa via a navbar. Make sure you have both frontend and backend validation on your form to require the name and organization and only allow the 5 organizations you've hardcoded (they can be any organizations you want to hard code). Also make sure that you have extracted the common template HTML code to a layout.
