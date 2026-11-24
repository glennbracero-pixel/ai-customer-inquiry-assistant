\# AI Customer Inquiry Assistant



\## Project Overview



The AI Customer Inquiry Assistant is an automation prototype designed for a digital marketing agency. It uses artificial intelligence to analyze customer inquiries, categorize requests, assess priority, and prepare email response drafts for human review.



The goal is to reduce repetitive administrative work while keeping a human in control of customer communication.



\## Business Scenario



This project simulates a Digital Growth Agency offering:



\- Search Engine Optimization (SEO)

\- Social Media Marketing

\- Paid Advertising (Google Ads and Meta Ads)

\- Content Marketing



\## How It Works



1\. A potential customer submits an inquiry through Google Forms.

2\. The inquiry is automatically recorded in Google Sheets.

3\. A Python automation checks the spreadsheet every 60 seconds.

4\. A locally running AI model analyzes the inquiry.

5\. The system generates a suggested response and identifies the inquiry category, intent, and priority.

6\. The results are saved to Google Sheets for human review.

7\. An authorized human changes the inquiry status to Approved.

8\. The automation validates the email address and prepares a Gmail draft.

9\. Duplicate-draft checking helps prevent repeated drafts.

10\. The email remains a draft until a human reviews and sends it.



\## Technology Stack



| Technology | Purpose |

|---|---|

| Python | Main automation logic |

| Google Forms | Customer inquiry collection |

| Google Sheets | Inquiry database |

| Ollama | Local AI runtime |

| Qwen 3.5 4B | AI inquiry analysis |

| Gmail API | Email draft creation |

| gspread | Google Sheets integration |

| Google Authentication | API authentication |



\## Implemented Features



\- Automated Google Sheets polling

\- AI-powered inquiry classification

\- Customer intent detection

\- Inquiry priority assessment

\- Suggested email response generation

\- Email address validation

\- AI response structure validation

\- Human approval workflow

\- Gmail draft creation

\- Duplicate-draft prevention using unique inquiry IDs

\- Logging and error handling

\- Startup connection retries



\## Safety and Human Oversight



This prototype does not automatically send customer emails.



A human must approve an inquiry before a Gmail draft is created. The human remains responsible for reviewing the suggested response and deciding whether to send it.



The system also validates email addresses and checks for existing drafts before creating another one.



\## Current Limitations



\- The automation runs locally on the computer.

\- The computer and Python process must remain running for automatic polling.

\- The current polling interval is 60 seconds.

\- Cloud deployment and 24/7 availability are not yet implemented.

\- AI-generated responses require human review.

\- The project has been tested with sample inquiries and a personal Gmail account.



\## Future Improvements



\- Cloud deployment for continuous operation

\- Webhook-based inquiry processing

\- n8n workflow integration

\- Improved monitoring and reporting

\- More advanced error recovery

\- A customer-facing inquiry dashboard

\- Multi-client configuration



\## Project Status



\*\*Working local portfolio prototype.\*\*



This project demonstrates practical skills in Python automation, AI integration, Google Workspace APIs, workflow design, and human-in-the-loop automation.



\## Security Notice



Credential files, OAuth tokens, API keys, and customer information must never be committed to a public repository.



\## Project Screenshot



Here is a preview of the Google Sheets dashboard used by the AI Customer Inquiry Assistant.



!\[Google Sheets Dashboard](screenshots/google-sheets.png)



The dashboard stores customer inquiries and displays AI-generated categories, priorities, suggested replies, and processing statuses.



Additional screenshots demonstrating AI-generated replies and Gmail draft creation will be added as the project documentation expands.

