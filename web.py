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