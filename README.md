# dushu

```
https://dushu.richyan.com
```

## Python environment setup

```
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

### Problem when converting HTML in chinese to pdf

```
sudo apt-get install --assume-yes fontconfig

sudo mkdir -p /usr/share/fonts/windows

sudo cp -r /mnt/c/Windows/Fonts/*.ttf /usr/share/fonts/windows/

fc-cache

sudo locale-gen zh_CN.UTF-8
```

## Frontend setup

```
npm install
```

### Compiles and hot-reloads for development

```
npm run serve
```

### Compiles and minifies for production

```
npm run build
```

### Run your unit tests

```
npm run test:unit
```

### Lints and fixes files

```
npm run lint
```
