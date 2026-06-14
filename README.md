# 3-Tier Task Manager Application

This repository contains the Frontend Tier of a highly available, fault-tolerant 3-tier web application deployed on AWS (`ap-south-1`).

## System Architecture

```mermaid
graph TD
    classDef public fill:#e1f5fe,stroke:#03a9f4,stroke-width:2px;
    classDef privateApp fill:#fff3e0,stroke:#ff9800,stroke-width:2px;
    classDef privateDB fill:#ffebee,stroke:#f44336,stroke-width:2px;
    classDef lb fill:#e8f5e9,stroke:#4caf50,stroke-width:2px;

    subgraph VPC ["AWS VPC (10.0.0.0/16)"]
        ExtLB["Internet-Facing Load Balancer"]:::lb
        
        subgraph AZ1 ["AZ: ap-south-1a"]
            Web1["EC2: Web Tier<br/>(Flask - Port 5000)"]:::public
            App1["EC2: App Tier<br/>(Node.js - Port 3000)"]:::privateApp
            DB1[("Database<br/>(Tasks Table)")]:::privateDB
        end

        subgraph AZ2 ["AZ: ap-south-1b"]
            Web2["EC2: Web Tier<br/>(Flask)"]:::public
            App2["EC2: App Tier<br/>(Node.js)"]:::privateApp
            DB2[("Database")]:::privateDB
        end

        subgraph AZ3 ["AZ: ap-south-1c"]
            Web3["EC2: Web Tier<br/>(Flask)"]:::public
            App3["EC2: App Tier<br/>(Node.js)"]:::privateApp
            DB3[("Database")]:::privateDB
        end

        IntLB["Internal Load Balancer"]:::lb
    end

    User((User / Internet)) --> ExtLB
    ExtLB --> Web1 & Web2 & Web3
    Web1 & Web2 & Web3 --> IntLB
    IntLB --> App1 & App2 & App3
    App1 --> DB1
    App2 --> DB2
    App3 --> DB3
