<h1>Git Cloner</h1>

<h3>Self replicating git repository </h3>

Steps to run the application
1. Clone this repo to your server
2. Install docker engine and docker compose to the server (https://docs.docker.com/install/linux/docker-ce/ubuntu/, https://docs.docker.com/compose/install/)
3. Register new GitHub app https://github.com/settings/applications/new
4. Set your server url and callback url ($SERVER_URL/github-callback)
5. Remove credentials from git tracking (`git rm --cached credentials.env`)
6. Fill credentials.env with appropriate data, including GitHub App credential
7. Run `docker-compose up -d` command
8. Your application is up and running