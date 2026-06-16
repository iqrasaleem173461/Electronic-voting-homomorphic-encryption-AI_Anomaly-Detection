# AI Assistant Documentation

This document provides a comprehensive guide to the AI Assistant integration in the SecureVote E-Voting system, covering the Webhook-based architecture, interactive greeting features, and initial setup.

## 1. Webhook-Based AI Bridge

The AI Assistant is configured as a **Context-Aware Webhook Bridge**. This allows external AI agents to access real-time website data for a professional "call center" experience.

### How it Works
When a user interacts with the Chat or Voice assistant:
1. The backend gathers live information from the database (Active Elections, Candidates, Manifestos, System Rules).
2. It forwards this context along with the user's message to the configured **Webhook URL**.
3. The external agent processes the data and returns a text response and optional audio.

### Webhook JSON Protocol
External developers should ensure their webhook handles **POST** requests with the following JSON structure:

**Incoming Request:**
```json
{
  "message": "User query or transcript",
  "language": "ur/en",
  "greeting": false,
  "agent": {
    "name": "Configured Agent Name",
    "instructions": "System instructions"
  },
  "context": {
    "activeElections": [ ... ],
    "candidates": [ ... ]
  }
}
```

**Expected Response:**
```json
{
  "response": "AI Text Response",
  "audio": "Optional base64 encoded MP3 audio"
}
```

---

## 2. Interactive AI Voice Greeting

The assistant is designed to be proactive, initiating conversation as soon as a voice call starts.

### Features
- **Proactive Greeting**: AI speaks first (e.g., "Assalam-o-Alaikum, I am SecureVote AI...") using the configured Agent Name.
- **Smart Microphones**: The user's microphone is only activated *after* the AI finishes its welcome message.
- **Backend Trigger**: Supports a `greeting: true` flag in the voice endpoint to generate natural welcome messages.

---

## 3. Context Data Endpoint

For external tools (like Gemini Tools or ElevenLabs Webhook Tools), a dedicated endpoint provides structured system data.

- **URL**: `http://<your-domain>/api/ai/context`
- **Method**: `GET`
- **Response**: Returns a JSON object containing current elections, candidates, and agent instructions.

---

## 4. Setup Guide (Eleven Labs & Gemini)

### Phase 1: API Keys
1. **Eleven Labs**: Sign up at [elevenlabs.io](https://elevenlabs.io), get your API Key and a Voice ID (e.g., "Rachel").
2. **Gemini**: Get a Gemini 2.5 Flash API Key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### Phase 2: Configuration
1. Log in to the **Admin Panel**.
2. Navigate to **AI Settings**.
3. Enter your Gemini and Eleven Labs API Keys.
4. (Optional) Provide your **Webhook URL** for external agent processing.
5. Click **Save Changes**.

---

---

## 5. SMS Integration Guide (Production Setup)

For real-world user verification, you must integrate an SMS Gateway. Local Pakistani providers are recommended for better delivery and lower costs.

### Recommended Providers (Pakistan)
- **EasySendSMS / Sendpk.com**: Good for developers, easy API integration.
- **LifetimeSMS**: Supports branded masking (e.g., your project name as sender).
- **Jazz Business / Telenor API**: Official carrier gateways.

### Setup Steps
1. **Create Account**: Register on your chosen provider's portal.
2. **Purchase Credits**: Buy SMS credits based on your expected traffic.
3. **Get API Credentials**:
   - **API Key**: Found in your provider's developer console.
   - **Base URL**: The endpoint for sending messages (e.g., `https://api.provider.com/sendsms`).
4. **Admin Configuration**: Enter these into the **Admin Panel > AI Settings** under **SMS Gateway Settings**.

---

## 6. Local Testing vs. Production

### Debug Mode (Development)
While `NODE_ENV` is set to `development` (as it is currently on your local machine), the system will include an `otp_debug` field in the API response. This allows you to test the registration flow without receiving a real SMS. Valid for **5 minutes**.

### Production Mode (Go-Live)
When you deploy to a server and set `NODE_ENV=production`:
- The `otp_debug` field will be **automatically removed**.
- Users will only be able to verify their accounts using the OTP sent to their mobile phones via the configured SMS Gateway.

---

## 7. Local Testing (Ngrok)
When testing on localhost, external services cannot reach your server directly. Use **Ngrok** to create a public tunnel:
1. Run `ngrok http 5000`.
2. Use the generated `https://...` link in your Webhook Tool settings.
