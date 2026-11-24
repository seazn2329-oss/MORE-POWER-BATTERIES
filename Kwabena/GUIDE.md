# Kwabena: real estate listings

You are building a listings website for houses, rooms, and land in Accra, then an AI agent on Dify that can search listings and book a viewing by calling your website. This guide starts with an empty folder and ends with the chat button on the site.

Dify is the site at https://cloud.dify.ai . The spoken name sounds like "DeFi", but the address is dify.ai.

The site is Flask. It runs on port 5000.

## 1. Write these down first

Use the same details on the website and in the agent.

- Agency name
- Agent phone number
- An API key you invent, at least 24 characters, with no spaces. Example shape: `kwabena-homes-7kQm29LxP4nR8wTz`. The website and Dify must use this exact string.

## 2. Install the tools

1. Python 3.11 or newer. In PowerShell run `python --version`. If that fails, install Python from https://www.python.org/downloads/ and tick "Add python.exe to PATH".
2. Cursor from https://cursor.com . Sign in. If your class uses GitHub Copilot in VS Code, or another coding chat, you can use that instead. The prompt is the same. Step 4 says where to paste it.
3. A free account at https://cloud.dify.ai .
4. ngrok from https://ngrok.com . Sign up and install it. Dify's servers cannot call `localhost`. Your laptop has to be reachable on the internet while you test.

## 3. Create the project folder and open it

The guide folder you were given is only the instructions. The website needs its own empty folder.

1. Open File Explorer.
2. Go to Documents.
3. Create a folder named `kwabena-listings`.
4. Open Cursor.
5. File, then Open Folder, and choose `kwabena-listings`.
6. If Cursor asks whether to trust the folder, trust it.
7. Confirm the folder is empty. Do not copy this guide into it.

## 4. Build the website in Cursor or Copilot

In Cursor:

1. Open the chat panel with Ctrl+L.
2. Set the mode to Agent, if you see a mode selector.
3. Open `build_prompt.md` from the folder your lecturer gave you. Select all of it and copy it.
4. Paste it into the agent and send it.
5. Wait until it finishes writing files. You should see `app.py`, `models.py`, `routes.py`, `templates`, `static`, `seed.py`, `requirements.txt`, `.env.example`, `README.md`, and `ai_services.py`.
6. If a file from that list is missing, send a follow-up in the same chat: name the missing file and ask for it. Do not start a second project in this folder.

In GitHub Copilot, open the same empty folder in VS Code, open Copilot Chat, switch to agent mode if it is there, and paste `build_prompt.md`. Any other coding agent works the same way: the folder must be the one it is allowed to edit, and you paste the whole build prompt.

Read the pages it created before you move on. You are the one who will demo this. If something from the page list in step 6 is missing, say so in the chat and ask for that page.

## 5. Run the site

In Cursor's terminal (or PowerShell), with `kwabena-listings` as the current folder:

```
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
```

If PowerShell blocks the activate script, run this once, then try activate again:

```
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Open `.env` and set `API_KEY` to the key from step 1. Set `SECRET_KEY` to a different long random string. Leave `MODEL_API_KEY` empty unless your lecturer gave you a model key. The chatbot runs on Dify, so the site can work without that key. The extra AI pages will show a friendly "not configured" message.

Then:

```
python seed.py
python app.py
```

If `python app.py` does not start the server, use the command the agent printed. It should be serving http://127.0.0.1:5000 .

Leave this terminal open. Closing it stops the site.

## 6. Click through the website

Open http://127.0.0.1:5000 and check each of these yourself.

1. Home loads, with featured listings. Narrow the browser and check it is still usable.
2. Search for 2 bedrooms in Madina. A seeded apartment at GH₵1,800 a month should appear. Open it. The gallery, price, and location should be on the detail page.
3. Request a viewing with your name, phone number, a date, and a time. As admin, confirm the viewing request is listed.
4. Mark that listing rented or sold. Run the same search again. It should no longer appear as available.
5. The agent profile page loads for the seeded agent.
6. In the page source of any page (right-click, View page source), find the comment `<!-- CHATBOT WIDGET HERE -->` just before `</body>`. You will paste the chat script under that comment later. Do not delete the comment.

## 7. Test the API from PowerShell

Open a second terminal, activate the venv the same way, and replace `YOUR_KEY` with your API key.

```
Invoke-RestMethod http://127.0.0.1:5000/api/health
```

That one needs no key. You want a status of ok.

```
Invoke-RestMethod -Headers @{"X-API-Key"="YOUR_KEY"} "http://127.0.0.1:5000/api/listings/search?location=Madina&max_price=2000&bedrooms=2&type=apartment"
```

```
Invoke-RestMethod -Headers @{"X-API-Key"="YOUR_KEY"} http://127.0.0.1:5000/api/listings/1
```

Use the id from the search if it is not 1.

```
Invoke-RestMethod -Method POST -Headers @{"X-API-Key"="YOUR_KEY"; "Content-Type"="application/json"} -Body '{"listing_id":1,"date":"2026-11-25","time":"10:00","name":"Ama Mensah","phone":"0244000000"}' http://127.0.0.1:5000/api/viewings
```

A wrong key should be rejected. A request with no `X-API-Key` header should be rejected too. If PowerShell says the body was rejected, open the route in the code or in `/openapi.json` and use the field names that are actually there.

Open http://127.0.0.1:5000/openapi.json . You need these exact operation ids:

- `search_listings`
- `get_listing_details`
- `schedule_viewing`

If the ids are missing or different, ask the coding agent to set `operationId` to those names. Dify uses that id as the tool name, and the system prompt talks to the tools by those names.

## 8. Let Dify reach the site

The site and this next program both have to keep running.

1. In a new terminal, from any folder, run `ngrok http 5000`.
2. Copy the https forwarding URL. It looks like `https://something.ngrok-free.app`.
3. In the browser, open `https://something.ngrok-free.app/api/health`. You want the same ok status. If ngrok shows a warning page first, click through it. That warning is only in your browser.
4. Find where the OpenAPI schema sets the server URL. It might be inside `app.py` or a generated `openapi.json`. Change `http://127.0.0.1:5000` to your ngrok https URL, with no trailing path. Restart `python app.py`.
5. Open `https://YOUR-NGROK-URL/openapi.json` and confirm the server URL in the file is the https one, not localhost.

