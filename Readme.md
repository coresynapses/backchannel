# Backchannel

A backchannel is a secret line of communication.

Backchannel is a Multimedia and Code-collaborative board with a focus on
the transformation of uploaded files.

Users without accounts can make threads and post to threads and have
limited multimedia and code functionality available to them.

Users with accounts have greater multimedia and code functionality
subject to reasonable generous limits.

Paid users can create boards powered by the Matrix protocol and these
are the backchannels.

## How to run

Requirements:
- Python 3.11
- Django 4.2
- PostgreSQL 16.1

Once these technologies are installed, you need create your PostgreSQL
user:
`createuser --interactive`

Create a database named "backchan" using the following command:
`createdb backchan`

Create the file named ".pg_service.conf" and save it in the
corresponding directory:
- Linux or macOS: ~/.pg_service.conf
- Windows: %APPDATA%\postgresql\.pg_service.conf

The contents should be as follows:

``[backchan]
host=localhost
user=[psql_username]
dbname=backchan
port=5432``

Create the PostgreSQL file and save it in the corresponding directory:
- Linux or macOS: ~/.pgpass
- Windows: %APPDATA%\postgresql\pgpass.conf

The contents should be as follows:

`localhost:5432:backchan:[psql_username]:[psql_password]`

Then go to the root directory of the repository and run:

`python manage.py runserver`

Go the following url in your browser:
https://localhost:8000

The website should be working.

## Technologies Used

Frontend:
- Vanilla CSS
- Vanilla JS

Backend:
- Python
- Django
- PostgreSQL

## Channels

A Channel is similar to a subreddit or a board.

A User with an account can create any board they want.

There are default channels that are already provided by the creator.

Each channel consists of initial posts.

Those posts then point to an undirected graph of posts.

## Posting

Posts are modeled as follows:
- Int: ID
- String: Author
- Array of Ints: Replies
- Array of Ints: References
- Date: PostDate
- String: Text
- String: FilePathImage
- String: FilePathPdf
- String: FilePath3DModel
- Graph: GraphData
- String: ExecutableCode

Any visitor can post on any given channel on Backchan.

The posts can be anonymous whether they have an account or not.

Posts will not be hierarchical like Reddit nor trees like 4chan.

They will be undirected graphs.

Posts can make references to posts made before and after post
creation.

Posts can be edited but versions will stored and displayed for access.

The posts can be: 
- simple text, 
- an image, 
- a video, 
- a pdf document that is scanned by the server, 
- a 3D model with optional animation data, 
- a graph of arbitrarily-labeled nodes, or 
- executable common lisp/scheme/clojure code that is sandboxed by the
  website.

The posts are formatted according to the org-mode specification.

However, LaTeX code blocks are rendered in full LaTeX symbols.

Code written on a post can use data from other posts and operate it on
its data, input, or output.
