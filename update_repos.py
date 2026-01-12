import requests
import re
import random

# Fetch repos
response = requests.get('https://api.github.com/users/DarylFernandes99/repos')
repos = response.json()

max_repos = 4

# Sort by stars + forks
top_repos = sorted(repos, key=lambda x: x['stargazers_count'] + x['forks_count'], reverse=True)[:max_repos]

# Get random backdrop
backdrops = ['Signal', 'Charlie Brown', 'Formal Invitation', 'Plus', 'Circuit Board', 'Overlapping Hexagons', 'Brick Wall', 'Floating Cogs', 'Diagonal Stripes']
random_backdrops = random.sample(range(1, len(backdrops)), max_repos)

# Generate HTML
repo_html = '<div align="center">\n'
for repo, backdrop in zip(top_repos, random_backdrops):
    repo_html += f'''  <a href="{repo['html_url']}">
    <img width="400" src="https://socialify.git.ci/DarylFernandes99/{repo['name']}/image?font=JetBrains%20Mono&forks=1&language=1&name=1&stargazers=1&theme=Dark&pattern={backdrops[backdrop]}" />
  </a>\n'''
repo_html += '</div>'

# Update README
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# Replace content
pattern = r'<!-- REPO-LIST:START -->.*?<!-- REPO-LIST:END -->'
new_content = f'<!-- REPO-LIST:START -->\n{repo_html}\n<!-- REPO-LIST:END -->'
readme = re.sub(pattern, new_content, readme, flags=re.DOTALL)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)
