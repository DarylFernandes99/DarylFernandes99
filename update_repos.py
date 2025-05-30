import requests
import re

# Fetch repos
response = requests.get('https://api.github.com/users/DarylFernandes99/repos')
repos = response.json()

# Sort by stars + forks
top_repos = sorted(repos, key=lambda x: x['stargazers_count'] + x['forks_count'], reverse=True)[:4]

# Generate HTML
repo_html = '<div align="center">\n'
for repo in top_repos:
    repo_html += f'''  <a href="{repo['html_url']}">
    <img width="400" src="https://github-readme-stats.vercel.app/api/pin/?username=DarylFernandes99&repo={repo['name']}&theme=dark&hide_border=true&bg_color=0d1117&title_color=58a6ff&text_color=c9d1d9&icon_color=40c463" />
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
