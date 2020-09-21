# slackbot_bdd
A library of behave steps to interact with Slack API and bots

First iteration is a recorded set of commands to simulate 3 players game
with human observation.

## How to use

### Virtual Environment
You can use any virtual environment of your choice or even on root.
Here's one way to do it

```
python3 -m venv .venv
source .venv/bin/activate
```

### Install requirements

```
pip install -r requirements.txt
```

### Setting up auths
Run Emojirades app on the side. Or you can test against the live app as well.
Although the dummy bots need to be setup manually and added to the workplace.

You'll need 4 apps in total:
- BDD app as the observer (# TODO: future assertion will be added)
- 3 dummy player bots.

Copy each of the Bot User OAuth Access Token to `config/bots`

### Running the app

```
./bin/run
```
