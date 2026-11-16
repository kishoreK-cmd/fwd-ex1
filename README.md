# EX01 Developing a Simple Webserver
## Date:

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TCP/IP Model — Rain Effect</title>

  <style>
    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      min-height: 100vh;
      overflow-x: hidden;
      padding: 30px 15px;
      color: white;
      background: #07111f;
      font-family: Arial, sans-serif;
      text-align: center;
    }

    /* Animated rain in the background */
    .rain {
      position: fixed;
      inset: 0;
      z-index: -1;
      overflow: hidden;
      pointer-events: none;
    }

    .drop {
      position: absolute;
      top: -60px;
      width: 2px;
      height: 45px;
      background: linear-gradient(transparent, #64d8ff);
      opacity: 0.6;
      animation: fall linear infinite;
    }

    @keyframes fall {
      to {
        transform: translateY(110vh);
      }
    }

    h1 {
      margin-bottom: 30px;
      color: #8be9ff;
      text-shadow: 0 0 15px #00aaff;
    }

    .layer {
      max-width: 520px;
      margin: 16px auto;
      padding: 14px;
      border: 1px solid rgba(139, 233, 255, 0.4);
      border-radius: 12px;
      background: rgba(10, 35, 55, 0.85);
      box-shadow: 0 0 16px rgba(0, 170, 255, 0.2);
    }

    .application { border-left: 6px solid #ff5c8a; }
    .transport   { border-left: 6px solid #ffb84d; }
    .internet     { border-left: 6px solid #a78bfa; }
    .network      { border-left: 6px solid #4de1c1; }

    @media (prefers-reduced-motion: reduce) {
      .drop {
        animation: none;
      }
    }
  </style>
</head>

<body>
  <div class="rain" id="rain" aria-hidden="true"></div>

  <h1>TCP/IP Model</h1>

  <section class="layer application">
    <h2>Application Layer</h2>
    <p>Provides network services to applications. Examples: HTTP, DNS, and SMTP.</p>
  </section>

  <section class="layer transport">
    <h2>Transport Layer</h2>
    <p>Transfers data between devices. Examples: TCP and UDP.</p>
  </section>

  <section class="layer internet">
    <h2>Internet Layer</h2>
    <p>Routes data between networks. Example: IP.</p>
  </section>

  <section class="layer network">
    <h2>Network Access Layer</h2>
    <p>Sends data over a local network. Examples: Ethernet and Wi-Fi.</p>
  </section>

  <script>
    const rain = document.getElementById("rain");

    for (let i = 0; i < 90; i++) {
      const drop = document.createElement("span");
      drop.className = "drop";
      drop.style.left = Math.random() * 100 + "vw";
      drop.style.animationDuration = (0.6 + Math.random() * 1.2) + "s";
      drop.style.animationDelay = Math.random() * 2 + "s";
      rain.appendChild(drop);
    }
  </script>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()


## OUTPUT:
<img width="1920" height="1080" alt="Screenshot 2026-11-14 161724" src="https://github.com/user-attachments/assets/792d92e3-6e68-4360-beec-db5973a84565" />

<img width="1920" height="1080" alt="Screenshot 2026-11-15 093527" src="https://github.com/user-attachments/assets/86b96bd0-dd9d-4cfd-b4fe-9acc589d42ae" />



## RESULT:
The program for implementing simple webserver is executed successfully.

