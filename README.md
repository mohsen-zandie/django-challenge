# django-challenge

The volleyball Federation decided to use an online selling platform for the next season, and our company has been chosen for implementing that.

## Requirements

Our system should have REST APIs for the following tasks:

- User signup and login
- Adding a new stadium
- Defining matches
- Defining the place of seats for each match
- Buying seats of a match (There is no need for using a payment gateway)

## Implementation details

We don't need a GUI for this system. You can use the Django admin.
Try to write your code as **reusable** and **readable** as possible. Also, don't forget to **document your code** and clear the reasons for all your decisions in the code.
Using API documentation tools is a plus.
Don't forget that many people trying to buy tickets for a match. So try to implement your code in a way that could handle the load. If your solution is not sample enough for implementing fast, you can just describe it in your documents.

Please fork this repository and add your code to that. Don't forget that your commits are so important. So be sure that you're committing your code often with a proper commit message.

# Installation

To run the project and build the Docker image, use the following command:

`docker-compose up --build`


For running the project in the background, use the following command:

`docker-compose up --build -d`


To create a new app, use the following command:

`docker-compose exec backend sh -c "python manage.py startapp payments"`


# Usage

The project is designed to be used with the Django admin interface. The following endpoints are available as REST APIs:

- User signup and login
- Adding a new stadium
- Defining matches
- Defining the place of seats for each match
- Buying seats of a match

# Configuration

Ensure you have the required dependencies listed in the 'requirements.txt' file. Also, set up environment variables for the necessary configurations.

# Features

- User authentication and authorization
- Stadium and match management
- Seat allocation and ticket purchase

# File Structure

The main directories in the project include:

- `accounts/` - for user management
- `events/` - for defining matches
- `tickets/` - for handling seat allocation and ticket purchase
- `payments/` - for managing payments
- `stadiums/` - for adding new stadiums

# Dependencies

The project requires the following dependencies:

- Django
- Python Decouple
- Django Rest Framework
- Markdown
- Django Filter
- DRF-YASG
- Django Rest Framework Simple JWT
- Celery
- Redis
- Django Redis

# Testing

To run the tests, use the following command:

`docker-compose exec backend sh -c "pytest ."`



