from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="churn-prediction",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Customer Churn Prediction using Machine Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/churn-prediction-ml-project",
    packages=find_packages(exclude=["tests", "docs"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": ["pytest", "black", "flake8", "mypy", "isort"],
        "notebook": ["jupyter", "ipykernel"],
    },
    entry_points={
        "console_scripts": [
            "churn-train=src.models.train_model:main",
            "churn-predict=src.models.predict_model:main",
        ],
    },
)
