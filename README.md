# Pontarth Village Shop

## Code Institute Milestone Project 4
A website where Pontarth's grocery sales, blog and events listing can share a single site.

# Initial Design
### Strategy
## Owner Key Goals:
- to sell groceries via Click & Collect Service
- to update locals via their blog
- to advertise events hosted at the shop's space

## Shopper Key Goals:
- to buy groceries quickly to pick up later
- to checkout latest news at the shop
- to find out more info about events
- to have my details stored for faster checkouts in future

## User Stories

### Navigation
| ID | As the ... | I want to ... | So that ... |
| ---|-----------|-------------|--------|
| 001 | Site visitor | be able to view all products in one page | I can browse all items |
| 002 | Site visitor | search for a specific item | So I don't have to manually search for something |
| 003 | Site visitor | view products by category | I can look for specific items within a section |
| 004 | Site visitor | See latest news first on the Updates page | I can see what the latest news is without having to go through the whole page |
| 005 | Site visitor | View more details on specific events | I can read up on any event I'm interested in |

### Accounts 
| ID | As the ... | I want to ... | So that ... |
| ---|-----------|-------------|--------|
| 006 | Site visitor | view the products, blog and events without creating an account | I can decide if I need to register first |
| 007 | Site visitor | create an account | my details are saved |
| 008 | Site visitor | update my password | to keep my account secure |
| 009 | Site owner | ensure my users are verified by email | to have a necessary security check |
| 010 | Site visitor | log in and out of my account as needed | to keep my information secure when I am not using the site |

### Admin 
| ID | As the ... | I want to ... | So that ... |
| ---|-----------|-------------|--------|
| 011 | Site owner | Create a blog post | I can share information with readers easily |
| 012 | Site owner | Edit a blog post | Make ad hoc changes to a published post |
| 013 | Site owner | Delete a blog post | Remove posts when they are no longer required. |
| 014 | Site owner | Add an event listing | I can create dedicated posts for events separate to blog posts |
| 015 | Site owner | Edit an event listing | I can make changes when an event is updated |
| 016 | Site owner | Delete an event listing | I can remove posts if an event is over or cancelled |
| 017 | Site owner | Add a new product | Add new items to sell |
| 018 | Site owner | Edit a product | I can change a product price or description without adding it brand new |
| 019 | Site owner | Delete a product | I can remove items no longer for sale |

### Purchases
| ID | As the ... | I want to ... | So that ... |
| ---|-----------|-------------|--------|
| 020 | Shopper | add items to my bag | they save and I can continue shopping |
| 021 | Shopper | edit quantity before adding an item to my bag | I can add multiple at once |
| 022 | Shopper | view the items in my bag | I can check what's saved |
| 023 | Shopper | proceed to checkout | begin the payment transaction |
| 024 | Shopper | enter my payment details securely | I feel like my information is safe |
| 025 | Shopper | be ifnromed when my payment is successful | I know the transaction is complete |

## Database Design
Based on the above initial designs, the database was designed with the following relationships using Figma:
![database initial design](bookreviews/static/assets/design-images/TortoisePrizeDBDesign.png)
- Teachers are linked to each of their students by their primary key
- Students are linked to each of their reviews by their primary key
- Students and Teachers both have roles assigned by linking to the Role's primary key
- Each review will be linked to a book by the latter's primary key.


# Frontend Design
## Wireframes
Provided are scans of the original wireframes.
![Home screen wireframe](bookreviews/static/assets/design-images/homescreenwireframe.png)
![Account wireframe](bookreviews/static/assets/design-images/accountwireframe.png)
![Register wireframe](bookreviews/static/assets/design-images/registrationwireframe.png)
![Reviews wireframe](bookreviews/static/assets/design-images/reviewswireframe.png)
The original plan for the home page was to keep it sparse, with just some text about the history of the shop, and the click & collect service. However, this looked boring, so it was decided to create a gallery page instead to bring some colour and shop in pictures that it's both a shop and event space. 
## Colour Scheme
- The colour scheme is black and white for a minimalistic look.
- Between the product images and blog/event images, there is already a lot of colour on these pages, and a monochromatic theme prevents clashes.
## Typography
- The fonts were selected to provide an academic vibe that wasn't overly formal. 
- From Google Fonts, 'Prata' was selected for the headers and some text. Times New Roman is also used to improve legibility.

