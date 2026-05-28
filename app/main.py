from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return '''
    <html>
    <head>
        <title>SRPE AI Inventory</title>
        <style>
            body {
                font-family: Arial;
                margin: 40px;
                background: #f5f5f5;
            }
            .card {
                background: white;
                padding: 20px;
                border-radius: 12px;
                max-width: 700px;
                margin: auto;
            }
            table {
                width: 100%;
                border-collapse: collapse;
            }
            td, th {
                border-bottom: 1px solid #ddd;
                padding: 10px;
                text-align: left;
            }
            h1 {
                color: #333;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>SRPE AI Inventory</h1>
            <p>香港一手樓可售單位</p>

            <table>
                <tr>
                    <th>項目</th>
                    <th>單位</th>
                    <th>價格</th>
                    <th>狀態</th>
                </tr>

                <tr>
                    <td>Demo Residence</td>
                    <td>18A</td>
                    <td>688萬</td>
                    <td>可售</td>
                </tr>

                <tr>
                    <td>Demo Residence</td>
                    <td>23B</td>
                    <td>712萬</td>
                    <td>可售</td>
                </tr>
            </table>

        </div>
    </body>
    </html>
    '''
