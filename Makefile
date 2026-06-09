
### 3. `Makefile`
```makefile
.PHONY: help data train test clean run-app docker-build docker-up

help:
	@echo "Available commands:"
	@echo "  make data      - Generate synthetic dataset"
	@echo "  make train     - Train models"
	@echo "  make test      - Run tests"
	@echo "  make clean     - Clean temporary files"
	@echo "  make run-app   - Run web application"
	@echo "  make docker-build - Build Docker image"
	@echo "  make docker-up - Run with Docker Compose"

data:
	python src/data/make_dataset.py

train:
	python src/models/train_model.py

test:
	pytest tests/ -v --cov=src

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".pytest_cache" -delete
	find . -type d -name "*.egg-info" -delete
	rm -rf .coverage htmlcov/

run-app:
	python app/app.py

docker-build:
	cd docker && docker build -t churn-prediction .

docker-up:
	cd docker && docker-compose up

install:
	pip install -r requirements.txt
	pip install -e .

format:
	black src/ tests/ app/
	isort src/ tests/ app/

lint:
	flake8 src/ tests/ app/
	mypy src/
