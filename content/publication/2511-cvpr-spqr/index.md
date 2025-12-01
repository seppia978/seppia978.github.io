---
title: SPQR: A Standardized Benchmark for Modern Safety Alignment Methods in Text-to-Image Diffusion Models'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - Mohammed Talha Alam
  - Nada Saadi
  - Fahad Shamshad
  - Nils Lukas
  - Karthik Nandakumar
  - Fakhri Karray
  - admin

# Author notes (optional)
# author_notes:
#   - 'Equal contribution'
#   - 'Equal contribution'
#   - 'Equal contribution'

date: '2025-11-24T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2017-01-01T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['article']

# Publication name and optional abbreviated publication name.
# publication: In *Arxiv*
# publication_short: In *Arxiv*
abstract: |
  Text-to-image diffusion models can emit copyrighted, unsafe, or private content. Safety alignment aims to suppress specific concepts, yet evaluations seldom test whether safety persists under benign downstream fine-tuning routinely applied after deployment (e.g., LoRA personalization, style/domain adapters). We study the stability of current safety methods under benign fine-tuning and observe frequent breakdowns. As true safety alignment must withstand even benign post-deployment adaptations, we introduce the SPQR benchmark (Safety-Prompt adherence-Quality-Robustness). SPQR is a single-scored metric that provides a standardized and reproducible framework to evaluate how well safety-aligned diffusion models preserve safety, utility, and robustness under benign fine-tuning, by reporting a single leaderboard score to facilitate comparisons. We conduct multilingual, domain-specific, and out-of-distribution analyses, along with category-wise breakdowns, to identify when safety alignment fails after benign fine-tuning, ultimately showcasing SPQR as a concise yet comprehensive benchmark for T2I safety alignment techniques for T2I models.


# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags:
  - NSFW
  - T2I Diffusion Models
  - AI Safety Benchmarks
  - AI Safety

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://arxiv.org/abs/2511.19558'
# url_code: 'https://github.com/aimagelab/safe-clip'
# url_dataset: 'https://huggingface.co/datasets/aimagelab/ViSU-Text'
# url_poster: ''
# url_project: 'https://aimagelab.github.io/safe-clip/'
# url_slides: ''
# url_source: 'https://github.com/HugoBlox/hugo-blox-builder'
# url_video: 'https://youtube.com'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: '' #Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
# projects:
#   - ELIAS

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---

<!-- {{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

{{% callout note %}}
Create your slides in Markdown - click the _Slides_ button to check out the example.
{{% /callout %}} -->

<!-- Add the publication's **full text** or **supplementary notes** here. You can use rich formatting such as including [code, math, and images](https://docs.hugoblox.com/content/writing-markdown-latex/). -->
