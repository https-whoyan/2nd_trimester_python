<h2 align="center"> My Final Python Project </h2>
<hr>

This is a Telegram bot that allows you to view in a convenient format the latest personal 
successful submissions of tasks that users have solved on <a>LeetCode.com</a>.
</h4>

<hr>
<h3 align="center"> App Architecture: </h3>

<pre>
<code style="display: block">
...
config.py: load .env file
.env file: secret information (keys, password, etc.)
src
├── bot
|    ├── bot.py: main bot py file
|    ├── schemas.py: schemas for correct bot work
|    └── utils.py
|
└── database
|    ├── database.py: main connection.
|    └── utils.py: database work functions
|
└── parser
|    ├── parser.py: main parser file. GrapQL parser
|    ├── schemas.py: classes for convenient work
|    └── utils.py
|
└── main.py: main file.
</code> 
</pre>

<h3 align="center"> Database Architecture: </h3>
<img src=".github/database_architecture.png">

<hr>
<h3 align="center"> How it works: </h3>
The startup comes from the src.main.py file.
The botMain function is launched from it, which starts the telegram bot. <br>
<b>The telegram bot has 2 handlers - start command and message. 
All commands are validated through the message handler. </b> <br>
Let's analyze the main command. As soon as the user types the <b>/viewLCSubmissions</b> command, the parser will fetch 
the last 5 solved problems via GraphQL query, save them in the database, 
and the attempts themselves will be taken from the database. <br>
Primarily use <b>asynchronous</b> work during program execution work.

<hr>
<h3 align="center"> Used Libraries and technologies: </h3>
<a href="https://graphql.org/"> 
<img src="https://upload.wikimedia.org/wikipedia/commons/1/17/GraphQL_Logo.svg" width="40px"> 
</a>
<a href="https://www.postgresql.org/"> 
<img src="https://upload.wikimedia.org/wikipedia/commons/2/29/Postgresql_elephant.svg" width="40px"> 
</a>
<a href="https://github.com/aiogram/aiogram"> 
<img src="https://avatars.githubusercontent.com/u/33784865?s=200&v=4" width="40px"> 
</a>
<a href="https://github.com/graphql-python/gql"> 
<img src=".github/gql3_logo_preview_rev_1.png" width="40px"> 
</a>
<a href="https://github.com/psf/requests"> 
<img src="https://upload.wikimedia.org/wikipedia/commons/a/aa/Requests_Python_Logo.png" width="40px" height="40px"> 
</a>

<hr>
<h3 align="center"> My Contacts </h3>
<b>Telegram:
<a href="https://t.me/https_whoyan">
<img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" width="18">
</a> <br>
Gmail:
<a href="mailto:yaniknezhin@gmail.com">
<img src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Gmail_icon_%282020%29.svg" width="20">
</a> </b>

<h3 align="center"> Thanks for watching and reading! </h3>