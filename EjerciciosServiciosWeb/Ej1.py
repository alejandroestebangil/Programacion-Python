from ftplib import FTP

def upload_file(ftp, file_path, remote_path):
    with open(file_path, 'rb') as file:
        ftp.storbinary(f'STOR {remote_path}', file)

def download_file(ftp, remote_path, local_path):
    with open(local_path, 'wb') as file:
        ftp.retrbinary(f'RETR {remote_path}', file.write)

def main():
    ftp_host = 'ftp.example.com'
    ftp_user = 'alejandro'
    ftp_password = '1234'

    ftp = FTP(ftp_host)
    ftp.login(ftp_user, ftp_password)

    # Upload file
    local_file_path = 'local_file.txt'
    remote_file_path = 'remote_file.txt'
    upload_file(ftp, local_file_path, remote_file_path)
    print(f"File '{local_file_path}' uploaded to '{remote_file_path}'")

    # Download file
    local_download_path = 'downloaded_file.txt'
    download_file(ftp, remote_file_path, local_download_path)
    print(f"File '{remote_file_path}' downloaded to '{local_download_path}'")

    ftp.quit()

if __name__ == "__main__":
    main()
