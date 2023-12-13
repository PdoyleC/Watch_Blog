# Welcome to the **[Watch Blog](https://watch-blog-1e2436fde037.herokuapp.com/)**

## [Link, to live project](https://watch-blog-1e2436fde037.herokuapp.com/)

![Watch on wrist image](documentation/watch.jpg)

## **Purpose of the site**
<p>This site is a blog style watch site, aimed at people interested in Watches and new Watches on the market.</p>

## Design
<details>
<summary>Watch Favicon Image</summary>

- the watch logo was created in Publisher, and can be found in the documentation folder. 
- Paint was used to design the image.
- favicon was used for website image tab [Link](https://favicon.io/favicon-converter/)
  

![Watch on wrist image](documentation/paintfco.jpg)
</details>


<details>
<summary>Database schema diagram</summary>

This was completed using [DrawSQL](https://drawsql.app/)


![Database structure](documentation/drawsql.png)

</details>

## Features
<details>
<summary>NavBar</summary>
For authenticated users it links to:

- Home Page
- About page
- Write a Post Page
- Logout Page
- Welcome User Name display

![NavBar image](documentation/navbar.png)
</details>
<details>
<summary>NavBar Not signed in</summary>
For authenticated users it links to:

- Home Page
- About page
- Register Page
- Login Page
  
![NavBar not signed in image](documentation/navbarnotreg.png)
</details>
<details>
<summary>Footer</summary>

- Links to facebook, Twitter, GitHub, Instragram and Youtube

![Footer image](documentation/footer.png)
</details>
<details>
<summary>About Page</summary>

-Contains info about the site.

![About page image](documentation/aboutpage.png)
</details>
<details>
<summary>Registration Page</summary>

- Where new users are able to create an account to post an article. 
![Registration page image](documentation/regpage.png)
</details>
<details>
<summary>Edit & Delete button</summary>

- Where users can Edit and delete a post that they have created, this is only visible if your the author of the post. 

![Delete image](documentation/delete.png)
</details>
<details>
<summary>Delete Confirmation Page</summary>

- Just a check to see if the user wants to delete there post.

![Delete page image](documentation/deletepage.png)
</details>

## Languages Used

- [HTML](https://en.wikipedia.org/wiki/HTML/)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)

## Manual Testing
- There are some features that are only visible when the user is logged in. 
<details>
<summary>Manual Testing</summary>

**User Not Registered**

- If there is no user logged in, The home page won't show Crate a post.
- The user will be able to see a post entry but won't be able to add a comment.
- The user isn't able to edit or deleted a post unless its a post that the user has created.

<details>
<summary>Login and Not Logged in Page</summary>

![Watch on wrist image](documentation/testing/notlogin.png)
![Watch on wrist image](documentation/testing/notlogincom.png)
</details>


**User Registered**

- If a user is registered, they will be able to create a post.
- If the user has created a post, that user will be able to edit and deleted there own post.
- If the user isn't the creator of the post the user can't edit or deleted the post, only add coments.
- Alert messages appear when a use has logged in, logged out, a comment added, a post is edited and a when a post is deleted.

**Checks Completed**
- The following check have been conpleted
  

|Test|       Action                             |   Result                                                                  |Done   |
|----|------------------------------------------|---------------------------------------------------------------------------|-------|
| 1  |  Login is Clicked                        |  Redirected to login page                                                 | PASS  |
| 2  |  Watch Blog logo clicked on about page   |  Redirected to home page                                                  | PASS  |
| 3  |  Register is Clicked	                    |  Redirected to Sign up page                                               | PASS  |
| 4  |  Login is Clicked	                    |  Signed in and redirected to Blog home page                               | PASS  |
| 5  |  Logout is clicked 	                    |  Redirected to Sign out page, sign out clicked, and sign out              | PASS  |
| 6  |  Home page clicked post entry	        |  Directed to post entry.                                                  | PASS  |
| 7  |  Bolg Post edit/delete post	            |  <details><summary>Not correct user, can't edit or delert post</summary><img src="./documentation/testing/notlogincom.png"></details>                              | PASS  |
| 8  |  Create a Post	                        |  Redirected to create a post page                                         | PASS  |
| 9  |  Create a Post page	                    |  No title entered, post button clicked, error field appears               | PASS  |
| 10 |  Create a Post page	                    |  No Contect entered, post button clicked, error field appears             | PASS  |
| 11 |  Create a Post page	                    |  No image entered, post button clicked,default image  appears in blog     | PASS  |
| 12 |  Bolg Post edit, creator	                |  <details><summary>Edit button visible</summary><img src="./documentation/testing/editingpost.png"></details>                                                      | PASS  |
| 13 |  Bolg Post delete, creator	            |  <details><summary>Delete button visible</summary><img src="./documentation/testing/editingpost.png"></details>                                                    | PASS  |
| 14 |  Delete button clicked	                |  Confirmation button appears                                              | PASS  |
| 15 |  Blog home page, comment icon clicked.	|  Redirect to blog post                                                    | PASS  |
| 16 |  Comment icon	                        |  Correct number on blog page and home page                                | PASS  |
| 17 |  Like heart button clicked on blog page	|  Increments number by 1                                                   | PASS  |
| 18 |  heart icon	                            |  Correct number on blog page and home page                                | PASS  |
| 19 |  Footer, clicking facebook icon	        |  <details><summary>Redirected to facebook</summary><img src="./documentation/testing/footerlinks.png"></details>                                                   | PASS  |
| 20 |  Footer, clicking Twitter (x) icon	    |  <details><summary>Redirected to Twitter</summary><img src="./documentation/testing/footerlinks.png"></details>                                                | PASS  |
| 21 |  Footer, clicking Github icon	        |  <details><summary>Redirected to Github</summary><img src="./documentation/testing/footerlinks.png"></details>                                                     | PASS  |
| 22 |  Footer, clicking Instagram icon	        |  <details><summary>Redirected to Instagram</summary><img src="./documentation/testing/footerlinks.png"></details>                                                  | PASS  |
| 23 |  Footer, clicking Youtube icon	        |  <details><summary>Redirected to Youtube</summary><img src="./documentation/testing/footerlinks.png"></details>                                                 | PASS  |
| 24 |  Message alert for Signed in	            |  <details><summary>Alert Appears</summary><img src="./documentation/testing/alerts.png"></details>                                                            | PASS  |
| 25 |  Message alert for Signed out	        |  <details><summary>Alert Appears</summary><img src="./documentation/testing/alerts.png"></details>                                                            | PASS  |
| 26 |  Message alert for post edited	        |  <details><summary>Alert Appears</summary><img src="./documentation/testing/alerts.png"></details>                                                            | PASS  |
| 27 |  Message alert for post deleted	        |  <details><summary>Alert Appears</summary><img src="./documentation/testing/alerts.png"></details>                                                            | PASS  |
| 28 |  Message alert for comment added	        |  <details><summary>Alert Appears</summary><img src="./documentation/testing/alerts.png"></details>                                                            | PASS  |
| 29 |  Next and Prev buttons	                |  Direct to next and Prevous pages                                         | PASS  |


|Test|     Post Detail Page                     |   Result                                                                  |Done   |
|----|------------------------------------------|---------------------------------------------------------------------------|-------|
| 1  |  Edit button                             | Visable for authenticated user of post                                    | PASS  |
| 2  |  Edit button                             | Isn't Visable for unauthenticated user of post                            | PASS  |
| 3  |  Deleted button	                        | Visable for authenticated user of post                                    | PASS  |
| 4  |  Deleted button	                        | Isn't Visable for unauthenticated user of post                            | PASS  |
| 5  |  Add comment button 	                    | Visable for authenticated user of the site                                | PASS  |


|Test|     Sign Up page                         |   Result                                                                  |Done   |
|----|------------------------------------------|---------------------------------------------------------------------------|-------|
| 1  |  Valid info, submitted                   | Redirected to blog                                                        | PASS  |
| 2  |  Invalid info, submitted                 | Error message appears                                                     | PASS  |
| 3  |  Sign Up button	                        | Hover over, colour changes                                                | PASS  |
| 4  |  Sign Up button clicked	                | Signed up and redirected to Blog home page                                | PASS  |

|Test|     Logout Page                          |   Result                                                                  |Done   |
|----|------------------------------------------|---------------------------------------------------------------------------|-------|
| 1  |  Sign Out button                         | Hover over, colour changes                                                | PASS  |
| 2  |  Sign Up button clicked                  | Redirected to Blog home page, Alert message appears                       | PASS  |


|Test|     Logout Page                          |   Result                                                                  |Done   |
|----|------------------------------------------|---------------------------------------------------------------------------|-------|
| 1  |  Sign In button                          | Hover over, colour changes                                                | PASS  |
| 2  |  Sign Up link clicked                    | Redirected to Sign Up page                                                | PASS  |
| 3  |  Invalid Username/Password	            | Asked to enter correct username                                           | PASS  |

|Test|     Create Post Page                     |   Result                                                                  |Done   |
|----|------------------------------------------|---------------------------------------------------------------------------|-------|
| 1  |  Link to Go Back pressed                 | Redirected to Blog/Home page                                              | PASS  |
| 2  |  Link to Go Back pressed                 | Redirected to Blog/Home page                                              | PASS  |





</details>



## Deplyoment

The website uses [ElephantSQL](https://www.elephantsql.com/) for its database.

- I signed up with my GitHub account.
- I created a new instance and the free plan was selected and Europe was selected as the region.
- Once created I was able to access the url and password for the database.

The website uses [Cloudinary](https://cloudinary.com/) for storing images.

- I created an account in Cloudinary.
- I copied the API environment variable over to the code.

The website was deployed to [Heroku](https://heroku.com/) by following these steps:

- I created a new app/Project.
- Inside the project settings tab and clicked reveal configuration vars
- I added the following configuration vars: CLOUDINARY_URL, DATABASE_URL, PORT, SECRET_KEY - DISABLE_COLLECTSTATIC = Only for initial deployment-
- I went to the deploy tab and connected the GitHub repository
- Made sure DEBUG was set to False and removed DISABLE_COLLECTSTATIC in configuration vars.
- selected Deploy tab and clicked Main branch.
- clicked on Open app.

## Issues

- SummerNote wasn't connecting because of Django clickjacking [Link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options).
- Tried to have a Conyact Us page on the site, but the was an issue with Elephant sql and a corrupt database.

## Technologies Used

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [Favicon.io](https://favicon.io/) has been used for the favicon.
- [GitHub](https://github.com/PdoyleC/Watch_Blog) repository has been used for hosting the code.
- Cloudinary has been used to store media files.
- [Font Awesome](https://fontawesome.com/icons) has been used for icons.
- ElephantSQL has been used as database solution.

### Frameworks, Libraries & Programs Used
- [Cloudinary](https://cloudinary.com/)  used to upload, store, manage, and link images.
- [Django](https://www.djangoproject.com/) is a free Python-based web framework that encourages rapid development with model–template–views.
- [Font Awesome](https://fontawesome.com/) is a font icons toolkit for aesthetic buttons and links.


## Security
- The SECRET_KEY has been changed since the second commit / push to GitHut, and env.py placed into gitignore. 

## Credits

- Photos saved in Cloudinary and images taken by myself and images from [Pxhere](https://pxhere.com/),[Pexels](https://www.pexels.com/),[Unsplash](https://unsplash.com/).

## Credits

- This website was built by following the walkthrough project Django Blog by Code Institute.
- Dj-ango Generic view documentation: [Django Generic view](https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-display/).
- Django admin site documentation: [Django admin site](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display).
- Django URL dispatcher documentation: [Django URL dispatcher site](https://docs.djangoproject.com/en/3.2/topics/http/urls/#how-django-processes-a-request).
- SummerNote, editor for the Posts: [SummerNote](https://summernote.org/).
- Single sign in for a site: [django-allauth site](https://docs.allauth.org/en/latest/).
- Building a blog application with Django [Django app build](https://djangocentral.com/building-a-blog-application-with-django).
- CSRF, Cross-Site Request Forgery, protection against attackers, [CSRF](https://docs.djangoproject.com/en/3.2/ref/csrf/).
- Django Crispy Forms for built-in template packs, [Crispy Link](https://django-crispy-forms.readthedocs.io/en/latest/index.html).
- Alerts in bootstrap [Alerts](https://getbootstrap.com/docs/5.0/components/alerts/).
- To highlight the current page with an underline, [W3 schools](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_active_element2),
[Stack overflow L1](https://stackoverflow.com/questions/72685196/how-to-highlight-the-current-section-the-user-is-viewing-in-javascript),
[Stack overflow L2](https://stackoverflow.com/questions/20410623/how-to-add-active-class-to-html-actionlink-in-asp-net-mvc),
[Stack overflow L3](https://stackoverflow.com/questions/62451903/how-i-can-underline-the-current-page-inside-my-bootstrap-nav),
[Stack overflow L4](https://stackoverflow.com/questions/26819675/navbar-highlight-for-current-page).
- Code for deleting a post was used from [Stackoverflow](https://stackoverflow.com/questions/31843145/deleteview-with-confirmation-template-and-post-method).
- Message Alerts when signed in and out in bootstrap [Message Alerts](https://ordinarycoders.com/blog/article/django-messages-framework).
- Python Django video Tutorial: [Full-Featured Web App](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
- Django Blog Application video Tutorial - [Full Tutorial 2022](https://www.youtube.com/watch?v=I8TRkEcw9Mg)
- Django For Everybody video Tutorial - [Full Python University Course](https://www.youtube.com/watch?v=o0XbHvKxw7Y)
- Build a Social Media App with Django video Tutorial [Python Web Framework Tutorial](https://www.youtube.com/watch?v=xSUm6iMtREA)
- Codemy.com- video Tutorial [Create A Simple Django Blog](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)
- Codemy.com- video Tutorial [Stack overflow](https://stackoverflow.com/questions/534839/how-to-create-a-guid-uuid-in-python)

<https://stackoverflow.com/questions/534839/how-to-create-a-guid-uuid-in-python>

## Credits to Tutor support

- The following tutors online at CI, guided and helped me during this project - Osin, John, Rebecca, Martin, Gemma, Joanne, jason, Kevin, Sean.
