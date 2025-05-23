.PHONY: install test lint format clean run setup-env

# Development commands
install:
	poetry install

setup-env:
	python scripts/generate_env_example.py
	python scripts/setup_env.py

test:
	poetry run pytest

lint:
	poetry run flake8 src tests
	poetry run mypy src tests
	poetry run black --check src tests
	poetry run isort --check-only src tests

format:
	poetry run black src tests
	poetry run isort src tests

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	find . -type d -name ".mypy_cache" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -r {} +
	find . -type d -name "*.egg" -exec rm -r {} +
	find . -type d -name "dist" -exec rm -r {} +
	find . -type d -name "build" -exec rm -r {} +

run:
	poetry run python -m ontario_driving_school_manager

# Database commands
db-init:
	poetry run alembic upgrade head

db-migrate:
	poetry run alembic revision --autogenerate -m "$(message)"

db-upgrade:
	poetry run alembic upgrade head

db-downgrade:
	poetry run alembic downgrade -1 