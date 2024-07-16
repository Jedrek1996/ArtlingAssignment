# Local setup

Here is what you need to do to get the assignment code running on your machine:
You start two Docker containers, one for the Django backend and one for the 
Remix frontend. You then use VSCode to connect to both of these containers. 
In each VSCode instance, you use the terminal to start the backend and frontend 
servers and then you work on the project in each of those two VSCode instances.

Here are step by step instructions:

- Install [Docker](https://docs.docker.com/desktop/) and [docker-compose](https://docs.docker.com/compose/install/) on your machine
- You should have the `docker` and `docker-compose` commands available in your terminal.
- Install [VSCode](https://code.visualstudio.com/download)
- Install the following plugins for VSCode:
    - `ms-vscode-remote.remote-containers`
    - `ms-vscode-remote.vscode-remote-extensionpack`
- Create a `Projects` folder in your home directory: `mkdir ~/Projects`
- Clone this repository: `git clone https://github.com/theartling/assignment-full-stack.git`
- Change directory: `cd ~/Projects/assignment-full-stack`
- Install the containers: `docker-compose up`
- Open VSCode: `code .`
- Use the `Command Palette` and run the `Dev Containers: Attach to Running Container` command
    - select the `dummy_django_backend` container
- In the new VSCode window that is connected to `dummy_django_backend` container:
    - Open folder `/usr/src/app/`
    - You may want to install the Python plugin into this container (`ms-python.python`)
    - Make sure that the Python interpreter at `/usr/local/bin/python` is selected (version `3.12.4`) by clicking the bottom right corner in VSCode.
    - Open the terminal and run `make run`
        - This will run `./manage.py runserver 0.0.0.0:8000`  
        - You should now be able to browse to `http://localhost:8000/admin/` and login with username `admin` and password `test123`
        - You should also be able to browse to `http://localhost:8000/team/` and see some JSON output
- Use the `Command Palette` and run the `Dev Containers: Attach to Running Container` command again
    - Select the `dummy_remix_frontend` container
- In the new VSCode window that is connected to `dummy_remix_frontend` container:
    - Open folder `/usr/src/app/`
    - You may want to install the Tailwind plugin into this container (`bradlc.vscode-tailwindcss`)
    - Open the terminal and run `npm install` and then `npm run dev`
    - You should now be able to browse to `http://localhost:5173` and see the root view
    - Click at the `/team/` link and see the team view.

# Your task:

## Django backend:

On the Django backend, the `team` app has a model `Member` which currently
has the fields `name`, `image`, `bio` and `date_joined`. 

The `Member` class also has a function `get_member_since_str()` which is
currently not implemented. Please implement this function.

At The Artling, we strive to keep up 100% code coverage for all new code that
we write, so after implementing the function, please also write tests in the
file `test_models.py` that ensures 100% code coverage. In the terminal you
can run `make test` and you will see output that shows if there are missing
lines in `models.py` that are not covered by tests. As long as you still see
`models.py` show up in the output it means that your tests are not covering
all lines yet. If you need to create `Member` instance in your test, you
can do so via `mixer` using something like
`mixer.blend('team.Member', date_joined="2021-01-01")`.

## Remix frontend:

At The Artling we use [Remix.run](https://remix.run/) as our frontend framework
and [TailwindCSS](https://tailwindcss.com/) as our CSS framework.

Your task is to make the `/team/` view look like the two screenshots provided 
[here](https://github.com/TheArtling/assignment-full-stack/blob/master/mobile.png) and [here](https://github.com/TheArtling/assignment-full-stack/blob/master/desktop.png). As you can see, we use responsive design, so the view
looks slightly different on mobile vs. on desktop.

The file you need to work on is `team.tsx`. We have already queried the Django
view that returns the data from the backend. You can see the data in the
console output of your browser.

Tip: Have a look at `tailwind.config.ts`. You will find some colors defined
in there that will be useful. Also, please use the font sizes that are defined
in that file and use `font-serif` and `font-sansSerif` appropriately on all
elements that contain text. For the distances between all the elements you can
use the `mt-6`, `ml-6`, `mr-6`, `mx-6`, `my-6` classes. The gap between the grid
items is `gap-4`.

Tip: To render the avatar placeholder image, you can use `http://localhost:8000/media/IMAGE_FILENAME.png`. The filename is part of the data that the view has access
to.

To keep things simple, only work in the `team.tsx` file. You do not need to
create components in separate files for the elements that you will create. Just
put everything into the `function TeamView()`.

Also, please do not use the `style` attribute on any elements. Always use
`className` and then use the TailwindCSS classes.

# Time

We think that this assignment should take you about 2-4 hours, if you are
familiar with Docker, VSCode and TailwindCSS. 

If not, please note that the Tailwind docs are quite good, so you can always 
search for the css style that you want to apply and figure out what the 
corresponding TailwindCSS class name is.

# Submission

You may make as many commits as you like. When you are done, please make sure
that all changes are committed and then zip the entire `assignment-full-stack`
folder and send it to us.

# Questions

If you have any questions or issues with the set up, please do not hesitate to reach out to 
`pengyu at theartling dot com`.

# Grading

For this assignment, we will grade you on the following criteria:

- Are you able to write clean Python code?
- Are you able to write 100% test coverage for your code?
- Are you able to create a frontend view with React based on a given screenshot?
- Are you able to use TailwindCSS, especially it's grid system?
