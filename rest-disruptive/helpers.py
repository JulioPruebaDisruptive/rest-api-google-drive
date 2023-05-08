import logging



# Logger 
class Logger:

    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s"))
    log.addHandler(handler)

# Tools
class Tools:

    def get_files_from_folder(service, folder_name):
        resp = []
        query = "mimeType='application/vnd.google-apps.folder' and name='%s'" % folder_name
        folder = service.files().list(q=query, pageSize=4, fields="files(id, name)").execute().get('files', [])

        try:
            if len(folder) > 0:
                folder_id = folder[0]['id']
                query = f"'{folder_id}' in parents"
                results = service.files().list(q=query, fields="nextPageToken, files(id, name)").execute()
                items = results.get('files', [])
                if len(items) > 0:
                    for item in items:
                        logging.debug(f"Archivo: {item['name']}")
                        resp.append(item['name'])
            else:
                logging.info("Folder not found")

            if not items:
                logging.info("This folder hasn't files")

            for item in items:
                print (f"name: {item['name']}")
        except Exception as e:
            return e

        return resp