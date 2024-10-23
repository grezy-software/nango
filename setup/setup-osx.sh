brew install pnpm
brew install python@3.12
brew install virtualenv
virtualenv .venv --python=python3.12
printf "\n===============================================\nVirtual python environment has been created.\n"
source .venv/bin/activate
pip3 install pip-tools
printf "Virtual python environment has been activated.\n"
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12
brew install stripe/stripe-cli/stripe

# Install requirements
printf "Compiling requirements... This may take a few minutes.\n"
# Must be call at the root of the project with "make setup" command
pip-compile ./backend/requirements/development.txt --output-file ./backend/requirements/full-requirements.txt --resolver=backtracking --strip-extras
pip install -r ./backend/requirements/full-requirements.txt

# Install pre-commit hooks
pre-commit install
# Generate .envs files
python ./setup/env_file_generator.py development
python ./setup/env_file_generator.py production

printf "Done installing requirements for local .venv!\nHave fun coding!\n"
