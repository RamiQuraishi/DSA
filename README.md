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

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ontario-driving-school-manager.git
cd ontario-driving-school-manager
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Copy the example environment file and configure it:
```bash
cp .env.example .env
```

4. Initialize the database:
```bash
poetry run alembic upgrade head
```

## Development

1. Activate the virtual environment:
```bash
poetry shell
```

2. Run the application:
```bash
python -m ontario_driving_school_manager
```

## Testing

Run tests using pytest:
```bash
poetry run pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request 