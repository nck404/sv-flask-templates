# Flask Application Architecture

## Project Structure

```
src/backend/
├── app.py                 # Main Flask application
├── config/               # Configuration files
│   └── config.py        # Application configuration
├── models.py            # Database models
├── routes/              # Route blueprints
│   ├── auth.py         # Authentication routes
│   ├── lessons.py       # Lesson management routes
│   └── blog.py          # Blog routes
├── migrations/          # Database migrations
├── tests/               # Test files
└── utils/               # Utility functions
```

## Key Components

### 1. Flask Application (`app.py`)
- Main application entry point
- Configuration setup
- Blueprint registration
- CORS configuration
- Database initialization

### 2. Configuration (`config/`)
- Environment-based configuration
- CORS allowed domains
- Database settings
- JWT secret key management

### 3. Models (`models.py`)
- SQLAlchemy ORM models
- Database relationships
- Data validation

### 4. Routes (`routes/`)
- Modular route organization
- Blueprint-based routing
- Authentication middleware
- Error handling

## Configuration Management

The application uses environment variables for configuration:
- `DATABASE_URL`: Database connection string
- `ALLOWED_DOMAINS`: Comma-separated list of CORS origins
- `JWT_SECRET_KEY`: JWT signing secret
- `SECRET_KEY`: Flask secret key

## CORS Configuration

CORS is configured to allow:
- `http://localhost:3000`
- `http://127.0.0.1:3000`
- `http://localhost:5173`
- `http://localhost:8080`

## Database Setup

- Uses SQLite as the default database
- SQLAlchemy ORM for database operations
- Automatic table creation on startup
- Relationship-based data modeling