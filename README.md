## Security Toolkit
#### Overview

The Security Toolkit is a simple and user-friendly web application designed to run a variety of network and security scans. It provides a form-based interface where users can input a target (URL or IP address) and select one or more scanning actions. The results are displayed in real-time, making it easy to monitor the progress of scans and analyze the output.
Features

Multiple Scan Actions: Run various network and security scans such as:
    nmap: Perform common or full port scans.
    nslookup: Perform DNS lookups.
    whois: Query WHOIS data.
    sslscan: Check SSL/TLS configurations.
    traceroute: Trace the network path to the target.
    And more!

#### Installation

Clone the repository:

    git clone https://github.com/yourusername/security-toolkit.git
    cd security-toolkit

Install dependencies:

  Set up a virtual environment:
    
    python3 -m venv venv
    source venv/bin/activate

  Install required Python packages:

    pip install -r requirements.txt

  Set up Django project:

    Apply migrations:

    python manage.py migrate

  Run the development server:

    python manage.py runserver

  The application will be available at http://127.0.0.1:8000.

#### Usage:

Run Scans: Select a target (URL or IP) and one or more scan actions from the form.
View Results: After submission, scan results will appear on the right side of the page. Each scan can be expanded for more details and closed when done.
Interactive Cards: Click the close button on the top-right of each scan result card to remove it.

#### Contributing:

We welcome contributions to enhance the Security Toolkit! If you have suggestions for new features or improvements, please feel free to submit a pull request or open an issue.
