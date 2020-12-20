# free_places

Project defense for Python Web Framework course in SoftUni.

Functionality

The simple goal of the application is to make it easy to find a hospital place in a set of establishments. It does not aim to provide a full hospital
management system whick would require more details and does not dive into the intricacies of hospital management. Application shows only cities and
establishments with currently allocated places as to keep the application views simple and efficient.

All the data is visible to unregistered users. Admin user can edit everything. The only users required to log in are establishment representatives that would 
need to log in to allocate new places dedicated to the current pandemic, edit and delete these places.

SoftUni project defense requirements are as follows:

- The project must have login/register functionality
- Must have public part (A part of the website, which is accessible by everyone – un/authenticated users and admins)
- Must have private part (accessible only by authenticated user and admins)
- Admin part (accessible only to admins)
- Unauthenticated users (public part) have only 'get' permissions (for Example – could see а landing page and for example all animals/furniture or whatever
products you will have)
- Authenticated users (private part) – have full CRUD for all of their created content (not observed due to different business logic)
- Admin part – Admin/s has full CRUD for all products/content, created by users on the website
- Forms (for register/login)
- Templates (your controllers/views must return HTML files) – one and the same template could be re-used/used multiple times (with the according adjustments,
if such needed)
- Github/Gitlab – at least 5 commits and at least 5 days of history + README

License

GitHub license MIT
