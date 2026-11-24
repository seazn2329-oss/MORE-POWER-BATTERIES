You are a senior Python developer and AI engineer. Build the complete project described below as a working website in the current empty folder. Do not stop after a plan. Create every file in full.

The site is for a second-year student. Comment the code simply.

Tech rules
- Backend: Python 3.11+ with Flask. Use SQLite with SQLAlchemy so no database server is needed.
- Frontend: Jinja2 templates, Bootstrap 5 via CDN, a little vanilla JavaScript. Mobile-friendly and clean.
- Make `python app.py` start the server on http://127.0.0.1:5000 .
- Structure: `app.py`, `models.py`, `routes.py`, `templates/` (with a base layout), `static/`, `seed.py`, `requirements.txt`, `.env.example`, `README.md`, `ai_services.py`.
- Security: password hashing for admin login, input validation, CSRF protection on HTML forms, secrets only in `.env`.
- `.env.example` must contain `SECRET_KEY`, `API_KEY`, and `MODEL_API_KEY` (left blank).

Chatbot-ready rules
The website will be connected to an agent on Dify. So:
1. JSON API endpoints under `/api/` for the tools below. Clear inputs and outputs. Prices in GH₵.
2. Protect every `/api/` route except `/api/health` with a header `X-API-Key`, read from `.env`.
3. Serve the OpenAPI schema at `/openapi.json`. Set `operationId` to exactly the names listed below. The `servers` url must be `http://127.0.0.1:5000` so the student can change it to a public https URL later. No secrets in the schema.
4. In the base template, leave this comment just before `</body>`: `<!-- CHATBOT WIDGET HERE -->`
5. `GET /api/health` returns `{"status": "ok"}` with no API key.

Project: real estate listings
Business: a small agency listing houses, rooms, and land for rent or sale across Accra.

Seed data must include a 2 bedroom apartment in Madina, type `apartment`, rent GH₵1,800 per month, status available, with at least one image and one agent. Include other listings in other Accra neighbourhoods, some for sale. Seed an admin user and print the admin email and password at the end of `seed.py`.

Public pages: Home with featured listings, search with filters (location, price range, bedrooms, type), listing detail with an image gallery, viewing request form, agent profiles.

Admin pages: Login, add/edit/delete listings, mark as sold or rented, view viewing requests, view `ai_logs`.

Database tables: `listings` (title, type, price, location, bedrooms, bathrooms, description, status, rent period), `images`, `agents`, `viewing_requests`, `admins`, `ai_logs`.

Chatbot tool endpoints:
- `GET /api/listings/search?location=&min_price=&max_price=&bedrooms=&type=` operationId `search_listings`. Returns only available listings.
- `GET /api/listings/<id>` operationId `get_listing_details`.
- `POST /api/viewings` operationId `schedule_viewing`. Body: listing id, date, time, name, phone.

AI add-ons, in `ai_services.py`
Read `MODEL_API_KEY` from `.env`. If it is missing, return a friendly message and do not crash.
- A listing description writer: the agent enters basic facts and gets a description. It must not invent rooms or prices that were not in the facts.
- A natural-language search box. Example: "2 bedroom near Madina under 2000 a month" becomes filters, then runs the real search.
- A price suggestion that compares similar listings and explains the comparison.
Log AI questions in `ai_logs`, and add a simple admin page to view them.

When you finish, list every file you created, the exact PowerShell commands to install and run the site on Windows, and one sample request for each `/api/` endpoint using `Invoke-RestMethod` and the `X-API-Key` header.
