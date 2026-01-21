<div>
<h3>Docker Deploy</h3>
Open a terminal and run the following command:

```commandline
git clone https://github.com/735Andrew/Videostorage
```
<br>
Create a <b>.env</b> file in the root directory with the following variables: <br>
<b>/Videostorage/.env</b>

```commandline 
POSTGRES_USER = <USER_VARIABLE>
POSTGRES_PASSWORD = <PASSWORD_VARIABLE>
POSTGRES_DB = <DB_VARIABLE>
DATABASE_URL = postgresql+asyncpg://<USER_VARIABLE>:<PASSWORD_VARIABLE>@db:5432/<DB_VARIABLE>
```
<br>
Open a terminal in the root directory and execute this command to build the Docker container:

```commandline
docker-compose up -d 
```
</div>
