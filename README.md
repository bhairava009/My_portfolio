
# My_portfolio
A sleek, responsive portfolio website showcasing skills, projects, and professional experience in data analysis, visualization, and software development. Built with Flask, Tailwind CSS, and Jinja2 templating for easy customization and scalability.
# Sonu Kumar - Personal Portfolio Website

A comprehensive Flask-based portfolio website showcasing data analysis skills, projects, and professional experience.

## Features

- **Responsive Design**: Built with Tailwind CSS for optimal viewing on all devices
- **Dynamic Content**: Uses JSON files to simulate database functionality
- **Interactive Elements**: JavaScript-powered animations and user interactions
- **Contact Form**: Functional contact form with backend processing
- **Blog Section**: Static blog with detailed posts about data analysis and programming
- **Project Showcase**: Detailed project descriptions with technology stacks
- **Skills Visualization**: Interactive skill progress bars and categorization
- **Professional Timeline**: Experience and education timeline

## Technology Stack

### Frontend
- HTML5
- Tailwind CSS
- JavaScript (ES6+)
- Font Awesome Icons
- Google Fonts (Inter)

### Backend
- Flask (Python web framework)
- Jinja2 templating
- JSON data storage
- Form handling and validation

### Deployment Ready
- Configured for deployment on Render, Railway, or Vercel
- Environment variable support
- Production-ready Flask configuration

## Project Structure

```
portfolio-website/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── data/                  # JSON data files
│   ├── personal_info.json
│   ├── skills.json
│   ├── projects.json
│   ├── certificates.json
│   ├── education.json
│   ├── blog_posts.json
│   └── contacts.json
├── templates/             # Jinja2 templates
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── skills.html
│   ├── projects.html
│   ├── experience.html
│   ├── blog.html
│   ├── blog_post.html
│   └── contact.html
├── static/               # Static assets
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
└── README.md
```

## Installation and Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd portfolio-website
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the website**
   Open your browser and navigate to `http://localhost:5000`

## Data Management

The application uses JSON files in the `data/` directory to simulate database functionality:

- `personal_info.json`: Personal details and contact information
- `skills.json`: Technical skills with proficiency levels
- `projects.json`: Project portfolio with descriptions and technologies
- `certificates.json`: Professional certifications and achievements
- `education.json`: Educational background
- `blog_posts.json`: Blog posts with full content
- `contacts.json`: Contact form submissions (auto-generated)

## Key Features

### 1. Dynamic Content Loading
- All content is loaded from JSON files
- Easy to update without code changes
- Modular data structure

### 2. Responsive Design
- Mobile-first approach
- Tailwind CSS for consistent styling
- Interactive elements with hover effects

### 3. Contact Form Processing
- Server-side form validation
- Data logging to console and file
- AJAX submission with user feedback
- Flash message system

### 4. Blog System
- Full blog posts with rich content
- Category and tag system
- Reading time calculation
- Responsive blog layout

### 5. Skills Visualization
- Animated progress bars
- Skill categorization
- Interactive skill filtering

### 6. Project Portfolio
- Detailed project descriptions
- Technology stack highlighting
- External links to demos and code
- Project categorization

## Customization

### Updating Personal Information
Edit `data/personal_info.json` to update:
- Name and title
- Contact information
- Bio and summary
- Social media links

### Adding Projects
Add new projects to `data/projects.json`:
```json
{
  "id": 3,
  "title": "New Project",
  "description": "Project description",
  "technologies": ["Tech1", "Tech2"],
  "category": "category-name",
  "demo_url": "https://demo.com",
  "github_url": "https://github.com/username/repo"
}
```

### Adding Blog Posts
Add new blog posts to `data/blog_posts.json`:
```json
{
  "id": 5,
  "title": "New Blog Post",
  "excerpt": "Brief description",
  "content": "Full blog content with markdown support",
  "date": "2024-01-01",
  "category": "Category",
  "tags": ["tag1", "tag2"]
}
```

## Deployment

### Render Deployment
1. Connect your GitHub repository to Render
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `python app.py`
4. Deploy

### Railway Deployment
1. Connect repository to Railway
2. Railway will auto-detect Flask application
3. Set environment variables if needed
4. Deploy

### Vercel Deployment
1. Install Vercel CLI: `npm i -g vercel`
2. Run `vercel` in project directory
3. Follow deployment prompts
4. Configure for Python runtime

## Environment Variables

For production deployment, set these environment variables:
- `FLASK_ENV=production`
- `SECRET_KEY=your-secret-key`
- `PORT=5000` (or as required by hosting platform)

## Performance Optimizations

- Lazy loading for images
- Minified CSS and JavaScript
- Optimized image formats
- Efficient JSON data loading
- Responsive image sizing

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

**Sonu Kumar**
- Email: sonumishra9809@gmail.com
- LinkedIn: [linkedin.com/in/sonu-kumar-465050250](https://www.linkedin.com/in/sonu-kumar-465050250)
- GitHub: [github.com/bhairava009](https://github.com/bhairava009)
- Location: Muzaffarpur, Bihar 843113
- Phone: 9973044979

Built with ❤️ using Flask, Tailwind CSS, and modern web technologies.
