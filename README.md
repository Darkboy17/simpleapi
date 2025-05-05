# 🚀 Simple API for Project Management

This is a simple, production-ready REST API built with **FastAPI, PostgreSQL, and SQLModel as ORM** for managing projects. It supports JWT-based authentication, CRUD operations on projects, and is container-ready for deployment.

***
## 🎥 Video Walkthrough
Check out the following link to see a walk-through of the API.

https://drive.google.com/file/d/1ciFDSTac3otE2paVx37O_Jylknbn7gKj/view?usp=sharing

***
## 🧩 Features

- 🔐 **JWT Authentication** (OAuth2 password flow)
- 📁 **CRUD APIs** for managing projects
- 🧼 **Validation** using Pydantic models ( as`SQLModel` inherits from Pydantic's `BaseModel`)
- 🧪 **Interactive Swagger Docs** for testing
- 📦 **PostgreSQL** as the database
- 🚀 **Production-ready deployment** with Docker
- 🔄 **Token-based auth for Swagger UI**
- ⚠️ **Duplicate project prevention**
- 🗃️ **Consistent ID assignment** (handles gaps in project IDs after deletion)

***
## 📦 Requirements

- Python 3.8+
- PostgreSQL
- Docker (optional for deployment)

***
##  🌐 Live Link

If you simply want to avoid the hassle of setting up the project locally on your machine, please use this live link to start using and testing the API right away.

https://simpleapi.duckdns.org

***
## 🧪 Using the API via Swagger UI

### Step 1: Register a New User

- Open: [https://simpleapi.duckdns.org/docs](https://simpleapi.duckdns.org/docs)
- Expand the `POST /register` endpoint.
- Click "Try it out" and fill in your ```username```, ```password```, and ```role```.
- Click "Execute" to register.

Check the **Responses** section if you have been registered successfully or not. Then, proceed to Step 2.

### Step 2: Log In to Get a Token

- Expand the `POST /login` endpoint.
- Enter the ```username``` and ```password``` you just registered with in the **Request Body**.
- Click "Execute" and scroll down to the **Reponses** section to get an `access_token` as shown below.

	```json
	{
	  "access_token": "long_token_string",
	  "token_type": "bearer"
	}
	```
	Copy the ```access_token```.

### Step 3: Authorize Swagger

- Click the `Authorize` button at the top of the Swagger UI.
- Paste the ```access_token``` in the **Value** field.
- Click "Authorize" then "Close".

### Step 4: Use the Protected Endpoints

Now you can use all authenticated endpoints based on what role you chose while registering:

  [ admin, user ]:
  - `GET /projects/` – List all projects (Read)

  [ admin ]:
  - `POST /projects/` – Create a project (Create)
  - `PUT /projects/{id}` – Update a project (Update)
  - `DELETE /projects/{id}` – Delete a project (Delete)

***
## ⚙️For Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Darkboy17/simpleapi.git
cd simpleapi
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv # Or python -m venv venv
source venv/bin/activate # On Windows venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/simple-api
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
> Note: Please double check that you have Postgres setup locally and replace `username` and `password` in the `DATABASE_URL` with yours.
> 
> For the ```SECRET_KEY``` please use the "secrets-generator.py" which can be found under app/utils/. Run the script, and copy the key and paste it as a value for ```SECRET_KEY```.
> 
> Since, you are running locally, your simple-api database will initially be empty. You can speed up the process of pre-seeding the database with 20 mock data by running the "projects_seeder.py" script. You'd see a message "✅ 20 projects added successfully." in you terminal if pre-seeding succeeds.
> 
> You can set ```ACCESS_TOKEN_EXPIRE_MINUTES``` to your wish, however 30 minutes is the default for security reasons.

***
## ▶️ Running the App

```bash
uvicorn app.main:app --reload
```

Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)  

For an interactive API documentation from an OpenAPI specification, use:
ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)


***
## 🧪 Using the API via Swagger UI

- Open: [http://localhost:8000/docs](http://localhost:8000/docs)
-  Similarly, follow the steps as given in the **Using the API via Swagger UI** section above.

***
## 🚀 Containerize the API using Docker (Optional)

> 1. Make sure you have Docker installed on your local machine and it is running in the background.
> 2. Open your code editor if you haven't and navigate to simpleapi root folder in the terminal.
> 
#### Then, run one of  the following docker command to dockerize the app based on which platform you are going to run the docker container on:
```powershell
# Build for Linux ARM64 (e.g., Apple Silicon M1/M2, Raspberry Pi)
docker build --platform linux/arm64 -t simple-api:arm64 .

# Build for Linux AMD64 (e.g., most cloud servers, Intel/AMD desktops)
docker build --platform linux/amd64 -t simple-api:amd64 .

# Optional: Build for Windows AMD64 (usually not recommended for Linux-targeted APIs)
docker build --platform windows/amd64 -t simple-api:windows-amd64 .
```
#### Finally, run the docker image using the following command relative to what you chose above when building the image:

Update the `PORT`, `SERVER_POSTGRES_URL`, `SECRET_KEY`, and other environment variables with your actual values.
```powershell
# For Linux ARM64 (Apple M1/M2, Raspberry Pi)
docker run -d -p PORT:8000 \
  -e SERVER_POSTGRES_URL="postgresql://username:password@<host>:5432/simple-api" \
  -e SECRET_KEY="your_generated_secret_key" \
  -e ALGORITHM="HS256" \
  -e ACCESS_TOKEN_EXPIRE_MINUTES=30 \
  --name simple-api-arm64 \
  darkboy18/simple-api:arm64

# For Linux AMD64 (Intel/AMD-based PCs, most servers)
docker run -d -p PORT:8000 \
  -e SERVER_POSTGRES_URL="postgresql://username:password@<host>:5432/simple-api" \
  -e SECRET_KEY="your_generated_secret_key" \
  -e ALGORITHM="HS256" \
  -e ACCESS_TOKEN_EXPIRE_MINUTES=30 \
  --name simple-api-amd64 \
  darkboy18/simple-api:amd64

# (Optional) For Windows AMD64 (if supported)
docker run -d -p PORT:8000 `
  -e SERVER_POSTGRES_URL="postgresql://username:password@<host>:5432/simple-api" `
  -e SECRET_KEY="your_generated_secret_key" `
  -e ALGORITHM="HS256" `
  -e ACCESS_TOKEN_EXPIRE_MINUTES=30 `
  --name simple-api-windows `
  darkboy18/simple-api:windows-amd64
```

> 💡 Replace `<host>` with `localhost` if PostgreSQL is on the same machine, or with the host IP if it's remote.

You can also push this to Dockerhub for production if you want.

***
## 📬 Contact

Created by **[Kordor Pyrbot](https://github.com/Darkboy17)**  - Feel free to reach out on opcodegenerator@gmail.com.
