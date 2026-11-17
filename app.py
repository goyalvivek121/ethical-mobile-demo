from flask import Flask, request, jsonify, send_from_directory
from pathlib import Path
from datetime import datetime, timezone
import json, os, secrets
app=Flask(__name__)
ROOT=Path(__file__).parent
DB=ROOT/'sessions.json'
ADMIN_KEY=os.environ.get('ADMIN_KEY')
if not ADMIN_KEY:
    raise RuntimeError('Set ADMIN_KEY environment variable before starting the app.')
def get_rows():
    if not DB.exists(): return []
    try: return json.loads(DB.read_text(encoding='utf-8'))
    except Exception: return []
@app.get('/')
def home(): return send_from_directory(ROOT,'index.html')
@app.get('/admin')
def admin(): return send_from_directory(ROOT,'admin.html')
@app.post('/api/submit')
def submit():
    d=request.get_json(silent=True) or {}
    if d.get('consent') is not True: return jsonify(error='Consent required'),400
    sid=d.get('sessionId') or secrets.token_urlsafe(8)
    keys=('platform','browser','language','screen','timezone','deviceClass','location')
    clean={k:d[k] for k in keys if k in d}
    a=get_rows(); old=next((x for x in a if x['sessionId']==sid),None)
    if old: old.update(clean); old['time']=datetime.now(timezone.utc).isoformat()
    else: clean.update(sessionId=sid,time=datetime.now(timezone.utc).isoformat()); a.append(clean)
    DB.write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
    return jsonify(ok=True,sessionId=sid)
@app.get('/api/sessions')
def sessions():
    if request.headers.get('X-Admin-Key')!=ADMIN_KEY: return jsonify(error='Unauthorized'),401
    return jsonify(get_rows())
if __name__=='__main__': app.run(host='0.0.0.0',port=int(os.environ.get('PORT','5000')),debug=False)
