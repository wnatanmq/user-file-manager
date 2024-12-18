import os

class File():
    def __init__(self):
        self.path = "/tmp/user-file-manager/"
        self._config_path()
        self.max_item_per_page = 5
    def _config_path():
        if not os.path.exists(
            "/tmp/user-file-manager/"
        ):
            os.mkdir("/tmp/user-file-manager/")
            
    def create_file_by_user(
        file_name : str,
        file : bytes,
        user_name : str
    ):
        dir_file = f"/tmp/user-file-manager/{user_name}/" 
        if not os.path.exists(dir_file):
            os.mkdir(dir_file)
        with open(dir_file + file_name, "a") as f:
            f.write(file)
            f.close()

    def list_file_by_user(
        self,
        user_name : str,
        index_file=0,        
    ):
        dir_file = f"/tmp/user-file-manager/{user_name}/"         
        if not os.path.exists(dir_file):
            return []
        all_files = os.listdir(dir_file)
        return all_files[
            index_file : all_files + self.max_item_per_page
        ]
        