## Technologies Used
### Languages
![HTML5](https://en.wikipedia.org/wiki/HTML5)
![CSS3](https://en.wikipedia.org/wiki/CSS)
![jQuery](https://jquery.com/)
![Python3](https://www.python.org/downloads/)

### Frameworks
![Bootstrap 5](https://getbootstrap.com/)
![Heroku](https://heroku.com/)
![Django](https://getbootstrap.com/)
![Elephantsql](https://www.elephantsql.com/)
![Stripe](https://stripe.com/)
Stripe was used for payments on the site.
![AWS](https://aws.amazon.com/)
Amazon S3 was used to manage media and static files.

# Features
## Home Screen Display of Books
![home screen](bookreviews/static/assets/design-images/Homescreen.png)
- The books were entered into the application on first access (the code is available to view, commented out, for information only in the routes file). This prevents the user being able to adapt the table in any way, as this particular table will not require amending.
- They are listed on the home page using Jinja as an announcement of the nominees to commence this year's reviews.
- A row of images, the cover of each book, is visible below the announcement card. 
- A tutorial page at [w3Schools](https://www.w3schools.com/howto/howto_css_images_side_by_side.asp) enabled this banner to be created, by modifying the code provided. 
- A post on [Stack Overflow](https://stackoverflow.com/questions/19414856/how-can-i-make-all-images-of-different-height-and-width-the-same-via-css) provided code which when modified, was able to create consistency in height  between the six images.

## Register as Teacher
![register as teacher screen](bookreviews/static/assets/design-images/Registerteacher.png)
- Teachers enter their details into the form, which is then used to create a new row in the Teachers table.
- The primary key, id, is the unique value used in the backend to associate teachers to students, in a one to many relationship. 
- This could be built upon in future, to be able to delete teachers fairly easily, as it would cascade down to delete their students' accounts and in turn their reviews, as currently composed within the model. 
- The user's email is used as their login id, and therefore is also unique. The system prohibits another user being created with the same email address. 
- A Teacher record by default is given the value 1 in its Roles column. 
- **Please note that user authentication for a SQL based database was not within the course. However, I discovered it was within the bonus content, and watched some of the videos there to learn how this worked. The Code Institute [GitHub](https://github.com/Code-Institute-Solutions/CombinedTaskManager2022) shows the project that taught me the majority of my understanding. I was also helped by this [Youtube](https://www.youtube.com/watch?v=1nxzOrLWiic&t=374s) video by Tech by Tim which gave me another perspective on managing users simply** 
## Create a Student account
![create student account screen](bookreviews/static/assets/design-images/CreateStudentAccount.png)
- Teachers create student accounts, which enables them to be associated easily
- The student's details are purposely sparse to retain their privacy when publishing reviews
- In order to enable a login, the password field is also here. This is admittedly poor practice, but as this project isn't an exercise in user authentication, it was determined as the simplest way to get the students logged in. It would be straightforward to add a password change option within a student's account, or alternatively look into OTP options. (Alternatively, students could participate in creating their own accounts, and enter their own password).
- When the completed form is submitted, in the backend a new row is added to the Students table. By default the row's teacher and school values are filled by taking them from the Teacher's ID and School values.
- The Student's primary key, their ID, will enable them to be identified as the author of any reviews they publish. Their email, used to login, is also unique; as with the Teacher registration, the application will prevent another Student being created with the same email address.
- The value books_read is also added to the newly created Student record and set to 0. This value is used to track how many reviews the Student has created.
- A Student record by default is given the value 2 in its Roles column. 

## Login Pages
![login screen](bookreviews/static/assets/design-images/login.png)
- Because of the separation needed between Teachers and Students, I split the login into three pages: One asking whether the user is a Teacher or Student, and then an actual log-in form for each user type. This allows both pages to run separate queries to their respective Tables, to find the user.
- There are probably more elegant solutions for this. However, user authentication is a new challenge and for my first attempt I wanted to simplify the process. 

## Account page 
![teacher account screen](bookreviews/static/assets/design-images/teacheraccount.png)
![student account page](bookreviews/static/assets/design-images/studentaccount.png)
- The Role id within each user determines the view on this page: 1 = Teacher, 2 = Student.
Teachers have the following features: 
- They can view their own details
- They can view each student and have the option to update or delete
- They have a list of each student again, but this time it shows how many reviews each has written. They can navigate to read their students' reviews.
While Students have these features:
- They can see their own details but cannot edit (if they felt it needed updating, they could speak to their teacher)
- They can see a list of reviews they have written so far and can navigate to view them in full
- They can see how many books are left to review, made possible by the books_read value attached to each Student record. If they have reviewed all 6 books, an alternative message is shown informing them they are eligible to receive their certificate and book token
- If they do have books left to review, they can navigate from here to create a new review (this button is unavailable if their books_read = 6)

## Create Review 
![create review screen](bookreviews/static/assets/design-images/createreview.png)
- Only Students can create reviews
- They can select the book they wish to review via dropdown. To enable this, a query was created that first checked which books the user had reviewed within the Reviews table. A second query, this time in the Books table, subtracts that list from the six results available, and the remainder is shown to the user.
- The concept of subqueries was very new, and supplied by a lot of searching and eventually finding this suggestion in [Stack Overflow](https://stackoverflow.com/questions/38878897/how-to-make-a-subquery-in-sqlalchemy)
- The user must complete all fields to submit the form.
- When the form is submitted, a new record is added to the Reviews table, where the Review is tied to the Student's ID as it's 'author' value, and the book's ID as it's 'book' field.
- When a review is successfully added, the user's books_read is incremented by 1.

## Update Review
- A student is able to update any review they have published. The values are pre-filled with their original content, and the record cannot be updated if the user clears a field and leaves it blank.
- Once the form is submitted, the record is updated in the backend within the Reviews table.

## Delete Review
- If the user opts to delete a review, a modal appears asking them to confirm. 
- When they confirm, the record is deleted in the Reviews table.
- This then decrements their books_read by 1, and also will allow them to create a fresh Review (i.e. a brand new record) within the Reviews table.

## Update Teacher Details
- A teacher may update their own details 
- The values are pre-filled with their original content, and the record cannot be updated if the user clears a field and leaves it blank.
- Once the form is submitted, the record is updated in the backend within the Teachers table.

## Update Student Details
- A teacher may update their associated student's details.
- The values are pre-filled with their original content, and the record cannot be updated if the user clears a field and leaves it blank.
- Once the form is submitted, the record is updated in the backend within the Students table.

## Delete Student Details
- A teacher can delete an associated student's account
- If the user presses Delete, a modal appears asking them to confirm.
- When they confirm, the record is deleted within the Students table.
- This will also by default delete any review(s) published by the Student within the Reviews table. 

## Delete a Student's Review
![delete review screen](bookreviews/static/assets/design-images/deletereview.png)
- In order to accomplish the supervision element of the scope, if a teacher determines a review is unsuitable to be visible to other readers (eg. bad language), they can delete an associated Student's review. 
- A modal appears asking the user to confirm the review deletion.
- On confirming, the Student who wrote the review will have their books_read decremented by 1 the same as if the Student had deleted the review

## View all reviews
- Anyone who visits the site can view all reviews
- The only details about the author are their first name and initial, maintaining privacy
- Initially the reviews were displayed in order of ID, which kept the list static. This felt unfair to reviewers who publish later, who are less likely to get their work read.
- To fix this, I looked into how to randomly display all results, and this post from [Stack Overflow](https://stackoverflow.com/questions/66247588/randomly-shuffle-query-results-where-values-are-the-same) contained the code that enabled this to occur. 

# Testing
## Static Testing

### HTML Validation
[W3C](https://validator.w3.org/) was used to validate the HTML. Where the user had to log in, I navigated to 'View Page Source" and pasted the contents into the validator. 
#### identified issues
[alt tags](bookreviews/static/assets/design-images/altimage.png)
- identified no alt tags were added to my images; this is now fixed.

### CSS Validation 
[Jigsaw](https://jigsaw.w3.org/css-validator/) was used to validate the CSS.
![Jigsaw validation](bookreviews/static/assets/design-images/Jigsawvalidation.png)
No issues identified.

### JQuery Validation
[JSHint](https://jshint.com/) was used to validate the JQuery.
![JSHint validation](bookreviews/static/assets/design-images/jshintvalidation.png)
- an unnecessary semicolon was at the end of the code. This has been removed.

### Python Validation
[CI Pep8 Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code. 
![Python linter](bookreviews/static/assets/design-images/Pep8linter.png)
- received no errors on routes.py & models.py

## Dynamic Testing

### Functional System Tests

### Users not logged in
| ID | Test Case | Description | Result |
| ---|-----------|-------------|--------|
| 001 | Home page | The user is able to view the book titles on the home page | Pass |
| 002 | About | The user can view the About page and its text contents | Pass |
| 003 | Reviews | The user can see all presently published reviews | Pass |
| 004 | Review randomization | On navigating back to the Reviews page, the reviews are displayed in a different order. | Pass |
| 005 | Prohibited views | The user cannot view the Account or Logout buttons | Pass |
| 006 | Login or Register | The user can view the Login and Register screens, and the forms load correctly | Pass |
| 007 | Social links | When the user presses the social links, they load the corresponding websites | Pass |

### Users are Teachers
| ID | Test Case | Description | Result |
| ---|-----------|-------------|--------|
| 008| Incomplete form | On the register page, the user cannot proceed if they have blank fields on the form | Fail |
| 009| Existing email | On the registration page, if the user enters the email of a pre-existing Teacher account, the system will inform them on submitting the form that the user already exists | Pass|
| 010| Register teacher | Once all fields have been entered, when the user presses the Register button they are successfully registered and logged in | Pass |
| 011| View details | In the Account page, the teacher is able to view their details as entered previously | Pass |
| 012| Update details incomplete | On attempting to enter their details, the user cannot proceed if any fields are blank. | Pass |
| 013| Update details | On amending any or all fields, the user will be able to successfully update their details | Pass |
| 014| Create student | On the creation page, the user cannot proceed if they have blank fields on the form | Fail |
| 015| Existing student | If another Student record already exists with the same email address, the user will be notified on submission that the user already exists | Pass |
| 016 | Register student | Once all fields have been entered, the user will successfully create a Student account | Pass | 
| 017| View all students | All created student accounts will be visible in a list in the teacher's Account, with 'Update' and 'Delete' buttons available next to each Student name | Pass |
| 018| Update student details incomplete |  On attempting to update student details, if a field is blank, the user cannot proceed | Pass |
| 019 | Update student details | On amending field(s), when all fields are complete, the user will be able to successfully update the student account | Pass |
| 020 | Delete student modal | On pressing the Delete button next to a student, a modal will appear. Pressing Cancel will return the user with no change to the account | Pass |
| 021 | Delete student confirm | On pressing the Delete button and confirming within the Modal, the student will be deleted | Pass |
| 022 | Delete student with published reviews | On deleting a student with published reviews, the reviews will also be deleted | Pass |
| 023 | Display student review tally | The teacher will be able to see a list of associated student names, and the number of reviews they have created, which is 0 at minimum and 6 as maximum | Pass |
| 024 | View all reviews | The teacher is able to view all reviews published by associated students in a dedicated page | Pass |
| 025 | Delete review modal | For each review, the user is able to press a Delete button, which causes a modal to appear. On pressing Cancel, the box will disappear and the reviews page will be unchnaged. | Pass |
| 026 | Confirm review delete | If the user confirms in the modal to delete a student's review, the the record is deleted, removed from the Reviews page and the student's books_read will reduce by 1. This will be visible within the tally on the Teacher's account page, and in the Student's Accout page | Pass |
| 027| Press Register or Login | If the logged in user presses Register or Log Out buttons, they will be redirected to their Account page with an informative message | Pass |
| 028 | Logout | On pressing the Log Out button, the user is logged out of their account and returned to the Login Page | 
| 029 | Login without password | If the teacher tries to log in with incorrect details, they will be unsuccessful and an informagtive message is displayed | Pass |
| 030| Log in as teacher | User is able to log back into their account with email and password | Pass |


### Users are Students

| ID | Test Case | Description | Result |
| ---|-----------|-------------|--------|
| 031| Login with missing details | The student needs the correct email and password to login, otherwise are met with an informative message | Pass |
| 032| Log in as student | User is able to log in with their email and password | Pass |
| 033| View details | In the user's Account page, they can view their details in a read-only display. | Pass |
| 034 | Display number of books to review | In the user's Account page, they will see how many books they have left to review, or else a message congratulating them on reviewing all books | Pass |
| 035 | Create review books available | When creating a new review, only books the user has not yet reviewed will be available in the dropdown | Pass |
| 036 | Create review incomplete fields | The user cannot proceed when review fields are missing content | Pass |
| 037 | Create review | On completing all fields, the user can publish a review successfully. It will be immediately displayed in the list in their Account, and their books available will reduce by 1 | Pass | 
| 038 | Update review required fields missing | If the user tries to update a review, they will be unable to proceed if fields are blank | Pass |
| 039 | Update review | On changing field(s), when the user submits then the review is updated and changes are reflected immediately. | Pass |
| 040 | View reviews | The user is able to view all their reviews in full, with buttons to update or delete each one | Pass |
| 041| Delete review modal | If the user presses the Delete button, a modal appears asking them if they are sure. If they press Cancel the box closes, and their reviews are left unchanged. | Pass |
| 042 | Confirm deletion | If the user confirms deleting their review, then the review is removed from their reviews page successfully, their books_read is decremented by 1, the review is removed from the list in their Account page, and the associated book becomes available to review again. | Pass |
| 043| All books reviewed | When the user has submitted a review for each book, they can no longer access the create review screen. Instead they have a notification congratulating them on their work. | Pass |
| 044| Log out | On pressing the log out button, the user is logged out of their account and returned to the login page | Pass |


- It was identified that form fields were still missing 'Required' tags, causing tests to fail. This has been resolved.

## Known Defect
- During testing it became evident that a defect exists within both student and teacher update forms, where the user is able to update the user's email to an address that exists within another account. 
- In a live system, this would be unlikely to happen but where it did, probably through user error, it would cause significant issues for the affected records.
- I tried to remedy this by adding logic to check if the email address already exists, but that prevents the update altogether. 
- The form update as it is relies on the email address; I am reluctant to change this by removing the email from the form, as I do not have sufficient time to conduct regression testing against the change I would need to make to two different methods. 
- The defect is therefore staying in the system, and is a lesson learned in regards to authentication for myself. 

## Device & Browser testing 
- System testing took place on the follwoing devices:
- MacBook Air
- iPhone 12
- Unfortunately, no tablet was available for testing. I have used Chrome's Inspect tool for various tablets, however I know from experience this has limited accuracy. 

And on the following browsers:
- Safari
- Chrome
- Mozilla Firefox


# Deployment 
The following outlines the steps required to deploy the site:

## Basic Requirements
- IDE
- GitHub repository
- Heroku account
- Stripe account
- AWS S3 account
- Gmail account

## ElephantSQL
ElephantSQL was used to host the database.
- Navigate to [ElephantSQL](https://elephantsql.com)
- Click ‘Get a managed Database today”
- Select the Tiny Turtle option
- Select ‘Login with GitHub’ and authorize connection with your GitHub account
- Enter a team name and your email address, agree to ToS & GDPR then click ‘Create Team’
- Click ‘Create New Instance’
- Give your new plan a name and select the Tiny Turtle plan
- Press ’Select Region’ and pick the nearest location to yourself
- Click ‘Review’ and check your details are correct
- Click ‘Create Instance’

## Program modification
In order to connect with Heroku, the following amendments are required to the program:
- In your command line, enter: pip freeze — local > requirements.txt
- Within the root directory, create a file called Procfile
- Enter in this file: “web: python run.py”
- Open your settings file and make the following amendments to your if/else statement: 
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
- Save, push and commit changes

## Heroku
- Log into [Heroku](https://heroku.com), click ‘New’ 
- Click ‘Create a new app’
- Choose a unique name
- Select the region closest to yourself
- Click ‘ Create app’
- Go to Settings of the app
- Click ‘Reveal Config Vars’
- Return to ElephantSQL and copy the database URL found within Details
- In Heroku, add a Config Var called DATABASE_URL and paste the ElephantSQL URL in, then press ‘Add’
- Navigate to ‘Deploy’
- Select ‘Connect to GitHub’
- Search for your repository then click ‘Connect’

## Deployment
- Back in the IDE, run python3 manage.py makemigrations then python3 manage.py migrate.
- Run python3 manage.py loaddata categories, then python3 manage.py loaddata products.
- Create a superuser to access the Django admin panel 
- Install the Heroku CLI and log in with heroku login -i.
- Run heroku config:set DISABLE_COLLECTSTATIC=1 --app appnamehere.
- Run git add ., git commit -m "Your commit message here", git push.
- Add the hostname of your Heroku app to 'ALLOWED HOSTS' in your settings.py file. 
- Connect Heroku to Git by running: git remote add heroku {heroku git url}.
- Go to the 'Deploy' tab in Heroku, and click 'Enable Automatic Deployment'.
- Click 'Deploy Branch' to deploy your app onto the Heroku servers.
- Once the app has finished building, click 'Open App' to open your site.

## AWS
- In AWS S3, create a new bucket
- In Properties, turn on static website hosting.
- In Permissions, set up the CORS config to link Heroku and your S3 bucket.
- Go to 'Bucket Policy' >  'Edit' > 'Policy Generator'.
- In 'Select Type of Policy' choose 'S3 Bucket Policy'.
- In 'Add Statements', select 'Effect' of Allow, enter * into 'Principal', in 'Actions' choose GetObject, enter your ARN from your main S3 Bucket page, and click 'Add Statement'.
- Click 'Generate' and copy and paste your generated policy into the Bucket Policy area.
- Add /* at the end of the 'Resource' line, and save.
- Still in 'Permissions', go to the 'Access Control List', and select List next to 'Everyone'.

## IAM 
- Go to 'User Groups' > 'Create New Group', enter a name and click 'Create'.
- In 'Policies' navigate to 'Create New Policy' > 'JSON' > 'Import Managed Policy' > 'S3' > 'AmazonS3FullAccess' > 'Import'.
- Get the ARN from 'S3 Permissions'
- Click 'Next', 'Review', provide a name and description, and click 'Create Policy'.
- Go to 'User Groups' > 'Find New Group' > 'Permissions' > 'Add Permissions' > 'Attach Policies', then find the policy you created and click 'Add Permissions'.
- Go to 'Users', provide a name, and tick the checkbox beside 'Access key - Programmatic access'.
- Click 'Next', select the group you created, and click through to the end.
- Finally, click 'Create User' and download the CSV file, which will contain your AWS_SECRET_ACCESS_KEY and your AWS_ACCESS_KEY_ID. 

## Complete deployment
- Remove the DISABLE_COLLECTSTATIC variable from your environment variables.
- S3 now contains a static folder with your files.
- Create a media file in your S3 Bucket, click 'Upload'.
- Click 'Add Files', then select all your product images.
- Under 'Manage Public Permissions', select 'Grant Public Read Access'.
- Click Upload

## Change Email
- Log in to your GMail
- Go to Settings > Accounts and Imports > Other Google Account Settings
- Go to the 'Security' tab, and scroll to 'Signing in to Google'.
- Click on '2-step Verification', click 'Get Started', and enter your Gmail password.
- Turn on 2-step verification.
- Back in Security, go back to 'Signing in to Google', then go to 'App Passwords'.
- Enter your password again if prompted, then set 'App' to 'Mail', 'Device' to 'Other', and type in Django.
- Copy and paste the passcode that shows up, this is your 'EMAIL_HOST_PASS' variable.

# References

## Code
- Gallery Home Page: ![W3 Schools](https://www.w3schools.com/howto/howto_css_image_grid_responsive.asp)



## Images


## Media
- [Font Awesome](https://fontawesome.com/) for icons throughout the project
- [Google Fonts](https://fonts.google.com/) for the fonts used in the project

