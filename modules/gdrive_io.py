from pathlib import Path
from oauth2client import file, client, tools
from googleapiclient.discovery import build
from httplib2 import Http
from apiclient.http import MediaFileUpload


def g_authenticate():
    # If modifying these scopes, delete the file token.json.
    scopes = "https://www.googleapis.com/auth/drive"
    store = file.Storage(Path("data/token.json"))

    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(Path("data/credentials.json"), scopes)
        creds = tools.run_flow(flow, store)
    service = build("drive", "v3", http=creds.authorize(Http()))
    return service


def upload_csv(area_type):
    """ Get the fileID from the drive sheet url """
    print("uploading to Google Sheets...")

    service = g_authenticate()

    if area_type == "radius":
        fileId = "1dYUGY54QYEnAfcd2JN_TUY1Sba3TRFAGvDQFM-WteKA"
    else:
        # polylines area
        fileId = "1_95DWzlo5WF2vDSBSYKFEI08aGofGVnhwfIIXqVCBvc"

    _media = MediaFileUpload(
        Path("output/export_dataframe.csv"), mimetype="text/csv", resumable=True
    )
    _updatedFile = service.files().update(fileId=fileId, media_body=_media).execute()
    print("\tCSV data uploaded!")

    return