If you stop ngrok and start it again, the free URL usually changes. Update the schema again when that happens.

## 9. Create the agent on Dify

1. Sign in at https://cloud.dify.ai .
2. If the agent cannot reply yet, open Settings, then Model Provider, and connect the model your lecturer named. Without a model, there is nothing to write the replies.
3. Open Agents. Click Create, then Create from blank. Name it `the agency name`.
4. If your Dify still has the older screen, use Studio, Create blank app, and choose Agent. If you only see Chatbot, create a Chatbot and add tools the same way as below. The instructions box is the same box.

## 10. Paste the system prompt

1. Open `system_prompt.md`.
2. Replace every bracketed placeholder with your real details. The file uses `[AGENCY NAME]` and `[PHONE]`.
3. If Dify has a conversation opener, paste the opening message from the top of that file.
4. If it has suggested questions, add the three questions from that file.
5. Paste the instructions, from the "You are" line down to the end, into the agent's prompt or instructions box.
6. Do not leave the square brackets in. The agent will say them out loud.

## 11. Connect the website as tools

Dify calls this a Swagger or OpenAPI tool. The menu is Integrations, then Tools. On an older Dify it is Tools, then Custom, then Create custom tool.

1. Add a Swagger API tool.
2. Name it `Listings API`.
3. Either paste the full text of `https://YOUR-NGROK-URL/openapi.json`, or import that URL.
4. Check the list of operations. You want `search_listings`, `get_listing_details`, and `schedule_viewing`. If localhost is still the server, fix step 8 and import again.
5. Authentication: API Key. Header name exactly `X-API-Key`. Value: the same key as `API_KEY` in `.env`.
6. Save.
7. Open the agent again. Add this tool. Leave those operations on.
8. In the agent's test panel, use the questions in the next paragraph. The facts in the reply must match the website. If a price, stock level, time, or status is not on the site, the tool was not really used.

Say you want to rent, then: "2 bedroom apartments in Madina." It should show at most three listings, with price, location, and one feature each. The Madina apartment at GH₵1,800 a month must be among them if it is still available. It should say the rent is monthly.

Ask it to schedule a viewing. It should repeat the listing, date, time, name, and phone number, and wait for a yes. After you confirm, the request must be on the admin viewing list.

Ask it to offer a discount. It should refuse and give the agent phone number. It must not invent a listing you cannot find on the site.

If the tool test returns a web page instead of JSON, ngrok's browser warning is blocking Dify. On the custom tool, add a header `ngrok-skip-browser-warning` with value `true`, save, and test again.

If the agent invents a fact that should have come from the database, the tool was not called. Usual causes: the tool is not added to the agent, the server URL is still localhost, or the API key does not match.

## 12. Put the chat on the website

1. In Dify, click Publish. Do this again any time you change the prompt or the tools, or the website will keep the old agent.
2. Open the Access Point tab. On the Web App card, click Embed into site.
3. Copy the snippet Dify gives you.
4. In your project, open the base template (often `templates/base.html`). Find `<!-- CHATBOT WIDGET HERE -->`. Paste the snippet on the next line, still above `</body>`. Do not paste it inside the comment. A comment would hide the script.
5. If Dify only shows a token, paste this and replace both copies of `YOUR_TOKEN`:

```html
<script>
 window.difyChatbotConfig = {
  token: "YOUR_TOKEN",
  baseUrl: "https://udify.app"
 }
</script>
<script
 src="https://udify.app/embed.min.js"
 id="YOUR_TOKEN"
 defer>
</script>
```

6. Save, restart `python app.py` if the template is cached, and reload http://127.0.0.1:5000 .
7. A chat button should sit at the corner of every public page. Open it and ask one of the questions from step 11 from the website, not only from Dify's test panel.

The site on your laptop and the ngrok window both have to be running for the button to answer with live data. If either one is closed, the agent cannot see your database.

## 13. Connect WhatsApp

