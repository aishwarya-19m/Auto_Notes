# Fix Port Binding Error (Error 10048)

## Problem
Error: `error while attempting to bind on address ('0.0.0.0',8000)`
This means port 8000 is already in use by another process.

## Solution 1: Automatic Port Selection (Recommended)

The backend has been updated to automatically use port 8001 if port 8000 is busy.

**The backend will now:**
- Try port 8000 first
- If busy, automatically use port 8001
- Print which port it's using in the terminal

## Solution 2: Manually Free Port 8000

If you want to use port 8000 specifically:

```powershell
# Find what's using port 8000
Get-NetTCPConnection -LocalPort 8000

# Stop the process (replace PID with actual number)
Stop-Process -Id <PID> -Force

# Then restart backend
cd backend
.\venv\Scripts\Activate.ps1
python main.py
```

## Solution 3: Use Different Port

You can manually change the port in `backend/main.py`:

```python
uvicorn.run(app, host="0.0.0.0", port=8001)  # Change 8001 to any free port
```

## Check Which Port Backend is Using

After starting the backend, check the terminal output. It will show:
- `Starting server on port 8000...` (if 8000 is free)
- `Port 8000 busy, using port 8001 instead...` (if 8000 is busy)

Or test in browser:
- http://localhost:8000
- http://localhost:8001

## Update Frontend Configuration

If backend uses port 8001, update frontend:

**Option 1: Update vite.config.js**
```javascript
proxy: {
  '/api': {
    target: 'http://localhost:8001',  // Change to 8001
    changeOrigin: true,
  }
}
```

**Option 2: Use environment variable**
Create `frontend/.env`:
```
VITE_API_URL=http://localhost:8001
```

## Quick Fix Commands

```powershell
# Kill all Python processes
Get-Process python | Stop-Process -Force

# Wait a few seconds
Start-Sleep -Seconds 3

# Start backend (will auto-select port)
cd backend
.\venv\Scripts\Activate.ps1
python main.py
```

## Verify Backend is Running

Test in browser or PowerShell:
```powershell
# Test port 8000
Invoke-RestMethod -Uri "http://localhost:8000/"

# Test port 8001
Invoke-RestMethod -Uri "http://localhost:8001/"
```

One of these should return: `{"message":"AutoNotes Pro API is running"}`

