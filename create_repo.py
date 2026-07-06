import subprocess, json, os

# Create repo via API
token = "ghp_2u...ZlWz"
headers = "-H 'Authorization: token {}' -H 'Accept: application/vnd.github+json'".format(token)

cmd = "curl -s {} https://api.github.com/user/repos -d '{{\"name\":\"marketing2974-landing\",\"description\":\"Landing page para Marketing2974.com — Plataforma de recomendación SaaS + IA\",\"private\":false,\"has_pages\":true}}'".format(headers)

result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
data = json.loads(result.stdout)

if "html_url" in data:
    print("REPO_CREATED: " + data["html_url"])
    print("CLONE_URL: " + data["clone_url"])
elif "errors" in data:
    print("ERROR: " + str(data["errors"]))
else:
    print("UNEXPECTED: " + json.dumps(data, indent=2)[:500])
