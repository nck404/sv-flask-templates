
# Svelte + Flask Full-Stack Template

A modern full-stack web application template built with Svelte (frontend) and Flask (backend). This template provides a solid foundation for building scalable web applications with authentication, database integration, and modern development practices.

## Project Structure

```
├── src/
│   ├── backend/                 # Flask API Server
│   │   ├── app.py              # Main Flask application
│   │   ├── models.py           # Database models
│   │   ├── routes/             # API route blueprints
│   │   │   ├── auth.py         # Authentication routes
│   │   │   ├── lessons.py      # Lesson management routes
│   │   │   └── blog.py         # Blog functionality routes
│   │   ├── .env                # Environment variables
│   │   └── requirements.txt   # Python dependencies
│   └── frontend/               # Svelte Frontend Application
│       ├── src/
│       │   ├── components/     # Reusable components
│       │   ├── lib/           # Utility functions and services
│       │   ├── routes/        # SvelteKit routes
│       │   └── stores/        # Svelte stores for state management
│       ├── static/            # Static assets
│       ├── .env               # Environment variables
│       └── package.json       # Node.js dependencies
├── docs/                      # Documentation
├── .gitignore                 # Git ignore rules
├── setup.bat                  # Development setup script
├── run.bat                    # Development run script
└── docker-compose.yml         # Docker configuration (optional)
```

## 🚀 Quick Start

### Prerequisites
- Node.js (v18+)
- Python (v3.9+)
- npm or yarn

### 1. Setup Project
Run the setup script to install all dependencies:

```bash
# Windows
setup.bat

# Linux/macOS (optional)
chmod +x setup.sh
./setup.sh
```

### 2. Run Project
Start both backend and frontend servers:

```bash
# Windows
run.bat

# Linux/macOS (optional)
chmod +x run.sh
./run.sh
```

### 3. Access Application
- Frontend: http://localhost:5173
- Backend API: http://localhost:5000
- API Documentation: http://localhost:5000/docs (if Swagger is added)

## 📦 Features

### Backend (Flask)
- RESTful API with Flask Blueprint architecture
- JWT Authentication with refresh tokens
- SQLAlchemy ORM with SQLite (development) support
- CORS enabled for frontend integration
- Environment variable configuration
- User management with profile updates
- Blog functionality with comments
- Lesson management system

### Frontend (Svelte)
- Modern SvelteKit framework
- TypeScript support
- Responsive design
- Authentication handling
- API integration with proper error handling
- State management with Svelte stores

## 🔧 Configuration

### Environment Variables

Create `.env` files in both backend and frontend directories:

**Backend (.env):**
```env
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key
DATABASE_URL=sqlite:///app.db
RECAPTCHA_SECRET_KEY=your-recaptcha-secret
```

**Frontend (.env):**
```env
VITE_API_URL=http://localhost:5000
VITE_APP_NAME=Your App Name
```

## 🛠️ Development

### Backend Development
```bash
cd src/backend
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
python app.py
```

### Frontend Development
```bash
cd src/frontend
npm install
npm run dev
```

## 📋 API Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - User login
- `GET /auth/me` - Get current user
- `PUT /auth/profile` - Update user profile

## 📦 Dependencies

### Backend
- Flask==3.0.3
- Flask-SQLAlchemy==3.1.1
- Flask-JWT-Extended==4.6.0
- Flask-CORS==4.0.0
- python-dotenv==1.0.1
- requests==2.32.3

### Frontend
- SvelteKit
- TypeScript
- Axios (for API calls)
- Tailwind CSS (recommended)

## Docker Support

Optional Docker configuration for easy deployment:

```bash
# Build and run with Docker Compose
docker-compose up --build
```

## 📝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Resources

- [Svelte Documentation](https://svelte.dev/docs)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [JWT Documentation](https://flask-jwt-extended.readthedocs.io/)

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.
