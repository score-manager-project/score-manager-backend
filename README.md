# Score Manager Backend

The backend server for score manager

## Tech Stack

**API Server:** FastAPI

**Database:** Deta Base

**Deployment Provider:** Deta

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`NYCU_OAUTH_CLIENT_ID`

`NYCU_OAUTH_CLIENT_SECRET`

`NYCU_OAUTH_REDIRECT_URI`

## Run Locally

Clone the project

```bash
git clone https://github.com/score-manager-project/score-manager-backend.git
```

Go to the project directory

```bash
cd score-manager-backend
```

Install dependencies

```bash
pdm install
```

Start the server

```bash
pdm run dev
```
