# sgarcia-dev: Personal Website (v2.2)

This repository hosts version 2.2 of a personal website, designed to showcase projects, skills, or personal information. The site features a frontend built with standard web technologies (HTML, CSS, JavaScript) and is potentially supported by a Python backend for dynamic content or server-side functionalities.

## Project Structure

- `attached_assets/`: Contains static assets like images, videos, or other media used on the website.
- `index.html`: The main entry point for the website, defining its structure and content.
- `styles.css`: Contains the CSS rules for styling the website's appearance.
- `script.js`: Holds JavaScript code for interactive elements and dynamic functionalities on the frontend.
- `server.py`: A Python script that likely functions as a backend server, serving the static files, handling API requests, or performing other server-side tasks.
- `.replit`, `replit.md`: Configuration files related to the Replit development and hosting environment.
- `README.md`: This file, providing an overview and instructions for the project.

## How It Works

The website is a combination of static and potentially dynamic content:

*   **Frontend:** `index.html`, `styles.css`, and `script.js` work together to render the user interface in a web browser.
*   **Backend (Optional/Dynamic):** If `server.py` implements a web server (e.g., using Flask or FastAPI), it would serve the frontend files and handle any API calls from the client-side JavaScript, allowing for features like contact forms, data fetching, or other interactive elements.

The `.replit` configuration suggests that the project can be easily run or deployed within the Replit environment.

## Getting Started

To view or run this personal website:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/samuelngarciar/sgarcia-dev.git
    cd sgarcia-dev
    ```
2.  **Run with Replit:** If you have a Replit account, you can import this repository directly into Replit for an instant development and hosting environment.
3.  **Local Setup (Python Backend):**
    *   Ensure Python is installed.
    *   Install any dependencies (if `server.py` has specific Python library requirements, these would typically be in a `requirements.txt` file, which is not present here but might be implicitly handled by Replit or a simple `pip install` for common web frameworks).
    *   Run the Python server: `python server.py` (or a similar command depending on the framework used in `server.py`).
4.  **Local Setup (Static Only):** You can open `index.html` directly in your web browser to view the static content.

## Contribution

Feel free to fork this repository, make improvements, and submit pull requests.