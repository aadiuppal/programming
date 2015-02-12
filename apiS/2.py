import dropbox

app_key="######"
app_secret="######"

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("Enter the authorization code here: ").strip()
#code=Y3GmRYyZIGcAAAAAAAAwvUf8wAfL90p5DSosUJ2pKkw
access_token, user_id = flow.finish(code)

client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()

folder_metadata = client.metadata('/')
print "metadata:", folder_metadata
