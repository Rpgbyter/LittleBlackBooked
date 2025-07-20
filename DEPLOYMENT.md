# Deployment Guide

## Hosting the Web Server Version Online

### Requirements
- Python 3.6+
- Flask
- Web server (Nginx/Apache recommended)
- Domain name (optional)

### Steps
1. **Server Setup**
   ```bash
   # Install dependencies
   sudo apt update
   sudo apt install python3 python3-pip nginx
   
   # Install Python requirements
   pip3 install flask
   ```

2. **Deploy Application**
   ```bash
   # Clone repository
   git clone https://github.com/Rpgbyter/LittleBlackBooked.git
cd LittleBlackBooked
   
   # Run server (development)
   python3 LBBook/LittleBlackBooked_Server.py
   
   # Or for production use:
   gunicorn -w 4 -b 0.0.0.0:8000 LBBook:app
   ```

3. **Configure Nginx (Production)**
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com;
       
       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

4. **HTTPS Setup (Recommended)**
   ```bash
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx -d yourdomain.com
   ```

### Hosting Options
1. **Traditional VPS** (DigitalOcean, Linode, AWS EC2)
2. **Serverless** (AWS Lambda, Google Cloud Functions)
3. **PaaS** (Heroku, PythonAnywhere)

### Maintenance
- Set up automatic renewals for SSL certificates
- Configure logging and monitoring
- Regular backups of data file
