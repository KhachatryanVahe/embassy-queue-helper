# Initial Setup

To use this application, you need to set up a Python virtual environment.

#### 1.Create a virtual environment and install requirements
```bash
python3 -m venv .venv
./.venv/bin/pip install webdriver_manager selenium
```

#### 2.Download `ChromeDriver`
Go to this [link](https://googlechromelabs.github.io/chrome-for-testing/), choose a suitable binary for your system, copy the download link, and open it in a new browser tab. After the download completes, unzip the driver and move it to `/usr/bin`.

#### 3. Run Google Chrome in remote debugging mode
> **_NOTE:_** To get your Chrome profile path and name, open `chrome://version` in browser tab.
```bash
google-chrome --remote-debugging-port=9222 --user-data-dir=~/.config/google-chrome/ --profile-directory="Profile 2"
```

#### 4.Provide env variables
```bash
cp env.example .env
```
And initialize values

#### 5.Lunch application
> **_NOTE:_** Before launching the application
> * Make sure you are logged into the target website in the browser (using the profile specified above).
> * Close the browser completely before running the script.

```bash
./.venv/bin/python main.py
```
