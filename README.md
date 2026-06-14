
# 3-Tier Task Manager Application

This repository contains a highly available, fault-tolerant 3-tier web application deployed on AWS (`ap-south-1`).

## System Architecture

```mermaid
graph TD
    %% High-Contrast Styling Rules %%
    classDef public fill:#b3e5fc,stroke:#03a9f4,stroke-width:2px,color:#000000,font-weight:bold;
    classDef privateApp fill:#ffe0b2,stroke:#ff9800,stroke-width:2px,color:#000000,font-weight:bold;
    classDef privateDB fill:#ffcdd2,stroke:#f44336,stroke-width:2px,color:#000000,font-weight:bold;
    classDef lb fill:#c8e6c9,stroke:#4caf50,stroke-width:2px,color:#000000,font-weight:bold;

    subgraph VPC ["AWS VPC (10.0.0.0/16)"]
        ExtLB["Internet-Facing Load Balancer"]:::lb
        
        subgraph AZ1 ["AZ: ap-south-1a"]
            Web1["Web Tier<br/>(Flask - Port 5000)"]:::public
            App1["App Tier<br/>(Node.js - Port 3000)"]:::privateApp
            DB1[("Database<br/>(Tasks Table)")]:::privateDB
        end

        subgraph AZ2 ["AZ: ap-south-1b"]
            Web2["Web Tier<br/>(Flask)"]:::public
            App2["App Tier<br/>(Node.js)"]:::privateApp
            DB2[("Database")]:::privateDB
        end

        subgraph AZ3 ["AZ: ap-south-1c"]
            Web3["Web Tier<br/>(Flask)"]:::public
            App3["App Tier<br/>(Node.js)"]:::privateApp
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
```
Infrastructure Configuration Details
Frontend Tier: Deployed on Ubuntu EC2 instances running a Flask web server on Port 5000.
Backend Tier: Deployed on isolated private subnets on Ubuntu EC2 instances running a Node.js Express server on Port 3000.
Database Connection: Connects locally to your database instance to safely manage and expose the Tasks table to the frontend via API endpoints
