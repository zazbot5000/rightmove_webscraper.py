"""https://stackoverflow.com/questions/53319936/how-do-i-replace-the-contents-of-a-google-drive-file-using-python"""

from oauth2client import file, client, tools
from googleapiclient.discovery import build
from httplib2 import Http
from io import BytesIO
from apiclient.http import MediaIoBaseUpload

def gauthenticate():
    # If modifying these scopes, delete the file token.json.
    SCOPES = 'https://www.googleapis.com/auth/drive'
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))
    return service

def SaveTxtGDrive(service):
    # Fill in your own file id here:
    fileId = '1kEyXXXXXXXX_gEd6lQq'
    _mimeType = 'text/plain'
    _textStream = BytesIO(b'Here is some arbitrary data\nnew text\nAnother line\n')
    _media = MediaIoBaseUpload(_textStream, mimetype=_mimeType,
        chunksize=1024*1024, resumable=True)
    _updatedFile = service.files().update(fileId=fileId,
        media_body=_media).execute()

def main():
    _service = gauthenticate()
    SaveTxtGDrive(_service)
    return

if (__name__ == '__main__'):
    main()