Do this after the chat button on the website already works. WhatsApp talks to the same Dify agent. You do not add WhatsApp code to the Flask or FastAPI site. The website and ngrok still have to be running, because the agent still calls your API for the facts.

1. Go to https://developers.facebook.com and sign in. If Facebook asks you to become a developer, accept that.
2. Open My Apps, then Create App. If it asks for a type, choose Business. Name the app after your business.
3. On the app page, add the WhatsApp product.
4. Open WhatsApp, then API Setup. Leave the test phone number Meta gives you.
5. On that page, copy the Phone number ID and the WhatsApp Business Account ID.
6. Generate an access token and copy it. A test token expires, often within a day. If WhatsApp goes quiet later, generate a new token and paste it into Dify again. Do not put this token in your website code or in git.
7. Under the "To" box, add your own mobile number and enter the code WhatsApp sends you. Only numbers you add here can message the test number.
8. In Dify, open the Marketplace. Search for WhatsApp and install the plugin `whatsapp-bot` by langgenius.
9. Open that plugin's settings and fill them in:
   - Access token: the token from step 6
   - Verify token: a private word you invent, such as `verify-token-class`. Write it down. Meta and Dify must use the same word.
   - Phone number ID
   - WhatsApp Business Account ID
   - App to reply with: the agent you already published
10. Save. Copy the webhook callback URL the plugin shows. It is an https address.
11. Back in Meta, open WhatsApp, then Configuration. Set the callback URL and the verify token. Verify and save. Subscribe to the messages field.
12. From your own phone, send a WhatsApp message to the Meta test number. Use the test in the next paragraph.

Ask: "2 bedroom apartments in Madina". The GH₵1,800 listing must appear if it is still available. The reply must not offer a discount.

If Meta will not verify the webhook, the verify token or the callback URL does not match what Dify shows.

If the test number repeats your words back and does nothing else, no agent is selected in the plugin. Select your published agent and save again.

## 14. Connect Gmail so the agent can fetch mail

The agent reads one mailbox: a Gmail address for this business. Create a new Gmail account for the project, or use one you own. It must not be a customer's account, and you must not type anyone's Gmail password into the chat.

1. In the Dify Marketplace, install the Gmail plugin by langgenius (`dify-gmail`). Do not also install Outlook on this agent. The tool names clash and the agent will not save.
2. Open the plugin's OAuth client settings and copy the redirect URL Dify shows.
3. Go to https://console.cloud.google.com and create a project named after your business.
4. Open APIs and Services, then Library. Search for Gmail API and enable it.
5. Open the OAuth consent screen. Google may call this Google Auth Platform. Choose External. Use your business name. Add your business Gmail address as a test user.
6. Open Credentials. Create an OAuth client ID. Application type: Web application.
7. Under Authorized redirect URIs, paste the URL from Dify. Save.
8. Copy the Client ID and the Client secret.
9. Paste both into the Dify Gmail plugin. Use the single shared account, which is the business mailbox, then save and authorize. Sign in as that Gmail user. If Google says the app is not verified, open Advanced and continue. The app is in testing, so only the test user you added can sign in.
10. On the agent, add the Gmail tools that search mail, read one message, and create a draft. Leave sending off until you have checked a draft. If the labels on your screen differ a little, pick search, read, and draft.
11. The mail rules are at the bottom of `system_prompt.md`. If they are not in the agent instructions yet, paste them in. Publish the agent again.
12. From a second email address, send a message to the business Gmail. Use the subject in the test below. In Dify's test panel, ask the agent to find that email.

Subject: "Viewing request for Madina". Ask the agent to read that email and draft a reply with the real price and location. It must not schedule the viewing until the date, time, name, and phone number are confirmed.

The draft should sit in Gmail's Drafts folder. The agent must not send it until you reply yes.

Another Dify marketplace tool, if your lecturer names one, follows this same order: install it, authorize it, add it to the agent, and add one line to the instructions that says when to use it. Finish WhatsApp and Gmail first.

## 15. Check this list before you submit

- The public pages and the admin pages in step 6 work.
- `/api/health` works with no key. The other API routes reject a missing or wrong key.
- The sample API calls return data that you can also see by clicking through the site.
- The Dify agent uses the tools. A change the agent makes shows up on the website, or a fact it quotes is one you can find on the site.
- The chat button is on the site, and a question from that button hits your API.
- The agent does not ask for a Mobile Money PIN or a card number.
- A WhatsApp message to the Meta test number got a reply that matches the website.
- The agent found the test email in the business Gmail and saved a draft. It did not send that draft by itself.

- You can explain, in one minute, which file holds the API key and why Dify cannot use `localhost`.

The AI add-ons in `ai_services.py` (listing description writer, natural-language search, price suggestion) are part of the build prompt. The price suggestion should compare similar listings and say how it got the figure. Try them if your lecturer gave you a `MODEL_API_KEY`. If the key is empty, those pages should say so plainly and the rest of the site should still work. Do not block the chat button on those extras.

What to hand in: the project folder, the Dify agent published, and a short note with your business name, the question you tested from the chat button, and whether the answer matched the website.
