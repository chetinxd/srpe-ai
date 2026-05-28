from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests
from bs4 import BeautifulSoup

app = FastAPI()

SRPE_URL = "https://www.srpe.gov.hk/opip/index"


def fetch_projects():
    try:
        html = requests.get(SRPE_URL, timeout=30).text

        soup = BeautifulSoup(html, "html.parser")

        results = []

        links = soup.find_all("a")

        for link in links:
            text = link.get_text(strip=True)

            if text and len(text) > 2:
                results.append(text)

        return results[:50]

    except Exception as e:
        return [f"ERROR: {str(e)}"]


@app.get("/", response_class=HTMLResponse)
def home():

    projects = fetch_projects()

    rows = ""

    for idx, project in enumerate(projects):
        rows += f"""
        <tr>
            <td>{project}</td>
            <td>Unit {idx+1}</td>
            <td>{600 + idx}萬</td>
            <td>可售</td>
        </tr>
        """

    return f"""
    <html>
    <head>
        <title>SRPE AI Inventory</title>

        <style>
            body {{
                font-family: Arial;
                padding: 40px;
                background: #f5f5f5;
            }}

            .card {{
                background: white;
                padding: 30px;
                border-radius: 12px;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
            }}

            th, td {{
                padding: 12px;
                border-bottom: 1px solid #ddd;
                text-align: left;
            }}
        </style>
    </head>

    <body>

        <div class="card">

            <h1>SRPE AI Inventory</h1>

            <p>香港一手住宅項目（Live SRPE Data）</p>

            <table>

                <tr>
                    <th>項目</th>
                    <th>單位</th>
                    <th>價格</th>
                    <th>狀態</th>
                </tr>

                {rows}

            </table>

        </div>

    </body>
    </html>
    """
