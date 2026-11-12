# SOC Detection Engineering Lab

A hands-on Security Operations Center (SOC) Detection Engineering project built using Wazuh SIEM, Shuffle SOAR, and Telegram.

This project demonstrates how security events can be monitored, detected, investigated, and responded to through automated security workflows.

## Project Overview

The lab simulates a Windows brute-force login attack and demonstrates how a SOC environment can identify repeated authentication failures, generate security alerts, notify analysts, and automatically disable a targeted test account.

The objective was to build and test an end-to-end detection and response workflow in a controlled virtual environment.

## Technologies Used

| Technology | Purpose |
|---|---|
| Wazuh SIEM | Security monitoring and event detection |
| Ubuntu Server | SIEM server environment |
| Windows 11 | Endpoint monitoring |
| Shuffle SOAR | Security workflow automation |
| Telegram Bot | Real-time security notifications |
| Python | Custom active response script |
| PowerShell | Windows account management |
| VirtualBox | Virtual lab environment |

## Lab Architecture

The project follows this workflow:

1. Windows endpoint generates authentication events.
2. Wazuh Agent forwards security events to the Wazuh Manager.
3. Custom detection rules identify repeated failed login attempts.
4. Wazuh forwards matching alerts to Shuffle SOAR.
5. Shuffle sends notifications through Telegram.
6. Wazuh Active Response executes a custom Python-based response on the Windows endpoint.

## Detection Engineering

Custom Wazuh rules were developed to detect repeated Windows authentication failures.

| Rule ID | Description | Severity |
|---|---|---|
| 100100 | Multiple Windows logon failures within 60 seconds | 10 |
| 100102 | Failed login attempt against SOC Test account | 5 |
| 100101 | Three failed login attempts against SOC Test within 60 seconds | 10 |

The detection logic uses event correlation and frequency thresholds to identify suspicious authentication activity.

## SOAR Integration

Shuffle SOAR was integrated with Wazuh to automate alert notification.

When the configured brute-force detection rule triggers:

- Wazuh sends the alert to Shuffle.
- Shuffle processes the incoming webhook.
- A Telegram notification is generated.

This demonstrates the integration of SIEM detection with SOAR-based notification workflows.

## Automated Incident Response

A custom Python-based active response script was developed and compiled into a Windows executable using PyInstaller.

When Rule ID `100101` triggers, the script:

- Validates the incoming Wazuh alert.
- Checks the detection rule and targeted agent.
- Confirms the affected account is `SOC Test`.
- Uses PowerShell to disable the test account.
- Records the response result in the Wazuh agent active response log.

The response was successfully tested in the lab.

**Safety note:** Automated account disabling was implemented only against a dedicated local test account in a controlled environment. This is a demonstration, not a production-ready response policy.

## Testing and Validation

The following scenarios were tested:

- Windows authentication failure monitoring.
- Detection of repeated failed login attempts.
- Validation of custom Wazuh detection rules.
- Alert forwarding from Wazuh to Shuffle.
- Telegram notification delivery.
- Automated disabling of the designated test account.

The end-to-end detection and response workflow was successfully demonstrated.

## Skills Demonstrated

- SIEM deployment and configuration
- Security event monitoring
- Windows event analysis
- Custom detection rule development
- Brute-force attack detection
- SIEM and SOAR integration
- Security alert automation
- Python scripting
- Windows endpoint response
- Security incident response

## Project Documentation

The repository includes project reports, implementation screenshots, and lab evidence.

Refer to the documentation and screenshots in this repository for implementation details and testing results.

## Disclaimer

This project was developed strictly for educational and cybersecurity lab purposes in a controlled environment. All attack simulations and response actions were performed against designated test systems and accounts.

---

**Project:** SOC Detection Engineering Lab  
**Course:** CICSA  
**Developed by:** Mohamed Adnan A T 
**Submitted to:** Alex Davy  
**Date:** November 2026
