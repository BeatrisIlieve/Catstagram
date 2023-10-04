# <p align="center"> *Catstagram* </p>
### <p align="center"> The project covers the following functionalities: user registration, login, and logout; each user can add cats to their profile and upload cat photos; a user can view all photos of cats, open details, can like and comment on a photo. Each user can edit and delete their photos and cat information. </p>
## Structure:
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

