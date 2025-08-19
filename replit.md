# Overview

This is a professional portfolio website for Samuel García, a Cloud Native consulting expert. The site showcases 15 years of software development experience with 5 years specialized in Cloud Native transformations. It's designed as a static website to highlight expertise in Kubernetes, Serverless, DevOps, and modern infrastructure solutions, serving as a digital business card and lead generation tool for potential clients.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Static HTML/CSS/JavaScript**: Traditional multi-page application approach using vanilla JavaScript for interactivity
- **Single Page Application (SPA) behavior**: Custom routing in the Python server handles non-file paths by serving index.html, enabling SPA-like navigation
- **Responsive Design**: Mobile-first approach with hamburger navigation and responsive layouts
- **Component-based CSS**: Modular CSS architecture using CSS custom properties for consistent theming

## Styling and Design
- **CSS Custom Properties**: Centralized design system with green color scheme reflecting cloud/tech branding
- **Font Awesome Integration**: External CDN for consistent iconography
- **Modern CSS Features**: Flexbox/Grid layouts, CSS transitions, and responsive design patterns

## Server Architecture
- **Python HTTP Server**: Custom HTTP handler extending SimpleHTTPRequestHandler for static file serving
- **Custom Routing Logic**: Intelligent file serving that defaults to index.html for directory requests and handles SPA routing
- **MIME Type Detection**: Automatic content-type headers based on file extensions
- **Static File Optimization**: Direct file serving with appropriate headers for performance

## JavaScript Functionality
- **Vanilla JavaScript**: No framework dependencies, focusing on core DOM manipulation
- **Event-driven Architecture**: Modular event listeners for navigation, scrolling effects, and form handling
- **Mobile Navigation**: Toggle-based hamburger menu with smooth animations
- **Smooth Scrolling**: Custom scroll behavior with navbar offset calculations

# External Dependencies

## CDN Resources
- **Font Awesome 6.0.0**: Icon library served from cdnjs.cloudflare.com for professional iconography

## Development Dependencies
- **Python 3**: Built-in http.server module for local development and potential deployment
- **Standard Web Technologies**: HTML5, CSS3, ES6+ JavaScript with no build process required

## Infrastructure Considerations
- **Static Hosting Ready**: Architecture supports deployment to any static hosting service (Netlify, Vercel, AWS S3, etc.)
- **Python Server Option**: Included Python server provides flexibility for environments requiring server-side routing
- **No Database**: Fully static architecture with potential for form handling through external services