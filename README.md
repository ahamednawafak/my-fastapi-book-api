\# 📚 FastAPI Book Management API



A secure, database-backed RESTful API built with \*\*Python\*\*, \*\*FastAPI\*\*, \*\*SQLAlchemy\*\*, and \*\*SQLite\*\*. This API provides complete CRUD (Create, Read, Update, Delete) functionality for managing a book inventory, protected by API Key authentication and automatically deployed to \*\*Render\*\*.



🌐 \*\*Live Demo \& Interactive Docs:\*\* \[https://my-fastapi-book-api.onrender.com/docs](https://my-fastapi-book-api.onrender.com/docs)



\---



\## ✨ Features



\- \*\*Full CRUD Support:\*\*

&#x20; - `GET /books`: Fetch all books stored in the database.

&#x20; - `POST /books`: Add a new book to the inventory.

&#x20; - `PUT /books/{book\_id}`: Update an existing book's details.

&#x20; - `DELETE /books/{book\_id}`: Permanently remove a book by ID.

\- \*\*API Key Security:\*\* All data-modifying and fetch routes are protected via custom HTTP Header authentication (`X-API-Key`).

\- \*\*Data Persistence:\*\* Integrated \*\*SQLAlchemy ORM\*\* backed by an \*\*SQLite\*\* database (`books.db`).

\- \*\*Auto-Generated OpenAPI Docs:\*\* Live interactive testing interface powered by Swagger UI at `/docs`.

\- \*\*CI/CD Integration:\*\* Automatically built and deployed on \*\*Render\*\* via GitHub pushes.



\---



\## 🛠️ Tech Stack



\- \*\*Language:\*\* Python 3.14+

\- \*\*Framework:\*\* FastAPI

\- \*\*ASGI Server:\*\* Uvicorn

\- \*\*ORM \& Database:\*\* SQLAlchemy \& SQLite

\- \*\*Validation:\*\* Pydantic

\- \*\*Cloud Hosting:\*\* Render



\---



\## 🔒 Security \& Authentication



All endpoints under `/books` require an API Key passed in the request header.



\* \*\*Header Key:\*\* `X-API-Key`

\* \*\*Header Value:\*\* `MySecretPassword123`



If the key is missing or incorrect, the API responds with a `401 Unauthorized` HTTP status code.



\---



\## 🚀 API Endpoints Overview



| Method | Endpoint | Protection | Description |

| :--- | :--- | :--- | :--- |

| `GET` | `/` | Public | Home / Health Check |

| `GET` | `/books` | Protected | Fetch all books |

| `POST` | `/books` | Protected | Add a new book |

| `PUT` | `/books/{book\_id}` | Protected | Update book details |

| `DELETE` | `/books/{book\_id}` | Protected | Delete a book by ID |

| `GET` | `/docs` | Public UI | Interactive Swagger UI Documentation |



\---



\## 🖥️ Local Setup \& Running Instructions



\### 1. Clone the repository

```bash

git clone \[https://github.com/ahamednawafak/my-fastapi-book-api.git](https://github.com/ahamednawafak/my-fastapi-book-api.git)

cd my-fastapi-book-api

