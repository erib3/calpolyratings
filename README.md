# calpolyratings
## How to run site
1. Clone repo

2. Create virtualenv

`virtualenv --python=/usr/bin/python3.6 venv`

3. Enter virtualenv

`source ./venv/bin/activate`

4. Install project requirements

`pip install -r requirements.txt`

5. Set DJANGO_SETTINGS_MODULE to dev_settings

`export DJANGO_SETTINGS_MODULE=cpratings.dev_settings`

6. Create secrets.json file in calpolyratings/cpratings directory
<pre>
{
 
  "SECRET_KEY" : "adkghlk1q(tf*6^y0nj9vak@533asd(a$)-v-(ii*lalrbb_xa@",

  "SQL_PW" : "----",

  "SQL_USERNAME" : "----",

  "RECAPTCHA_SECRET_KEY" : "",

  "ADMIN_URL" : "admin/",

  "EMAIL" : "---@gmail.com",

  "EMAIL_PW" : "---"

}
</pre>
7. In calpolyratings/ apply migrations

`python manage.py migrate`

8. Run scripts that generate test data

`./fixtures/load_data.sh`

9. Run site

`python manage.py runserver`
