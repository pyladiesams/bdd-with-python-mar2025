
# BDD with Python 
### Presentation: [Introduction to BDD in Python](https://docs.google.com/presentation/d/1t8gkZ9HH19cT_fM4AAfu3gPutuJZXZ2U1twyL3JOwhc)

## Offline Slides
- [PDF Version](./20250331%20Introduction%20to%20BDD%20in%20Python.pdf)
- [PowerPoint Version](./20250331%20Introduction%20to%20BDD%20in%20Python.pptx)

## Workshop description
This workshop introduces Behavior-Driven Development (BDD) in Python using behave and pytest-bdd. BDD helps teams write tests that are easy to understand and closely aligned with business requirements by using Given-When-Then scenarios in plain language.

BDD bridges the gap between developers, testers, and stakeholders by encouraging collaboration, promoting clean, well-tested code, and making test cases more meaningful and maintainable.

## Requirements
* Python>=3.8
 
## Usage
1. Start by cloning the repo:
```bash
git clone <github-url-of-workshop-repo>
cd <name-of-repo>
```

Inside the repo folder, you can then create a virtual environment and install dependencies in your preferred way.

### With UV
```bash
uv venv -p 3.8
uv lock # (optional)
uv sync --all-extras
source .venv/bin/activate # Or via IDE
```

### With venv
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

You can test that the setup was successful by running
```bash
behave -q -o test.txt solutions/features 
rm test.txt 
```
###### Writing to text file instead of stdout to prevent spoilers.

If everything went well, you should see `3 features passed, 0 failed, 0 skipped`, followed by more lines.

## Video record
Re-watch [this YouTube stream](https://www.youtube.com/watch?v=TynFKyY7wCQ).

## Credits
This workshop was set up by [@pyladiesams](https://github.com/pyladiesams) and [@gCaglia](https://github.com/gCaglia).

