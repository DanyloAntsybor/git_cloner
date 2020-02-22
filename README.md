<h1>Git Cloner</h1>

<h3>Self replicating git repository </h3>


Steps to run the application
1. Clone this repo to your server
2. Install docker engine and docker compose to the server (https://docs.docker.com/install/linux/docker-ce/ubuntu/, https://docs.docker.com/compose/install/)
2. Register new GitHub app https://github.com/settings/applications/new
3. Remove credentials from git tracking (`git rm --cached credentials.env`)
4. Fill credentials.env with appropriate data, including GitHub App credential
5. Navigate to /env folder and `run docker-compose -f docker-compose.prod.yml up -d ` command
6. Your application is up and running