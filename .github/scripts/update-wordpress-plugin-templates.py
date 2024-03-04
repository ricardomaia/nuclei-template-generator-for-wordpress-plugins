name: ✨ WordPress Plugins - Update

on:
  workflow_dispatch:

jobs:
  Update:
    runs-on: ubuntu-latest
    if: github.repository == 'projectdiscovery/nuclei-templates'
    steps:
      - name: Check out repository code
        uses: actions/checkout@v4
        with:
          persist-credentials: false # otherwise, the token used is the GITHUB_TOKEN, instead of your personal token
          fetch-depth: 0 # otherwise, you will failed to push refs to dest repo

      - name: Install Python3
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"
      - run: |
          python -m pip install --upgrade pip
          pip install -r .github/scripts/wordpress-plugins-update-requirements.txt

      - name: Update Templates
        id: update-templates
        run: |
          python3 .github/scripts/wordpress-plugins-update.py
          git status -s | wc -l | xargs -I {} echo CHANGES={} >> $GITHUB_OUTPUT

      - name: Commit files
        if: steps.update-templates.outputs.CHANGES > 0
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add --all
          git commit -m "Auto WordPress Plugins Update [$(date)] :robot:"

      - name: Push changes
        if: steps.update-templates.outputs.CHANGES > 0
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          branch: ${{ github.ref }}
