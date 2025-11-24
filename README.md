# Campus Item Recovery System (VIT Lost & Found)

A console-based Python application designed to facilitate the reporting and recovery of lost items within a university campus environment. This system fills the gap between finders and owners through a secure verification process based on unique item distinctions.

## 📂 Project Overview

The application functions as a digital ledger that persists data locally. It allows users to register accounts, report items they have found, and attempt to claim items they have lost. The core feature of this system is its **ownership verification algorithm**, which compares a hidden "distinction" (recorded by the finder) against a description provided by the claimant to prevent fraudulent claims.

## ✨ Key Features

  * **User Authentication:** Secure registration and login functionality that validates credentials against a stored user database.
  * **Persistent Storage:** Automatically initializes and maintains JSON databases (`users.json` and `items.json`) to store records between sessions.
  * **Item Reporting:** Users can log found items with details including name, category, location, and a critical "distinction" field used for future verification.
  * **Smart Claim Verification:** The system utilizes `difflib.SequenceMatcher` to perform fuzzy string matching. It calculates a similarity ratio between the claimant's proof and the finder's recorded distinction. Verification succeeds if the similarity ratio exceeds **0.3** or if a substring match is found.
  * **Dynamic Status Updates:** Items are tracked with statuses ("Open" or "Claimed"). Once successfully claimed, the system reveals the finder's contact information (registration number) to the owner.

## 🛠️ Technical Structure

The project is modularized into five distinct scripts:

1.  **`main.py`**: The entry point of the application. It handles the initialization of database files if they do not exist and manages the primary navigation loop between the Guest Menu and the User Dashboard.
2.  **`authentication.py`**: Manages the global current user session (`cuser`). It handles logic for creating new user dictionaries and verifying login inputs against the loaded user list.
3.  **`item_management.py`**: Contains the core business logic. It handles the `reportitem` inputs and the `claimitem` algorithm, including the specific similarity checks required to validate a claim.
4.  **`file_management.py`**: Acts as the Data Access Layer (DAL). It contains helper functions (`loadfile`, `savefile`) to safely read and write JSON data, handling potential `JSONDecodeError` exceptions.
5.  **`data.py`**: Defines the data schemas. It uses helper functions `new_user` and `new_item` to return structured dictionaries, ensuring consistency across the database. It also automatically timestamps new items using `datetime`.

## 🚀 Installation & Usage

### Prerequisites

  * Python 3.x
  * Standard libraries used: `os`, `json`, `difflib`, `datetime`.

### Running the Application

1.  Ensure all project files are in the same directory.
2.  Execute the main script:
    ```bash
    python main.py
    ```
3.  **First Run:** The system will automatically generate empty `users.json` and `items.json` files.

### Workflow

1.  **Register:** Create a new account with your Registration Number, Name, and Password.
2.  **Report an Item:** If you find an item, log in and select "Report Item." You must provide a "distinction"—a specific detail (e.g., "scratch on the screen").
3.  **Claim an Item:**
      * View the list of "Open" items.
      * Select the Item ID you wish to claim.
      * When prompted for "distinctions," describe the item.
      * If your description matches the finder's hidden note (via the similarity algorithm), ownership is verified.

## 🛡️ Verification Logic Explanation

To prevent theft, the system does not simply give the item to anyone who asks. When a user attempts to claim an item:

1.  The system retrieves the hidden `distinction` string recorded by the finder.
2.  The claimant inputs their own description (`proof`).
3.  The `SequenceMatcher` calculates how similar these two strings are.
4.  Access is granted only if the description is highly similar (Ratio \> 0.3) or matches exactly.

## Screenshots
!i[image](https://github.com/divybisht3021-botzai/VIT-L-F/blob/main/Screenshots/login.png?raw=true)

![image](https://github.com/divybisht3021-botzai/VIT-L-F/blob/main/Screenshots/register.png?raw=true)

![image](https://github.com/divybisht3021-botzai/VIT-L-F/blob/main/Screenshots/dashboard.png?raw=true)

![image](https://github.com/divybisht3021-botzai/VIT-L-F/blob/main/Screenshots/report%20item.png?raw=true)

![image](https://github.com/divybisht3021-botzai/VIT-L-F/blob/main/Screenshots/claim%20fail.png?raw=true)

![image](https://github.com/divybisht3021-botzai/VIT-L-F/blob/main/Screenshots/claim%20success.png?raw=true)
