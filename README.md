# Sport Types Management System

A Python-based command-line system to manage a collection of sport types. This system allows you to add, delete, edit, and display sport types from a predefined list of valid sports.

## Features

- **Sport Management**:
  - Add new sports to the list.
  - Delete existing sports from the list.
  - Edit sport types by replacing one with another.
  - Display all current sports in the system.

- **Sport Type Validation**:
  - Ensure only valid sport types can be added, based on a predefined list of supported sports.

- **User-Friendly Interface**:
  - An interactive and easy-to-follow menu for managing sport types.

## Requirements

- **Python 3.x** or higher.  
- No external libraries required.  

## How to Run

1. Clone or download this repository to your local machine.
2. Open your terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script with the following command:

```bash
python main.py
```

## Usage

The system provides the following options for sport management:

- **Add**:  Add a new sport type.
- **Delete**: Remove an existing sport type.
- **Edit**: Replace a sport type with a new one.
- **Show**: Display all current sport types.
- **Exit**: Exit the program.

## Example Usage Scenario
```
**************************************************
Welcome to the Sport Types Management System!

Type in:
"1" To see the list of sports
"2" To add a new type of sport
"3" To delete a type of sport
"4" To replace a type of sport
"0" To exit
::: 2

Type in a sport type to add: Tennis

"Tennis" sport type successfully added!
------------------------------------------------
List of Sports:
-------------------------------------
ID         Name
-------------------------------------
1.         Tennis    
-------------------------------------
Total number of sports: 1.

------------------------------------------------
```

## Code Structure

### Sport Type Management

- The sport types are managed in the `sport_types` list, where sports are added, removed, or replaced as per the user's commands.
- A predefined list, `valid_sport_types`, ensures that only recognized sport types can be added. If a user tries to add an invalid sport type, the system will reject the input.

### Class Implementation

- The system is implemented using a `Sport` class, which contains various methods to manage the sport types:
  - **`add_sport_type()`**: Adds a new sport type to the list after validating it against the `valid_sport_types` list.
  - **`delete_sport_type()`**: Deletes an existing sport type from the list by checking if it exists.
  - **`replace_sport_type()`**: Replaces an existing sport type with a new one.
  - **`display_sport_type()`**: Displays the list of currently available sport types, along with their IDs.
  
Each of these methods interacts with the `sport_types` list and provides a simple command-line interface for the user to manage the list of sport types.

## Author

- Developed by **GhostKX**
- GitHub: **[GhostKX](https://github.com/GhostKX/Sport-Types)**

