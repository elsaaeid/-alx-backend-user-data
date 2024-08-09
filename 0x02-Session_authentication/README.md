# 0x02-Session_authentication

<p>
  Simple HTTP API for playing with User model.
</p>

<h2>
  Files
</h2>

<h3>models/</h3>

<ul>
  <li>
    base.py: base of all models of the API - handle serialization to file
  </li>
  <li>
    user.py: user model
  </li>
</ul>

<h3>api/v1</h3>

<ul>
  <li>
    app.py: entry point of the API
  </li>
  <li>
    views/index.py: basic endpoints of the API: /status and /stats
  </li>
  <li>
    views/users.py: all users endpoints
  </li>
</ul>

<h2>Setup</h2>

<pre>
  <code>
    $ pip3 install -r requirements.txt
  </code>
</pre>


<h2>Run</h2>

<pre>
  <code>
    $ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
  </code>
</pre>

<h2>Routes</h2>

<ul>
  <li>
    GET /api/v1/status: returns the status of the API
  </li>
  <li>
    GET /api/v1/stats: returns some stats of the API
  </li>
    <li>
    GET /api/v1/users: returns the list of users
  </li>
    <li>
    GET /api/v1/users/:id: returns an user based on the ID
  </li>
    <li>
    DELETE /api/v1/users/:id: deletes an user based on the ID
  </li>
    <li>
    POST /api/v1/users: creates a new user (JSON parameters: email, password, last_name (optional) and first_name (optional))
  </li>
    <li>
    PUT /api/v1/users/:id: updates an user based on the ID (JSON parameters: last_name and first_name)
  </li>
    <li>
    GET /users/me: retrieves the authenticated User object
  </li>
    <li>
    POST /auth_session/login: authenticates the user so they can log in
  </li>
    <li>
    DELETE /api/v1/auth_session/logout: log out user by deleting current session
  </li>
</ul>
