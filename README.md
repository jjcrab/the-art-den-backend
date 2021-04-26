# The Little Art Den (backend)

This repo is the backend of the project The Little Art Den (TLAD)https://github.com/jjcrab/the-art-den

## Tech stack

Python, Django, PostgreSQL, AWS S3, Docker

## Deployment:

https://pacific-badlands-47817.herokuapp.com/

## Docker Image:

https://hub.docker.com/r/jingjingli/artden

## List of Model

### A user model

- Email (".edu" is required for stretch goal)
- Username

### A student-profile model with their personal information (connect this one to the user model for their authentication details)

- Name
- Avatar
- School
- Graduation year
- Personal story

### An artwork model (many-to-one relationship with the student-profile because each student will want to sell more than one piece of art)

- Title
- Artwork Image
- Price
- Added time

### Customer/Vistor

- email
- username

### MVP

- Docker/VM setup
- Setup all the modules
- CRUD
- User auth (only the student owner of the artwork can update/delete their own works of art).

### Stretch

- Build customer user account
