<h1 align="center">HealthyRecipyApp</h1>

<p align="center">
<img src="assets/documents/README_docs/responsive-site.png" width="800" height="100%">
</p>

You can find live site [here](https://mmmm.herokuapp.com/)

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


# Welcome to the HealthyRecipy community!

# About HealthyRecipy App

HealthyRecipy is a community-driven project that aims to provide easy access to healthy recipes for individuals looking to maintain a balanced diet, lose weight, or simply enjoy nutritious meals. Our platform encourages users to share their favorite recipes, discover new ones, and customize meals to suit their taste preferences and dietary requirements.

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

|I want to.. | So that I can.. | Acceptance Criteria
| ----------- | ----------- | ----------- |
| Create an account | Store my personal recipes | 1: user can create account  2: user can log in  AC 3: user can log out
| Browse through recipes | Find some new meals ideas | 1: Admin created recipes are available to all users 2: Non logged in users can view admin created recipes 3: Non-logged in users have read only access |

**Epic:Logged in User**

|I can.. | So that I can.. | Acceptance Criteria
| ----------- | ----------- | ----------- |
| Create an account | Store my personal recipes | 1: user can create account 2: user can log in 3: user can log out  |
| Edit or delete my recipes | Update them  | 1: Edit recipes functionality 2: Delete recipes functionality 3: Only for user who created the recipe, 403 error returned otherwise |
| Add picture and description to my recipes  | I can easily find the one I am looking for  |  1: add picture when uploading recipes 2: Pictures automatically resized 3: Can add a  recipe description |
| Store my recipes in one place  | I can easily browse and retrieve them  |  1: Create list view of all user recipes 2: Make each object a link to the full recipe |
| View the ingredients and method for my recipes  | Follow the recipe without having to touch the screen |  1: Put ingredients and methods side by side so both available on md and lg screens without scrolling |
| Have a personalised home page | View my own recipes | 1: Have generic home page 2: Have logged in user home page 
| Categorise my recipes by cooking method | Plan my meals easily |  1: Have categories to choose from on add recipe  2: Be able to filter recipes using these categories |
| Be able to log into the same account as my family  | my household can share an account |  1: Be able to log in by username 2: Have keep logged in function available |
| Search my recipes | To quickly find the recipe I want  |  1: Search bar in navigation 2: search bar functionality added 3: Have a variety of parameters to search with |
| Add recipes to favourites | View my favourite recipes easily |  1: Create add favourite button 2: Apply to user or admin recipes 3: Display these on their own page 4: Have indicator on recipe to skow if favourite or not |


**Epic: Admin**

| I can... | So that I can... | Acceptance Criteria |
| ----------- | ----------- | ----------- |
| Create, edit and delete recipes and comments | Manage the site content | **AC1:** Admin can access a form to input new recipe details, including title, description, ingredients, and preparation steps.<br>
| Access the admin panel | Manage recipes and comments | **AC1:** Admin can log in to the admin panel using their credentials.<br>**AC2:** Upon successful login, admin is directed to the dashboard where they can manage recipes, comments, and site content.<br>**AC3:** Incorrect login attempts are handled gracefully, displaying an error message and the opportunity to retry. |
| Log out of the admin panel | Disconnect from the website securely | **AC1:** A log-out option is clearly accessible from anywhere within the admin panel.<br>**AC2:** Selecting the log-out option immediately ends the admin session.<br>**AC3:** Upon logging out, the admin is redirected to the login page, ensuring they are fully disconnected. |



# Scope

## Features

### **Home Page**

_Navigation bar:_

- The navigation bar appears on every page so users can easily navigate through the site
- Navigation bar has links for 'Home', 'My recipes', 'Healthy Recipes', 'Add Recipe' and icons for login/out, and search bar
- 'My recipes' link will take the user his/her 'Personalised Home Page' and a 

_Account - Login/Register:_

- The Login/Register feature is located in the upper right corner and offers the user to log in or register for an account as well as log out of the site
- When the user is logged in links for 'Login' and 'Register' will have access to their personalised recipe book.
- The admin user has extra access that allow them to add, update and remove recipes from the website

_Footer:_

- Appears on every page and contains Social links
- Social links are opened in a new tab to avoid dragging users from our site


<p align="center">
<img src="assets/documents/README_docs/gifs/home-page.gif" width="900" height="100%">
</p>

### **User Profile**

- A logged-in user can access to the Personalised Home Page, this page displayed links to personal details, previous orders and wishlist
- The personal details page is where the user can update their default shipping/billing address, change email address and password
- The previous order displays a list of all the orders previously made by the user


<p align="center">
<img src="assets/documents/README_docs/gifs/user-profile.gif" width="900" height="100%">
</p>

### **Admin**

- Admin can preform full CRUD functionalliy without having to enter the default 'admin panel' from django
- Admin can add recipes in the account menu from the navigation bar
- Admin can unsubscribe user
- Admin can edit/delete recipes from 'Healthy Recipes' page 



<p align="center">
<img src="assets/documents/README_docs/gifs/admin.gif" width="900" height="100%">
</p>


### **Healthy Recipes Page**

- The Healthy Recipes page shows all recipes 
- Each recipe has an image, recipe title, author, method of conservation, ingrdients list, cooking method
- Each book card takes users to the book details page

<p align="center">
<img src="assets/documents/README_docs/user-story-testing/epic_navigation/book-list.png" width="900" height="100%">
</p>

### **Categories**

- Categories dropdown from Navbar, allowing the user to access specific categories
- Categories:
  - Board Books
  - Pitcure Story Books
  - First Reads
  - Early Readers
  - Fiction Books
  - Non Fiction Books


