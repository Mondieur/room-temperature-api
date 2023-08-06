### Config my-flask-app 
1. `python3 -m venv venv`
2. `. /venv/bin/activate`
3. Intall through .txt `pip install requirements.txt` or...
```sh
pip install Flask # Flask
pip intall python-dotenv # Env Vars
pip intall psycopg2 # PostgreSQL
``` 

3. `du -sh`: disk usage 
4. `export FLASK_APP=app.py`
5. `export FLASK_ENV=development`
6. `flask run`

**GitHub Connection (Step by Step)**
1. Set your crendentials: `https://<username>:<password>@github.com/<username>/<repo>`
2. And visit GitHub Profile Page: `https://github.com/<your_username_here>`

**PostgreSQL Connection:**  [locally](https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application)
**PostgreSQL Connection:**  [remotelly](https://www.elephantsql.com/)

### TODO Items for POC
- [x] Apply Clean Architecture
- [x] Layer Abstraction
- [x] Dependency Injection
- [x] UseCase Implementation
- [x] Serialization / Deserialization
- [x] Mock Repo Implementation
- [x] Handle Exceptions
- [x] Response Marshalling
- [x] Review usecase.execute() with Req/Resp
- [x] Review API Documentation
- [ ] Implement Full Story with Entity, ValueObject
- [ ] Request Validation with Marshmallow
- [ ] Deal with Date/DateTime
- [ ] Database with SQLAlchemy
- [ ] Logging
- [ ] OAuth2 with Authlib Implementation
- [ ] Authentication to Resource API
- [ ] Dev/Prod Configuration
- [ ] Apply Tests
- [ ] WSGI Settings

## Reference
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Flask RESTPlus](https://flask-restplus.readthedocs.io/en/stable/)
- [Injector](https://github.com/alecthomas/injector)
- [Flask Injector](https://github.com/alecthomas/flask_injector)
- [attrs](https://www.attrs.org/en/stable/)
- [cattrs](https://github.com/Tinche/cattrs)
- [Authlib](https://docs.authlib.org/en/latest/)
- [marshmallow](https://marshmallow.readthedocs.io/en/stable/)
- [SQLAlchemy](https://www.sqlalchemy.org/)