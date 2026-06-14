import os
os.environ["DATABASE_URL"]="sqlite:///./test_expowatch.db"
from fastapi.testclient import TestClient
from app.main import app
from app.seed.seed_data import seed
seed()
client=TestClient(app)
def test_health(): assert client.get('/api/health').json()['status']=='ok'
def test_events_seeded():
    r=client.get('/api/events'); assert r.status_code==200; assert len(r.json())>=10
def test_lead_preview_caveat():
    ev=client.get('/api/events').json()[0]
    r=client.get(f"/api/events/{ev['slug']}/lead-package/preview")
    assert 'not proof of criminality' in r.json()['html']
