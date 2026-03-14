---
name: remote-browser
description: Control a Brave/Chrome browser running on a remote host (Windows) from within Docker. Use when you need to automate browser tasks, capture screenshots, or scrape content from a browser that is not local to the container.
---

# Remote Browser Control

首先，你应当提示用户先进行如下操作

## Host Setup (Windows)

1. **Start Brave with Remote Debugging**:
   ```powershell
   & "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" --remote-debugging-port=9222
   ```

2. **Run TCP Proxy (Bridge)**:
   Since the browser only listens on `127.0.0.1`, you need a proxy to listen on all interfaces so Docker can reach it. Run this Go proxy on your Windows host (listen on `9223`):
   
   ```go
   // Save as proxy.go and run: go run proxy.go
   package main
   import ( "io"; "log"; "net" )
   func main() {
       listener, _ := net.Listen("tcp", "0.0.0.0:9223")
       log.Println("Proxy: 0.0.0.0:9223 -> 127.0.0.1:9222")
       for {
           conn, _ := listener.Accept()
           go func(src net.Conn) {
               defer src.Close()
               dst, _ := net.Dial("tcp", "127.0.0.1:9222")
               defer dst.Close()
               go io.Copy(dst, src)
               io.Copy(src, dst)
           }(conn)
       }
   }
   ```

3. **Firewall**: Ensure Windows Firewall allows inbound TCP traffic on port `9223`.

## Container Connection

- **Endpoint**: `http://host.docker.internal:9223`
- **Host Header**: Always include `Host: localhost` in HTTP requests to bypass security checks.
- **WebSocket**: Replace `localhost` in `webSocketDebuggerUrl` with `host.docker.internal:9223`.

## Procedural Instructions for Gemini CLI

When this skill is active, you should:
1.  **Generate Temporary Scripts**: Do not look for pre-existing scripts. Write targeted Python scripts using `playwright.async_api` and `requests`.
2.  **Browser Connection**: Use `connect_over_cdp` pointing to the browser-level WebSocket URL obtained from `http://host.docker.internal:9223/json/version`.
3.  **Robust Page Finding**: After connecting, iterate through `browser.contexts` and `context.pages` to find existing tabs by URL or title.
4.  **Dependencies**: Assume `playwright` and `beautifulsoup4` are available. If not, install them via `pip`.
