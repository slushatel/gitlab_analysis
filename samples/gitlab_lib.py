import gitlab
import logging

logging.basicConfig(level=logging.ERROR)

# private token or personal token authentication
gl = gitlab.Gitlab('http://gitlab.com', private_token='AtKBow56qjVEjfDxupsW')

# # oauth token authentication
# gl = gitlab.Gitlab('http://10.0.0.1', oauth_token='my_long_token_here')
#
# # username/password authentication (for GitLab << 10.2)
# gl = gitlab.Gitlab('http://10.0.0.1', email='jdoe', password='s3cr3t')

# anonymous gitlab instance, read-only for public resources
# gl = gitlab.Gitlab('http://gitlab.com')

# make an API request to create the gl.user object. This is mandatory if you
# use the username/password authentication.
gl.auth()

g2 = gitlab.Gitlab('http://gitlab-poc.globallogic.com', private_token='KonoEtYRBWstrcaFxXrg')
g2.auth()

# list all the projects
projects = g2.projects.list()
for project in projects:
    print(project)

i = 0
for project in projects:
    i += 1
    try:
        lang = project.languages()
    except Exception as ex:
        logging.error(ex)
        lang = None
    print(str(i) + ":" + project.name + ":" + str(lang))
    if lang is not None:
        for l in lang:
            print(l + ":" + str(lang[l]))
