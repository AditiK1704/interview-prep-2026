```mermaid 
classDiagram

class Customer{
    +int customerId
    +String customerName
    +String address
    +String phoneNumber
    +openAccount()
    +deposit(amount)
    +withdraw(amount)
    +transfer(amount, targetAccount)
    +checkBalance()
}

class Bank{
    +String bankName
    +String branchName
    +String ifscCode
    +createAccount(customer)
    +closeAccount(accountNumber)
    +findAccount(accountNumber)
    +displayAccounts()
}

class BankAccount{
    #int accountNumber
    #double balance
    #String accountType
    +deposit(amount)
    +withdraw(amount)
    +transfer(amount, targetAccount)
    +getBalance()
    +updateBalance()
}

class SavingsAccount{
    +double interestRate
    +calculateInterest()
}

class CurrentAccount{
    +double overdraftLimit
    +checkOverdraft()
}

class Transaction{
    +int transactionId
    +Date transactionDate
    +String transactionType
    +double amount
    +saveDeposit()
    +saveWithdrawal()
    +recordTransfer()
    +viewTransaction()
}

class InterestCalculator{
    +double interestRate
    +calculateInterest(balance)
}

Customer "1" --> "1..*" BankAccount : owns
BankAccount "1..*" --> "1" Bank : managed by
BankAccount *-- Transaction : stores
SavingsAccount --|> BankAccount
CurrentAccount --|> BankAccount
InterestCalculator ..> SavingsAccount : calculates