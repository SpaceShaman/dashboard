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

The build writes minified `app.css` and `app.js` to `app/static/` and copies
Lucide SVG files to `app/icons/`. Include both directories when deploying the
Python application; Node is only required for building assets. FastHTML serves
the CSS and JavaScript under `/static`; icons are embedded directly in HTML.

Use `Icon("info", cls="size-4")` in Python components. Icon names match the
SVG filenames in `lucide-static` (for example `circle-x`). No JavaScript imports
or HTMX initialization are needed. `npm run dev` and `npm run build` copy icons
automatically; `npm run build:icons` can also be run separately. Source SVGs are
cached in Python, so restart the server after updating the icon package.

Start the server without watchers or reload:

```sh
./run.sh serve --host 0.0.0.0 --port 8000
```

Edit `assets/app.css` for custom styles. Use complete Tailwind class names in
Python strings so the compiler can detect them. Basecoat styles can be used
with FastHTML attributes such as `cls="btn"` and
`data_variant="outline"`.
