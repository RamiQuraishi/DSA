# Ontario Driving School Manager

A comprehensive management system for Ontario driving schools, built with Python and PyQt5.

## Features

- Student management and tracking
- Course scheduling and management
- Instructor management
- Vehicle fleet management
- Financial tracking and reporting
- Compliance and documentation management

## Requirements

- Python 3.9 or higher
- Poetry for dependency management
- Docker (optional, for containerized development)

## Setup

1. **Install Dependencies**
   ```bash
   poetry install
   ```

2. **Environment Setup**
   ```bash
   # Generate .env file from example
   python scripts/setup_env.py
   
   # Edit .env file with your configuration
   # (Optional) Edit src/ontario_driving_school_manager/config/logging.yaml for logging settings
   ```

3. **Database Setup**
   ```bash
   # Initialize database
   poetry run python -m ontario_driving_school_manager.data.db_setup
   
   # Run migrations
   alembic upgrade head
   ```

4. **Run Tests**
   ```bash
   poetry run pytest
   ```

## Configuration

### Environment Variables (.env)
- `DATABASE_URL`: Database connection string
- `LOG_LEVEL`: Logging level (INFO, DEBUG, etc.)
- `LOG_FILE`: Path to log file
- `APP_NAME`: Application name
- `APP_VERSION`: Application version
- `APP_ENV`: Environment (development, production)
- `SECRET_KEY`: Secret key for security
- `DEBUG`: Debug mode (True/False)

### Logging Configuration (logging.yaml)
- Console and file logging
- Separate error log file
- Configurable log levels and formats
- Third-party library logging settings

## Development

1. Activate the virtual environment:
```bash
poetry shell
```

2. Run the application:
```bash
python -m ontario_driving_school_manager
```

### Code Style
- Follow PEP 8 guidelines
- Use type hints
- Write docstrings for all functions and classes

### Testing
- Write unit tests for new features
- Run tests before committing
- Maintain test coverage

### Database Migrations
- Use Alembic for all database changes
- Review auto-generated migrations
- Test migrations before applying

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request 