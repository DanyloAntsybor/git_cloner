<h1>Git Cloner</h1>

<h3>Self replicating git repository </h3>

Steps to run the application
1. Clone this repo to your server
2. Install docker engine and docker compose to the server (https://docs.docker.com/install/linux/docker-ce/ubuntu/, https://docs.docker.com/compose/install/)
3. Register new GitHub app https://github.com/settings/applications/new
4. Set your server url and callback url ($SERVER_URL/github-callback)
5. Create credentials.env providing variables from .env.example
6. Run `docker-compose up -d` command
7. Your application is up and running

Known issue: One might need to reload the page after initially reaching the the server url in order to see the response