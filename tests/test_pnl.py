import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from models.portfolio import Portfolio
from services.pnl_service import PnLService


def test_unrealized_pnl():
    portfolio = Portfolio()
    portfolio.add_stock("TCS", 10, 1000)

    summary = PnLService().portfolio_summary(
        portfolio, {"TCS": 1150}
    )

    assert summary["total_invested"] == 10000
    assert summary["total_current_value"] == 11500
    assert summary["total_unrealized_pnl"] == 1500
