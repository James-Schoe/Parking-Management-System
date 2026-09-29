# Parking Management System PMS
A multi‑stage digital engineering pilot project designed to track vehicle bay occupancy, made during my time at Rolls Royce Motor Cars. The system integrates microcontroller hardware, cloud services, and industry level automation tools to provide a reliable, scalable parking‑status interface.
_This Repo only looks at the initial PMS prototype I developed in a personal environment. The latter stages of this project can't be disclosed publicly in order to protect sensitive company data._

# Technical Highlights
- Cloud Architecture: Azure Functions, SharePoint REST API, _Integration of prototype to corporate cloud structure._
- Languages: C#, Micro‑Python, HTML, JSON.
- Hardware: Raspberry Pi Pico W, Raspberry Pi 4, HC-SR04 ultrasonic sensor.
- Documentation: Extensive use of Microsoft Graph Explorer, Azure documentation, and BMW internal IT resources.
- Collaboration: Worked closely with BMW IT teams in Germany to overcome integration barriers.

# Features
- Real‑time bay occupancy detection using HC-SR04 ultrasonic sensors.
- Microcontroller‑driven updates via Raspberry Pi Pico W devices.
- Backend integration using an Azure Function.
- SharePoint‑based data storage feeding directly into a PowerApp UI.
- JSON‑based payloads and schemas defined for structured bay‑status updates.
- HTML test scripts used to validate API calls.
- Scalable multi‑bay architecture designed for workshop environments.

# The Process 

## Requirements & Planning
Defined requirements (create a live bay‑occupancy UI) and mapped out the full data path from sensor to MCU to backend to PowerApp (UI). Prior to this project I had no experience with Azure Functions or APIs. Consequently, before building a prototype, I heavily researched Azure Functions and SharePoint APIs (using the Microsoft Graph Explorer). Additionally, I researched BMW’s internal IT constraints to ensure the concept was technically viable before development.

## Prototype Development
- Setup personal Microsoft business account to host Azure Function App.
- Created Azure Function App using Microsoft documentation and Azure UI.
- Configured Raspberry Pi Pico W with HC-SR04 ultrasonic sensor.
- Coded Pico W in Micro-Python, including JSON payload logic to transmit bay status in Azure Function http call.
- Created HTML script to test http request from Pico W and verify functionality of JSON payload and schema. 
- Created http triggered Azure Function using C#, to transmit sensor data to a SharePoint list via a Graph API call.

## Corporate Integration 
After creating a working prototype in my own Microsoft tenant, the next step was integrating the system into BMW's network structure. Due to strict security and compliance requirements, the project had to undergo a full architecture redesign. While I can't disclose the technical steps taken to achieve this redesign, I can outline the process taken to overcome this challenge: 
- Frequent discussions with BMW IT specialists.
- Hours familiarising myself with IT security documentation.
- Hands-on experience with the latest methods of cloud-data transfer. 

# Status
The system was successfully prototyped, integrated into BMW’s approved workflow, and handed over for final completion. The architecture and implementation strategy remain fully functional and scalable for future development. Although, this Repo only demonstrates the PMS prototype I made in my personal tenant. The full BMW integrated version of this project is not displayed in this Repo to protect sensitive company data. 
