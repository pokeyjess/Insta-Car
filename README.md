# Welcome to InstaCar, our awesome Capstone project!

By Jess, John, Ken and Lori.

SE-OCT-2019

This is our final project for Kenzie Academy, a group effort. We have created an Instagram-like photo-sharing service, geared specifically for car enthusiasts.

<img width="1221" alt="Screen Shot 2020-10-19 at 10 33 46 PM" src="https://user-images.githubusercontent.com/65363804/96535690-61afbe80-1260-11eb-92c5-0497e1e2ab8a.png">

## Overview

From hot rods to Volkswagens to Teslas -- all cars are welcome at InstaCar! Search through our database to find pictures of your favorie models. Create a profile and begin uploading photos of your own. Along with a photo, you can tell us more about the car -- year, make, model, and go ahead and put a caption on it!

## Features

Users are able to create accounts with profile pictures, biographical information and a place to put a link to a website. We also collect e-mail addresses from new users, which can later be used for verification purposes, should we choose to wire that up.

The profile page shows all the posts made by that user. Unless you are on your own page, Follow/Unfollow buttons will appear, depending on whether you are following that person already. On your own page, options are available to edit or delete your account -- unless you are a staff member. In that case, you will have to go through the admin panel.

<img width="1029" alt="Screen Shot 2020-10-19 at 10 38 13 PM" src="https://user-images.githubusercontent.com/65363804/96535886-d71b8f00-1260-11eb-8a54-0b9c4f6164da.png">

When creating a new post, drop down menus give the user options for year (dating back to 1960), make and model. Other fields are filled in manually, such as "color" and "caption."

Each post, on either the profile page or homepage, links to a "post detail" page. There, you will see an enlarged version of the featured photo, along with more information about it. At the bottom, comments will appear. Only the person who wrote it can edit a comment, though comments can be deleted by both the author and the person who owns the post on which it appears.

A picture of the post's creator appears on the page, with a link back to that user's profile page.

The posts, as well as the individual comments, can be "liked" by users. Total likes are displayed.

<img width="1078" alt="Screen Shot 2020-10-19 at 10 08 22 PM" src="https://user-images.githubusercontent.com/65363804/96535980-0b8f4b00-1261-11eb-942b-15b269d0e0bb.png">

## Work in progress

We were on a deadline, so we were not able to implement every feature we wanted. We would still like to improve our search feature and add a tagging/notification system.

## Credits

Authors: Jessica Benson, Lori Henderson, Ken Stephens and John Wilkinson.

Clipart for the default images were from Clipart-library.com

Photos of cars, Jeeps and motorcycles used in the demo are courtesy of Ken Stephens and friends.

Our facilitator, Matthew Perry, did help us on a few of the finer technical points. Thanks, Matt!

## Acknowledgements

We'd each like to take this opportunity to give special thanks to those who have supported us over the past year.

Jess:

Thank you to my family -- Mum and Dad, Justine and Chris, and Craig, Shalini, Ila, Ravi and Sunna. I appreciate your support while undergoing this crazy mid-life career change. But most of all, thank you to my daughter, Leanne, for getting me into this Kenzie mess to begin with. To have someone to share the experience with, in all its joys and frustrations (and there have been many), has been priceless. I wouldn’t have even made it through the first half without you, child. Glad I could return the favor in the second half ;)

Lori:

Thanks to my parents who supported me throughout my Kenzie career. Special shoutouts to my Kenzie family who supported me and helped me grow, not only as an individual, but as a software developer. I wouldn't be where I am if it wasn't for all of them.

Ken:

I would like to thank each and every one of you for all you have done and for clarifying and assisting me with my roadblocks. I would also like to thank @sweetly_insane and @thatguyw_stat for allowing me to use their cars for this project.

## Requirements

To run the project, clone it to your local machine, and run "poetry install" to start up your virtual environment and install dependencies. Should you have any trouble, these are the dependencies you will need:

python = "^3.8"

django = "^3.1.2"

poetry >= "0.12"

django-cleanup = "^5.1.0"

pillow = "^7.2.0"

django-rotate-secret-key = "^0.3"
