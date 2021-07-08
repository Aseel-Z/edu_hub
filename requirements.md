## Vision
### What is the vision of this product?
#### Education is important for societies. It helps people to be specialized in a specific field and become an interactive individuals in their societies
### What pain point does this project solve?
#### When a student has some difficulties in understanding some of school or university courses, he can search for an educator who can help him to understand them
### Why should we care about your product?
#### Because it connects students with proper educators, so that they can understand their courses and pass their exams
## Scope
### What will your product do?
1. the product will let educators to make profiles so that they can insert/save and show their information for the public
2. the product will let the students to make profiles for their information
3. the product will let students to search for educators using filters
4. the product will let students to connect with the selected educators  
### What will your product not do ?
- It will not be available in offline mode
### What will your MVP functionality be?
1. Educators can register in the product
2. Students can register in the product
3. Students can search for educators
4. Students can set appointments with educators
### What stretch goals are you going to aim for?
1. Students can pay online
2. product can provide visual connection like a video call
3. product can provide educational tools as in miro 
## Functional Requirements
### Data Flow:
- When a user opens the product online, the product shows the home page which will give a brief for the product and also will provide a navigation bar so that the user can register as an educator or a student or log in if the user already registered 
- If the user chooses to register as an educator, the product will show a form for the user to fill the information and after finishing filling and submit the product will send the data to the database and save it in educators models then it will show a profile page for the educator that includes his information 
- If the user chooses to register as an student, the product will show a form for the user to fill the information and after finishing filling and submit the product will send the data to the database and save it in students models then it will show a profile page for the student that includes his information. The products provide a search bar with a filter, when a student presses on the filter it will show all the filter categories that can minimize the searching domain. After choosing the filter, the students press on search to see all possible educators. The product will show to him a page with all educators matching the filter requirements with some information for each educator and a link to the educator page in addition to a form to fill out for making an appointment.  
- When a student fills the appointment form and submits, the product will make a notification in the educator page and save the appointment in the database
- When a user logs in, the product shows the user page directly
## Non-Functional Requirements
- Security: 
  - All inputs should be validated and sanitized on the server-side to prevent malicious input
  - All processes such as create,update or delete that can be applied for a user's data  in a database should be authenticated by a username and password related to the data owner only to protect data from tampering.  
- Usability: 
  - All input should be validated on the client side, an appropriate error should be shown if the input is not valid, the UI should prevent the user from submitting the form until valid input is given
  - The pages design should be responsive for mobile and computers screens and attractive for users, the product should be easy to use and the data flow is smooth
