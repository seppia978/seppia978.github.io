# Samuele Poppi

Personal academic website for [Samuele Poppi](https://seppia978.github.io/), Postdoctoral Associate in AI Safety at MBZUAI.

The site is built with Hugo Blox and deployed to GitHub Pages through the workflow in `.github/workflows/publish.yaml`.

## Local Development

```bash
hugo server
```

## Build

```bash
hugo --minify --baseURL "https://seppia978.github.io/"
```

The generated `public/` directory is a build artifact. Source content lives mainly in:

- `content/_index.md` for the homepage
- `content/authors/admin/_index.md` for the bio and CV data
- `content/publication/` for papers
- `content/event/` for talks and lectures
- `config/_default/` for site configuration and navigation
