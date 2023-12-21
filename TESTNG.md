# Testing

Return back to the [README.md](README.md) file.


Manual testing is where the creator of the code/site does quality checks/tests on the code, this is completed step by step. The purpose of tests is to catch any bugs or issues in the site before going live.

Automated testing is where code is used to test the logic, set of instructions to validate a feature or expected outcome of the code/feature.

## Validator Testing

### HTML

Validator: [W3C Validator](https://validator.w3.org/).

- No errors or warnings to show for during the W3C Validator testing.

| Page     | Validator                                                                                                    | Result |
| -------- | ------------------------------------------------------------------------------------------------------------ | ------ |
| Blog     | <details><summary>Blog</summary>![Home page](documentation/testing/homeblog.png)</details>                   |  PASS  |
| Blog Post| <details><summary>Blog Post</summary>![Post](documentation/testing/blogpost.png)</details>                   |  PASS  |
| Login    | <details><summary>Login</summary>![Login](documentation/testing/login.png)</details>                         |  PASS  |
| Logout   | <details><summary>Logout</summary>![Logout](documentation/testing/logoutpage.png)</details>                  |  PASS  |
| Create   | <details><summary>Create</summary>![Create post](documentation/testing/createapost.png)</details>            |  PASS  |
| Contact  | <details><summary>Contact</summary>![contact page](documentation/testing/contactpage.png)</details>          |  PASS  |
| Register | <details><summary>Register</summary>![Register page](documentation/testing/regpage.png)</details>            |  PASS  |

<details>
<summary>W3C Validator Images</summary>

![Home page](documentation/testing/homeblog.png)
![Post](documentation/testing/blogpost.png)
![Login](documentation/testing/login.png)
![Logout](documentation/testing/logoutpage.png)
![Create post](documentation/testing/createapost.png)
![contact page](documentation/testing/contactpage.png)
![Register page](documentation/testing/regpage.png)
</details>

### CSS

Validator: [Jigsaw Validator](https://jigsaw.w3.org/css-validator/validator).
<details>
<summary>CSS Validation Image</summary>
No errors or warnings to show for during the CSS Validator testing.

![CSS validator](documentation/testing/css.png)
</details>

### JavaScript

Validator: [JSHint Validator](https://jshint.com/).
<details>
<summary>JS Validation Image</summary>
JSHint quality tool has been used to test the code, without finding any errros or warnings. THere is 1 underfined variable warning reported, were due to bootstrap.

![JS Validation](documentation/testing/script.png)
</details>

### Python

Validator: [CI Python Linter](https://pep8ci.herokuapp.com/).

| File     | Validator                                                                                         | Result |
| -------- | ------------------------------------------------------------------------------------------------- | ------ |
| Models   | <details><summary>Models</summary>![Model test](documentation/testing/modelpy.png)</details>      |  PASS  |
| Views    | <details><summary>Views</summary>![Views test](documentation/testing/viewspy.png)</details>       |  PASS  |
| Forms    | <details><summary>Forms</summary>![Forms test](documentation/testing/formspy.png)</details>       |  PASS  |
| Urls     | <details><summary>URLs</summary>![Home test](documentation/testing/urlpy.png)</details>           |  PASS  |
| Admin    | <details><summary>Admin</summary>![Admin test](documentation/testing/adminpy.png)</details>       |  PASS  |
| Settings | <details><summary>Settings</summary>![Setting test](documentation/testing/settings.png)</details> |  PASS  |

Settings py validation errors of line to long are from the original django configuration set up and are left for readability.

# Manual Testing

**User Registered**

- There are some features that are only visible when the user is logged in.
- User can create a post.
- User can edit their own post they created.
- User can leave a comment.
- User can delete their own post they created
  
**User Not Registered**

- If there is no user logged in, the home page won't show Crate a post.
- The user will be able to see a post entry but won't be able to add a comment.
- The user isn't able to edit or deleted a post unless it's a post that the user has created.

<details>
<summary>Login and Not Logged in Page</summary>

![not Logged in](documentation/testing/notlogin.png)
![not Logged in](documentation/testing/notlogincom.png)
</details>

**User Registered**

- If a user is registered, they will be able to create a post.
- If the user has created a post, that user will be able to edit and deleted their own post.
- If the user isn't the creator of the post the user can't edit or deleted the post, only add comments.
- Alert messages appear when a use has logged in, logged out, a comment added, a post is edited and a when a post is deleted.

**Image display**

- Code was added to the default image in index.html and alt text appear instead of the image. There is a comparison in the image below.

<details>
<summary>Image error</summary>

![Watch test](documentation/testing/watchalttest.png)
</details>

## Checks Completed

- The following check have been completed
  
|Test|       Action                             |   Result                                                                  |Done   |
|----|------------------------------------------|---------------------------------------------------------------------------|-------|
| 1  |  Login is Clicked                        |  Redirected to login page                                                 | PASS  |
| 2  |  Watch Blog logo clicked on about page   |  Redirected to home page                                                  | PASS  |
| 3  |  Register is Clicked	                    |  Redirected to Sign up page                                               | PASS  |
| 4  |  Login is Clicked	                    |  Signed in and redirected to Blog home page                               | PASS  |
| 5  |  Logout is clicked 	                    |  Redirected to Sign out page, sign out clicked, and sign out              | PASS  |
| 6  |  Home page clicked post entry	        |  Directed to post entry.                                                  | PASS  |
| 7  |  Bolg Post edit/delete post	            |  <details><summary>Not correct user, can't edit or delete post</summary><img src="./documentation/testing/notlogincom.png"></details>                              | PASS  |
| 8  |  Create a Post	                        |  Redirected to create a post page                                         | PASS  |
| 9  |  Create a Post page	                    |  No title entered, post button clicked, error field appears               | PASS  |
| 10 |  Create a Post page	                    |  No Content entered, post button clicked, error field appears             | PASS  |
| 11 |  Create a Post page	                    |  No image entered, post button clicked, default image  appears in blog    | PASS  |
| 12 |  Bolg Post edit, creator	                |  <details><summary>Edit button visible</summary><img src="./documentation/testing/editingpost.png"></details>                                                      | PASS  |
| 13 |  Bolg Post delete, creator	            |  <details><summary>Delete button visible</summary><img src="./documentation/testing/editingpost.png"></details>                                                    | PASS  |
| 14 |  Delete button clicked	                |  Confirmation button appears                                              | PASS  |
| 15 |  Blog home page, comment icon clicked.	|  Redirect to blog post                                                    | PASS  |
| 16 |  Comment icon	                        |  Correct number on blog page and home page                                | PASS  |
| 17 |  Like heart button clicked on blog page	|  Increments number by 1                                                   | PASS  |
| 18 |  heart icon	                            |  Correct number on blog page and home page                                | PASS  |
| 19 |  Footer, clicking facebook icon	        |  <details><summary>Redirected to Facebook</summary><img src="./documentation/testing/footerlinks.png"></details>                                                   | PASS  |
| 20 |  Footer, clicking Twitter (x) icon	    |  <details><summary>Redirected to Twitter</summary><img src="./documentation/testing/footerlinks.png"></details>                                                | PASS  |
| 21 |  Footer, clicking GitHub icon	        |  <details><summary>Redirected to GitHub</summary><img src="./documentation/testing/footerlinks.png"></details>                                                     | PASS  |
| 22 |  Footer, clicking Instagram icon	        |  <details><summary>Redirected to Instagram</summary><img src="./documentation/testing/footerlinks.png"></details>                                                  | PASS  |
| 23 |  Footer, clicking YouTube icon	        |  <details><summary>Redirected to YouTube</summary><img src="./documentation/testing/footerlinks.png"></details>                                                 | PASS  |
| 24 |  Message alert for Signed in	            |  <details><summary>Alert Appears</summary><img src="./documentation/testing/alerts.png"></details>                                                            | PASS  |
| 25 |  Message alert for Signed out	        |  <details><summary>Alert Appears</summary><img src="./documentation/testing/alerts.png"></details>                                                            | PASS  |
| 26 |  Message alert for post edited	        |  <details><summary>Alert Appears</summary><img src="./documentation/testing/alerts.png"></details>                                                            | PASS  |
| 27 |  Message alert for post deleted	        |  <details><summary>Alert Appears</summary><img src="./documentation/testing/alerts.png"></details>                                                            | PASS  |
| 28 |  Message alert for comment added	        |  <details><summary>Alert Appears</summary><img src="./documentation/testing/alerts.png"></details>                                                            | PASS  |
| 29 |  Next and Prev buttons	                |  Direct to next and Previous pages                                         | PASS  |


|Test|     Post Detail Page                     |   Result                                                                  |Done   |
|----|------------------------------------------|---------------------------------------------------------------------------|-------|
| 1  |  Edit button                             | Visible for authenticated user of post                                    | PASS  |
| 2  |  Edit button                             | Isn't Visible for unauthenticated user of post                            | PASS  |
| 3  |  Deleted button	                        | Visible for authenticated user of post                                    | PASS  |
| 4  |  Deleted button	                        | Isn't Visible for unauthenticated user of post                            | PASS  |
| 5  |  Add comment button 	                    | Visible for authenticated user of the site                                | PASS  |


|Test|     Sign Up page                         |   Result                                                                  |Done   |
|----|------------------------------------------|---------------------------------------------------------------------------|-------|
| 1  |  Valid info, submitted                   | Redirected to blog                                                        | PASS  |
| 2  |  Invalid info, submitted                 | Error message appears                                                     | PASS  |
| 3  |  Sign Up button	                        | Hover over, colour changes                                                | PASS  |
| 4  |  Sign Up button clicked	                | Signed up and redirected to Blog home page                                | PASS  |


|Test|     Contact Page                         |   Result                                                                  |Done   |
|----|------------------------------------------|---------------------------------------------------------------------------|-------|
| 1  |  Submit button                          | Hover over, colour changes                                                | PASS  |
| 2  |  Submit button clicked                  | Message sends, Alert message appears                                      | PASS  |
| 3  |  Submit button clicked                  | Django admin app is updated with contact name, email and message          | PASS  |


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


|Test|     404 Error   Page                     |   Result                                                                  |Done   |
|----|------------------------------------------|---------------------------------------------------------------------------|-------|
| 1 |  Incorrect page entered for 404 error	    |  <details><summary>404 error page</summary><img src="./documentation/testing/404errorpage.png"></details>                                                | PASS  |





## WAVE

- I used [WAVE](https://wave.webaim.org/)  (Web Accessibility Evaluation Tool) in chrome developer tools to test the website accessibility. WAVE is a tool that identifies ways to make a webpage more accessible to people with disabilities. WAVE scans the website for on-page and technical accessibility issues and errors to bring the site in line with recognized accessibility standards, like the Web Content Accessibility Guidelines (WCAG).

<details>
<summary>Wave Testing Image</summary>

![waveblog image](documentation/testing/waveblog.png)
</details>

## Lighthouse

- Lighthouse in chrome developer tool, was used to test the website for:
- Performance - how the page performs whilst loading.
- Accessibility - how accessible is the site for all users and how can it be improved.
- Best practices - how does the site conform to industry best practices.
- SEO - search engine optimization. Is the site optimized for search engine result rankings.


<details>
<summary>Lighthouse Testing Image</summary>

![waveblog image](documentation/testing/lighthouse.png)

- Performance is down to the images and their size.
- Best Practices  [Lighthouse](https://developer.chrome.com/docs/lighthouse/pwa/is-on-https)


</details>

# Automated Testing

- Some code was written for automated testing, more research and learning needs to go into this so I can learn how to code the tests and improve the auto testing function.

![autotest11 image](documentation/testing/autotest11.png)

![coverage image](documentation/testing/coverage.png)

![coverage html  image](documentation/testing/coveragehtml.png)

![Forms code image](documentation/testing/testformspy.png)

![Views code image](documentation/testing/testviewspy.png)

# Browsers compatibility

The website has been tested in the following browsers on desktop:

<details>
<summary>Chrome Test </summary>

![Chrome image](documentation/testing/chromotest.png)
</details>
<details>
<summary>Fire Fox Test </summary>

![Fire Fox image](documentation/testing/firefoxtest.png)
</details>
<details>
<summary>Edge Test </summary>

![Edge image](documentation/testing/edgetest.png)
</details>
