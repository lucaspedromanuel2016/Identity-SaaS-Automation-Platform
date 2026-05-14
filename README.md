# Identity SaaS Automation Platform

![CI](https://github.com/lucaspedromanuel2016/Identity-SaaS-Automation-Platform/actions/workflows/ci.yml/badge.svg)

Enterprise-style IAM automation platform integrating Auth0 APIs, Slack webhooks, RBAC automation, MFA workflows, and GitHub Actions CI/CD using Python and REST APIs.

---

# Features

- Auth0 Management API integration
- Automated user provisioning
- RBAC role assignment automation
- MFA enforcement workflows
- Slack security notifications
- GitHub Actions CI/CD
- Secure environment variable management
- Audit logging
- DevSecOps workflow practices

---

# Architecture

```text
Python Automation Scripts
        ↓
Auth0 Management API
        ↓
RBAC + MFA Enforcement
        ↓
Slack Notifications
        ↓
GitHub Actions CI/CD
```

---

# Technologies Used

## Identity & Security
- Auth0
- OAuth 2.0
- RBAC
- MFA
- REST APIs

## Automation & DevOps
- Python
- Bash
- GitHub Actions
- dotenv
- logging

## Integrations
- Slack Incoming Webhooks

---

# Project Structure

```text
Identity-SaaS-Automation-Platform/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── logs/
│
├── scripts/
│   ├── create_auth0_user.py
│   ├── assign_role.py
│   ├── enforce_mfa.py
│   ├── onboard_user.py
│   └── test_env.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/lucaspedromanuel2016/Identity-SaaS-Automation-Platform.git
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create `.env`

```env
AUTH0_DOMAIN=YOUR_AUTH0_DOMAIN
AUTH0_CLIENT_ID=YOUR_AUTH0_CLIENT_ID
AUTH0_CLIENT_SECRET=YOUR_AUTH0_CLIENT_SECRET
AUTH0_ROLE_ID=YOUR_AUTH0_ROLE_ID
SLACK_WEBHOOK_URL=YOUR_SLACK_WEBHOOK_URL
```

---

# Automation Workflows

## Create Auth0 User

```bash
python scripts/create_auth0_user.py
```

---

## Assign RBAC Role

```bash
python scripts/assign_role.py
```

---

## MFA Enforcement Workflow

```bash
python scripts/enforce_mfa.py
```

---

## Slack Onboarding Alert

```bash
python scripts/onboard_user.py
```

---

# CI/CD Pipeline

GitHub Actions automatically:
- installs dependencies
- validates Python scripts
- runs CI pipeline checks

Workflow file:

```text
.github/workflows/ci.yml
```

---

# Security Best Practices

- Secrets stored in `.env`
- `.env` protected via `.gitignore`
- No credentials committed to GitHub
- Slack webhook secret rotation supported
- Secure OAuth token handling

---

# Future Enhancements

- Docker containerization
- Terraform infrastructure automation
- Adaptive MFA
- SCIM provisioning
- Flask admin dashboard
- Audit analytics
- SIEM integrations

---

# Resume Highlights

This project demonstrates:
- IAM engineering
- Identity lifecycle automation
- RBAC workflows
- DevSecOps practices
- CI/CD automation
- SaaS integrations
- Cloud security engineering

---

# Author

Lucas Pedro Manuel