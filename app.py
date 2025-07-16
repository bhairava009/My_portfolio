from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import json
import os
from datetime import datetime
import logging

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load data from JSON files
def load_json_data(filename):
    try:
        with open(f'data/{filename}', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"File {filename} not found")
        return {}
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in {filename}")
        return {}
        

@app.route('/')
def index():
    """Home page with hero section"""
    personal_info = load_json_data('personal_info.json')
    return render_template('index.html', personal_info=personal_info)

@app.route('/about')
def about():
    """About page with personal information"""
    personal_info = load_json_data('personal_info.json')
    education = load_json_data('education.json')
    return render_template('about.html', personal_info=personal_info, education=education)

skills_data = {
    "technical_skills": {
        "languages": ["Python", "SQL", "R"],
        "tools": ["Tableau", "Excel"]
    },
    "soft_skills": ["Communication", "Problem-solving"]
}

@app.route('/skills')
def skills():
    personal_info = load_json_data('personal_info.json')
    return render_template('skills.html', skills=skills_data, personal_info=personal_info)

@app.context_processor
def inject_personal_info():
    return {'personal_info': {'name': 'Sonu Kumar'}}

@app.route('/projects')
def projects():
    """Projects page"""
    projects_data = load_json_data('projects.json')
    return render_template('projects.html', projects=projects_data)

@app.route('/certificates')
def experience():
    """Experience and certificates page"""
    certificates = load_json_data('certificates.json')
    return render_template('certificates.html', certificates=certificates)

@app.route('/blog')
def blog():
    """Blog listing page"""
    blog_posts = load_json_data('blog_posts.json')
    return render_template('blog.html', posts=blog_posts.get('posts', []))

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    """Individual blog post page"""
    blog_posts = load_json_data('blog_posts.json')
    posts = blog_posts.get('posts', [])
    post = next((p for p in posts if p['id'] == post_id), None)
    if not post:
        flash('Blog post not found', 'error')
        return redirect(url_for('blog'))
    return render_template('blog_post.html', post=post)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page with form"""
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Validate form data
        if not all([name, email, subject, message]):
            flash('All fields are required', 'error')
            return render_template('contact.html')
        
        # Create contact data
        contact_data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
            'timestamp': datetime.now().isoformat()
        }
        
        # Log to console
        logger.info(f"New contact form submission: {contact_data}")
        
        # Save to file
        try:
            contacts_file = 'data/contacts.json'
            if os.path.exists(contacts_file):
                with open(contacts_file, 'r') as f:
                    contacts = json.load(f)
            else:
                contacts = {'submissions': []}
            
            contacts['submissions'].append(contact_data)
            
            with open(contacts_file, 'w') as f:
                json.dump(contacts, f, indent=2)
            
            flash('Thank you for your message! I will get back to you soon.', 'success')
            return redirect(url_for('contact'))
            
        except Exception as e:
            logger.error(f"Error saving contact form: {e}")
            flash('There was an error sending your message. Please try again.', 'error')
    
    personal_info = load_json_data('personal_info.json')
    return render_template('contact.html', personal_info=personal_info)

@app.route('/api/contact', methods=['POST'])
def api_contact():
    """API endpoint for contact form (for AJAX submissions)"""
    try:
        data = request.get_json()
        
        # Validate data
        required_fields = ['name', 'email', 'subject', 'message']
        if not all(field in data for field in required_fields):
            return jsonify({'success': False, 'message': 'All fields are required'}), 400
        
        # Create contact data
        contact_data = {
            'name': data['name'],
            'email': data['email'],
            'subject': data['subject'],
            'message': data['message'],
            'timestamp': datetime.now().isoformat()
        }
        
        # Log to console
        logger.info(f"New API contact submission: {contact_data}")
        
        # Save to file
        contacts_file = 'data/contacts.json'
        if os.path.exists(contacts_file):
            with open(contacts_file, 'r') as f:
                contacts = json.load(f)
        else:
            contacts = {'submissions': []}
        
        contacts['submissions'].append(contact_data)
        
        with open(contacts_file, 'w') as f:
            json.dump(contacts, f, indent=2)
        
        return jsonify({'success': True, 'message': 'Message sent successfully!'})
        
    except Exception as e:
        logger.error(f"Error in API contact: {e}")
        return jsonify({'success': False, 'message': 'Server error'}), 500
    
skills_data = {
    "technical_skills": {
        "languages": [
            {"name": "C/C++", "level": 85, "category": "programming"},
            {"name": "Java", "level": 50, "category": "programming"},
            {"name": "HTML", "level": 75, "category": "web"},
            {"name": "R Programming", "level": 70, "category": "data"}
        ],
        "technologies": [
            {"name": "Tableau", "level": 90, "category": "visualization"},
            {"name": "R Studio", "level": 90, "category": "data"},
            {"name": "Git", "level": 80, "category": "tools"},
            {"name": "GitHub", "level": 80, "category": "tools"},
            {"name": "Ubuntu", "level": 75, "category": "systems"},
            {"name": "Tableau Prep", "level": 85, "category": "data"}
        ],
        "core_skills": [
            {"name": "Data Structures and Algorithms", "level": 50, "category": "programming"},
            {"name": "Problem-Solving", "level": 90, "category": "analytical"},
            {"name": "Responsive Dashboard Development", "level": 95, "category": "visualization"},
            {"name": "Predictive Analysis", "level": 80, "category": "data"},
            {"name": "Data Science", "level": 85, "category": "data"}
        ]
    },
    "categories": [
        {"id": "programming", "name": "Programming Languages", "color": "blue"},
        {"id": "web", "name": "Web Technologies", "color": "green"},
        {"id": "data", "name": "Data Analysis", "color": "purple"},
        {"id": "visualization", "name": "Data Visualization", "color": "orange"},
        {"id": "tools", "name": "Tools & Platforms", "color": "gray"},
        {"id": "systems", "name": "Systems", "color": "red"},
        {"id": "analytical", "name": "Analytical Skills", "color": "indigo"}
    ]
}

if __name__ == '__main__':
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=5000)