# Parking Management System PMS
A multi‑stage digital engineering pilot project designed to track vehicle bay occupancy, made during my time at Rolls Royce Motor Cars. The system integrates microcontroller hardware, cloud services, and BMW‑approved automation tools to provide a reliable, scalable parking‑status interface.

# Overview
The Parking Management System (PMS) was developed to give the analysis department a live view of which workshop bays were occupied by test vehicles. The system evolved through several iterations due to corporate IT constraints, networking limitations, and hardware restrictions.

The final architecture combines Raspberry Pi microcontrollers, ultrasonic sensors, a master Raspberry Pi 4, and a BMW‑approved Power Automate workflow to update a SharePoint list consumed by a Power App front‑end.

# Features
- Real‑time bay occupancy detection using ultrasonic sensors.
- Microcontroller‑driven updates via Raspberry Pi Pico W devices.
- Secure data transmission through a master Raspberry Pi 4 with virus‑protected LAN access.
- BMW‑approved backend integration using Power Automate instead of Azure Functions.
- SharePoint‑based data storage feeding directly into a Power App UI.
- JSON‑based payloads for structured bay‑status updates.
- Scalable multi‑bay architecture designed for workshop environments.

# System Architecture
Stage 1 — Prototype (Personal Tenant)
- Azure Function App written in C#.
- MCU → Azure Function → SharePoint List → Power App.
- Successful prototype, but not compatible with BMW’s corporate Azure environment.

# Stage 2 — Corporate Integration
- Azure Function replaced with Power Automate due to BMW platform restrictions.
- HTML test scripts used to validate SharePoint API calls.
- JSON schema defined for incoming bay‑status payloads.

# Stage 3 — Hardware Networking Workaround
- Pico W devices could not join BMW WLAN due to missing virus protection.
- Introduced a Raspberry Pi 4 hotspot:
- Pico W → Pi 4 (local Wi‑Fi) → LAN → Power Automate → SharePoint → Power App.
- Implemented Micro‑Python MCU logic to detect distance changes and send JSON updates.

# Technical Highlights
- Cloud Architecture: Azure Functions, Power Automate, SharePoint REST API.
- Languages: C#, Micro‑Python, HTML, JSON.
- Hardware: Raspberry Pi Pico W, Raspberry Pi 4, HC-SR04 ultrasonic sensor.
- Documentation: Extensive use of Microsoft Graph Explorer, Azure documentation, and BMW internal IT resources.
- Collaboration: Worked closely with BMW IT teams in Germany to overcome integration barriers.

# Project Management & Handover
- The PMS was developed over several months, including:
- Managing setbacks such as blocked applications, networking restrictions, and compliance requirements.
- Reprioritising tasks and systematically reviewing implementation options.
- Creating a structured four‑week handover plan for the incoming intern.
- Successfully transferring knowledge and ensuring project continuation.

# Status
The system was successfully prototyped, integrated into BMW’s approved workflow, and handed over for final completion. The architecture and implementation strategy remain fully functional and scalable for future development.
