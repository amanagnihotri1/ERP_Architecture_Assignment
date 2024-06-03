#### Frappe Assignment Reports+Server Side
## Technologies Used

- Frappe
- Docker


## Prerequisites

Before running this project, ensure you have the following installed:

- #### Docker Desktop (Docker)
    Docker Desktop is a one-click-install application for your Mac, Linux, or Windows environment that lets you build, share, and run containerized applications and microservices.It provides a straightforward GUI (Graphical User Interface) that lets you manage your containers, applications, and images directly from your machine. Docker Desktop reduces the time spent on complex setups so you can focus on writing code. It takes care of port mappings, file system concerns, and other default settings, and is regularly updated with bug fixes and security updates.To Install Docker Desktop <a href="https://docs.docker.com/desktop/" alt="not found">Click Here</a>

- #### Frappe
    Frappe, pronounced fra-pay, is a full stack, batteries-included, web framework written in Python and Javascript with MariaDB as the database. It is the framework which powers ERPNext, is pretty generic and can be used to build database driven apps. To install latest version <a href="https://frappeframework.com/docs/user/en/introduction" alt="not found">Click Here</a>


## Installation
1. Install Docker desktop and open command prompt.
2. Inside command promt type this command
   ```bash
   docker pull ubuntu:22.04
   docker run -dt --name bench -p 8000:8000 ubuntu:22.04 /bin/bash
   ```
4. Next setup frappe framework, to setup <a href="https://wiki.nestorbird.com/wiki/install-frappe-v15">Click here</a>
5. Navigate to **Customization > DocType**
6. Create a new DocType named "Student".
7. Add the specified fields according to the provided instructions.
## Usage
1. open bench directory and inside that enable developer mode -
 ```bash
bench set-config -g developer_mode 1
  ```
2. start postgres service by running this command
   ```bash
   sudo service postgresql start
   ```
3. Start Bench with 2 commands
   ```bash
   bench use your_bench_name
   bench start
   ```
1. Navigate to the list view of the Customer Doctype.
2. Click on the "Export" button to trigger the export functionality.
3. Once the export is complete, the system will generate a CSV file containing the specified customer and address data.  

## Implementation Steps

To implement this functionality, follow these steps:

1. **Modify Customer Doctype:**
   - Add a button named "Export" to the list view of the Customer Doctype.

2. **Backend Logic:**
   - Implement backend logic to handle the button click event.
   - Fetch the required data from the database, including the specified fields from both Customer and Address doctypes.

3. **CSV File Generation:**
   - Generate a CSV file dynamically, populating it with the fetched data.

4. **Error Handling:**
   - Handle any error cases or exceptions that may occur during the export process to ensure a smooth user experience.

