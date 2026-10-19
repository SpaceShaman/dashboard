# Dashboard

## Development

Install Python and frontend dependencies:

```sh
uv sync
npm ci
```

Start the frontend watchers and Uvicorn with Python reload:

```sh
./run.sh dev
```

The script builds assets once before starting the server. Ctrl+C stops the
server and frontend watchers together. If either process exits, the other is
stopped too. It uses Bash and Linux `setsid`.

Additional Uvicorn options can be passed through:

```sh
./run.sh dev --port 8080
```

To run only the frontend watchers, use `npm run dev`.
Tailwind scans `app/` for CSS classes; esbuild bundles `assets/app.js` and its
imports (HTMX and Basecoat). It does not start the Python server or reload the
browser.

## Production assets

```sh
npm ci
./run.sh build
```

The build writes minified `app.css` and `app.js` to `app/static/`.
Include these files when deploying the Python application; Node is only required
for building assets. FastAPI serves them under `/static`.

Start the server without watchers or reload:

```sh
./run.sh serve --host 0.0.0.0 --port 8000
```

Edit `assets/app.css` for custom styles. Use complete Tailwind class names in
Python strings so the compiler can detect them. Basecoat styles can be used
with Ludic attributes such as `class_="btn"` and
`dataset={"variant": "outline"}`.
