
# Random Calculation Project

This project generates random calculations using a Flask API and displays them on a web page. The frontend is hosted on Netlify, while the backend is hosted on Vercel.



## Project Structure

- **Frontend**: HTML, CSS, JavaScript (Hosted on Netlify)
- **Backend**: Flask API (Hosted on Vercel)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run this project locally, you need to set up the frontend and backend parts separately.

### Backend (Flask API)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask API**:
   ```bash
   python app.py
   ```
   The API will be available at `http://127.0.0.1:5000`.

### Frontend (HTML, CSS, JavaScript)

Open `index.html` in your browser directly, or use a simple HTTP server to serve it.

Update the fetch URL in `index.html`:
```javascript
const response = await fetch("http://127.0.0.1:5000/calculate"); // Change this URL if needed
```

## Usage

Click the "Generate Calculation" button to fetch a random calculation from the backend API and display it on the webpage.

## Deployment

### Deploy Backend to Vercel

1. **Install Vercel CLI**:
   ```bash
   npm install -g vercel
   ```

2. **Deploy your Flask app to Vercel**:
   ```bash
   vercel
   ```

3. Update the fetch URL in `index.html` to use your Vercel deployment URL, like:
   ```javascript
   const response = await fetch("https://your-vercel-backend-url.vercel.app/calculate");
   ```

### Deploy Frontend to Netlify

1. Go to Netlify and log in.
2. Create a New Site and select the repository.
3. Netlify will automatically deploy the frontend.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Hosting**: Vercel (Backend), Netlify (Frontend)

## Contributing

1. Fork this repository.
2. Create a new branch: 
   ```bash
   git checkout -b feature-branch-name
   ```

3. Make your changes and commit them: 
   ```bash
   git commit -m 'Add some feature'
   ```

4. Push to the branch:
   ```bash
   git push origin feature-branch-name
   ```

5. Submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
