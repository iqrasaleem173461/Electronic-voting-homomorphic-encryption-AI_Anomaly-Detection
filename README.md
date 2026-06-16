# AI-Based Secure E-Voting System

A comprehensive, secure, and AI-powered E-Voting system built for university Final Year Projects.

## 🚀 Features
- **AI Fraud Detection:** Machine learning model (Random Forest) monitors voting patterns to detect suspicious behavior.
- **NLP Chatbot:** AI Assistant to help voters with registration and voting processes. (See [AI Assistant Documentation](AI_ASSISTANT_DOCS.md) for Webhook & Voice setup).
- **NADRA Verification:** Simulated identity verification against a database of 100+ citizen records.
- **One Vote Policy:** Securely enforces that each citizen can only vote once per election.
- **Modern Dashboard:** Professional interfaces for both Voters and Administrators.
- **Analytics:** Real-time vote counting and election statistics with interactive charts.
- **Dark/Light Mode:** Full theme support with a premium Green & White aesthetic.

## 🛠️ Tech Stack
- **Frontend:** Next.js, React, Chart.js, React Icons, Axios.
- **Backend:** Node.js, Express.js, MongoDB, Mongoose, JWT.
- **AI Service:** Python, FastAPI, spaCy, scikit-learn, joblib.

## 📦 Project Structure
- `/frontend`: Next.js web application.
- `/backend`: Node.js Express API.
- `/ai-service`: Python FastAPI AI services.
- `/database`: Seed scripts and NADRA record simulations.

## 🛠️ Setup Instructions

### 1. Prerequisites
- Node.js (v18+)
- Python (3.9+)
- MongoDB (Running locally on default port 27017)

### 2. Backend Setup
```bash
cd backend
npm install
# Ensure .env is configured (pre-configured for local use)
npm run seed  # This populates NADRA records and creates an admin user
npm run dev
```

### 3. AI Service Setup
```bash
cd ai-service
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python main.py
```

### 4. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## 🔐 Default Admin Credentials
- **CNIC:** `00000-0000000-0`
- **Password:** `admin123`

## 🛡️ Security Measures
- **Rate Limiting:** Protects against brute-force attacks on login/OTP.
- **Helmet Middleware:** Adds security headers to Express.
- **JWT Authentication:** Secure stateless session management.
- **Encrypted PWs:** All passwords hashed with bcrypt.
- **Activity Logging:** Comprehensive audit trail for all critical actions.
