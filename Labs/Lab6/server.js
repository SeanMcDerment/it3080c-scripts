const express = require('express');
const os = require('os');

const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.sendFile('./index.html');
});

app.get('/sysinfo', (req, res) => {
  const HostName = os.hostname();
  const networkInterfaces = os.networkInterfaces();
  const ipAddress = networkInterfaces.Ethernet ? networkInterfaces.Ethernet[0].address : 'N/A';

    const utSecs = os.uptime();
    const utMinutes = Math.floor((utSecs % 3600) / 60);
    const utHours = Math.floor((utSecs % (3600 * 24)) / 3600);
    const utDays = Math.floor(utSecs / (3600 * 24));


  const utSecs = Math.floor(utSecs % 60);

  const tMemoryMB = (os.totalmem() / (1024 * 1024)).toFixed(2);
  const freeMemMB = (os.freemem() / (1024 * 1024)).toFixed(2);

  const numCPUs = os.cpus().length;

  const html = `
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${HostName}</p>
        <p>IP: ${ipAddress}</p>
        <p>Server Uptime: ${utDays}d ${utHours}h ${utMinutes}m ${utSecs}s</p>
        <p>Total Memory: ${tMemoryMB} MB</p>
        <p>Free Memory: ${freeMemMB} MB</p>
        <p>Number of CPUs: ${numCPUs}</p>
      </body>
    </html>`;

  res.send(html);
});

app.listen(port, () => {
  console.log(`Server listening on http://localhost:${port}`);
});
