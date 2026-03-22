web: pip install -r backend/requirements.txt && gunicorn -w 4 -k uvicorn.workers.UvicornWorker backend.app.main:app --bind 0.0.0.0:${PORT:-8000} --chdir backend
