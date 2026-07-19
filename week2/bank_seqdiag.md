```mermaid
sequenceDiagram
    actor Customer
    participant Bank
    participant Account as BankAccount
    participant Transaction
    participant Interest as InterestCalculator

    Customer->>Bank: Open New Account
    Bank->>Account: Create Account(customer)
    Account-->>Bank: Account Created
    Bank-->>Customer: Account Details
    
    Customer->>Account: Deposit(amount)
    Account->>Transaction: Save Deposit
    Transaction-->>Account: Transaction Saved
    Account->>Account: Increase Balance
    Account-->>Customer: Deposit Completed
    
    Customer->>Account: Withdraw(amount)

    alt Balance Available
        Account->>Transaction: Save Withdrawal
        Transaction-->>Account: Transaction Saved
        Account->>Account: Decrease Balance
        Account-->>Customer: Withdrawal Completed
    else Insufficient Balance
        Account-->>Customer: Withdrawal Failed
    end
   
    Customer->>Account: Transfer(amount, Target Account)

    alt Valid Balance
        Account->>Transaction: Record Transfer
        Transaction-->>Account: Transfer Recorded
        Account->>Account: Update Source Balance
        Account->>Account: Update Target Balance
        Account-->>Customer: Transfer Successful
    else Insufficient Balance
        Account-->>Customer: Transfer Failed
    end

    Customer->>Account: Check Balance
    Account-->>Customer: Current Balance
    
    Customer->>Interest: Calculate Interest
    Interest->>Account: Get Balance
    Account-->>Interest: Balance
    Interest-->>Customer: Interest Amount
