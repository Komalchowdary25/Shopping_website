ShopSphere – E-Commerce Web Application
A full-stack e-commerce web application built using Python, Django, HTML, CSS, and SQLite that allows users to browse products, view product details, and experience a basic online shopping workflow. The application demonstrates Django’s MVT architecture, template rendering, static file handling, and database integration.

Live Demo
Live Demo:https://shopping-website-1-jh4k.onrender.com 

Tech Stack
Backend: Python, Django (MVT Architecture)
Frontend: HTML, CSS, Django Templates
Database: SQLite
Authentication: Django Built-in Authentication System
Version Control: Git & GitHub

User Roles & Access Control
The system supports two types of users using Django’s authentication system.

1) Guest User (Not Logged In)
Guest users can browse the website but have limited functionality.
Permissions:
View all products on the homepage
Search products by name, description, price, or category
View product details
Browse products by category
View trending products
View products with offers
Access informational pages like Know Us and Support
Guest users cannot add items to cart or manage profile without logging in.

2) Registered User (Authenticated User)
Registered users have full access to shopping functionality.
Permissions:
Authentication & Profile Management
Register a new account
Login and logout securely
View user profile
Update profile information
Reset password
Recover password using username
Product Interaction
Browse all available products
Search products using keywords
View product details
Cart Management
Add products to cart
Increase product quantity in cart
Decrease product quantity in cart
Remove products from cart
View cart with total price calculation
Shopping Experience
View trending products
View special offer products
View cart item count in navigation bar
Functionalities Implemented

The application includes the following major modules:
Product Management
Products contain the following information:
Product name
Description
Category
Price
Product image
Trending flag
Offer flag
Products can be filtered by category, trending products, and special offers.
Product Search
Users can search products based on:
Product name
Description
Category
Price
Search results display matching products dynamically.
Shopping Cart System

The cart system allows users to:
Add products to cart
Modify product quantities
Remove items from cart
Automatically calculate total cart price
The system ensures that:
Quantity updates correctly
Total price is dynamically updated
Each user has their own cart
Authentication System
Authentication is implemented using Django's built-in authentication framework.

Features include:
User registration
Login authentication
Logout functionality
Password reset
Forgot password recovery

Sensitive pages are protected using:
@login_required decorator
Informational Pages
The website also includes informational pages:
Know Us – provides details about the platform
Support – provides help or support information

Author:-
Komal Chowdary
Associate Software Engineer | Full-Stack Developer
Email:- komalchowdary25@gmail.com
GitHub: https://github.com/Komalchowdary25
