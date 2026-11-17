ETHICAL MOBILE SECURITY AWARENESS LAB — WINDOWS 11 + ANDROID + IPHONE

WHAT THIS LAB DOES
- Participant opens the shared HTTPS link.
- After explicit consent, limited browser/device details are sent to the Admin dashboard.
- Optional location is sent only after a separate browser location permission.
- Camera test shows a local preview on the participant's own phone only. It does NOT stream, record, or upload video.
- Hacker-style scan messages are clearly marked SIMULATION.
- No gallery scraping, call history, SMS, WhatsApp, contacts, passwords, or hidden remote control.

LOCAL TEST ON WINDOWS 11
1. Install Python 3 from python.org and tick "Add Python to PATH".
2. Extract this ZIP.
3. Open Command Prompt inside this folder.
4. Run: py -m pip install -r requirements.txt
5. Set a private admin key: set ADMIN_KEY=Use-A-Long-Random-Private-Key
6. Run: py app.py
7. Participant page: http://127.0.0.1:5000
8. Admin page: http://127.0.0.1:5000/admin
9. Enter the same private admin key in the Admin page.

PUBLISH A SHAREABLE HTTPS LINK USING RENDER
1. Create/sign in to GitHub and create a repository named ethical-mobile-demo.
2. Upload app.py, index.html, admin.html, requirements.txt. Do NOT upload sessions.json or any secrets.
3. Sign in to Render and choose New -> Web Service.
4. Connect the GitHub repository.
5. Set Runtime/Language to Python 3.
6. Build Command: pip install -r requirements.txt
7. Start Command: gunicorn app:app
8. In Environment, add:
   Key: ADMIN_KEY
   Value: a long random secret known only to the instructor.
9. Deploy. Render will provide an HTTPS URL.
10. Test the participant URL on your own Android and iPhone first. Admin page is the same URL plus /admin.
11. Share the participant URL with volunteers only after telling them exactly what is collected.

IMPORTANT HOSTING/DATA NOTES
- Render free services may sleep after inactivity; first request can take time to wake up.
- Render's default filesystem is ephemeral. This demo stores session data in sessions.json, so entries can disappear on restart/redeploy. For a continuing class, use a properly configured persistent datastore/disk or keep the demo short-lived. Do not assume the free service retains records.
- Never publish the Admin key or send the /admin key to participants.
- Use HTTPS only for browser camera/location permissions.
- Delete demo participant records after the lecture and avoid collecting real sensitive information.
