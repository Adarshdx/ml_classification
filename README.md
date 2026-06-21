<div align="center">

#  Customer Churn Prediction

## End-to-End Machine Learning Classification Project

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=flat&logo=githubactions&logoColor=white)](https://github.com/features/actions)

</div>

---

##  Table of Contents
- [Project Overview](#project-overview)
- [Key Results](#key-results)
- [Live Demo](#live-demo)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Model Performance](#model-performance)
- [Business Impact](#business-impact)
- [Web Application](#web-application)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

##  Project Overview

This repository contains a **production-ready machine learning system** that predicts customer churn for a telecommunications company. The project demonstrates a complete ML pipeline from data preprocessing to model deployment, comparing two classification algorithms to identify the most effective solution.

### The Problem
Customer churn costs telecom companies **billions annually**. Identifying at-risk customers before they leave enables proactive retention strategies, saving revenue and improving customer satisfaction.

### The Solution
A binary classification system that predicts churn probability using customer demographics, usage patterns, and service history. The system achieves **86.2% ROC-AUC** and identifies **79% of actual churners**.

### Why This Project Matters
-  **Complete ML lifecycle** from data to deployment
-  **Rigorous comparison** of multiple algorithms
-  **Production-ready code** with testing and CI/CD
-  **Interactive dashboard** for business users
-  **Docker support** for easy deployment

---
### Module dependency graph
<img width="4774" height="231" alt="deepseek_mermaid_20260607_856d57" src="https://github.com/user-attachments/assets/a087e75d-566d-457e-ab65-afede0c44fc5" />
<img width="3597" height="2791" alt="deepseek_mermaid_20260607_bfe41d" src="https://github.com/user-attachments/assets/af3bd0e7-c8e5-4b92-ac14-1da0e328256b" />

##  Key Results

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC | 
|-------|----------|-----------|--------|----------|---------|
| Logistic Regression | 80.1% | 62.4% | 71.8% | 66.7% | 0.803 |
| **Random Forest** | **84.9%** | **69.6%** | **78.9%** | **74.0%** | **0.862** |

### Winner: Random Forest Classifier 

**Why Random Forest won:**
-  **+5.9%** higher ROC-AUC (better class separation)
-  **+7.3%** higher F1-Score (better precision-recall balance)
-  **+7.1%** higher recall (finds more actual churners)
-  Handles non-linear relationships automatically

---

## DEMO
<img width="1325" height="892" alt="Screenshot 2026-06-09 212430" src="https://github.com/user-attachments/assets/0350e1b2-df77-45fe-ace8-15fb2ffd7414" />
.
.
.
