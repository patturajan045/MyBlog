# MyBlog
blog website by PattuRajan

# 📝 MyBlog

A modern and responsive **Django Blog Website** built using Python and Bootstrap.  
This project demonstrates how to create a dynamic blog platform where users can explore posts, view details, and connect through a contact form.

---

## 🚀 Features

- 📰 Display all blog posts dynamically from the database  
- 🏷️ Category-based post filtering  
- 💬 Contact form with email logging  
- 🖼️ Responsive design with Bootstrap 5  
- 🧩 Modular Django app structure (views, templates, static files)  
- 🛠️ Django Admin panel for easy content management  

---

## 🏗️ Tech Stack

| Technology | Purpose |
|-------------|----------|
| **Python 3.11+** | Backend logic |
| **Django 5+** | Web framework |
| **SQLite3** | Default database |
| **Bootstrap 5** | Frontend styling |
| **HTML5 / CSS3 / JS** | Templating and interactivity |
| **Git & GitHub** | Version control and collaboration |

---

## ⚙️ Installation Guide

Follow these steps to set up the project locally 👇

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/patturajan045/MyBlog.git
cd MyBlog



## virtual Environment 

python -m venv venv
venv\Scripts\activate      # For Windows
# or
source venv/bin/activate   # For macOS/Linux

pip install -r requirements.txt ----> Install Dependencies


python manage.py migrate  -----> Apply Migrations

python manage.py runserver -----> Run the Server



## project structure 

MyBlog/
│
├── blog/                     # Main app
│   ├── templates/blog/       # HTML templates
│   ├── static/blog/          # CSS, JS, images
│   ├── views.py              # App views
│   ├── models.py             # Database models
│   ├── urls.py               # App URLs
│   └── forms.py              # Contact forms
│
├── MyBlog/                   # Project settings folder
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md


🧠 Future Enhancements

✨ Add user authentication (login/register)

⭐ Enable comments and likes

📈 Integrate a rich text editor for blog creation

☁️ Deploy on cloud (e.g., Render / Railway / Heroku)


👨‍💻 Author

Patturajan M
📧 Email: [your.email@example.com
]
🌐 GitHub: https://github.com/patturajan045


📜 License

This project is licensed under the MIT License – feel free to use and modify it.



---

Would you like me to include a **`requirements.txt`** file for your Django project as well (so others can install dependencies easily)?
