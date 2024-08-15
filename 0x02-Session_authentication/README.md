# 0x02-Session_authentication

<p>
  Simple HTTP API for playing with <code>User</code> model.
</p>

<h2>
  Files
</h2>

<h3><code>models/</code></h3>

<ul>
  <li>
    <code>base.py</code>: base of all models of the API - handle serialization to file
  </li>
  <li>
    <code>user.py</code>: user model
  </li>
</ul>

<h3><code>api/v1</code></h3>

<ul>
  <li>
    <code>app.py</code>: entry point of the API
  </li>
  <li>
    <code>views/index.py</code>: basic endpoints of the API: /status and /stats
  </li>
  <li>
    <code>views/users.py</code>: all users endpoints
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
    <code>GET /api/v1/status</code>: returns the status of the API
  </li>
  <li>
    <code>GET /api/v1/stats</code>: returns some stats of the API
  </li>
    <li>
    <code>GET /api/v1/users</code>: returns the list of users
  </li>
    <li>
    <code>GET /api/v1/users/:id</code>: returns an user based on the ID
  </li>
    <li>
    <code>DELETE /api/v1/users/:id</code>: deletes an user based on the ID
  </li>
    <li>
    <code>POST /api/v1/users</code>: creates a new user (JSON parameters: <code>email</code>, <code>password</code>, <code>last_name</code> (optional) and first_name (optional))
  </li>
    <li>
    <code>PUT /api/v1/users/:id</code>: updates an user based on the ID (JSON parameters: <code>last_name</code> and<code>first_name</code>)
  </li>
    <li>
    <code>GET /users/me</code>: retrieves the authenticated User object
  </li>
    <li>
    <code>POST /auth_session/login</code>: authenticates the user so they can log in
  </li>
    <li>
    <code>DELETE /api/v1/auth_session/logout</code>: log out user by deleting current session
  </li>
</ul>
