#!/usr/bin/python
import paramiko


def remoteUpload(loacfilepath, remotefilepath):
    # 建立连接
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机。
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("221.122.128.54", 31011, "meirtz", "594249q")
    # 测试-ls
    stdin, stdout, stderr = ssh.exec_command('ls')
    # print(stdout.readlines()
    # 使用sftp上传下载命令
    sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
    sftp = ssh.open_sftp()
    # 上传文件
    sftp.put(loacfilepath, remotefilepath)
    # 文件下载
    # shell = "scp -P 31011 " + "/Users/apple/Downloads/upload.py" + \
    #         " meirtz@221.122.128.54:/home/meirtz/hackathon/"
    print('finish')


def remoteDownload(remotefilepath, localfilepath):
    # 建立连接
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机。
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("221.122.128.54", 31011, "meirtz", "594249q")
    # 使用sftp上传下载命令
    sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
    sftp = ssh.open_sftp()
    # 上传文件
    sftp.get(remotefilepath, localfilepath)
    # 文件下载
    # shell = "scp -P 31011 " + "/Users/apple/Downloads/upload.py" + \
    #         " meirtz@221.122.128.54:/home/meirtz/hackathon/"
    print('finish')


def remoteIsExist(remotefilepath, targetfile):
        # 建立连接
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机。
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("221.122.128.54", 31011, "meirtz", "594249q")
    v = "ls"
    c = v + " " + remotefilepath
    stdin, stdout, stderr = ssh.exec_command(c)
    result1 = stdout.readlines()
    filename = targetfile + '\n'
    print(result1)
    return filename in result1


if __name__ == "__main__":
    # remoteUpload('/Users/apple/Downloads/1.png',
    #              '/home/meirtz/hackathon/1.png')
    # remoteDownload('/home/meirtz/hackathon/1.png', '/Users/apple/Downloads/test/1.jpg', )
    print(remoteIsExist('/home/meirtz/hackathon', "jksdha.png"))
