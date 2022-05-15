# Sandy Blog

## Description

This Application that allows writers to post blogs, edit and delete blogs. It also allows users who have signed up to comment on the blogs that has been posted by a writer. It also allows a person to subscribed to recieve email everytime a new blog is posted by a writer.


## Author

Sandra Dindi

You can view the site at:[]()

## User Stories
As a user I would like to:
* See various blogs posts 
* Allowed to subscribe to email service 
* Allowed to comment on blog posts
* A writer allowed to register
* A writer is allowed to Create blog,delete comments
* A writer is able to comment on pitches



## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display  blog posts | **On page load** | List of various blogs from writers is displayed in a page|
| Display random quotes from API | **On Tab link click** | Clickable links to open quote origins|
| Display tabs for login page  | **On page load** | Registered writers can log into their accounts and create,update and delete blogs and comments |
| Display tabs for Signup | **On page load** | Signup users are redirected to Log in |
| To create a blog post  | **On log in** |  writers  can create and post blogs|
|Users can subscribe in | on subscription | users can comment on blog posts


## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pip venv


### Cloning
* In your terminal:

        $ git clone git@github.com:Dindihub/Personal-blog.git
        $ cd personal-blog

## Running the Application
* Creating the virtual environment

        $ pip install virtualenv 
        $ virtualenv env
        $ source env/bin/activate
       


* To run the application, in your terminal:

        $ python3 manage.py 
        $ flask run

## Testing the Application
* To run the tests for the class files:

        $ python3  manage.py tests 

## Technologies Used
* Python3.8
* Flask

## Known Bugs
No known bugs

### License
MIT (c) 2022 **[Sandra Dindi](https://github.com/Dindihub/Personal-blog.git)**







