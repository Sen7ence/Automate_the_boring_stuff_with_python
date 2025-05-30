import requests

res = requests.get("http://www.gutenberg.org/cache/epub/1112/pg1112.txt")
res.raise_for_status()  # Ensure we got a successful response
playFile = open(
    r"D:\Python\PythonLearning\book\hy\11\RomeoAndJuliet.txt", "wb"
)  # 指定保存路径
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
