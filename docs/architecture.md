# System Architecture

```text
User
  |
  v
Presentation/UI
  |
  v
Service Layer
  |-- PortfolioService
  |-- TransactionService
  `-- PnLService
  |
  v
Model Layer
  |-- Portfolio
  `-- Transaction
  |
  v
Data Layer
  `-- stocks.py
```

The architecture separates user interaction, business logic, domain models, and reference data.
