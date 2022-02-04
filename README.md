
## Setup

Create a virtual environment:

```sh
conda create -n rps-env python=3.8
```

Activate the virtual environment:

```sh
conda activate rps-env
```

Install package dependencies (mainly for testing):

```sh
pip install -r requirements.txt
```

## Usage

Run the rock paper scissors game:
```sh
python game.py
```
## Customization
If you prefer to enter your own username before playing, run the game with: 
```sh
PLAYER_NAME="Jon Snow" python game.py
```

## Testing

Run tests:

```sh
pytest
```
