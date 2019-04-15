Development/Deployment Time: < 5 hours

To solve this problem, I start with the front-end:

	What do users need to do?
	How are they going to do it?

I create a web form that initially has a Risk Name field and two data fields:
	- Data Name (Max size: 16)
	- Data Type (Drop down box)[String,data,number,email,enum]
	- IF ENUM: Unhide 3rd field and alert user to separate choices with a comma

Below is an "add field" button so that users can append fields.

The submit button sits below all of the fields.

On-Submit:
This takes users to a page where they can fill in data for the forms they created themselves.


BACKEND

For python, I use the Flask API
    - Create a class called RISK that will hold custom data
    - On submit, create a RISK object (Risk Name and list containing (key,value,enumOptions) tuples)
    - Save risk object in JSON Format with Risk Name as file name (Checks if existing)



Risks can be revisited by navigating to 'view' (GET with 'riskName' as param) to display a form using RISK object data loaded from JSON


DEPLOYMENT
    - Using python anywhere

Sample Risk:
http://nicholasconrad.pythonanywhere.com/view?riskName=Nick%27s%20Risk

http://nicholasconrad.pythonanywhere.com/


