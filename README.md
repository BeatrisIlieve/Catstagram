# <p align="center"> *Catstagram* </p>
### <p align="center"> The project covers the following functionalities: user registration, login, and logout; each user can add cats to their profile and upload cat photos; a user can view all photos of cats, open details, can like and comment on a photo. Each user can edit and delete their photos and cat information. </p>
## Solution:
### 1. **Models**
#### CatstagramUser
- `Email`
- `Password`
#### Profile
- `First Name`
- `Last Name`
- `User`
#### Cat
- `Cat Name`
- `Cat Photo`
- `Slug`
- `Date of birth`
#### PhotoComment
- `Text`
- `Publication Time`
- `Photo`
- `User`
#### PhotoLike
- `Photo`
- `User`
#### Photo
- `Photo`
- `Description`
- `Location`
- `Publication Date`
- `Tagged Cats`
- `User`
### 2. **Structure**
#### Navigation Bar
- `Petstagram button` that leads to the home page
- `Add Pet button` that leads to the pet add page
- `Add Photo button` that leads to the photo add page
- `Login button` that leads to the login page (visible only to unauthenticated users)
- `Register button` that leads to the register page (visible only to unauthenticated users)
- `Profile button` that leads to the user profile details page (visible only to authenticated users)
- `Logout button` that logs out the logged-in user (visible only to authenticated users)
#### Home Page
- `Search Bar`
- `Cat Photos`
- `Like Button`
- `Total Lekes`
#### 404 Page Not Found
#### Registration Page
- `Email`
- `Password`
#### Login Page
- `Email`
- `Password`
- When a user is logged in he/she is redirected to the Home page
#### Profile Details Page
- `Edit button`
- `Delete button`
- `Total number of photos`
- `Total number of likes`
- `Total number of pets`
- Else `No posts yet`
#### Profile Edit Page
- `Email`
- `First Name`
- `Last Name`
#### Profile Delete Page
- `Are you sure you want to delete your profile?`
- `Yes`
- `Go Back`
-  If the user clicks on the "Yes" button the profile is deleted, and all the user's photos, cats and likes as well, and the user is redirected to the Home page
#### Cat Add Page
- `Cat Name`
- `Date of Birth`
- `Upload image field`
