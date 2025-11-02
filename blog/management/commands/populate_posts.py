from typing import Any
from django.core.management.base import BaseCommand
from blog.models import Post 
from blog.models import Category
import random



class Command(BaseCommand):
    help = "This command populates and inserts Post data into the database"

    def handle(self, *args: Any, **options: Any):

        # Delete Exixting Data
        Post.objects.all().delete()
 


        titles = [
            "The Future of AI",
            "10 Django Tips for Faster Development",
            "Easy Guide to Python Virtual Environments",
            "The Rise of Quantum Computing",
            "Top Web Development Trends 2025",
            "Build a Portfolio Site with Django",
            "Mastering Django REST API Integration",
            "Complete Python Roadmap for Beginners",
            "How Cloud Computing Transforms Business",
            "Cybersecurity in the AI Era",
            "Deploying Django on AWS",
            "Power of Open Source in Tech",
            "Why Learn Docker in 2025",
            "Django vs FastAPI: Backend Showdown",
            "AI’s Impact on Education",
            "Database Optimization in Django",
            "AI and Creativity: The New Frontier",
            "The Value of Clean Code",
            "Using ChatGPT API with Django",
            "Ethics in Artificial Intelligence",
            "Best Debugging Practices in Python",
            "Modern Web Apps with Django & React",
            "Beginner’s Guide to Machine Learning",
            "Securing Your Django Website",
            "Deploy Django with Docker & Nginx",
            "Build an E-commerce Site in Django",
            "Connect Django with MySQL",
            "Serverless Computing Explained",
            "Common Django Developer Mistakes",
            "Beautiful APIs with Django REST"
        ]

        contents = [
            "Artificial Intelligence continues to evolve, transforming industries from healthcare to education. The future of AI lies in ethical innovation, human collaboration, and smarter automation. As AI systems learn to adapt to real-world scenarios, we’re entering a new era of intelligent technology.",
            "Django offers powerful tools for rapid web development. By using class-based views, optimizing queries, and leveraging signals, developers can create faster, cleaner, and more scalable applications efficiently.",
            "Python virtual environments isolate project dependencies. They make package management easy and prevent version conflicts between projects, ensuring a smoother workflow for developers.",
            "Quantum computing is reshaping how data is processed. With massive computational power, it can solve complex problems that classical computers cannot — from cryptography to material science.",
            "The biggest web trends in 2025 include AI-powered applications, serverless architecture, and progressive web apps. Staying ahead ensures developers build smarter, more responsive web experiences.",
            "A portfolio website is essential for showcasing skills. Using Django, developers can easily create a dynamic portfolio with blog sections, project showcases, and an admin dashboard.",
            "The Django REST Framework simplifies API development. With serializers and viewsets, it enables developers to create scalable and well-structured APIs for any type of client.",
            "Python offers endless opportunities. From automation to AI, mastering its fundamentals, libraries, and frameworks helps developers move quickly from beginner to professional.",
            "Cloud computing empowers businesses to grow efficiently. Platforms like AWS and Azure make it easy to scale apps, secure data, and collaborate effectively across teams.",
            "In the age of AI, cybersecurity is more important than ever. Protecting APIs, encrypting data, and monitoring threats ensure safety in digital ecosystems.",
            "AWS offers the perfect environment for Django deployments. Using EC2, RDS, and S3, developers can host scalable, secure, and high-performing web applications easily.",
            "Open source fuels innovation and collaboration. Developers worldwide contribute code, share ideas, and create technologies that drive the digital revolution.",
            "Docker is a must-have in 2025 for building consistent environments. It simplifies deployments, reduces setup issues, and enhances scalability in development pipelines.",
            "Django and FastAPI both shine in web backend development. Django is robust for large apps, while FastAPI provides unmatched speed for lightweight APIs.",
            "AI is revolutionizing education with personalized learning tools and intelligent tutoring systems that adapt to each student’s pace and style.",
            "Database optimization boosts Django performance. Using indexing, caching, and query tuning helps reduce load times and improve efficiency.",
            "AI-driven tools are inspiring creativity across art, writing, and design. The collaboration between humans and machines is shaping a new creative frontier.",
            "Writing clean, readable code ensures long-term success. Consistent formatting, clear comments, and modular design make software easier to maintain.",
            "Integrating ChatGPT with Django allows developers to add conversational AI to their apps — perfect for chatbots, support systems, or AI-driven assistants.",
            "Ethical AI ensures innovation remains fair and transparent. Developers must address bias and privacy to create systems that serve everyone responsibly.",
            "Debugging is a vital developer skill. Using Python tools like pdb or print statements effectively can save hours and lead to more stable applications.",
            "Combining Django and React results in modern, dynamic web apps. Django handles backend logic, while React builds fast and interactive frontends.",
            "Machine learning with Python is simple using libraries like scikit-learn and pandas. Beginners can train predictive models and analyze data efficiently.",
            "Security is crucial in Django apps. Enabling HTTPS, protecting against CSRF, and managing permissions are key to preventing vulnerabilities.",
            "Docker and Nginx make Django deployment easier and more reliable. Together, they ensure your app is scalable, secure, and production-ready.",
            "Django makes building e-commerce sites efficient. You can manage users, orders, and payments directly from the admin dashboard with minimal effort.",
            "Connecting Django with MySQL gives developers a reliable database backend. With correct configurations, it ensures smooth and efficient data handling.",
            "Serverless computing automates scaling and reduces infrastructure costs. It’s a game-changer for deploying lightweight Django APIs or microservices.",
            "Avoiding mistakes like skipping migrations or leaving DEBUG=True improves Django app performance, security, and maintainability.",
            "Django REST Framework helps create beautiful, well-documented APIs. With minimal code, you can deliver powerful backend services to multiple clients."
        ]

        

        image_urls = [
            f"https://picsum.photos/id/{i}/200/300" for i in range(1, 31)
        ]

        categories = Category.objects.all()
        for title, content, image_url in zip(titles, contents, image_urls):
            category = random.choice(categories)
            Post.objects.create(title=title, content=content, img_url=image_url , Category = category)


        self.stdout.write(self.style.SUCCESS("Completed inserting post data successfully!"))
