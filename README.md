# MarketRadar-AI

**An AI-powered, TCP-based stock analysis and alerting platform for Indian equity markets (NSE/BSE).**  
This project demonstrates a **real-time stock analysis engine** with fundamental & technical insights, watchlist management, and event-driven alerts — all built with Python, async architecture, and free public APIs.

## Features

### Stock Analysis
- Fundamental insights (revenue, debt, ROE, etc.)
- Technical indicators (SMA, RSI, trends, support/resistance)
- AI-driven explanations in simple language

### Watchlist & Alerts
- Add stocks to monitor with target price
- Background tasks check live prices
- Alerts triggered when target price is reached
- Persistent watchlist storage (SQLite)

### Interfaces
- TCP client for chat-like interaction
- Future-proof design for Web UI

### Tech Stack
- Python 3.11+
- `asyncio` for async TCP server
- `aiohttp` for API requests
- `APScheduler` for background alerts
- `SQLite` for watchlist storage
- Docker-ready for deployment

---

## Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/market-radar-ai.git
cd market-radar-ai
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run the Server:
```
python app/server.py
```

4. Run the TCP client (in another terminal):
```
python client/tcp_client.py
```

---

## Step 1: Installation & Setup

To run the **MarketRadar-AI** bot locally, you'll need to set up the following:

1. Clone the repository:
```bash
git clone https://github.com/your-username/market-radar-ai.git
cd market-radar-ai
```

2. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables (you can add them in a `.env` file):
- API Keys (for fetching stock data)
- Scheduler settings (for alert timings)
- Cloud deployment keys (for Azure if deploying later)

Run the bot:
```bash
python app/server.py
```
Your bot will now be ready to listen for incoming commands.

## Step 2: How It Works

The StockAgent now listens for these commands:

**1. Analyze stock:**
- Command: "Analyze VEDL"
- Response: Fundamental and technical analysis of Vedanta (VEDL).

**2. Monitor stock at a price:**
- Command: "Monitor TCS at 3200"
- Response: Adds TCS (Tata Consultancy Services) to the watchlist, with a price target of ₹3200.

**3. Show your watchlist:**
- Command: "Show my watchlist"
- Response: Displays all the stocks in your watchlist and their corresponding target prices.

## Step 3: Test the Bot

1. Open a terminal window.
2. Run your bot using the following command:
You should see the bot starting up and listening for commands.
```bash
python app/server.py
```

3. Now, test your bot by entering different commands. You can enter the following commands:
- "Analyze TCS"
- "Monitor VEDL at 1000"
- "Show my watchlist"
- "Help"

## Deploying the Bot on Azure (with Terraform)

To deploy this bot on Azure follow below steps.

**Step 1: Set Up Azure Account**
- Create an Azure account if you don’t have one: [Azure](https://azure.microsoft.com/en-us/free/)
- Set up a Resource Group, App Service, and Database (for storing alerts and stock data).

**Step 2: Create a Terraform Configuration**

`terraform/main.tf` – This file contains the cloud infrastructure configuration for Azure.
```hcl
provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "market-radar-ai-rg"
  location = "East US"
}

resource "azurerm_app_service_plan" "example" {
  name                = "market-radar-ai-plan"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  sku {
    tier = "Free"
    size = "F1"
  }
}

resource "azurerm_web_app" "example" {
  name                = "market-radar-ai-webapp"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  app_service_plan_id = azurerm_app_service_plan.example.id

  app_settings = {
    "KEY" = "VALUE"  # Replace with your environment variables, e.g., API keys
  }
}

output "web_app_url" {
  value = azurerm_web_app.example.default_site_hostname
}
```

This will:
- Create a resource group
- Deploy an App Service plan (for hosting the bot)
- Create a web app where your bot will run

**Step 3: Deploy the Infrastructure**
1. Install Terraform if you don’t have it yet.
2. Run these commands to deploy the bot:
```bash
terraform init
terraform plan
terraform apply
```

**Step 4: Deploy the Bot to Azure**

1. Build the Docker container for your bot:
```bash
docker build -t market-radar-ai .
```

2. Push the container to Azure Container Registry:
- Create an Azure Container Registry (ACR) via the Azure portal.
- Push your Docker image:

```bash
docker tag market-radar-ai <your-acr-name>.azurecr.io/market-radar-ai:v1
docker push <your-acr-name>.azurecr.io/market-radar-ai:v1
```

3. Deploy the container to Azure App Service:
- Use Azure CLI or the portal to link your ACR with the App Service.
- Deploy the container to run your bot.

Once the deployment is complete, you can access your bot through the provided Azure URL.

### Disclaimer

This project is for educational purposes only. It does not provide financial advice. Stock prices are retrieved from free public APIs and may be delayed.

### Contribution

Contributions welcome! Fork, create issues, and send pull requests.
Designed to be modular and scalable.