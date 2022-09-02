from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext


site_url = "https%3A%2F%2Fnetorg5477163.sharepoint.com"
ctx = ClientContext(site_url).with_credentials(UserCredential("apena@texasaft.org", "Lmplgp9!9!"))
web = ctx.web
ctx.load(web)
ctx.execute_query()

print(web.properties['Title'])
