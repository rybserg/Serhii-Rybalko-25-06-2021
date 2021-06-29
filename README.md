App on Heroku: https://limitless-hamlet-47005.herokuapp.com/  

Django Admin Interface: https://limitless-hamlet-47005.herokuapp.com/admin/  
Login: admin  
Password: adminadmin  

Native Django forms (crispy):   
* App Login: https://limitless-hamlet-47005.herokuapp.com/accounts/login/  
* Register: https://limitless-hamlet-47005.herokuapp.com/accounts/register/  

DRF endpoints:  
* Get current user https://limitless-hamlet-47005.herokuapp.com/api/user/ GET, HEAD, OPTIONS  
* Get user emails (as sender or/and receiver) /api/users/{user_id}/emails/ GET, HEAD, OPTIONS  
* Create email /api/emails/ POST, OPTIONS  
* Delete email /api/emails/{id}/ DELETE, OPTIONS  

Bonus task (only Backend part)  
DRF endpoints that not used for now in frontend app:  
* Create email by logged in user / get emails related to logged in user (as sender or/and receiver) /api/personal-emails/ GET, POST, HEAD, OPTIONS  
* Get (for sender or receiver), PUT/PATCH/DELETE email related to logged in user (only for sender) /api/personal-emails/{id}/ GET, PUT, PATCH, DELETE, HEAD, OPTIONS  
* Update is_read and is_spam fields of Email by receiver /api/personal-emails/{id}/mark/ PATCH, OPTIONS
* Search users /api/users/?search=username GET, HEAD, OPTIONS  

App pages:  
* Compose Email (available after login) https://limitless-hamlet-47005.herokuapp.com/  
* Manage Emails https://limitless-hamlet-47005.herokuapp.com/manage-emails  

Logout:
https://limitless-hamlet-47005.herokuapp.com/accounts/logout/
