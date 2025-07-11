<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚀 Godmode System Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            min-height: 100vh;
            color: white;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }
        .header {
            text-align: center;
            margin-bottom: 40px;
            animation: fadeInDown 1s ease-out;
        }
        .header h1 {
            font-size: 3.5rem;
            margin-bottom: 10px;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.5);
            background: linear-gradient(45deg, #ff6b6b, #feca57, #48cae4, #06ffa5);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: rainbow 3s ease-in-out infinite alternate;
        }
        .launch-section {
            text-align: center;
            margin: 40px 0;
        }
        .mega-launch-btn {
            background: linear-gradient(45deg, #ff6b6b, #feca57);
            border: none;
            padding: 30px 80px;
            font-size: 2.5rem;
            font-weight: bold;
            border-radius: 50px;
            color: white;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 15px 30px rgba(0,0,0,0.3);
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        .mega-launch-btn:hover {
            transform: translateY(-8px) scale(1.05);
            box-shadow: 0 25px 50px rgba(0,0,0,0.4);
        }
        .revenue-display {
            font-size: 4rem;
            font-weight: bold;
            color: #00ff88;
            text-align: center;
            margin: 20px 0;
            text-shadow: 0 0 30px rgba(0,255,136,0.8);
            animation: pulse 2s ease-in-out infinite alternate;
        }
        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin-top: 40px;
        }
        .card {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(15px);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            border: 1px solid rgba(255,255,255,0.2);
            transition: all 0.3s ease;
        }
        .card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }
        .metric {
            font-size: 1.2rem;
            margin: 10px 0;
        }
        .metric-value {
            font-size: 2rem;
            font-weight: bold;
            color: #00ff88;
        }
        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-50px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes rainbow {
            0% { filter: hue-rotate(0deg); }
            100% { filter: hue-rotate(360deg); }
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            100% { transform: scale(1.05); }
        }
        .status-indicator {
            display: inline-block;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #00ff88;
            animation: blink 1s ease-in-out infinite alternate;
            margin-right: 10px;
        }
        @keyframes blink {
            0% { opacity: 0.5; }
            100% { opacity: 1; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀💰🧠 GODMODE SYSTEM 🧠💰🚀</h1>
            <p>Auto-Improving AI • $1,000+ Daily Revenue • 24/7 Learning</p>
        </div>
        
        <div class="launch-section">
            <div class="revenue-display" id="revenue">$0.00</div>
            <button class="mega-launch-btn" onclick="launchSystem()">
                🚀 LAUNCH_GODMODE 🚀
            </button>
            <div class="status" id="status">Ready for ultimate launch...</div>
        </div>
        
        <div class="dashboard-grid">
            <div class="card">
                <h3><span class="status-indicator"></span>💰 Revenue Tracking</h3>
                <div class="metric">
                    Current Revenue: <span class="metric-value" id="currentRevenue">$0.00</span>
                </div>
                <div class="metric">
                    Daily Target: <span class="metric-value" id="dailyTarget">$1,000+</span>
                </div>
            </div>
            
            <div class="card">
                <h3><span class="status-indicator"></span>🧠 AI Learning</h3>
                <div class="metric">
                    Patterns Learned: <span class="metric-value" id="patternsLearned">0</span>
                </div>
                <div class="metric">
                    Optimizations: <span class="metric-value" id="optimizations">0</span>
                </div>
            </div>
            
            <div class="card">
                <h3><span class="status-indicator"></span>📈 System Status</h3>
                <div class="metric">
                    Status: <span class="metric-value" id="systemStatus">Initializing</span>
                </div>
                <div class="metric">
                    Uptime: <span class="metric-value" id="uptime">00:00:00</span>
                </div>
            </div>
            
            <div class="card">
                <h3><span class="status-indicator"></span>🎯 Performance</h3>
                <div class="metric">
                    Success Rate: <span class="metric-value" id="successRate">0%</span>
                </div>
                <div class="metric">
                    Growth Rate: <span class="metric-value" id="growthRate">0%</span>
                </div>
            </div>
        </div>
    </div>
    
    <script>
       
             // ===== SERVERLESS-AWARE LAUNCH SYSTEM ===== //
const API_BASE = window.location.origin + '/api';
let godmodeActive = false;

async function warmUpBackend() {
  const statusEl = document.getElementById('status');
  
  // Give user feedback about cold start
  statusEl.innerHTML = '<span class="status-indicator"></span> Warming up serverless backend...';
  
  // Wait a bit for initial cold start
  await new Promise(resolve => setTimeout(resolve, 2000));
  
  // Try to ping backend with retries
  for (let attempt = 1; attempt <= 3; attempt++) {
    try {
      statusEl.innerHTML = `<span class="status-indicator"></span> Attempt ${attempt}/3: Connecting to backend...`;
      
      const response = await fetch(`${API_BASE}/health`, { 
        method: 'GET',
        headers: { 'Cache-Control': 'no-cache' }
      });
      
      if (response.ok) {
        statusEl.innerHTML = '<span style="color:#00ff88">✓</span> Backend connected!';
        return true;
      }
      
    } catch (error) {
      console.log(`Attempt ${attempt} failed:`, error.message);
    }
    
    // Wait between retries (longer each time)
    if (attempt < 3) {
      await new Promise(resolve => setTimeout(resolve, attempt * 2000));
    }
  }
  
  throw new Error('Backend failed to respond after 3 attempts');
}

async function launchSystem() {
  if (godmodeActive) return;
  
  const btn = document.getElementById('godmode-launcher');
  const statusEl = document.getElementById('status');
  
  // Visual loading state
  btn.disabled = true;
  btn.innerHTML = '🚀 INITIALIZING...';

  try {
    // 1. WARM UP BACKEND FIRST (handles cold starts)
    await warmUpBackend();
    
    // 2. Small delay to ensure backend is fully ready
    await new Promise(resolve => setTimeout(resolve, 1000));
    
    // 3. Activate GODMODE
    statusEl.innerHTML = '<span class="status-indicator"></span> Activating GODMODE...';
    
    const launchResponse = await fetch(`${API_BASE}/launch`, {
      method: 'POST',
      headers: { 
        'Content-Type': 'application/json',
        'X-GODMODE-Version': 'ULTRA',
        'Cache-Control': 'no-cache'
      }
    });
    
    if (!launchResponse.ok) {
      throw new Error(`Launch failed: ${launchResponse.status} ${launchResponse.statusText}`);
    }

    // 4. Success!
    statusEl.innerHTML = '<span style="color:#00ff88">✓</span> GODMODE ONLINE';
    btn.innerHTML = '⚡ SYSTEM ACTIVE ⚡';
    godmodeActive = true;
    
  } catch (error) {
    statusEl.innerHTML = `<span style="color:#ff6b6b">✗</span> ${error.message}`;
    btn.innerHTML = '🚀 RETRY ACTIVATION 🚀';
    console.error('LAUNCH ERROR:', error);
  } finally {
    btn.disabled = false;
  }
}

// Initialize
document.getElementById('godmode-launcher').onclick = launchSystem;  
