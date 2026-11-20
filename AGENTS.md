# Repository Guidelines

## Project Structure

This is a static Russian-language site for the Gurman restaurant in Tyumen. The banquet landing page lives in `index.html` and `styles.css`. The takeaway menu at `/delivery/` has its own `delivery/index.html` and `delivery/styles.css`. Page-specific JavaScript is inline. Use `assets/gallery/` for gallery photos, `assets/menu/` for dish photos, and `files/` for downloadable menus and QR assets. Tests live in `tests/`.

## Local Development

- `python3 -m http.server 8080 --bind 127.0.0.1` serves the repository for quick checks of `/` and `/delivery/`.
- `docker build -t gurman-local .` packages the static files and Nginx configuration.
- `docker run --rm -p 127.0.0.1:8089:80 gurman-local` previews the packaged site, including Nginx redirects and the custom 404 page.

## Coding Style

Match nearby indentation. Use two spaces for CSS declarations and nested markup in the takeaway menu. Reuse existing CSS custom properties and use lowercase kebab-case for classes, dish IDs, and asset names, such as `chicken-wings.webp`. Keep customer-facing copy in Russian. Preserve image dimensions and meaningful alt text. Use confirmed dish photos, portion sizes, and prices.

## Testing

Run `python3 -B -m unittest discover -s tests -v`. Use `test_*.py` filenames and `test_*` methods. The suite checks local dish photos, portion markup, and active-section navigation. The navigation test requires `node` on PATH. For visual changes, check narrow mobile and desktop widths, including sticky navigation and anchor landing on the takeaway page.

## Commits and Pull Requests

Use a short English subject with a lowercase imperative verb. Follow the recent scoped pattern where helpful, for example `fix(delivery): align menu anchors`. Write PR descriptions in Russian. Explain the reason for the change, record verification results, link the related issue when available, and include screenshots for visual changes. Open work in progress as a draft. Push to `main` only when explicitly requested because it triggers production deployment.
