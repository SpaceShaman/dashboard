# Dashboard

## Development

Install Python and frontend dependencies:

```sh
uv sync
npm ci
```

Build and watch CSS and JavaScript:

```sh
npm run dev
```

Run the application in a separate terminal:

```sh
uv run uvicorn main:app --app-dir app --reload
```

`npm run dev` runs Tailwind CLI and esbuild together and stops both with Ctrl+C.
Tailwind scans `app/` for CSS classes; esbuild bundles `assets/app.js` and its
imports (HTMX and Basecoat). It does not start the Python server or reload the
browser.

## Production assets

```sh
npm ci
npm run build
```

The build writes minified `app.css` and `app.js` to `app/static/`.
Include these files when deploying the Python application; Node is only required
for building assets. FastAPI serves them under `/static`.

Edit `assets/app.css` for custom styles. Use complete Tailwind class names in
Python strings so the compiler can detect them. Basecoat styles can be used
with Ludic attributes such as `class_="btn"` and
`dataset={"variant": "outline"}`.
