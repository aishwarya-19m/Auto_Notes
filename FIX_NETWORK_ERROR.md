# Fix Network Error - Step by Step

## ✅ Backend Status: RUNNING
- Backend is confirmed running on http://localhost:8000
- Python process is active

## 🔍 Most Common Cause: Frontend Not Running

The "Network Error" usually means the frontend can't connect to the backend. This is most often because **the frontend is not running**.

## 🔧 Solution Steps

### Step 1: Start the Frontend

**Open a NEW PowerShell/Terminal window** (keep backend terminal open):

```powershell
cd "C:\Users\Aishwarya\Desktop\Autonotes Pro\frontend"
npm run dev
```

**You should see:**
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:3000/
```

### Step 2: Verify Both Are Running

**Check Backend:**
- Open browser: http://localhost:8000
- Should see: `{"message":"AutoNotes Pro API is running"}`

**Check Frontend:**
- Open browser: http://localhost:3000
- Should see the AutoNotes Pro interface

### Step 3: Test the Connection

1. Open http://localhost:3000 in your browser
2. Try to generate notes from a YouTube URL
3. If you still see "Network Error", continue to Step 4

### Step 4: Check Browser Console

1. Press **F12** in your browser
2. Go to **Console** tab
3. Look for error messages
4. Common errors:
   - `ERR_CONNECTION_REFUSED` → Backend not running
   - `CORS error` → CORS configuration issue
   - `Network Error` → Frontend can't reach backend

### Step 5: Verify Ports

**Check if ports are in use:**
```powershell
# Check port 8000 (backend)
Get-NetTCPConnection -LocalPort 8000 -ErrorAction SilentlyContinue

# Check port 3000 (frontend)
Get-NetTCPConnection -LocalPort 3000 -ErrorAction SilentlyContinue
```

## 🚨 Quick Fixes

### Fix 1: Restart Backend
```powershell
# In backend terminal, press Ctrl+C to stop
# Then restart:
cd backend
.\venv\Scripts\Activate.ps1
python main.py
```

### Fix 2: Restart Frontend
```powershell
# In frontend terminal, press Ctrl+C to stop
# Then restart:
cd frontend
npm run dev
```

### Fix 3: Clear Browser Cache
- Press `Ctrl+Shift+Delete`
- Clear cached images and files
- Or use Incognito/Private mode

### Fix 4: Check Firewall
- Windows Firewall might be blocking connections
- Allow Python and Node.js through firewall

## 📋 Checklist

- [ ] Backend is running (http://localhost:8000 works)
- [ ] Frontend is running (http://localhost:3000 works)
- [ ] Both terminals are open and showing running status
- [ ] Browser console shows no errors
- [ ] Tried hard refresh (Ctrl+Shift+R)
- [ ] Checked firewall settings

## 🆘 Still Not Working?

1. **Check backend terminal for errors**
   - Look for Python errors
   - Check if it says "Uvicorn running"

2. **Check frontend terminal for errors**
   - Look for npm/node errors
   - Check if it says "Local: http://localhost:3000"

3. **Try accessing API directly:**
   - Open: http://localhost:8000/docs
   - This confirms backend is fully working

4. **Check .env file:**
   ```powershell
   cd backend
   # Make sure .env exists and has your API key
   ```

## 💡 Pro Tip

**Always run both servers:**
- Terminal 1: Backend (`python main.py`)
- Terminal 2: Frontend (`npm run dev`)

Both must be running simultaneously for the app to work!

