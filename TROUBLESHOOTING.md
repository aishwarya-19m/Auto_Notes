# Troubleshooting Network Errors

## Backend is Running ✅

The backend server is running at: **http://localhost:8000**

## Common Network Error Solutions

### 1. Check if Frontend is Running

Make sure the frontend is running in a separate terminal:

```powershell
cd frontend
npm run dev
```

You should see:
```
➜  Local:   http://localhost:3000/
```

### 2. Verify Backend is Accessible

Test the backend directly in your browser:
- Open: http://localhost:8000/
- You should see: `{"message":"AutoNotes Pro API is running"}`

### 3. Check API Documentation

Open: http://localhost:8000/docs
- This confirms the backend is fully operational

### 4. Common Issues

**Issue: "Network Error" in Frontend**
- ✅ Backend is running (verified)
- Make sure frontend is also running
- Check browser console for detailed error messages
- Try refreshing the page

**Issue: CORS Error**
- Already fixed in the code
- Backend allows requests from localhost:3000

**Issue: Connection Refused**
- Make sure backend is running: `python main.py` in backend folder
- Check if port 8000 is being used by another application

### 5. Quick Test

Test the connection from PowerShell:
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/" -Method Get
```

Should return: `{"message":"AutoNotes Pro API is running"}`

### 6. Restart Both Servers

If issues persist:

**Terminal 1 - Backend:**
```powershell
cd backend
.\venv\Scripts\Activate.ps1
python main.py
```

**Terminal 2 - Frontend:**
```powershell
cd frontend
npm run dev
```

Then open: http://localhost:3000

