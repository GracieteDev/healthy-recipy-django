# healthy-recipy-django


## User Stories

As a non-logged in user:

|I want to.. | So that I can.. | Acceptance Criteria
| ----------- | ----------- | ----------- |
| Create an account | Store my personal recipes | 1: user can create account  2: user can log in  AC 3: user can log out
| Browse through recipes | Find some new meals ideas | 1: Admin created recipes are available to all users 2: Non logged in users can view admin created recipes 3: Non-logged in users have read only access |


As a logged in user:

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
