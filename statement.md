# Project Statement: VIT Campus Lost & Found System

## 🚩 Problem Statement
In a busy university environment, personal belongings are frequently misplaced, leading to distress and financial loss for students. Traditional manual "Lost and Found" boxes are often disorganized, insecure, and lack a reliable method to verify if a claimant is the actual owner. Furthermore, there is a communication gap between the person who finds an item and the person who lost it, as finding contact details for specific students can be difficult. This project addresses the need for a centralized, digital repository that not only lists found items but also implements a security layer to prevent fraudulent claims through specific ownership verification logic.

## 🔭 Scope of the Project
The scope of this application is defined as a console-based utility designed for the VIT Bhopal campus community. It encompasses the entire lifecycle of item recovery:
* **Data Persistence:** The system maintains a local database of users and items using JSON file handling to ensure records survive between sessions.
* **Digital Reporting:** It replaces physical logbooks with a digital entry system that captures critical metadata, including item category, location, and hidden distinct features.
* **Verification Protocol:** The scope is limited to logical verification. It does not handle the physical transfer of items but rather facilitates the connection by validating ownership claims.
## 👥 Target Users
The primary target audience includes the academic community within the university:
1.  **Students (The Losers):** Individuals who have misplaced items and need a centralized platform to search for and claim them securely.
2.  **Students (The Finders):** Individuals who locate lost property and wish to report it responsibly without the burden of manually searching for the owner.
3.  **Administrators/System:** The logic supports a "finder" entity (identified by Registration Number) to ensure accountability.

## 🚀 High-Level Features

### 1. Secure Authentication System
Users must register and log in using their University Registration Number. This ensures that every report and claim is tied to a verified identity, preventing anonymous or malicious spamming of the system.

### 2. "Hidden Distinction" Reporting
When a user reports a found item, they are required to input a "distinction"—a specific mark or feature (e.g., a scratch, a sticker, or a specific wallpaper). This data is stored privately and is not shown in the public list of lost items, acting as a security key for future claims.

### 3. Smart Claim Verification Engine
The system employs the `difflib.SequenceMatcher` to compare the claimant's description against the finder's recorded distinction. Instead of requiring an exact character-for-character match, the system uses a similarity ratio (threshold > 0.3) or substring matching. 

### 4. Automated Contact Facilitation
Upon successful verification of ownership, the system automatically generates and displays the finder's contact email in the specific format `Name.RegNo@vitbhopal.ac.in`. This ensures that contact details are only revealed to verified owners, protecting the privacy of the finder.

### 5. Real-Time Status Tracking
The system filters and displays items based on their status. Users browse a list of "Open" items. Once an item is successfully verified and claimed, its status is updated to "Claimed" in the database, and it is not displayed in the item list.
