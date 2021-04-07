# django-referer

**django-referer** is a Django app for **displaying different referer details based on a customizable query parameter** and **keeping this query parameter while user navigates in the site**. \
It provides sales, partners and affiliates custom links to send out in order to get private traffic.
It gives sales, partners and affiliates their opportunity to convert every contact detail on the website to their own.
It thus encourages sales, partners and affiliates to promote the website and the business.
In addition, with the help of analytics scripts, traffic data can be easily distinguished and analyzed.

## Demo

1. URL with referer parameter
e.g. [https://zhujia.com.au/?refer=14](https://zhujia.com.au/?refer=14)

![django-referer Demo - Link with referer](https://yifanai.s3-ap-southeast-2.amazonaws.com/dr/dr14p.jpg)
(The chosen query parameter is kept by django-referer's middleware while user navigates between links)
![django-referer Demo 2 - Link with referer](https://yifanai.s3-ap-southeast-2.amazonaws.com/dr/dr14a.jpg)

2. URL without referer parameter (falls back to the default referer)
e.g. [https://zhujia.com.au](https://zhujia.com.au)

![django-referer Demo - Link without referer](https://yifanai.s3-ap-southeast-2.amazonaws.com/dr/drp.jpg)
![django-referer Demo 2 - Link without referer](https://yifanai.s3-ap-southeast-2.amazonaws.com/dr/dra.jpg)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install django-referer.
```bash
pip install django-referer
```

## Usage

### Step 1. Add referer middleware (in settings.py file)
```python
MIDDLEWARE = [
    'referer.middleware.referer.RefererMiddleware',  # here 
    'django.middleware.security.SecurityMiddleware',
    '...'
]
```

### Step 2. Add referer context processor (in settings.py file)
```python
TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                '...',
                'django.contrib.messages.context_processors.messages',
                'referer.context_processors.referer',  # here
            ],
        },
    },
]
```

### Step 3. Customize referer settings (in settings.py file) (optional)
The defaults are:
```python
REFERER_LINK_PARAMETER = 'referer'
REFERER_DEFAULT_ID = 1
# -> ?referer=1

REFERER_MODEL_FROM = 'django.contrib.auth.models'
REFERER_MODEL_IMPORT = 'User'
# -> from REFERER_MODEL_FROM import REFERER_MODEL_IMPORT

REFERER_IGNORED_LINKS = []
```

### Step 4. Display referer information (in .html file)
```html
<a href="mailto:{{ referer.email }}">Email</a>
<p>{{ referer.first_name }} {{ referer.last_name }}</p>
```

## Contributing
Issues and pull requests are welcomed.

## License
[MIT](https://choosealicense.com/licenses/mit/) © [Yifan Ai](https://yifanai.com)
