---
title: 'From Text to Vision: Ensuring Responsibility and Safety in Modern AI'

event: Responsible Generative AI - National PhD Program in AI For Society
# event_url: https://example.org

location: Scuola Normale Superiore di Pisa
address:
  street: 7 Piazza dei Cavalieri
  city: Pisa
  region: Tuscany
  postcode: '56126'
  country: Italy

summary: Attacks and defences for single- and multi-modal models.
abstract: 'As generative AI systems grow in complexity and adoption, ensuring their safety and alignment becomes both more critical and more challenging. This talk explores the fragility of modern AI models—from text-only large language models (LLMs) to multimodal architectures—when exposed to adversarial manipulation. We begin by examining redteaming techniques that reveal how easily current LLMs can be jailbroken through methods such as prompt injection, character roleplay, and fine-tuning attacks. We then present recent findings showing that multilingual safety alignment can be compromised even by monolingual fine-tuning, highlighting the presence of language-agnostic safety parameters. To investigate this phenomenon, we introduce Safety Information Localization (SIL), a method to identify and manipulate the minimal set of parameters encoding safety-critical behavior. Finally, we transition to multimodal models and demonstrate Safe-CLIP, a framework that directly edits the CLIP embedding space to suppress harmful visual-textual associations. Together, these insights suggest that model safety must be embedded at a fundamental level—across languages, modalities, and representations—to ensure robust and responsible AI systems.'

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2025-05-27T14:00:00Z'
date_end: '2025-05-27T16:00:00Z'
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: '2017-01-01T00:00:00Z'

authors:
  - admin

tags: []

# Is this a featured talk? (true/false)
featured: true

image:
  caption: ''
  focal_point: 'Right'

#links:
#  - icon: twitter
#    icon_pack: fab
#    name: Follow
#    url: https://twitter.com/georgecushen
# url_code: 'https://github.com'
# url_pdf: ''
# url_slides: 'https://slideshare.net'
# url_video: 'https://youtube.com'

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
# projects:
#   - example
---
<!-- 
{{% callout note %}}
Click on the **Slides** button above to view the built-in slides feature.
{{% /callout %}}

Slides can be added in a few ways: -->

<!-- - **Create** slides using Hugo Blox Builder's [_Slides_](https://docs.hugoblox.com/reference/content-types/) feature and link using `slides` parameter in the front matter of the talk file
- **Upload** an existing slide deck to `static/` and link using `url_slides` parameter in the front matter of the talk file
- **Embed** your slides (e.g. Google Slides) or presentation video on this page using [shortcodes](https://docs.hugoblox.com/reference/markdown/).

Further event details, including [page elements](https://docs.hugoblox.com/reference/markdown/) such as image galleries, can be added to the body of this page. -->
