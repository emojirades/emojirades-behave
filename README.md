# Emojirade Behavioral Tests
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
Dummy bots need to be setup and added to the workplace manually.

You'll need 4 apps in total:
- BDD app as the observer (# TODO: future assertion will be added)
- 3 dummy player bots.

Steps:
- Remove `template` from `config/bots.template` 
- Copy each of the Bot User OAuth Access Token to `config/bots`
- Remove `template` from `config/auth.json.template`
- Update `auth.json` with `emojiradebot` access token

### Running the app

```
./bin/run
```
