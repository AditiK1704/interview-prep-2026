
```mermaid

%%SmartLibrary - Use Case Diagram

graph LR 
    Student((Student))
    Librarian((Librarian))

    subgraph Library system
        UC1[Borrow book]
        UC2[Return book]
        UC3[Check Membership]
        UC4[Search book]
        UC5[Verify availability]
        UC6[Issue book]
        UC7[Update books inventory]
        UC8[Calculate fine]
        UC9[Add new book]
        UC10[Remove damaged book]
        UC11[Check history]
        UC12[Pay fine]
    end

    Student --> UC1
    Student --> UC2
    Student --> |<<extend>>|UC11
    Student --> UC12

    Librarian --> |include|UC3
    Librarian --> UC4
    Librarian --> UC6
    Librarian --> UC5
    Librarian -.-> |include|UC7
    Librarian --> UC8
    Librarian --> UC9
    Librarian --> UC10

    UC8 --> |include|UC12 
    UC1 --> |include|UC7
    UC2 -.-> |include|UC7
    








