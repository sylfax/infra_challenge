from fastapi import APIRouter

from apis.onboarding import routes_onboarding
from apis.auth import routes_auth
from apis.transactions import routes_transactions
from apis.alerts import routes_alerts
from apis.customers import routes_customers

api_router = APIRouter()

# include router for ONBOARDING API
api_router.include_router(routes_onboarding.router, prefix="/api/onboarding", tags=["Onboarding"])

# include router for LOGIN API
api_router.include_router(routes_auth.router, prefix="/api/auth", tags=["Authentication"])

# include router for TRANSACTIONS API
api_router.include_router(routes_transactions.router, prefix="/api/transactions", tags=["Transactions"])

# include router for ALERTS API
api_router.include_router(routes_alerts.router, prefix="/api/alerts", tags=["Alerts"])

# include router for ALERTS API
api_router.include_router(routes_customers.router, prefix="/api/customers", tags=["Customers"])

