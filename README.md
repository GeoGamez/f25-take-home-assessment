# Lynkr Technical Assessment

## Canadidate Comments
Due to not having an api key for the historic endpoint, I was unable to test this. 
I was able to successfully run the code with current which is on the branch current.

## Overview

Build a weather data system where users can submit weather requests and retrieve stored results by ID.

## Project Structure

```
├── frontend/          # Next.js frontend application
│   ├── src/
│   │   ├── app/       # Next.js app router pages
│   │   └── components/ # React components
│   └── package.json
└── backend/           # FastAPI backend application
    ├── main.py        # Main API application
    └── requirements.txt
```

## Prerequisites

- Node.js 18+ and npm/yarn
- Python 3.8+
- WeatherStack API key (free at https://weatherstack.com/)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-forked-repo-url>
cd f25-take-home-assessment
```

### 2. Backend Setup

First, create and activate a Python virtual environment to keep dependencies isolated:

**On macOS/Linux:**

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**On Windows:**

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Note:** You'll need to activate the virtual environment each time you work on the backend

### 3. Frontend Setup

```bash
cd frontend
npm install
# or
yarn install
```

### 4. Get WeatherStack API Key

1. Create a free account at https://weatherstack.com/
2. Get your API key from the dashboard
3. You'll need this for implementing the POST /weather endpoint

## Running the Application

### Start Backend (Terminal 1)

```bash
cd backend
python main.py
```

Backend will run on http://localhost:8000

### Start Frontend (Terminal 2)

```bash
cd frontend
npm run dev
# or
yarn dev
```

Frontend will run on http://localhost:3000

## What's Already Implemented

### ✅ Backend Features

- Basic FastAPI application with CORS configured
- **GET /weather/{id}** endpoint that retrieves stored weather data
- In-memory storage system
- Sample data for testing
- Pydantic models for request/response validation

### ✅ Frontend Features

- **Weather submission form** with date, location, and notes fields
- Form validation and error handling
- Responsive design with Tailwind CSS
- Dark/light theme support

## Your Tasks

### Backend Task: Implement POST /weather endpoint

**What you need to build:**

- Endpoint that receives form data (date, location, notes)
- Integration with WeatherStack API to fetch weather data
- Store combined data with unique ID in memory
- Return the ID to the frontend

**API Endpoint:** `POST /weather`

**Expected Request Body:**

```json
{
  "date": "2024-01-15",
  "location": "New York",
  "notes": "Optional notes"
}
```

**Expected Response:**

```json
{
  "id": "unique-weather-id"
}
```

### Frontend Task: Build data lookup interface

**What you need to build:**

- Input field for entering weather data ID
- Button to fetch data from backend
- Display retrieved weather information in a nice format
- Error handling for invalid IDs

**Existing Backend Endpoint:** `GET /weather/{id}`

## Testing Your Implementation

### Testing the Backend

1. Submit a weather request through the frontend form
2. You should receive an ID back
3. Use that ID to test the GET endpoint: `http://localhost:8000/weather/{id}`

### Testing the Frontend

1. Use the sample ID printed in the backend console when starting the server
2. Enter it in your lookup interface
3. You should see the sample weather data displayed

## Success Criteria

- Form submission returns an ID
- ID can be used to look up and display weather data
- Basic error handling for invalid forms/IDs
- Clean, functional code

## Optional Bonus Features

- Better styling and UX improvements
- Form validation enhancements
- Additional weather data fields
- Loading states and better error messages
- Data persistence improvements

## Submission

Push your completed code to your forked repository and submit the public GitHub URL.
