## Debian 11 安装 Python 3.13

### 依赖

```bash
apt update -y && apt upgrade -y && \
apt install -y apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev pkg-config
```

### 下载源码并解压

```bash
wget https://www.python.org/ftp/python/3.13.0/Python-3.13.0.tgz && \
tar zxvf Python-3.13.0.tgz && \
cd Python-3.13.0
```

### 编译

```bash
# 查看 CPU 核数，用于后面的 `make -j <N>`
# nproc

./configure --enable-optimizations && \
make -j $(nproc) && \
make altinstall && \
python3.13 --version
```

### venv

#### 安装

```bash
/usr/local/bin/pip3.13 install virtualenv
```

#### 使用

```bash
# 创建
python3.13 -m venv venv

# 激活
source venv/bin/activate

# 退出
deactivate
```

### 替换系统中的 Python3 (可选)

```bash
update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.13 1
update-alternatives --install /usr/bin/pip3 pip3 /usr/local/bin/pip3.13 1
```
