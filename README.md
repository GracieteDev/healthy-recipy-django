<h1 align="center">HealthyRecipyApp</h1>

<p align="center">
<img src="assets/documents/README_docs/responsive-site.png" width="800" height="100%">
</p>

You can find live site [here](https://mmmm.herokuapp.com/)

# About HealthyRecipy App

HealthyRecipy is a community-driven project that aims to provide easy access to healthy recipes for individuals looking to maintain a balanced diet, lose weight, or simply enjoy nutritious meals. Our platform encourages users to share their favorite recipes, discover new ones, and customize meals to suit their taste preferences and dietary requirements.


# Table of Contents

1. [UX](#ux)

   - [Strategy](#strategy)
   - [User Stories](#user-stories)

2. [Scope](#scope)

   - [Features](#features)
   - [Future Features](#future-features)

3. [Structure](#structure)

   - [Sitemap](#sitemap)
   - [Wireframes](#wireframes)
   - [Database schema](#database-schema)
   - [Business Model](#business-model)
   - [Marketing](#marketing)

4. [Surface](#surface)

5. [Technologies Used](#technologies-used)

6. [Testing](#testing)

7. [Deployment](#deployment)

8. [Credits](#credits)




# UX

## Strategy

Using the core UX principles I envisaged a Strategy, thinking about the features, goals, needs, and  target audience, they would benefit from.

### Features

- **Expansive Recipe Database**: From breakfast to dinner, find recipes that taste great and are good for you.
- **Customizable Meal Plans**: Tailor your meal plan according to your dietary needs, preferences, and fitness goals.
- **Nutritional Information**: Every recipe comes with detailed nutritional information to help you keep track of your calorie intake and nutrient balance.
- **Easy-to-Use Interface**: Our user-friendly platform makes it simple to search, find, and store your favorite recipes.
- **Community Contributions**: Share your own recipes with the community and explore creations from other health-conscious cooks.
- **Cross-Platform Accessibility**: Access HealthyRecipy from any device, ensuring you have your recipes and meal plans handy whether you're at home or on the go.

### Goals

- To make healthy eating accessible and appealing to a wide audience by providing a diverse range of recipes.
- To foster a supportive community of individuals who are passionate about healthy living and cooking.
- To empower users with tools and information that aid in making informed dietary choices.

### Needs

- An easy-to-use platform to store, categorise, and retrieve recipes. 
- Quick editing capabilities for personalizing recipes based on preferences. 
- Mobile-friendly access for convenience while shopping or cooking. 

### Target Audience

HealthyRecipy is designed for individuals of all ages who are interested in maintaining a healthy lifestyle through diet. Specifically, our platform caters to:

- **Age**: Adults of all ages, from young adults (18+) to seniors.
- **Occupation**: Includes but is not limited to busy professionals, parents, and students who are looking for quick, healthy meal solutions.
- **Interests**: Individuals with a keen interest in nutrition, cooking, and fitness. Those looking to lose weight, manage dietary conditions, or simply lead a healthier lifestyle.
- **Tech-Savviness**: Our platform is designed to be accessible for users with varying levels of technological expertise, from beginners to advanced.

By addressing the needs and challenges faced by our target audience, HealthyRecipy aims to be a comprehensive resource for anyone looking to enhance their dietary habits through healthy, delicious recipes.


## User Stories

**Epic:Non-logged in user**

| I want to... | So that I can... | Acceptance Criteria |
| ----------- | ----------- | ----------- |
| Create an account | Store my personal recipes | **AC1:** User can create an account through a registration form.<br>**AC2:** User can log in to their account using their credentials.<br>**AC3:** User can log out of their account, ensuring their session is securely ended. |
| Browse through recipes | Find some new meal ideas | **AC1:** Admin-created recipes are available to all users, ensuring wide accessibility.<br>**AC2:** Non-logged in users can view admin-created recipes, promoting discovery without the need for account creation.<br>**AC3:** Non-logged in users have read-only access to recipes, allowing browsing without the ability to alter content. |


**Epic:Logged in User**

| I can... | So that I can... | Acceptance Criteria |
| ----------- | ----------- | ----------- |
| Create an account | Store my personal recipes | **AC1:** User can create an account through a registration form.<br>**AC2:** User can log in to their account using their credentials.<br>**AC3:** User can log out of their account, ensuring their session is securely ended. |
| Edit or delete my recipes | Update them | **AC1:** Users can edit their recipes through an edit functionality accessible on their recipe pages.<br>**AC2:** Users can delete their recipes using a delete option available on their recipe pages.<br>**AC3:** Edit and delete functionalities are only available to the user who created the recipe; a 403 error is returned otherwise. |
| Add picture and description to my recipes | I can easily find the one I am looking for | **AC1:** Users can add a picture when uploading or editing recipes.<br>**AC2:** Pictures are automatically resized to fit the website’s layout.<br>**AC3:** Users can add a description to their recipes during the upload process. |
| Store my recipes in one place | I can easily browse and retrieve them | **AC1:** Users have a list view of all their recipes for easy browsing.<br>**AC2:** Each recipe in the list view is a clickable link that takes the user to the full recipe page. |
| View the ingredients and method for my recipes | Follow the recipe without having to touch the screen | **AC1:** Ingredients and method sections are displayed side by side on medium and large screens to minimize scrolling. |
| Have a personalised home page | View my own recipes | **AC1:** A generic homepage is available for all users.<br>**AC2:** Logged-in users see a personalized homepage displaying their own recipes. |
| Categorise my recipes by cooking method | Plan my meals easily | **AC1:** Users can select categories for their recipes when adding or editing them.<br>**AC2:** Users can filter recipes by these categories to find them more easily. |
| Be able to log into the same account as my family | My household can share an account | **AC1:** Users can log in using a username that allows multiple people to access the same account.<br>**AC2:** A "keep logged in" function is available for ease of access. |
| Search my recipes | To quickly find the recipe I want | **AC1:** A search bar is included in the site’s navigation.<br>**AC2:** The search bar functionality enables searching through recipes.<br>**AC3:** Users can search recipes using a variety of parameters. |
| Add recipes to favourites | View my favourite recipes easily | **AC1:** Users can add recipes to their favourites using a specific button.<br>**AC2:** This functionality applies to both user and admin recipes.<br>**AC3:** Favourite recipes are displayed on a dedicated page.<br>**AC4:** Recipes have an indicator to show if they are a favourite. |



**Epic: Admin**

| I can... | So that I can... | Acceptance Criteria |
| ----------- | ----------- | ----------- |
| Create, edit and delete recipes and comments | Manage the site content | **AC1:** Admin can access a form to input new recipe details, including title, description, ingredients, and preparation steps.<br>
| Access the admin panel | Manage recipes and comments | **AC1:** Admin can log in to the admin panel using their credentials.<br>**AC2:** Upon successful login, admin is directed to the dashboard where they can manage recipes, comments, and site content.<br>**AC3:** Incorrect login attempts are handled gracefully, displaying an error message and the opportunity to retry. |
| Log out of the admin panel | Disconnect from the website securely | **AC1:** A log-out option is clearly accessible from anywhere within the admin panel.<br>**AC2:** Selecting the log-out option immediately ends the admin session.<br>**AC3:** Upon logging out, the admin is redirected to the login page, ensuring they are fully disconnected. |



# Scope

## **Features**

### **Home Page**
*Navigation bar:* 
- The navigation bar appears on every page so users can easily navigate through the site
- Navigation bar has links for 'Home', 'My Recipes', 'Healthy Recipes', 'Add recipe' and 'Login/Register' more links will be shown to logged in users
- If the user is logged in then they can access pages that only authorized users can visit and use, they are: 'Favorite Recipes', 'Your Recipes' and  'Logout'. Otherwise, the user will be given the option to 'Register' or 'Login'
- A search bar is nested in the navbar to find recipes quickly
- The navbar is fully responsive, collapsing into a hamburger menu for medium and small screen size

<p align="center">
<img src="assets/images-features/navbar.png" width="100%" height="100%">
</p>


*Hero Image:*
- The hero image welcomes the user with a short message advertising what the website is about
- The Login / Register button will take users to the login page, if users do not have an account there is a link to the registration page

<p align="center">
<img src="assets/images-features/hero-image.png" width="100%" height="100%">
</p>

*Recently added recipes:*
- Recently Added section shows the latest published recipes so users can quickly see recently published recipes
- The Recently Added section is fully responsive, showing 4 recipe cards
- Each recipe takes the user to the recipe details page
- Users can also see title, image, author, date posted, short description and number of likes

<p align="center">
<img src="assets/images-features/recently-added-recipes.png" width="100%" height="100%">
</p>


*Most Loved Recipes:*
- Each recipe takes the user to the recipe details page
- At the bottom of the list there is a link to the Recipes page that takes users to the page with all the recipes
<p align="center">
<img src="assets/images-features/most-loved-recipes.png" width="100%" height="100%">
</p>


*Footer:*
- Appears on every page and contains social links
- Links are opened in a new tab to avoid dragging users from our site
<p align="center">
<img src="assets/images-features/footer.png" width="100%" height="100%">
</p>

### **Healthy Recipes Page**
- The Recipes page shows all the published recipes, recipes are shown in order from newest to oldest
- The site will paginate all recipe cards to display 6 to a page
- Each recipe card will display an image and title of the recipe
- Each recipe card takes users to the recipe details page 
<p align="center">
<img src="assets/images-features/all-recipes-page.png" width="100%" height="100%">
</p>

### **Login/Register**
- The Login / Register button takes users to the login page where they can also find a link to the Register page where they can create an account
<p align="center">
<img src="assets/images-features/signin.png" width="100%" height="100%">
</p>

<p align="center">
<img src="assets/images-features/register.png" width="100%" height="100%">
</p>

### **Favorite Recipes Page**
- Only logged in users can see Favorite Recipes Page
- The Favorite Recipes page shows all the recipes that the user liked
<p align="center">
<img src="assets/images-features/favourite-recipes-page.png" width="100%" height="100%">
</p>

### **My Recipes Page**
- The 'My Recipes' page displays all the recipes that user has created
- At the top there is an Add Recipe button which takes user to the add recipe page
- Each recipe has two buttons, Edit and Delete
- Edit button takes user to the edit page
- Clicking the Delete button will display the message asking the users if they are sure they want to delete that particular recipe
<p align="center">
<img src="assets/images-features/your-recipes-page.png" width="100%" height="100%">
</p>

### **Recipes Details Page**
- The Recipes Details Page displays all the information about the selected recipes
- At the top of the page, the recipe card will display Recipes name, author name, date posted and image
- The main body of the page contains short description of the recipe, ingredients and preparation steps
- Number of likes and comments are displayed after the preparation steps
- Commenting section is located at the end of the page, only logged in users can leave a comment
<p align="center">
<img src="assets/images-features/recipe-details-card-head.png" width="100%" height="100%">
</p>

<p align="center">
<img src="assets/images-features/recipe-details-body.png" width="100%" height="100%">
</p>

### **Add Recipe Page**
- On the Add Recipe page users can add their recipes to the website
- The user must fill in all the fields in order for the recipe to be published
- If the user doesn't fill in one of the fields the error message appears
- If the user doesn't provide their image, the default image is displayed
- The Add Recipe button is located at the end of the page
<p align="center">
<img src="assets/images-features/add-recipe.png" width="100%" height="100%">
</p>

### Future Features
- Categories
- Users settings
- Calories Intake/per meal
- Preparation time
- Notification for likes and comments

# Structure
 
 Simplicity helps users to quickly and easily access the app and navigate within the app.

#Apps in the project


# Wireframes



All wireframes were created used [draw.io](https://draw.io/)

Wireframes for each device are linked here:
- [Desktop](assets/documents/Images/wireframe_desktop_1.png)
- [Desktop](assets/documents/Images/wireframe_desktop_2.png)
- [Tablet](assets/documents/Tablet-wireframes)
- [Mobile](assets/documents/Mobile-wireframes)


# Database schema

<p align="center">
<img src="assets/images/database-schema.png" width="900" height="100%">
</p>

## Models
### **Recipe Model**


<p align="center">
<img src="assets/images/post-model.png" width="900" height="100%">
</p>

### **Comment Model**

<p align="center">
<img src="assets/images/comment-model.png" width="900" height="100%">
</p>


# Surface

## Design 

## Chosen Color 
Color palette from [Coolorpalettes][[https://colorpalettes.net/color-palette-4486/]

<p align="center">
<img src="assets/images/used-colors.png" width="800" height="300">
</p>

- **#** - Color for the navigation bar. Complements the hero image well.
- **#** - Color selected for the buttons. This hue was picked as it harmonizes with the page's overall aesthetic and enhances its appearance.
- **#** - Main body color of the site. Chosen for its compatibility with the page's design, this color offers a softer alternative to stark white.
- **#** - Chosen as the backdrop for the login/register sections, this color coordinates well with the adjacent image.
- **#** - Background color used for the footer.



## Font 
- Verdana, sans-serif - main font
- Nadira- for navbar logo and welcome message


# Technologies Used

## Languages 
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Python](https://www.python.org/)


## Frameworks, Libraries & Programs Used
[GitHub](https://github.com/) - Holds the repository of my project, GitHub connects to GitPod and Heroku.

[GitPod](https://gitpod.io/workspaces) – Connected to GitHub, GitPod hosted the coding space, allowing the project to be built and then committed to the GitHub repository. 

[Heroku](https://www.heroku.com/) - Connected to the GitHub repository, Heroku is a cloud application platform used to deploy this project so the backend language can be utilised/tested. 

[Django](https://www.djangoproject.com/) - This framework was used to build the foundations of this project

[Gunicorn](https://gunicorn.org/) - Gunicorn is a pure-Python HTTP server for WSGI applications.

[Dj Database URL](https://pypi.org/project/dj-database-url/) - This allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.

[Bootstrap](https://getbootstrap.com/) - Used to quickly add design to my website, Bootstrap focuses on mobile first design meaning this website is responsive across multiple devices ans screen sizes. 

[Cloudinary](https://cloudinary.com/?utm_source=google&utm_medium=cpc&utm_campaign=Rbrand&utm_content=492438439811&utm_term=cloudinary&gclid=Cj0KCQiAt8WOBhDbARIsANQLp96hTerzfFJ_P9lX0tEYEdtM3tSsYB6fhw-x3wQxOO0oc4hXm-A2ZBUaAptIEALw_wcB) - Used to store images online for the recipe posts. 

[Summernote](https://summernote.org/) Used to add a text area field to the admin setup to enable a list of ingredients and method steps.

[Google Fonts](https://fonts.google.com/https://fonts.google.com/) - provide fonts for the website.

[Font Awesome](https://fontawesome.com/) -was used for icons.

[Drawio](https://draw.io/) - was used to create site wireframes.

[Am I Responsive](http://ami.responsivedesign.is/) - to check if the site is responsive on different screen sizes.

[Pixabay](https://pixabay.com/) and [Unsplash](https://unsplash.com/) - were used for all the images

[W3C Markup Validator](https://validator.w3.org/#validate_by_input) - was used to validate HTML

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - was used to validate CSS

[Beautify](https://www.jpkc.com/tools/beautify/) - was used to correct indentation issues and get rid of too much whitespace - HTML, CSS

[Coolors]- to make color palette


# Testing


## User Story Testing

### **Testing Users Stories form (UX) Section**

**EPIC: Superuser / Admin**

**EPIC: User Interaction**


**EPIC: User Recipes**


**EPIC: Login/Register**

## Bugs and Issues
-

# Deployment
This project was deployed using Github and Heroku.

## Github 
To create a new repository I took the following steps:

- Logged into Github.
- Clicked over to the ‘repositories’ section.
- Clicked the green ‘new’ button. This takes you to the create new repository page.
- I am using VS Code therefore I creatdd my own template from scrath and also setup my virtual environment in the VS Code terminal.
- I created the repository for this project in GitHub and then I open it via GitHub Desktop and cloned it to my local machine.
- I then open the repository in VS Code and worked and estabished the virtual environment via Git Bash.


## Django and Heroku 
- To get the Django framework installed and set up I followed the Code institutes [Django Blog cheatsheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)

# Credits




## Media
- All images were taken from


## Acknowledgements



