### Team Members:

- Aseel Alzweri
- Hamzh Suilik
- Hisham Khalil
- Reema Eilouti
- Yahya Omari

# eduHub

eduHub is a professional networking platform for local educators mainly, namely school teachers, professors, trainers, mentors, coaches and private tutors.

The platform helps local jordanian educators apply for jobs, connect with other educators in the field, and allows employers to post job openings and announcements.
Additionally, it helps students, individuals, startups, companies approach local freelance educators.

# Minimum Viable Product

eduHub will have a Web and Mobile application version. Basic features will include the following:

- Users database.
- Profile for each user.
- Post Feature.
- Direct Messaging Feature.

# User Stories


### [1] Member Registration
#### As a member, I want to receive a confirmation message when I submit the registration form.

Feature Tasks:
An alert message which confirms user registration, should appear on screen

Acceptance Tests:
Ensure user gets an alert upon registration


### [2] Organization Form
#### As an organization, I want to have customized form to complete the sign up process

Feature Task(s):
- Only fields relatable to organizations shall be rendered

Acceptance Test(s):
- Verify correct field are rendered
 
 
### [3] Student Form
#### As an student, I want to have customized form to complete the sign up process

Feature Task(s):
- Only fields relatable to students shall be rendered

Acceptance Test(s):
- Verify correct field are rendered


### [4] Educator Form
#### As an educator, I want to have customized form to complete the sign up process

Feature Task(s):
- Only fields relatable to educators shall be rendered

Acceptance Test(s):
- Verify correct field are rendered

### [5] Search for a member
#### As a member, I want to be able to search for other registered members, according to a specific criterion

### [6] Connect with a member
#### As a member, I want to be able to connect with other members.

Feature Task(s):
- A member should be able to send a connection request to other member.
- A member should be notified when he/she receives a connection request   
-  A member should be able to receive a connection request
- A member should be able to accept or decline a connection request
- A member should be able to view latest connections list

Acceptance Test(s):
- Ensure connections data are updated once a connection request is confirmed or declined
- Ensure that a member gets notified when receiving a connection request
- Ensure that a member can view latest updated connections list
- Ensure that a member can send a connection request to another member


### [7] Direct Messaging
#### As a user, I want to be able to send direct messages to other users

Feature Task(s):
Each user (student, educator, organization) can send a direct message to other users(student, educator, organization)

Acceptance Test(s):
Ensure the message is sent to the right recipeint and added to the database

# Database Schema Diagram
![DataBase_Schema](https://i.ibb.co/k1zyxQB/UML-Diagram.jpg)

# Domain Modeling
![UML Diagram (1)](https://i.ibb.co/jzvWwq2/UML-Diagram-1.jpg)

- The user can register as an educator, a student or an organization. Each user will be able to send direct messages, post announcements and connect with other users.

- One user can send many messages, post many announcements and have many connections.

# Wireframe 

## Home Page 
![home page](https://user-images.githubusercontent.com/77917134/124910402-39394180-dff4-11eb-8fe5-de21a380afae.PNG)

## Home Page - User Signed In
![home page - signed in](https://user-images.githubusercontent.com/77917134/124910420-40604f80-dff4-11eb-8a74-c83d7042968d.PNG)

## Sign Up Page
![signup](https://user-images.githubusercontent.com/77917134/124911408-63d7ca00-dff5-11eb-8b1e-73f252d180ec.PNG)

## User Profile
![profile](https://user-images.githubusercontent.com/77917134/124911383-5b7f8f00-dff5-11eb-9349-43ea2cad8743.PNG)

## About Us Page
![about us page](https://user-images.githubusercontent.com/77917134/124910469-4b1ae480-dff4-11eb-9d44-7d1977538e5f.PNG)


